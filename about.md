---
title: 关于
create: 2016.12.13
modified: 2017.6.20
tags: About
---

## 关于
riteme来自HNSDFZ。

### The sitegen.py
使用`Python3`编写的不清真站点生成器。
参见左侧栏"[GitHub项目](https://github.com/riteme/riteme.github.io)"。

需要的依赖：

* Python 3 (>= 3.4)
* Python Markdown
* Pygments (用于提供代码高亮)
* Beautiful Soup 4

独立模块功能：

* `info`: 提取文档基本信息 (右上角)。
* `navigater`: 辅助文件夹导航。
* `parser`: Markdown阶段预处理特殊语法。
* `tag`: 标签生成。
* `tipuesearch`: 生成Tipuesearch的搜索数据。
* `tocer`: 提取并生成目录。

可执行工具：

* `pagegen.py`: 用于生成单个页面。
* `sitegen.py`: 用于生成整个网站。
* `setup.py`: 简单网站架设工具。

### The Material Design
使用的是功能比较简单的[Material Design Lite](http://getmdl.io/)。

### 数学公式
使用[MathJax](http://www.mathjax.org/)。

以后计划抛弃笨重的MathJax，换用清真的KaTeX。

### 站内搜索
使用[Tipuesearch](http://www.tipue.com/search/)。

Tipuesearch有个缺点就是需要浏览器将搜索数据下载下来。而这个文件通常很大。以后可能会考虑换成其它的东西。

### 评论
使用[Gitment](https://github.com/imsun/gitment)。

### 友链
欢迎互换友链~~~

### 联系我
我的邮箱：<riteme@qq.com>
我的GitHub：<https://github.com/riteme>
我的知乎：<https://www.zhihu.com/people/riteme>
