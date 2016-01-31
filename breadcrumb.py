# breadcrumb.py处理以下内容
# breadcrumb


class BreadcrumbNode(object):

    """表示导航栏的一个节点"""

    NORMAL_TEMPLATE = "<li><a href=\"{href}\">{text}</a></li>"
    ALIVE_TEMPLATE = "<li class=\"active\">{text}</li>"

    def __init__(self, text, href, is_alive=False):
        super(BreadcrumbNode, self).__init__()
        self.text = text
        self.href = href
        self.is_alive = is_alive

    def __str__(self):
        if self.is_alive:
            return BreadcrumbNode.ALIVE_TEMPLATE.format(
                text=self.text
            )
        else:
            return BreadcrumbNode.NORMAL_TEMPLATE.format(
                href=self.href,
                text=self.text
            )


class Breadcrumb(object):

    """表示导航栏"""

    BREADCRUMB_TEMPLATE = "<ul class=\"breadcrumb\">{code}</ul>"

    def __init__(self):
        super(Breadcrumb, self).__init__()
        self.nodes = []

    def append(self, text, href, is_alive=False):
        self.nodes.append(BreadcrumbNode(text, href, is_alive))

    def __str__(self):
        nodes = [str(node) for node in self.nodes]

        return Breadcrumb.BREADCRUMB_TEMPLATE.format(
            code="".join(nodes)
        )
