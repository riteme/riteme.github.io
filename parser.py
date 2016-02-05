# parser.py用于处理以下信息
# content

import re


class Syntax(object):

    """表示Markdown中特殊语法"""

    def __init__(self, syntax):
        super(Syntax, self).__init__()
        self.syntax = syntax
        self._matcher = re.compile(syntax)

    def is_match(self, source):
        return not self._matcher.match(source) is None

    def parse(self, source):
        """用于解析语法
        @param source (str) 表示源代码
        @return:
            (str) 返回解析后的HTML代码
        @remark:
            作为基类不提供实现
        """
        raise NotImplementedError("It's just a base class.")


class PanelBeginSyntax(Syntax):

    """表示Panel语法的声明部分: [[[Title]]]"""

    def __init__(self):
        super(PanelBeginSyntax, self).__init__("\[\[\[[\w\s]+\]\]\]")
        self._catcher = re.compile("\[\[\[([\w\s]+)\]\]\]")
        template_code = ['<div class="panel panel-info">',
                         '<div class="panel-heading">',
                         '<h3 class="panel-title">{text}</h3>',
                         '</div><div class="panel-body">'
                         ]

        self._template = "".join(template_code)

    def parse(self, source):
        # 获取标题
        title = self._catcher.match(source).group(1)

        return self._template.format(text=title)


class PanelEndSyntax(Syntax):

    """表示Panel语法的结束部分: [[[#]]]"""

    def __init__(self):
        super(PanelEndSyntax, self).__init__("\[\[\[#\]\]\]")
        self._template = "</div></div>"

    def parse(self, source):
        return self._template


class Parser(object):

    """表示Markdown的定制解析器
    remark:
        只解析自定语法，其他均保留
    """

    def __init__(self):
        super(Parser, self).__init__()
        self._matcher = []

    def load_syntax(self, syntax):
        """载入指定的解析器
        @param syntax (derived Syntax) 解析器
        """
        assert issubclass(syntax, Syntax), "Must be a derived class of Syntax."

        self._matcher.append(syntax())

    def process(self, fp):
        """处理Markdown
        @param fp (file-like) Markdown文件
        @return (dict(str, str), list(str)) 返回处理后的文件信息和内容
        @remark:
            此函数不会关闭文件，推荐使用`with`:
            ```python
            parser = Parser()
            parser.load_all_syntax()
            with open("test.md") as fp:
                parser.process(fp)
            ```
        """
        flag = False
        is_temporary = False
        panel_started = False
        info_matcher = re.compile("([a-zA-Z]+):\s*([\w\s\d+/\\\.]*)")
        info = {}
        content = []

        for line in fp:
            line = line[:-1]  # 忽略结尾换行

            if line.startswith("---"):
                flag = not flag
            elif line.startswith("[temporary]"):
                is_temporary = True
            elif flag:
                match = info_matcher.match(line)
                info[match.group(1)] = match.group(2)
            else:
                is_parsed = False

                for matcher in self._matcher:
                    if matcher.is_match(line):
                        is_parsed = True
                        content.append(matcher.parse(line))

                        if isinstance(matcher, PanelBeginSyntax):
                            panel_started = True
                        elif isinstance(matcher, PanelEndSyntax):
                            panel_started = False
                        break
                if not is_parsed:
                    if panel_started:
                        content[-1] += line
                        panel_started = False
                    else:
                        content.append(line)

        return (info, content, is_temporary)
