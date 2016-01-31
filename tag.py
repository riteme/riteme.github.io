# tag.py处理以下信息
# tags


class Tag(object):

    """表示一个标签"""

    def __init__(self, text):
        super(Tag, self).__init__()
        self.text = text
        self._style = "<span class=\"label label-default\">{tag}</span>"

    def __str__(self):
        return self._style.format(tag=self.text)


class TagGroup(object):

    """表示一个标签组"""

    def __init__(self):
        super(TagGroup, self).__init__()
        self.tags = []

    def __str__(self):
        code = [str(tag) for tag in self.tags]

        return " ".join(code)

    def append(self, text):
        if text.strip() == "":
            return

        self.tags.append(Tag(text))
