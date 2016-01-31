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
        super(PanelBeginSyntax, self, "\[\[\[[a-zA-Z]+\]\]\]").__init__()
        self._catcher = re.compile("\[\[\[([a-zA-Z]+)\]\]\]")
        self._template = """
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">{text}</h3>
          </div>
          <div class="panel-body">
        """

    def parse(self, source):
        # 获取标题
        title = self._catcher.match(source).group(1)

        return self._template.format(text=title)


class PanelEndSyntax(Syntax):

    """表示Panel语法的结束部分: [[[#]]]"""

    def __init__(self):
        super(PanelEndSyntax, self, "\[\[\[#\]\]\]").__init__()
        self._template = """
          </div>
        </div>
        """

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

    def load_all_syntax(self):
        """将本模块内的所有解析器载入"""
        for obj in dir():
            if isinstance(obj, Syntax) and obj is not Syntax:
                self._matcher.append(obj())

    def load_syntax(self, syntax):
        """载入指定的解析器
        @param syntax (derived Syntax) 解析器
        """
        assert isinstance(syntax, Syntax), "Must be a derived class of Syntax."

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
        info_matcher = re.compile("([a-zA-Z]+):(.*)")
        info = {}
        content = []

        for line in fp:
            if line.startswith("---"):
                flag = not flag
            if flag:
                match = info_matcher.match(line)
                info[match.group(1)] = match.group(2)
            else:
                for matcher in self._matcher:
                    if matcher.is_match(line):
                        content.append(matcher.parse(line))
                        break

        return (info, content)
