# 用于生成tipuesearch的搜索数据

import json

indices = {}

ITEM_TEMPLATE = "{\"title\": \"%s\",\"text\": \"%s\",\"tags\": \"%s\",\"url\": \"%s\"}"
INDEX_TEMPLATE = "var tipuesearch = {\"pages\": [%s]};"


def load_index(filepath):
    """载入索引数据
    filepath (str): 索引位置，JSON文件
    """

    global indices
    with open(filepath) as reader:
        indices = json.load(reader)


def save_index(js_file, json_file):
    """保存索引数据
    js_file (str): tipuesearch使用的数据位置
    json_file (str): 索引数据的位置
    """

    global indices

    with open(js_file, "w") as writer:
        writer.write(generate_index())

    with open(json_file, "w") as writer:
        writer.write(json.dumps(indices, sort_keys = True, indent = 0))


def add_index_info(title, text, tags, url):
    """添加索引数据
    title (str): 标题
    text (str): 用于显示在搜索结果的文本
    tag (list): 标签
    url (str): 链接（相对链接）
    """

    global indices

    if not title in indices:
        indices[title] = {
            "text": "",
            "tags": "",
            "url": ""
        }

    indices[title]["text"] = text
    indices[title]["tags"] = " ".join(tags)
    indices[title]["url"] = url


def generate_index():
    """生成索引数据
    """

    global indices

    data = []
    for key, value in indices.items():
        data.append((key, value))

    # 保证每次顺序不变，防止git多次更新
    data = sorted(data, key = lambda x: x[0])
    index_data = []
    for key, value in data:
        index_data.append(ITEM_TEMPLATE % (key, value["text"], value["tags"], value["url"]))

    return INDEX_TEMPLATE % (",\n".join(index_data))
