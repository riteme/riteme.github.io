#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""CSS-HTML-JS-Minify.

StandAlone Async single-file cross-platform no-dependency Minifier for the Web.
"""


import itertools
import logging as log
import signal
import socket
import sys
import traceback
from argparse import ArgumentParser
from ctypes import byref, cdll, create_string_buffer
from datetime import datetime
from doctest import testmod
from getpass import getuser
from json import dumps
from json import loads
from multiprocessing import cpu_count, Pool
from platform import platform, python_version
from subprocess import call
from time import sleep
from webbrowser import open_new_tab
import functools
import os
import re
import stat
from copy import copy
from hashlib import sha1
from shutil import make_archive, rmtree
from tempfile import gettempdir
from css_html_js_minify import __version__, __url__, __source__
from css_html_js_minify.variables import *
from functools import partial

try:
    from urllib import request
    from subprocess import getoutput
    from shutil import disk_usage
    from io import StringIO  # pure-Python StringIO supports unicode.
except ImportError:
    request = getoutput = disk_usage = None
    from StringIO import StringIO  # lint:ok
try:
    import resource  # windows dont have resource
except ImportError:
    resource = None

try:
    import resource
except ImportError:
    resource = None  # MS Window dont have resource

if sys.version_info.major == 3:
    open_utf8_kw = dict(encoding="utf-8")
    open_utf8sig_kw = dict(encoding="utf-8-sig")
else:
    open_utf8_kw = open_utf8sig_kw = dict()


CONFIG = None
start_time = datetime.now()


# Force CTRL+C to work to quit the app
signal.signal(signal.SIGINT, signal.SIG_DFL)


def make_logger(name=str(os.getpid())):
    """Build and return a Logging Logger."""
    if not sys.platform.startswith("win") and sys.stderr.isatty():
        def add_color_emit_ansi(fn):
            """Add methods we need to the class."""
            def new(*args):
                """Method overload."""
                if len(args) == 2:
                    new_args = (args[0], copy(args[1]))
                else:
                    new_args = (args[0], copy(args[1]), args[2:])
                if hasattr(args[0], 'baseFilename'):
                    return fn(*args)
                levelno = new_args[1].levelno
                if levelno >= 50:
                    color = '\x1b[31;5;7m\n '  # blinking red with black
                elif levelno >= 40:
                    color = '\x1b[31m'  # red
                elif levelno >= 30:
                    color = '\x1b[33m'  # yellow
                elif levelno >= 20:
                    color = '\x1b[32m'  # green
                elif levelno >= 10:
                    color = '\x1b[35m'  # pink
                else:
                    color = '\x1b[0m'  # normal
                try:
                    new_args[1].msg = color + str(new_args[1].msg) + ' \x1b[0m'
                except Exception as reason:
                    print(reason)  # Do not use log here.
                return fn(*new_args)
            return new
        log.StreamHandler.emit = add_color_emit_ansi(log.StreamHandler.emit)
    log_file = os.path.join(gettempdir(), str(name).lower().strip() + ".log")
    log.basicConfig(level=-1, filemode="w", filename=log_file)
    log.getLogger().addHandler(log.StreamHandler(sys.stderr))
    adrs = "/dev/log" if sys.platform.startswith("lin") else "/var/run/syslog"
    try:
        handler = log.handlers.SysLogHandler(address=adrs)
    except Exception:
        log.debug("Unix SysLog Server not found, ignored Logging to SysLog.")
    else:
        log.getLogger().addHandler(handler)
    log.debug("Logger created with Log file at: {0}.".format(log_file))
    return log


def typecheck(f):
    """Decorator for Python3 annotations to type-check inputs and outputs."""
    def __check_annotations(tipe):
        _type, is_ok = None, isinstance(tipe, (type, tuple, type(None)))
        if is_ok:  # Annotations can be Type or Tuple or None
            _type = tipe if isinstance(tipe, tuple) else tuple((tipe, ))
            if None in _type:  # if None on tuple replace with type(None)
                _type = tuple([_ if _ is not None else type(_) for _ in _type])
        return _type, is_ok

    @functools.wraps(f)  # wrap a function or method to Type Check it.
    def decorated(*args, **kwargs):
        msg = "Type check error: {0} must be {1} but is {2} on function {3}()."
        notations, f_name = tuple(f.__annotations__.keys()), f.__code__.co_name
        for i, name in enumerate(f.__code__.co_varnames):
            if name not in notations:
                continue  # this arg name has no annotation then skip it.
            _type, is_ok = __check_annotations(f.__annotations__.get(name))
            if is_ok:  # Force to tuple
                if i < len(args) and not isinstance(args[i], _type):
                    log.critical(msg.format(repr(args[i])[:50], _type,
                                            type(args[i]), f_name))
                elif name in kwargs and not isinstance(kwargs[name], _type):
                    log.critical(msg.format(repr(kwargs[name])[:50], _type,
                                            type(kwargs[name]), f_name))
        out = f(*args, **kwargs)
        _type, is_ok = __check_annotations(f.__annotations__.get("return"))
        if is_ok and not isinstance(out, _type) and "return" in notations:
            log.critical(msg.format(repr(out)[:50], _type, type(out), f_name))
        return out    # The output result of function or method.
    return decorated  # The decorated function or method.


def make_root_check_and_encoding_debug():
    """Debug and Log Encodings and Check for root/administrator,return Bool."""
    log.info(__doc__)
    log.debug("Python {0} on {1}.".format(python_version(), platform()))
    log.debug("STDIN Encoding: {0}.".format(sys.stdin.encoding))
    log.debug("STDERR Encoding: {0}.".format(sys.stderr.encoding))
    log.debug("STDOUT Encoding:{}".format(getattr(sys.stdout, "encoding", "")))
    log.debug("Default Encoding: {0}.".format(sys.getdefaultencoding()))
    log.debug("FileSystem Encoding: {0}.".format(sys.getfilesystemencoding()))
    log.debug("PYTHONIOENCODING Encoding: {0}.".format(
        os.environ.get("PYTHONIOENCODING", None)))
    os.environ["PYTHONIOENCODING"] = "utf-8"
    sys.dont_write_bytecode = True
    if not sys.platform.startswith("win"):  # root check
        if not os.geteuid():
            log.warning("Runing as root is not Recommended !.")
            return False
    elif sys.platform.startswith("win"):  # administrator check
        if getuser().lower().startswith("admin"):
            log.warning("Runing as Administrator is not Recommended !.")
            return False
    return True


def set_process_name_and_cpu_priority(name):
    """Set process name and cpu priority."""
    try:
        os.nice(19)  # smooth cpu priority
        libc = cdll.LoadLibrary("libc.so.6")  # set process name
        buff = create_string_buffer(len(name.lower().strip()) + 1)
        buff.value = bytes(name.lower().strip().encode("utf-8"))
        libc.prctl(15, byref(buff), 0, 0, 0)
    except Exception:
        return False  # this may fail on windows and its normal, so be silent.
    else:
        log.debug("Process Name set to: {0}.".format(name))
        return True


def set_single_instance(name, single_instance=True, port=8888):
    """Set process name and cpu priority,return socket.socket or None."""
    __lock = None
    if single_instance:
        try:  # Single instance app ~crossplatform, uses udp socket.
            log.info("Creating Abstract UDP Socket Lock for Single Instance.")
            __lock = socket.socket(
                socket.AF_UNIX if sys.platform.startswith("linux")
                else socket.AF_INET, socket.SOCK_STREAM)
            __lock.bind(
                "\0_{name}__lock".format(name=str(name).lower().strip())
                if sys.platform.startswith("linux") else ("127.0.0.1", port))
        except socket.error as e:
            log.warning(e)
        else:
            log.info("Socket Lock for Single Instance: {}.".format(__lock))
    else:  # if multiple instance want to touch same file bad things can happen
        log.warning("Multiple instance on same file can cause Race Condition.")
    return __lock


def make_post_execution_message(app=__doc__.splitlines()[0].strip()):
    """Simple Post-Execution Message with information about RAM and Time."""
    use, al = 0, 0
    if sys.platform.startswith("linux"):
        use = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss *
                  resource.getpagesize() / 1024 / 1024 if resource else 0)
        al = int(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') /
                 1024 / 1024 if hasattr(os, "sysconf") else 0)
    msg = "Total Maximum RAM Memory used: ~{0} of {1}MegaBytes".format(use, al)
    log.info(msg)
    if start_time and datetime:
        log.info("Total Working Time: {0}".format(datetime.now() - start_time))
    print("Thanks for using this App,share your experience! {0}".format("""
    Twitter: https://twitter.com/home?status=I%20Like%20{n}!:%20{u}
    Facebook: https://www.facebook.com/share.php?u={u}&t=I%20Like%20{n}
    G+: https://plus.google.com/share?url={u}
    Send BitCoins !:
    https://www.coinbase.com/checkouts/c3538d335faee0c30c81672ea0223877
    """.format(u=__url__, n=app)))  # see the message, but dont get on logs.
    return msg


def get_or_set_config_folder(appname):
    """Get config folder cross-platform, try to always return a path."""
    if sys.platform.startswith("darwin"):  # Apples Macos
        config_path = os.path.expanduser("~/Library/Preferences")
    elif sys.platform.startswith("win"):  # Windown
        config_path = os.getenv("APPDATA", os.path.expanduser("~/.config"))
    else:
        config_path = os.getenv("XDG_CONFIG_HOME",
                                os.path.expanduser("~/.config"))
    if appname and len(appname) and isinstance(appname, str):
        config_path = os.path.join(config_path, appname.strip())
    log.debug("Config folder for {0} is: {1}".format(appname, config_path))
    if not os.path.isdir(config_path):
        log.debug("Creating new Config folder: {0}.".format(config_path))
        os.makedirs(config_path)
    return config_path


def get_or_set_temp_folder(appname):
    """Get a temp Sub-folder for this App only, cross-platform, return path."""
    if appname and len(appname) and isinstance(appname, str):
        temp_path = os.path.join(gettempdir(), appname.strip().lower())
    log.debug("Temp folder for {0} is: {1}.".format(appname, temp_path))
    if not os.path.isdir(temp_path):
        log.debug("Creating new Temp folder: {0}.".format(temp_path))
        os.makedirs(temp_path)
    return temp_path


def add_desktop_files(app, desktop_file_content):
    """Add to autostart of the Desktop."""
    config_dir = os.path.join(os.path.expanduser("~"), ".config", "autostart")
    autostart_file = os.path.join(config_dir, app + ".desktop")
    if os.path.isdir(config_dir) and not os.path.isfile(autostart_file):
        log.info("Writing Auto-Start file: " + autostart_file)
        with open(autostart_file, "w", **open_utf8_kw) as start_file:
            start_file.write(desktop_file_content)
    apps_dir = os.path.join(os.path.expanduser("~"),
                            ".local", "share", "applications")
    desktop_file = os.path.join(apps_dir, app + ".desktop")
    if os.path.isdir(apps_dir) and not os.path.isfile(desktop_file):
        log.info("Writing Desktop Launcher file: " + desktop_file)
        with open(desktop_file, "w", **open_utf8_kw) as desktop_file_obj:
            desktop_file_obj.write(desktop_file_content)
    return desktop_file


def log_exception():
    """Log Exceptions but pretty printing with more info, return string."""
    unfriendly_names = {"<module>": "Unnamed Anonymous Module Function",
                        "<stdin>": "System Standard Input Function"}
    line_tpl = "    |___ {key} = {val}  # Type: {t}, Size: {s}Bytes, ID: {i}\n"
    body_tpl = """
    ################################ D E B U G ###############################
    Listing all Local objects by context frame, ordered by innermost last:
    {body}
    Thats all we know about the error, check the LOG file and StdOut.
    ############################### D E B U G #############################"""
    tb, body_txt, whole_txt = sys.exc_info()[2], "", ""
    while 1:
        if not tb.tb_next:
            break
        tb = tb.tb_next
    stack = []
    f = tb.tb_frame
    while f:
        stack.append(f)
        f = f.f_back
    stack.reverse()
    traceback.print_exc()
    for frame in stack:
        if frame.f_code.co_name in unfriendly_names.keys():
            fun = unfriendly_names[frame.f_code.co_name]
        else:
            fun = "Function {0}()".format(frame.f_code.co_name)
        body_txt += "\nThe {nm} from file {fl} at line {ln} failed!.".format(
            nm=fun, fl=frame.f_code.co_filename, ln=frame.f_lineno)
        body_txt += "\n    {}\n    |\n".format(fun)
        for key, value in frame.f_locals.items():
            whole_txt += line_tpl.format(key=key, val=repr(value)[:50],
                                         t=str(type(value))[:25],
                                         s=sys.getsizeof(key), i=id(value))
    result = body_tpl.format(body=body_txt + whole_txt)
    log.debug(result)
    return result


def check_working_folder(folder_to_check=os.path.expanduser("~")):
    """Check working folder,passed argument,for everything that can go wrong.
    >>> check_working_folder()
    True
    """
    folder_to_check = os.path.abspath(folder_to_check)  # More Safe on WinOS
    log.debug("Checking the Working Folder: '{0}'".format(folder_to_check))
    # What if folder is not a string.
    if not isinstance(folder_to_check, str):
        log.critical("Folder {0} is not String type!.".format(folder_to_check))
        return False
    elif os.path.isfile(folder_to_check):
        log.info("Folder {0} is File or Relative Path".format(folder_to_check))
        return True
    # What if folder is not a folder.
    elif not os.path.isdir(folder_to_check):
        log.critical("Folder {0} does not exist !.".format(folder_to_check))
        return False
    # What if destination folder is not Readable by the user.
    elif not os.access(folder_to_check, os.R_OK):
        log.critical("Folder {0} not Readable !.".format(folder_to_check))
        return False
    # What if destination folder is not Writable by the user.
    elif not os.access(folder_to_check, os.W_OK):
        log.critical("Folder {0} Not Writable !.".format(folder_to_check))
        return False
    elif disk_usage and os.path.exists(folder_to_check):
        hdd = int(disk_usage(folder_to_check).free / 1024 / 1024 / 1024)
        if hdd:  # > 1 Gb
            log.info("Total Free Space: ~{0} GigaBytes.".format(hdd))
            return True
        else:  # < 1 Gb
            log.critical("Total Free Space is < 1 GigaByte; Epic Fail !.")
            return False
    return False


def walkdir_to_filelist(where, target, omit):
    """Perform full walk of where, gather full path of all files."""
    log.debug("Scan {},searching {},ignoring {}".format(where, target, omit))
    return tuple([os.path.join(r, f)
                  for r, d, fs in os.walk(where, followlinks=True)
                  for f in fs if not f.startswith('.') and
                  not f.endswith(omit) and
                  f.endswith(target)])  # only target files,no hidden files


def check_for_updates():
    """Method to check for updates from Git repo versus this version."""
    try:
        last_version = str(request.urlopen(__source__).read().decode("utf8"))
        this_version = str(open(__file__).read())
    except Exception:
        log_exception()
    else:
        if this_version != last_version:
            msg = "Theres a new Version!, update the App from: " + __source__
            log.warning(msg)
        else:
            msg = "No new updates!, You have the latest version of this app."
            log.info(msg)
        return msg


def json_pretty(json_dict):
    """Pretty-Printing JSON data from dictionary to string."""
    _json = dumps(json_dict, sort_keys=1, indent=4, separators=(",\n", ": "))
    posible_ends = tuple('true false , " ] 0 1 2 3 4 5 6 7 8 9 \n'.split(" "))
    max_indent, justified_json = 1, ""
    for json_line in _json.splitlines():
        if len(json_line.split(":")) >= 2 and json_line.endswith(posible_ends):
            lenght = len(json_line.split(":")[0].rstrip()) + 1
            max_indent = lenght if lenght > max_indent else max_indent
            max_indent = max_indent if max_indent <= 80 else 80  # Limit indent
    for line_of_json in _json.splitlines():
        condition_1 = max_indent > 1 and len(line_of_json.split(":")) >= 2
        condition_2 = line_of_json.endswith(posible_ends) and len(line_of_json)
        if condition_1 and condition_2:
            propert_len = len(line_of_json.split(":")[0].rstrip()) + 1
            xtra_spaces = " " * (max_indent + 1 - propert_len)
            xtra_spaces = ":" + xtra_spaces
            justified_line_of_json = line_of_json.split(":")[0].rstrip()
            justified_line_of_json += xtra_spaces
            justified_line_of_json += "".join(
                line_of_json.split(":")[1:len(line_of_json.split(":"))])
            justified_json += justified_line_of_json + "\n"
        else:
            justified_json += line_of_json + "\n"
    return str("\n\n" + justified_json if max_indent > 1 else _json)


def make_config(app):
    """Make a global config object."""
    global CONFIG
    config_file = os.path.join(get_or_set_config_folder(app), "config.json")
    if not os.path.isfile(config_file):
        log.debug("Creating a new JSON Config file: " + config_file)
        with open(config_file, "w", **open_utf8_kw) as config_object:
            config_object.write("{}\n")
    with open(config_file, "r", **open_utf8_kw) as config_object:
        log.debug("Reading JSON Config file: " + config_file)
        CONFIG = loads(config_object.read().strip())


def view_config(app):
    """Open the JSON config file for app."""
    return open_new_tab(
        os.path.join(get_or_set_config_folder(app), "config.json"))


def autosave_config(app):
    log.debug("Cleaning up, AutoSaving Configs and Shutting Down...")
    config_file = os.path.join(get_or_set_config_folder(app), "config.json")
    with open(config_file, "w", **open_utf8_kw) as config_object:
        config_object.write(json_pretty(CONFIG))


def delete_config(app):
    """Delete config folder."""
    return rmtree(get_or_set_config_folder(app), ignore_errors=True)


def backup_config(app):
    """AutoBackup config settings to a compressed ZIP."""
    output_file = os.path.join(os.path.expanduser("~"), app)
    make_archive(output_file, 'zip', get_or_set_config_folder(app), logger=log)
    return output_file + ".zip"


def watch(file_path, callback=None):
    """Watch a file path for changes run callback if modified. A WatchDog."""
    log.debug("Watching for changes on path: {0}.".format(file_path))
    previous = int(os.stat(file_path).st_mtime)
    while True:
        actual = int(os.stat(file_path).st_mtime)
        if previous == actual:
            sleep(60)
        else:
            previous = actual
            log.debug("Modification detected on {0}.".format(file_path))
            return callback(file_path) if callback else file_path


def beep(waveform=(79, 45, 32, 50, 99, 113, 126, 127)):
    """Cross-platform Sound Playing with StdLib only,No Sound file required."""
    wavefile = os.path.join(gettempdir(), "beep.wav")
    if not os.path.isfile(wavefile) or not os.access(wavefile, os.R_OK):
        with open(wavefile, "w+") as wave_file:
            for sample in range(0, 1000, 1):
                for wav in range(0, 8, 1):
                    wave_file.write(chr(waveform[wav]))
    if sys.platform.startswith("linux"):
        return call("chrt -i 0 aplay '{fyle}'".format(fyle=wavefile), shell=1)
    if sys.platform.startswith("darwin"):
        return call("afplay '{fyle}'".format(fyle=wavefile), shell=True)
    if sys.platform.startswith("win"):  # FIXME: This is Ugly.
        return call("start /low /min '{fyle}'".format(fyle=wavefile), shell=1)


def about_python():
    """Open Python official homepage."""
    return open_new_tab('https://python.org')


def about_self():
    """Open this App homepage."""
    return open_new_tab(__url__)


def view_code():
    """Open this App local Python source code."""
    return open_new_tab(__file__)


def report_bug():
    """Open this App Bug Tracker."""
    return open_new_tab(__url__ + "/issues/new")


def pdb_on_exception(debugger="pdb", limit=100):
    """Install handler attach post-mortem pdb console on an exception."""
    pass

    def pdb_excepthook(exc_type, exc_val, exc_tb):
        traceback.print_tb(exc_tb, limit=limit)
        __import__(str(debugger).strip().lower()).post_mortem(exc_tb)

    sys.excepthook = pdb_excepthook

ipdb_on_exception = pdb_on_exception


def write_atomic(dest_path, **kwargs):
    """A convenient interface to AtomicWriter type."""
    return AtomicWriter(dest_path, **kwargs)


def rename_atomic(path, new_path, overwrite=False):
    """Atomic rename of a path."""
    if overwrite:
        os.rename(path, new_path)
    else:
        os.link(path, new_path)
        os.unlink(path)


_TEXT_OPENFLAGS = os.O_RDWR | os.O_CREAT | os.O_EXCL
if hasattr(os, 'O_NOINHERIT'):
    _TEXT_OPENFLAGS |= os.O_NOINHERIT
if hasattr(os, 'O_NOFOLLOW'):
    _TEXT_OPENFLAGS |= os.O_NOFOLLOW
_BIN_OPENFLAGS = _TEXT_OPENFLAGS
if hasattr(os, 'O_BINARY'):
    _BIN_OPENFLAGS |= os.O_BINARY

try:
    import fcntl as fcntl
except ImportError:
    def set_cloexec(fd):
        "Dummy set_cloexec for platforms without fcntl support."
        pass
else:
    def set_cloexec(fd):
        """Does a best-effort fcntl.fcntl call to set a fd to be
        automatically closed by any future child processes."""
        try:
            flags = fcntl.fcntl(fd, fcntl.F_GETFD, 0)
        except IOError:
            pass
        else:
            flags |= fcntl.FD_CLOEXEC  # flags read successfully, modify
            fcntl.fcntl(fd, fcntl.F_SETFD, flags)


class AtomicWriter(object):

    """context manager with a writable file which will be moved into place
    as long as no exceptions are raised within the context manager's block.
    These "part files" are created in the same directory as the destination
    path to ensure atomic move operations. Similar to Chrome Downloads.

    Args:
        dest_path (str): The path where the completed file will be written.
        overwrite (bool): overwrite destination file if exists. Defaults True.
        delete_part_if_fail (bool): Move *.part to temp folder if exception.
    """

    def __init__(self, dest_path, **kwargs):
        super(AtomicWriter, self).__init__(dest_path, **kwargs)
        self.dest_path = dest_path
        self.overwrite = kwargs.pop('overwrite', True)
        self.delete_part_if_fail = kwargs.pop('delete_part_if_fail', True)
        self.text_mode = kwargs.pop('text_mode', False)  # for windows
        self.dest_path = os.path.abspath(self.dest_path)
        self.dest_dir = os.path.dirname(self.dest_path)
        self.part_path = dest_path + '.part'
        self.mode = 'w+' if self.text_mode else 'w+b'
        self.open_flags = _TEXT_OPENFLAGS if self.text_mode else _BIN_OPENFLAGS
        self.part_file = None

    def _open_part_file(self):
        do_chmod = True
        try:
            stat_res = os.stat(self.dest_path)  # copy from file being replaced
            file_perms = stat.S_IMODE(stat_res.st_mode)
        except (OSError, IOError):
            file_perms = 0o644  # default if no file exists
            do_chmod = False  # respect the umask
        fd = os.open(self.part_path, self.open_flags, file_perms)
        set_cloexec(fd)
        self.part_file = os.fdopen(fd, self.mode, -1)
        if do_chmod:  # if default perms are overridden by the user or
            try:  # previous dest_path chmod away the effects of the umask
                os.chmod(self.part_path, file_perms)
            except (OSError, IOError):
                self.part_file.close()
                raise

    def setup(self):
        """Called on context manager entry (the with statement)."""
        if os.path.lexists(self.dest_path):
            if not self.overwrite:
                raise OSError('File already exists!: ' + self.dest_path)
        if os.path.lexists(self.part_path):
            os.unlink(self.part_path)
        self._open_part_file()

    def __enter__(self):
        self.setup()
        return self.part_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.part_file.close()
        tmp_file = os.path.join(gettempdir(), os.path.basename(self.part_path))
        if exc_type:
            if self.delete_part_if_fail:
                try:
                    rename_atomic(self.part_path, tmp_file, True)  # os.unlink
                except:
                    pass
            return
        try:
            rename_atomic(self.part_path, self.dest_path,
                          overwrite=self.overwrite)
        except OSError:
            if self.delete_part_if_fail:
                rename_atomic(self.part_path, tmp_file, True)  # os.unlink()
            raise  # could not save destination file


###############################################################################
# CSS minify


def _compile_props(props_text, grouped=False):
    """Take a list of props and prepare them."""
    props, prefixes = [], "-webkit-,-khtml-,-epub-,-moz-,-ms-,-o-,".split(",")
    for propline in props_text.strip().lower().splitlines():
        props += [pre + pro for pro in propline.split(" ") for pre in prefixes]
    props = filter(lambda line: not line.startswith('#'), props)
    if not grouped:
        props = list(filter(None, props))
        return props, [0]*len(props)
    final_props, groups, g_id = [], [], 0
    for prop in props:
        if prop.strip():
            final_props.append(prop)
            groups.append(g_id)
        else:
            g_id += 1
    return final_props, groups


def _prioritify(line_of_css, css_props_text_as_list):
    """Return args priority, priority is integer and smaller means higher."""
    sorted_css_properties, groups_by_alphabetic_order = css_props_text_as_list
    priority_integer, group_integer = 9999, 0
    for css_property in sorted_css_properties:
        if css_property.lower() == line_of_css.split(":")[0].lower().strip():
            priority_integer = sorted_css_properties.index(css_property)
            group_integer = groups_by_alphabetic_order[priority_integer]
            break
    return priority_integer, group_integer


def _props_grouper(props, pgs):
    """Return groups for properties."""
    if not props:
        return props
    # props = sorted([
        # _ if _.strip().endswith(";")
        # and not _.strip().endswith("*/") and not _.strip().endswith("/*")
        # else _.rstrip() + ";\n" for _ in props])
    props_pg = zip(map(lambda prop: _prioritify(prop, pgs), props), props)
    props_pg = sorted(props_pg, key=lambda item: item[0][1])
    props_by_groups = map(
        lambda item: list(item[1]),
        itertools.groupby(props_pg, key=lambda item: item[0][1]))
    props_by_groups = map(lambda item: sorted(
        item, key=lambda item: item[0][0]), props_by_groups)
    props = []
    for group in props_by_groups:
        group = map(lambda item: item[1], group)
        props += group
        props += ['\n']
    props.pop()
    return props


def sort_properties(css_unsorted_string):
    """CSS Property Sorter Function.

    This function will read buffer argument, split it to a list by lines,
    sort it by defined rule, and return sorted buffer if it's CSS property.
    This function depends on '_prioritify' function.
    """
    log.debug("Alphabetically Sorting all CSS / SCSS Properties.")
    css_pgs = _compile_props(CSS_PROPS_TEXT, grouped=False)  # Do Not Group.
    pattern = re.compile(r'(.*?{\r?\n?)(.*?)(}.*?)|(.*)',
                         re.DOTALL + re.MULTILINE)
    matched_patterns = pattern.findall(css_unsorted_string)
    sorted_patterns, sorted_buffer = [], css_unsorted_string
    re_prop = re.compile(r'((?:.*?)(?:;)(?:.*?\n)|(?:.*))',
                         re.DOTALL + re.MULTILINE)
    if len(matched_patterns) != 0:
        for matched_groups in matched_patterns:
            sorted_patterns += matched_groups[0].splitlines(True)
            props = map(lambda line: line.lstrip('\n'),
                        re_prop.findall(matched_groups[1]))
            props = list(filter(lambda line: line.strip('\n '), props))
            props = _props_grouper(props, css_pgs)
            sorted_patterns += props
            sorted_patterns += matched_groups[2].splitlines(True)
            sorted_patterns += matched_groups[3].splitlines(True)
        sorted_buffer = ''.join(sorted_patterns)
    return sorted_buffer


def remove_comments(css):
    """Remove all CSS comment blocks."""
    log.debug("Removing all Comments.")
    iemac, preserve = False, False
    comment_start = css.find("/*")
    while comment_start >= 0:  # Preserve comments that look like `/*!...*/`.
        # Slicing is used to make sure we dont get an IndexError.
        preserve = css[comment_start + 2:comment_start + 3] == "!"
        comment_end = css.find("*/", comment_start + 2)
        if comment_end < 0:
            if not preserve:
                css = css[:comment_start]
                break
        elif comment_end >= (comment_start + 2):
            if css[comment_end - 1] == "\\":
                # This is an IE Mac-specific comment; leave this one and the
                # following one alone.
                comment_start = comment_end + 2
                iemac = True
            elif iemac:
                comment_start = comment_end + 2
                iemac = False
            elif not preserve:
                css = css[:comment_start] + css[comment_end + 2:]
            else:
                comment_start = comment_end + 2
        comment_start = css.find("/*", comment_start)
    return css


def remove_unnecessary_whitespace(css):
    """Remove unnecessary whitespace characters."""
    log.debug("Removing all unnecessary white spaces.")

    def pseudoclasscolon(css):
        """Prevent 'p :link' from becoming 'p:link'.

        Translates 'p :link' into 'p ___PSEUDOCLASSCOLON___link'.
        This is translated back again later.
        """
        regex = re.compile(r"(^|\})(([^\{\:])+\:)+([^\{]*\{)")
        match = regex.search(css)
        while match:
            css = ''.join([
                css[:match.start()],
                match.group().replace(":", "___PSEUDOCLASSCOLON___"),
                css[match.end():]])
            match = regex.search(css)
        return css

    css = pseudoclasscolon(css)
    # Remove spaces from before things.
    css = re.sub(r"\s+([!{};:>\(\)\],])", r"\1", css)
    # If there is a `@charset`, then only allow one, and move to beginning.
    css = re.sub(r"^(.*)(@charset \"[^\"]*\";)", r"\2\1", css)
    css = re.sub(r"^(\s*@charset [^;]+;\s*)+", r"\1", css)
    # Put the space back in for a few cases, such as `@media screen` and
    # `(-webkit-min-device-pixel-ratio:0)`.
    css = re.sub(r"\band\(", "and (", css)
    # Put the colons back.
    css = css.replace('___PSEUDOCLASSCOLON___', ':')
    # Remove spaces from after things.
    css = re.sub(r"([!{}:;>\(\[,])\s+", r"\1", css)
    return css


def remove_unnecessary_semicolons(css):
    """Remove unnecessary semicolons."""
    log.debug("Removing all unnecessary semicolons.")
    return re.sub(r";+\}", "}", css)


def remove_empty_rules(css):
    """Remove empty rules."""
    log.debug("Removing all unnecessary empty rules.")
    return re.sub(r"[^\}\{]+\{\}", "", css)


def normalize_rgb_colors_to_hex(css):
    """Convert `rgb(51,102,153)` to `#336699`."""
    log.debug("Converting all rgba to hexadecimal color values.")
    regex = re.compile(r"rgb\s*\(\s*([0-9,\s]+)\s*\)")
    match = regex.search(css)
    while match:
        colors = map(lambda s: s.strip(), match.group(1).split(","))
        hexcolor = '#%.2x%.2x%.2x' % tuple(map(int, colors))
        css = css.replace(match.group(), hexcolor)
        match = regex.search(css)
    return css


def condense_zero_units(css):
    """Replace `0(px, em, %, etc)` with `0`."""
    log.debug("Condensing all zeroes on values.")
    return re.sub(r"([\s:])(0)(px|em|%|in|q|ch|cm|mm|pc|pt|ex|rem|s|ms|"
                  r"deg|grad|rad|turn|vw|vh|vmin|vmax|fr)", r"\1\2", css)


def condense_multidimensional_zeros(css):
    """Replace `:0 0 0 0;`, `:0 0 0;` etc. with `:0;`."""
    log.debug("Condensing all multidimensional zeroes on values.")
    return css.replace(":0 0 0 0;", ":0;").replace(
        ":0 0 0;", ":0;").replace(":0 0;", ":0;").replace(
            "background-position:0;", "background-position:0 0;").replace(
                "transform-origin:0;", "transform-origin:0 0;")


def condense_floating_points(css):
    """Replace `0.6` with `.6` where possible."""
    log.debug("Condensing all floating point values.")
    return re.sub(r"(:|\s)0+\.(\d+)", r"\1.\2", css)


def condense_hex_colors(css):
    """Shorten colors from #AABBCC to #ABC where possible."""
    log.debug("Condensing all hexadecimal color values.")
    regex = re.compile(
        r"""([^\"'=\s])(\s*)#([0-9a-f])([0-9a-f])([0-9a-f])"""
        r"""([0-9a-f])([0-9a-f])([0-9a-f])""", re.I | re.S)
    match = regex.search(css)
    while match:
        first = match.group(3) + match.group(5) + match.group(7)
        second = match.group(4) + match.group(6) + match.group(8)
        if first.lower() == second.lower():
            css = css.replace(
                match.group(), match.group(1) + match.group(2) + '#' + first)
            match = regex.search(css, match.end() - 3)
        else:
            match = regex.search(css, match.end())
    return css


def condense_whitespace(css):
    """Condense multiple adjacent whitespace characters into one."""
    log.debug("Condensing all unnecessary white spaces.")
    return re.sub(r"\s+", " ", css)


def condense_semicolons(css):
    """Condense multiple adjacent semicolon characters into one."""
    log.debug("Condensing all unnecessary multiple adjacent semicolons.")
    return re.sub(r";;+", ";", css)


def wrap_css_lines(css, line_length=80):
    """Wrap the lines of the given CSS to an approximate length."""
    log.debug("Wrapping lines to ~{0} max line lenght.".format(line_length))
    lines, line_start = [], 0
    for i, char in enumerate(css):
        # Its safe to break after } characters.
        if char == '}' and (i - line_start >= line_length):
            lines.append(css[line_start:i + 1])
            line_start = i + 1
    if line_start < len(css):
        lines.append(css[line_start:])
    return '\n'.join(lines)


def condense_font_weight(css):
    """Condense multiple font weights into shorter integer equals."""
    log.debug("Condensing font weights on values.")
    return css.replace('font-weight:normal;', 'font-weight:400;').replace(
        'font-weight:bold;', 'font-weight:700;')


def condense_std_named_colors(css):
    """Condense named color values to shorter replacement using HEX."""
    log.debug("Condensing standard named color values.")
    for color_name, color_hexa in iter(tuple({
        ':aqua;': ':#0ff;', ':blue;': ':#00f;',
            ':fuchsia;': ':#f0f;', ':yellow;': ':#ff0;'}.items())):
        css = css.replace(color_name, color_hexa)
    return css


def condense_xtra_named_colors(css):
    """Condense named color values to shorter replacement using HEX."""
    log.debug("Condensing extended named color values.")
    for k, v in iter(tuple(EXTENDED_NAMED_COLORS.items())):
        same_color_but_rgb = 'rgb({0},{1},{2})'.format(v[0], v[1], v[2])
        if len(k) > len(same_color_but_rgb):
            css = css.replace(k, same_color_but_rgb)
    return css


def remove_url_quotes(css):
    """Fix for url() does not need quotes."""
    log.debug("Removing quotes from url.")
    return re.sub(r'url\((["\'])([^)]*)\1\)', r'url(\2)', css)


def condense_border_none(css):
    """Condense border:none; to border:0;."""
    log.debug("Condense borders values.")
    return css.replace("border:none;", "border:0;")


def add_encoding(css):
    """Add @charset 'UTF-8'; if missing."""
    log.debug("Adding encoding declaration if needed.")
    return "@charset utf-8;" + css if "@charset" not in css.lower() else css


def restore_needed_space(css):
    """Fix CSS for some specific cases where a white space is needed."""
    return css.replace("!important", " !important").replace(  # !important
        "@media(", "@media (").replace(  # media queries # jpeg > jpg
            "data:image/jpeg;base64,", "data:image/jpg;base64,").rstrip("\n;")


def unquote_selectors(css):
    """Fix CSS for some specific selectors where Quotes is not needed."""
    log.debug("Removing unnecessary Quotes on selectors of CSS classes.")
    return re.compile('([a-zA-Z]+)="([a-zA-Z0-9-_\.]+)"]').sub(r'\1=\2]', css)


def css_minify(css, wrap=False, comments=False, sort=False):
    """Minify CSS main function."""
    log.info("Compressing CSS...")
    css = remove_comments(css) if not comments else css
    css = sort_properties(css) if sort else css
    css = unquote_selectors(css)
    css = condense_whitespace(css)
    css = remove_url_quotes(css)
    css = condense_xtra_named_colors(css)
    css = condense_font_weight(css)
    css = remove_unnecessary_whitespace(css)
    css = condense_std_named_colors(css)
    css = remove_unnecessary_semicolons(css)
    css = condense_zero_units(css)
    css = condense_multidimensional_zeros(css)
    css = condense_floating_points(css)
    css = normalize_rgb_colors_to_hex(css)
    css = condense_hex_colors(css)
    css = condense_border_none(css)
    css = wrap_css_lines(css, 80) if wrap else css
    css = condense_semicolons(css)
    css = add_encoding(css)
    css = restore_needed_space(css)
    log.info("Finished compressing CSS !.")
    return css.strip()


##############################################################################
# HTML Minify


def condense_html_whitespace(html):
    """Condense HTML, but be safe first if it have textareas or pre tags.

    >>> condense_html_whitespace('<i>  <b>    <a> test </a>    </b> </i><br>')
    '<i><b><a> test </a></b></i><br>'
    """  # first space between tags, then empty new lines and in-between.
    log.debug("Removing unnecessary HTML White Spaces and Empty New Lines.")
    is_ok = "<textarea" not in html.lower() and "<pre" not in html.lower()
    html = re.sub(r'>\s+<', '> <', html) if is_ok else html
    return re.sub(r'\s{2,}|[\r\n]', ' ', html) if is_ok else html.strip()


def condense_style(html):
    """Condense style html tags.

    >>> condense_style('<style type="text/css">*{border:0}</style><p>a b c')
    '<style>*{border:0}</style><p>a b c'
    """  # May look silly but Emmet does this and is wrong.
    log.debug("Condensing HTML Style CSS tags.")
    return html.replace('<style type="text/css">', '<style>').replace(
        "<style type='text/css'>", '<style>').replace(
            "<style type=text/css>", '<style>')


def condense_script(html):
    """Condense script html tags.

    >>> condense_script('<script type="text/javascript"> </script><p>a b c')
    '<script> </script><p>a b c'
    """  # May look silly but Emmet does this and is wrong.
    log.debug("Condensing HTML Script JS tags.")
    return html.replace('<script type="text/javascript">', '<script>').replace(
        "<style type='text/javascript'>", '<script>').replace(
            "<style type=text/javascript>", '<script>')


def clean_unneeded_html_tags(html):
    """Clean unneeded optional html tags.

    >>> clean_unneeded_html_tags('a<body></img></td>b</th></tr></hr></br>c')
    'abc'
    """
    log.debug("Removing unnecessary optional HTML tags.")
    for tag_to_remove in ("""</area> </base> <body> </body> </br> </col>
        </colgroup> </dd> </dt> <head> </head> </hr> <html> </html> </img>
        </input> </li> </link> </meta> </option> </param> <tbody> </tbody>
        </td> </tfoot> </th> </thead> </tr> </basefont> </isindex> </param>
            """.split()):
            html = html.replace(tag_to_remove, '')
    return html  # May look silly but Emmet does this and is wrong.


def remove_html_comments(html):
    """Remove all HTML comments, Keep all for Grunt, Grymt and IE.

    >>> _="<!-- build:dev -->a<!-- endbuild -->b<!--[if IE 7]>c<![endif]--> "
    >>> _+= "<!-- kill me please -->keep" ; remove_html_comments(_)
    '<!-- build:dev -->a<!-- endbuild -->b<!--[if IE 7]>c<![endif]--> keep'
    """  # Grunt uses comments to as build arguments, bad practice but still.
    log.debug("""Removing all unnecessary HTML comments; Keep all containing:
    'build:', 'endbuild', '<!--[if]>', '<![endif]-->' for Grunt/Grymt, IE.""")
    return re.compile('<!-- [^(build|endbuild)].*? -->', re.I).sub('', html)


def unquote_html_attributes(html):
    """Remove all HTML quotes on attibutes if possible.

    >>> unquote_html_attributes('<img   width="9" height="5" data-foo="0"  >')
    '<img width=9 height=5 data-foo=0 >'
    """  # data-foo=0> might cause errors on IE, we leave 1 space data-foo=0 >
    log.debug("Removing unnecessary Quotes on attributes of HTML tags.")
    # cache all regular expressions on variables before we enter the for loop.
    any_tag = re.compile(r"<\w.*?>", re.I | re.MULTILINE | re.DOTALL)
    space = re.compile(r' \s+|\s +', re.MULTILINE)
    space1 = re.compile(r'\w\s+\w', re.MULTILINE)
    space2 = re.compile(r'"\s+>', re.MULTILINE)
    space3 = re.compile(r"'\s+>", re.MULTILINE)
    space4 = re.compile('"\s\s+\w+="|\'\s\s+\w+=\'|"\s\s+\w+=|\'\s\s+\w+=',
                        re.MULTILINE)
    space6 = re.compile(r"\d\s+>", re.MULTILINE)
    quotes_in_tag = re.compile('([a-zA-Z]+)="([a-zA-Z0-9-_\.]+)"')
    # iterate on a for loop cleaning stuff up on the html markup.
    for tag in iter(any_tag.findall(html)):
        # exceptions of comments and closing tags
        if tag.startswith('<!') or tag.find('</') > -1:
            continue
        original = tag
        # remove white space inside the tag itself
        tag = space2.sub('" >', tag)  # preserve 1 white space is safer
        tag = space3.sub("' >", tag)
        for each in space1.findall(tag) + space6.findall(tag):
            tag = tag.replace(each, space.sub(' ', each))
        for each in space4.findall(tag):
            tag = tag.replace(each, each[0] + ' ' + each[1:].lstrip())
        # remove quotes on some attributes
        tag = quotes_in_tag.sub(r'\1=\2 ', tag)  # See Bug #28
        if original != tag:  # has the tag been improved ?
            html = html.replace(original, tag)
    return html.strip()


def html_minify(html, comments=False):
    """Minify HTML main function.

    >>> html_minify(' <p  width="9" height="5"  > <!-- a --> b </p> c <br> ')
    '<p width=9 height=5 > b c <br>'
    """
    log.info("Compressing HTML...")
    html = remove_html_comments(html) if not comments else html
    html = condense_style(html)
    html = condense_script(html)
    html = clean_unneeded_html_tags(html)
    html = condense_html_whitespace(html)
    html = unquote_html_attributes(html)
    log.info("Finished compressing HTML !.")
    return html.strip()


##############################################################################
# JS Minify


def remove_commented_lines(js):
    """Force remove commented out lines from Javascript."""
    log.debug("Force remove commented out lines from Javascript.")
    result = ""
    for line in js.splitlines():
        if line.strip().startswith("//") and not line.strip().endswith("*/"):
            continue
        result += line
    return result


def simple_replacer_js(js):
    """Force strip simple replacements from Javascript."""
    log.debug("Force strip simple replacements from Javascript.")
    return condense_semicolons(js.replace("debugger;", ";").replace(
        ";}", "}").replace("; ", ";").replace(" ;", ";").rstrip("\n;"))


def js_minify_keep_comments(js):
    """Return a minified version of the Javascript string."""
    log.info("Compressing Javascript...")
    ins, outs = StringIO(js), StringIO()
    JavascriptMinify(ins, outs).minify()
    return force_single_line_js(outs.getvalue())


def force_single_line_js(js):
    """Force Javascript to a single line, even if need to add semicolon."""
    log.debug("Forcing JS from ~{0} to 1 Line.".format(len(js.splitlines())))
    return ";".join(js.splitlines()) if len(js.splitlines()) > 1 else js


class JavascriptMinify(object):

    """Minify an input stream of Javascript, writing to an output stream."""

    def __init__(self, instream=None, outstream=None):
        """Init class."""
        self.ins, self.outs = instream, outstream

    def minify(self, instream=None, outstream=None):
        """Minify Javascript using StringIO."""
        if instream and outstream:
            self.ins, self.outs = instream, outstream
        write, read = self.outs.write, self.ins.read
        space_strings = ("abcdefghijklmnopqrstuvwxyz"
                         "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_$\\")
        starters, enders = '{[(+-', '}])+-"\''
        newlinestart_strings = starters + space_strings
        newlineend_strings = enders + space_strings
        do_newline, do_space = False, False
        doing_single_comment, doing_multi_comment = False, False
        previous_before_comment, in_quote = '', ''
        in_re, quote_buf = False, []
        previous = read(1)
        next1 = read(1)
        if previous == '/':
            if next1 == '/':
                doing_single_comment = True
            elif next1 == '*':
                doing_multi_comment = True
            else:
                write(previous)
        elif not previous:
            return
        elif previous >= '!':
            if previous in "'\"":
                in_quote = previous
            write(previous)
            previous_non_space = previous
        else:
            previous_non_space = ' '
        if not next1:
            return
        while True:
            next2 = read(1)
            if not next2:
                last = next1.strip()
                conditional_1 = (doing_single_comment or doing_multi_comment)
                if not conditional_1 and last not in ('', '/'):
                    write(last)
                break
            if doing_multi_comment:
                if next1 == '*' and next2 == '/':
                    doing_multi_comment = False
                    next2 = read(1)
            elif doing_single_comment:
                if next1 in '\r\n':
                    doing_single_comment = False
                    while next2 in '\r\n':
                        next2 = read(1)
                        if not next2:
                            break
                    if previous_before_comment in ')}]':
                        do_newline = True
                    elif previous_before_comment in space_strings:
                        write('\n')
            elif in_quote:
                quote_buf.append(next1)

                if next1 == in_quote:
                    numslashes = 0
                    for c in reversed(quote_buf[:-1]):
                        if c != '\\':
                            break
                        else:
                            numslashes += 1
                    if numslashes % 2 == 0:
                        in_quote = ''
                        write(''.join(quote_buf))
            elif next1 in '\r\n':
                conditional_2 = previous_non_space in newlineend_strings
                if conditional_2 or previous_non_space > '~':
                    while 1:
                        if next2 < '!':
                            next2 = read(1)
                            if not next2:
                                break
                        else:
                            conditional_3 = next2 in newlinestart_strings
                            if conditional_3 or next2 > '~' or next2 == '/':
                                do_newline = True
                            break
            elif next1 < '!' and not in_re:
                conditional_4 = next2 in space_strings or next2 > '~'
                conditional_5 = previous_non_space in space_strings
                conditional_6 = previous_non_space > '~'
                if (conditional_5 or conditional_6) and (conditional_4):
                    do_space = True
            elif next1 == '/':
                if in_re:
                    if previous != '\\':
                        in_re = False
                    write('/')
                elif next2 == '/':
                    doing_single_comment = True
                    previous_before_comment = previous_non_space
                elif next2 == '*':
                    doing_multi_comment = True
                else:
                    in_re = previous_non_space in '(,=:[?!&|'
                    write('/')
            else:
                if do_space:
                    do_space = False
                    write(' ')
                if do_newline:
                    write('\n')
                    do_newline = False
                write(next1)
                if not in_re and next1 in "'\"":
                    in_quote = next1
                    quote_buf = []
            previous = next1
            next1 = next2
            if previous >= '!':
                previous_non_space = previous


def js_minify(js):
    """Minify a JavaScript string."""
    js = remove_commented_lines(js)
    js = js_minify_keep_comments(js)
    return js.strip()


##############################################################################


def process_multiple_files(file_path, watch=False, wrap=False, timestamp=False,
        comments=False, sort=False, overwrite=False, gzip=False, prefix='',
        add_hash=False):
    """Process multiple CSS, JS, HTML files with multiprocessing."""
    log.debug("Process {} is Compressing {}.".format(os.getpid(), file_path))
    if watch:
        previous = int(os.stat(file_path).st_mtime)
        log.info("Process {} is Watching {}.".format(os.getpid(), file_path))
        while True:
            actual = int(os.stat(file_path).st_mtime)
            if previous == actual:
                sleep(60)
            else:
                previous = actual
                log.debug("Modification detected on {0}.".format(file_path))
                check_working_folder(os.path.dirname(file_path))
                if file_path.endswith(".css"):
                    process_single_css_file(file_path, wrap=wrap, timestamp=timestamp,
                        comments=comments, sort=sort, overwrite=overwrite, gzip=gzip,
                        prefix=prefix, add_hash=add_hash)
                elif file_path.endswith(".js"):
                    process_single_js_file(file_path, timestamp=timestamp,
                        overwrite=overwrite, gzip=gzip)
                else:
                    process_single_html_file(file_path, comments=comments,
                        overwrite=overwrite, prefix=prefix, add_hash=add_hash)
    else:
        if file_path.endswith(".css"):
            process_single_css_file(file_path, wrap=wrap, timestamp=timestamp,
                comments=comments, sort=sort, overwrite=overwrite, gzip=gzip,
                prefix=prefix, add_hash=add_hash)
        elif file_path.endswith(".js"):
            process_single_js_file(file_path, timestamp=timestamp,
                overwrite=overwrite, gzip=gzip)
        else:
            process_single_html_file(file_path, comments=comments,
                overwrite=overwrite, prefix=prefix, add_hash=add_hash)


def prefixer_extensioner(file_path, old, new, file_content=None, prefix='', add_hash=False):
    """Take a file path and safely preppend a prefix and change extension.

    This is needed because filepath.replace('.foo', '.bar') sometimes may
    replace '/folder.foo/file.foo' into '/folder.bar/file.bar' wrong!.
    >>> prefixer_extensioner('/tmp/test.js', '.js', '.min.js')
    '/tmp/test.min.js'
    """
    log.debug("Prepending '{}' Prefix to {}.".format(new.upper(), file_path))
    extension = os.path.splitext(file_path)[1].lower().replace(old, new)
    filenames = os.path.splitext(os.path.basename(file_path))[0]
    filenames = prefix + filenames if prefix else filenames
    if add_hash and file_content:  # http://stackoverflow.com/a/25568916
        filenames += "-" + sha1(file_content.encode("utf-8")).hexdigest()[:11]
        log.debug("Appending SHA1 HEX-Digest Hash to '{}'.".format(file_path))
    dir_names = os.path.dirname(file_path)
    file_path = os.path.join(dir_names, filenames + extension)
    return file_path


def process_single_css_file(css_file_path, wrap=False, timestamp=False,
        comments=False, sort=False, overwrite=False, gzip=False,
        prefix='', add_hash=False, output_path=None):
    """Process a single CSS file."""
    log.info("Processing CSS file: {0}.".format(css_file_path))
    with open(css_file_path, **open_utf8sig_kw) as css_file:
        original_css = css_file.read()
    log.debug("INPUT: Reading CSS file {}.".format(css_file_path))
    minified_css = css_minify(original_css, wrap=wrap,
                              comments=comments, sort=sort)
    if timestamp:
        taim = "/* {0} */ ".format(datetime.now().isoformat()[:-7].lower())
        minified_css = taim + minified_css
    if output_path is None:
        min_css_file_path = prefixer_extensioner(
            css_file_path, ".css", ".css" if overwrite else ".min.css",
            original_css, prefix=prefix, add_hash=add_hash)
        if only_on_py3(gzip):
            gz_file_path = prefixer_extensioner(
                css_file_path, ".css",
                ".css.gz" if overwrite else ".min.css.gz", original_css,
                prefix=prefix, add_hash=add_hash)
            log.debug("OUTPUT: Writing gZIP CSS Minified {}.".format(gz_file_path))
    else:
        min_css_file_path = gz_file_path = output_path
    if not only_on_py3(gzip) or output_path is None:
        # if a specific output path is requested, then write write only one output file
        with open(min_css_file_path, "w", **open_utf8_kw) as output_file:
            output_file.write(minified_css)
    if only_on_py3(gzip):
        with gzip.open(gz_file_path, "wt", **open_utf8_kw) as output_gz:
            output_gz.write(minified_css)
    log.debug("OUTPUT: Writing CSS Minified {0}.".format(min_css_file_path))
    return min_css_file_path


def process_single_html_file(html_file_path, comments=False,
        overwrite=False, prefix='', add_hash=False, output_path=None):
    """Process a single HTML file."""
    log.info("Processing HTML file: {0}.".format(html_file_path))
    with open(html_file_path, **open_utf8sig_kw) as html_file:
        minified_html = html_minify(html_file.read(),
        comments=only_on_py3(comments))
    log.debug("INPUT: Reading HTML file {0}.".format(html_file_path))
    if output_path is None:
        html_file_path = prefixer_extensioner(
            html_file_path, ".html" if overwrite else ".htm", ".html",
            prefix=prefix, add_hash=add_hash)
    else:
        html_file_path = output_path
    with open(html_file_path, "w", **open_utf8_kw) as output_file:
        output_file.write(minified_html)
    log.debug("OUTPUT: Writing HTML Minified {0}.".format(html_file_path))
    return html_file_path


def process_single_js_file(js_file_path, timestamp=False,
        overwrite=False, gzip=False, output_path=None):
    """Process a single JS file."""
    log.info("Processing JS file: {0}.".format(js_file_path))
    with open(js_file_path, **open_utf8sig_kw) as js_file:
        original_js = js_file.read()
    log.debug("INPUT: Reading JS file {0}.".format(js_file_path))
    minified_js = js_minify(original_js)
    if timestamp:
        taim = "/* {} */ ".format(datetime.now().isoformat()[:-7].lower())
        minified_js = taim + minified_js
    if output_path is None:
        min_js_file_path = prefixer_extensioner(
            js_file_path, ".js", ".js" if overwrite else ".min.js",
            original_js)
        if only_on_py3(gzip):
            gz_file_path = prefixer_extensioner(
                js_file_path, ".js", ".js.gz" if overwrite else ".min.js.gz",
                original_js)
            log.debug("OUTPUT: Writing gZIP JS Minified {}.".format(gz_file_path))
    else:
        min_js_file_path = gz_file_path = output_path
    if not only_on_py3(gzip) or output_path is None:
        # if a specific output path is requested, then write write only one output file
        with open(min_js_file_path, "w", **open_utf8_kw) as output_file:
           output_file.write(minified_js)
    if only_on_py3(gzip):
        with gzip.open(gz_file_path, "wt", **open_utf8_kw) as output_gz:
            output_gz.write(minified_js)
    log.debug("OUTPUT: Writing JS Minified {0}.".format(min_js_file_path))
    return min_js_file_path


def only_on_py3(boolean_argument=True):
    """Deprecate features if not using Python >= 3, to motivate migration."""
    if isinstance(boolean_argument, (tuple, list)):  # argument is iterable.
        boolean_argument = all(boolean_argument)
    else:  # argument is boolean, or evaluate as boolean, even if is not.
        boolean_argument = bool(boolean_argument)
    if sys.version_info.major >= 3:
        return boolean_argument  # good to go
    else:  # Migrate to python 3, is free and easy, get a virtualenv at least.
        log.critical("Feature only available on Python 3, feature ignored !.")
        log.debug("Please Migrate to Python 3 for better User Experience...")
        return False


def make_arguments_parser():
    """Build and return a command line agument parser."""
    parser = ArgumentParser(description=__doc__, epilog="""CSS-HTML-JS-Minify:
    Takes a file or folder full path string and process all CSS/HTML/JS found.
    If argument is not file/folder will fail. Check Updates works on Python3.
    Std-In to Std-Out is deprecated since it may fail with unicode characters.
    SHA1 HEX-Digest 11 Chars Hash on Filenames is used for Server Cache.
    CSS Properties are Alpha-Sorted, to help spot cloned ones, Selectors not.
    Watch works for whole folders, with minimum of ~60 Secs between runs.""")
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('fullpath', metavar='fullpath', type=str,
                        help='Full path to local file or folder.')
    parser.add_argument('--wrap', action='store_true',
                        help="Wrap output to ~80 chars per line, CSS only.")
    parser.add_argument('--prefix', type=str,
                        help="Prefix string to prepend on output filenames.")
    parser.add_argument('--timestamp', action='store_true',
                        help="Add a Time Stamp on all CSS/JS output files.")
    parser.add_argument('--quiet', action='store_true', help="Quiet, Silent.")
    parser.add_argument('--checkupdates', action='store_true',
                        help="Check for updates from internet while running.")
    parser.add_argument('--tests', action='store_true', help="Run Unit Tests.")
    parser.add_argument('--hash', action='store_true',
                        help="Add SHA1 HEX-Digest 11chars Hash to Filenames.")
    parser.add_argument('--gzip', action='store_true',
                        help="GZIP Minified files as '*.gz', CSS/JS only.")
    parser.add_argument('--sort', action='store_true',
                        help="Alphabetically Sort CSS Properties, CSS only.")
    parser.add_argument('--comments', action='store_true',
                        help="Keep comments, CSS/HTML only (Not Recommended)")
    parser.add_argument('--overwrite', action='store_true',
                        help="Force overwrite all in-place (Not Recommended)")
    parser.add_argument('--after', type=str,
                        help="Command to execute after run (Experimental).")
    parser.add_argument('--before', type=str,
                        help="Command to execute before run (Experimental).")
    parser.add_argument('--watch', action='store_true', help="Watch changes.")
    parser.add_argument('--multiple', action='store_true',
                        help="Allow Multiple instances (Not Recommended).")
    # global args
    return parser.parse_args()


def prepare():
    make_logger("css-html-js-minify")  # AutoMagically make a Logger Log
    make_root_check_and_encoding_debug()  # AutoMagically Check Encodings/root
    set_process_name_and_cpu_priority("css-html-js-minify")  # set Name
    set_single_instance("css-html-js-minify")  # AutoMagically set Single Instance
    make_config("css-html-js-minify")  # AutoMagically make a JSON-based Config


def main():
    """Main Loop."""
    args = make_arguments_parser()
    check_for_updates() if args.checkupdates else log.debug("No Check Updates")
    if args.tests:
        testmod(verbose=True, report=True, exclude_empty=True)
        sys.exit(0)
    log.disable(log.CRITICAL) if args.quiet else log.debug("Max Logging ON")
    log.info(__doc__ + __version__)
    check_working_folder(os.path.dirname(args.fullpath))
    if os.path.isfile(args.fullpath) and args.fullpath.endswith(".css"):
        log.info("Target is a CSS File.")  # Work based on if argument is
        list_of_files = str(args.fullpath)  # file or folder, folder is slower.
        process_single_css_file(args.fullpath, wrap=args.wrap, timestamp=args.timestamp,
            comments=args.comments, sort=args.sort, overwrite=args.overwrite, gzip=args.gzip,
            prefix=args.prefix, add_hash=args.hash)
    elif os.path.isfile(args.fullpath) and args.fullpath.endswith(
            ".html" if args.overwrite else ".htm"):
        log.info("Target is HTML File.")
        list_of_files = str(args.fullpath)
        process_single_html_file(args.fullpath, comments=args.comments,
            overwrite=args.overwrite, prefix=args.prefix, add_hash=args.hash)
    elif os.path.isfile(args.fullpath) and args.fullpath.endswith(".js"):
        log.info("Target is a JS File.")
        list_of_files = str(args.fullpath)
        process_single_js_file(args.fullpath, timestamp=args.timestamp,
            overwrite=args.overwrite, gzip=args.gzip)
    elif os.path.isdir(args.fullpath):
        log.info("Target is a Folder with CSS, HTML, JS files !.")
        log.warning("Processing a whole Folder may take some time...")
        list_of_files = walkdir_to_filelist(
            args.fullpath,
            (".css", ".js", ".html" if args.overwrite else ".htm"),
            (".min.css", ".min.js", ".htm" if args.overwrite else ".html"))
        log.info('Total Maximum CPUs used: ~{0} Cores.'.format(cpu_count()))
        pool = Pool(cpu_count())  # Multiprocessing Async
        pool.map_async(partial(process_multiple_files, watch=args.watch,
                wrap=args.wrap, timestamp=args.timestamp, comments=args.comments,
                sort=args.sort, overwrite=args.overwrite, gzip=args.gzip,
                prefix=args.prefix, add_hash=args.hash),
            list_of_files)
        pool.close()
        pool.join()
    else:
        log.critical("File or folder not found,or cant be read,or I/O Error.")
        sys.exit(1)
    if only_on_py3((args.after, getoutput)):
        log.info(getoutput(str(args.after)))
    log.info('\n {0} \n Files Processed: {1}.'.format('-' * 80, list_of_files))
    log.info('Number of Files Processed: {0}.'.format(
        len(list_of_files) if isinstance(list_of_files, tuple) else 1))
    make_post_execution_message()
