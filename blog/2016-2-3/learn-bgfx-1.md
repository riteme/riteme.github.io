[temporary]

---
title: 学习使用bgfx - 1
create: 2016.2.3
modified: 2016.2.3
tags: 图形 引擎 bgfx
---
# 学习使用bgfx (1)

[TOC]

最近发现了一个似乎很好的图形引擎[bgfx](https://github.com/bkaradzic/bgfx)。
它是使用C++进行编写的，也有C99的接口，功能还比较丰富，支持DirectX 9/11和OpenGL 2.1+。
这是一个跨平台的库，我在Ubuntu 14.04上编译了成功了。
编译过程十分简单。本文就介绍下编译过程。

## 编译
这里我只写了Linux的编译过程，其他平台我还没试过，具体参见[bgfx's document](https://bkaradzic.github.io/bgfx/build.html)。  
首先需要编译器支持，确保你的编译器满足下列要求：

* Clang 3.3及以上  
* GCC 4.6及以上

同时准备依赖库：

```shell
sudo apt-get install libgl1-mesa-dev x11proto-core-dev libx11-dev
```

然后从GitHub上下载源码。因为bgfx依赖于bx，因此我们还要下载bx：

```shell
cd ~/Downloads  # 下载到Downloads目录
git clone git://github.com/bkaradzic/bx.git
git clone git://github.com/bkaradzic/bgfx.git
cd bgfx  # 进入源码目录，准备编译
```

使用`make`生成工程：

```shell
make
```

接下来进行编译：

```shell
make linux-release64
```

[[[提示]]]
使用`make`还可以生成其他版本的，其格式是：

```shell
make [平台]-[release/debug][32/64]
```

例如，如果我要生成32位的bgfx，使用一下命令：

```shell
make linux-release32
```
[[[#]]]

## 运行
