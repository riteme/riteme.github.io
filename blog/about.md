---
title: 关于
create: 2016.12.13
modified: 2022.2.12
tags: About
location: ..
---

[TOC]

## 关于
*riteme* 来自 <span style="color:gray">CJP</span>→<span style="color:gray">GY</span>→<span style="color:gray">HNSDFZ</span>→**FDU**。

### Past 2020

<img src="/assets/nscscc.png" alt="NSCSCC 2020" /><center>NSCSCC 2020: team <a href="https://github.com/NSCSCC-2020-Fudan/FDU1.1-NSCSCC">FDU 1.1</a></center>

<br><img src="/assets/cbox2-720p-10k-8.png" alt="Cornell Box" /><center><i>Cornell Box</i>. Powered by <a href="https://github.com/CMU-Graphics/Scotty3D">Scotty3D</a>.</center>

<br><picture><source srcset="/assets/generals.apng" type="image/apng" /><img src="https://gitee.com/riteme/blogimg/raw/master/generals.gif" /></picture><center><a href="http://generals.io/replays/Btj7sy8CD">http://generals.io/replays/Btj7sy8CD</a></center>

### `sitegen.py`

使用 `Python 3` 编写的不清真站点生成器。
参见左侧栏 ["GitHub 项目"](https://github.com/riteme/riteme.github.io)。

需要的依赖：

* Python 3 (>= 3.7)
* Python Markdown (== 2.6.11)
* Pygments (用于提供代码高亮)
* css-html-js-minify (压缩 HTML 源码)
* Beautiful Soup 4
* lxml

```python
pip install markdown==2.6.11 pygments css-html-js-minify bs4 lxml
```

`sitegen.py` 基本结构

* `utility`: 基础辅助设施
* `navigater`: 辅助文件夹导航。
* `parser`: Markdown 阶段预处理特殊语法。
* `database`: 处理站点文章数据
* `logging`: 日志输出

可执行工具：

* `pagegen.py`: 用于生成单个页面。
* `sitegen.py`: 用于生成整个网站。

工具的配置参见 `preferences.py`

### Material Design
使用的是功能比较简单的 [Material Design Lite](http://getmdl.io/)，而且版本已经比较老了QAQ。

主题风格都是我自己 xjb 调的，本着能不用 JavaScript 就不用的态度，所以除了目录跳转，其余动画都是直接 `transition` qwq
目前页面上还是有一些已知的小问题，有些是老版本 MDL 的锅，实在是没精力换框架了 TAT。

### 数学公式
使用 [MathJax](http://www.mathjax.org/) 和 [KaTeX](http://khan.github.io/KaTeX/)。

~~以后计划抛弃笨重的 MathJax，换用清真的 KaTeX。~~
正在尝试 KaTeX......但现实很残酷，KaTeX 容错性实在不行，因此变成了浏览者可在 MathJax 和 KaTeX 之间二选一。
~~实际上 KaTeX 能够无错渲染的文章真的不多......~~ **KaTeX 0.10.0 版本大赞！**

### 站内搜索
使用 [Tipuesearch](http://www.tipue.com/search/)。

Tipuesearch 有个缺点就是需要浏览器将搜索数据下载下来。而这个文件通常很大。以后可能会考虑换成其它的东西。

### 评论
使用 [Gitment](https://github.com/imsun/gitment)。

自行魔改了下 JS 文件给汉化了。不知道现在 Gitment 自己有没有提供多语言支持。

评论系统的 GitHub OAuth 服务器换到了我自己的服务器上：<https://gh-oauth.riteme.site>，以防作者的服务器抽风 qwq

### 友链
欢迎互换友链 ~ ~ ~
想换友链的可以直接在评论里留言 ~ ~ ~

### 联系我
我的邮箱：<riteme@qq.com>
我的 GitHub：<https://github.com/riteme>
我的知乎：<https://www.zhihu.com/people/riteme>
