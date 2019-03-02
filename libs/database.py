# 处理整个站点的文章索引
# 元数据中 `index = false` 的文章将不会进入索引
# 负责输出至 JSON 数据库、Tipuesearch 搜索数据库和站点地图

import os
import json

from preferences import SITE_DOMAIN

indices = {}

TIPUESEARCH_ITEM_TEMPLATE = '{"title":"%s","tags":"%s","url":"%s","text":"%s"}'
TIPUESEARCH_TEMPLATE = 'var tipuesearch={"pages":[%s]}'


def load_index(filepath):
    """载入索引数据
    filepath (str): 索引位置，JSON 文件
    """

    global indices
    if not os.path.exists(filepath):
        with open(filepath, "w") as writer:
            writer.write("{}")
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

def add_index(title, url, text, meta):
    """添加索引数据
    title (str): 标题
    url (str): 链接（相对链接）
    text (str): 用于显示在搜索结果的文本
    meta (dict): Markdown 的元数据
    """

    global indices

    if title not in indices:
        indices[title] = {}

    indices[title]["text"] = text.replace("\"", " ")
    indices[title]["url"] = url
    indices[title]["meta"] = meta

def del_index(title):
    """删除索引数据
    title (str): 标题
    remark: 如果原本就没有索引数据，则无操作
    """

    global indices

    if title in indices:
        indices.pop(title)

def query_index(title):
    """查询索引数据
    title (str): 文章标题
    remark: 如果不存在则返回 None
    """
    
    global indices

    if title in indices:
        return indices[title]
    return

def save_json_index(filepath):
    """保存至 JSON 索引数据库
    filepath (str): JSON 文件的位置
    """

    global indices

    with open(filepath, "w") as writer:
        writer.write(json.dumps(indices, sort_keys=True, indent=2, ensure_ascii=False))

def _generate_tipuesearch_data():
    """生成索引数据
    """

    global indices

    return TIPUESEARCH_TEMPLATE % (",\n".join((
        TIPUESEARCH_ITEM_TEMPLATE % (title, ",".join(data["meta"]["tags"]), data["url"], data["text"])
        for title, data in sorted(indices.items(), key = lambda x: x[0])
    )))

def save_tipuesearch_index(filepath):
    """保存至 Tipuesearch 搜索数据库
    filepath (str): 搜索数据库的位置（JavaScript 文件）
    """

    with open(filepath, "w") as writer:
        writer.write(_generate_tipuesearch_data())

def save_text_sitemap(filepath):
    """保存至 TXT 格式的站点地图
    remark: 仅保存链接信息
    """

    global indices

    with open(filepath, "w") as writer:
        writer.write("\n".join(sorted(
            os.path.join(SITE_DOMAIN, data["url"]) for data in indices.values()
        )))

def save_xml_sitemap(filepath):
    """保存至 XML 格式的站点信息
    remark: 未实现
    """
    raise NotImplementedError