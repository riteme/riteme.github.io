---
title: 编译并使用bgfx
create: 2016.2.3
modified: 2016.2.4
tags: C/C++
      图形
      引擎
      bgfx
---
[TOC]
# 编译并使用bgfx
最近发现了一个似乎很好的图形引擎[bgfx](https://github.com/bkaradzic/bgfx)。
它是使用C++进行编写的，也有C99的接口，功能还比较丰富，支持DirectX 9/11和OpenGL 2.1+。
这是一个跨平台的库，我在Ubuntu 14.04上编译了成功了。
编译过程十分简单。本文就介绍**Linux下**的编译过程。

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
使用<code>make</code>还可以生成其他版本的，其格式是：
```shell
make [平台]-[release/debug][32/64]
```
例如，如果要生成32位的bgfx，使用以下命令：
```shell
make linux-release32
```
[[[#]]]

如果编译过程中没有报错，那么在`.build/`文件夹下会有对应的编译后的文件。

## 运行样例
bgfx提供了很多样例，编译后的样例在`.build/`对应的文件夹下(我的就在`.build/linux64_gcc/bin/`下），在目前bgfx没有什么教程的情况下是很好的学习资料。
由于样例需要很多资源文件（如着色器、材质之类的），而它们都在`exmaples/runtime`目录下，
因此需要在`exmaples/runtime`目录下用相对路径来运行。

首先我们切换到样例的目录。对我而言，使用以下命令：

```shell
cd .build/linux64_gcc/bin/
```

如果你编译的是32位，将上面的64改成32即可。

然后使用`ls`命令查看样例，可以看到目前有28个样例（包括`Hello, world!`）：

```shell
example-00-helloworldRelease         example-17-drawstressRelease
example-01-cubesRelease              example-18-iblRelease
example-02-metaballsRelease          example-19-oitRelease
example-03-raymarchRelease           example-20-nanovgRelease
example-04-meshRelease               example-21-deferredRelease
example-05-instancingRelease         example-22-windowsRelease
example-06-bumpRelease               example-23-vectordisplayRelease
example-07-callbackRelease           example-24-nbodyRelease
example-08-updateRelease             example-25-c99Release
example-09-hdrRelease                example-26-occlusionRelease
example-10-fontRelease               example-27-terrainRelease
example-11-fontsdfRelease            geometrycRelease
example-12-lodRelease                libbgfxRelease.a
example-13-stencilRelease            libbgfx-shared-libRelease.so
example-14-shadowvolumesRelease      libexample-commonRelease.a
example-15-shadowmaps-simpleRelease  shadercRelease
example-16-shadowmapsRelease         texturecRelease
```

可以看到每个样例都十分具有代表性，今后的学习就从它们开始。

同时注意到，有两个`.a`的静态库和一个`.so`的动态库，我们可以用它们来编译程序。

然而并不是在这里运行样例，我们要回到`runtime`目录来运行：

```shell
cd ../../../examples/runtime
```

假如要运行`00-helloworld`，使用以下命令：

```shell
../../.build/linux64_gcc/bin/example-00-helloworldRelease
```

如果不出意外，能看到以下窗口（图片来自`bgfx document`）：

![bgfx helloworld](https://github.com/bkaradzic/bgfx/raw/master/examples/00-helloworld/screenshot.png)

[bgfx的文档](https://bkaradzic.github.io/bgfx/examples.html)也给出了样例的列表。

## 编译我们自己的bgfx程序
为了通用性，这里使用最基础的终端编译的方法，我们直接用`g++`进行编译。

首先，我们创建一个目录来存放我们的程序：

```shell
mkdir my-first-bgfx
cd my-first-bgfx
```

然后将bgfx的静态库复制过来：

```shell
cp [bgfx的目录]/.build/linux64_gcc/bin/*.a .
```

这时目录下会多出两个`.a`文件： `libbgfxRelease.a`和`libexample-commonRelease.a`  
[[[静态库 vs 动态库]]]
我们在这里选用了静态库，而不是动态库，是考虑了用户的原因。  
因为bgfx没有什么很方便的安装方法，使用静态库就可以避免安装的过程，尽可能少的对用户的系统进行修改。  
当然，使用静态库会增大程序体积。静态链接后，我们的bgfx程序会有3MB多...
[[[#]]]

然后需要将bgfx及其依赖库的bx的头文件给复制进来。为了方便，我们还将bgfx用于样例的common库也复制进来：

```shell
cp -rf [bgfx的目录]/include/* .         # bgfx
cp -rf [bgfx的目录]/examples/common/ .  # bgfx-common
cp -rf [bx的目录]/include/* .           # bx
```

下面我们来照着bgfx的`hello, world`来写第一个程序。我们将会在窗口的左上角打出`Hello, world!`的字样：

创建程序`main.cpp`：

```shell
touch main.cpp
[使用你的编辑器] main.cpp
```

首先添加头文件：

```cpp
#include <cstdint>  // uint32_t

#include "bgfx/bgfx.h"      // bgfx
#include "common/common.h"  // bgfx-common
```

然后添加`_main_`函数。注意之所以是`_main_`而不是`main`，是因为bgfx的common库为了更好的处理以已经将`main`实现了，
于是设置`_main_`作为程序入口。

```cpp
int _main_(int argc, char *argv[]) {
    /* 代码 */
}
```

在`_main_`函数内，我们先做一些设定：

```cpp
uint32_t width  = 1280;              // 窗口宽度
uint32_t height = 720;               // 窗口高度
uint32_t debug  = BGFX_DEBUG_TEXT;   // debug模式开启，可以直接在窗口输出文字
uint32_t reset  = BGFX_RESET_VSYNC;  // 设置垂直同步
```

[[[注意]]]
似乎<code>width</code>和<code>height</code>的设置是没有用的，似乎无论设为多少，打开后都会变成<code>1280x720</code>，我也不知道是为什么...</br>
如果你也出现了这种情况，不要惊慌，不要害怕...
[[[#]]]

下面是加载bgfx：

```cpp
bgfx::init();                             // 载入
bgfx::reset(width, height, reset);        // 设置
bgfx::setDebug(debug);                    // 启用调试
bgfx::setViewClear(                       // 设置清空的状态
    0,                                    // bgfx中有View的概念，默认情况下是View 0
    BGFX_CLEAR_COLOR | BGFX_CLEAR_DEPTH,  // 表示要清空颜色缓冲和深度缓冲
    0xFFFFFFFF,                           // 颜色缓冲的清空值，0xFFFFFFFF是白色
    1.0f,                                 // 深度缓冲的清空值，默认为1.0f
    0                                     // 模板缓冲的清空值，默认为0
);
```

接下来就是渲染了，我们使用一个循环同时处理事件和渲染：

```cpp
// entry::processEvents是common库一个很方便的函数
// 它能帮我们处理几乎所有的窗口事件。
// 如果窗口大小有变化，width和height的值就会变化
// 如果窗口被关闭，就会返回true
while (not entry::processEvents(width, height, debug, reset)) {
    bgfx::setViewRect(0, 0, 0, width, height);  // 由于窗口大小会变化，因此这里要重新设置

    bgfx::touch(0);  // 切换到View 0

    bgfx::dbgTextClear();                                                      // 清空调试输出的文字
    bgfx::dbgTextPrintf(0, 0, 0x4F, "Hello, world!");                          // 打印"Hello, world!"
    bgfx::dbgTextPrintf(0, 1, 0x4F, "width = %d, height = %d", width, height); // 输出窗口大小

    bgfx::frame();  // 提交所有的渲染操作，准备切换到下一帧
}
```

[[[注意]]]
在函数<code>bgfx::dbgTextPrintf</code>中，第三个参数是设置文字的前景色和背景色。
其中，bgfx用<code>0-F</code>作为颜色的标记。在上面两位的十六进制数中，第一个指定背景色，第二个制定前景色。
这里将这些颜色标记列出来：
0: 无色
1: <font style="color: #CC0000">暗红色</font>  2: <font style="color: #4E9A06">暗绿色</font>  3: <font style="color: #C4A000">黄色<font style="color: #FFFFFF">，</font></font>
4: <font style="color: #3465A4">蓝色<font style="color: #FFFFFF">，</font></font>  5: <font style="color: #75507B">紫色<font style="color: #FFFFFF">，</font></font>  6: <font style="color: #06989A">深蓝色</font>
7: <font style="color: #D3D7CF; background: #000000;">灰色</font><font style="color: #FFFFFF">，</font>  8: <font style="color: #555753">深灰色</font>  9: <font style="color: #EF2929">红色<font style="color: #FFFFFF">，</font></font>
A: <font style="color: #8AE234">嫩绿色</font>  B: <font style="color: #FCE94F">米黄色</font>  C: <font style="color: #729FCF">浅蓝色</font>
D: <font style="color: #AD7FA8">浅紫色</font>  E: <font style="color: #34E2E2">天蓝色</font>  F: <font style="color: #FFFFFF; background: #000000;">白色</font>
[[[#]]]

最后，当窗口关闭时，`entry::processEvents`就会返回`true`，于是退出循环，最后要退出bgfx：

```cpp
bgfx::shutdown();
```

现在来编译`main.cpp`：

```shell
g++ -std=c++11 main.cpp -o exec -L. -lbgfxRelease -lexample-commonRelease -lpthread -lGL -lX11
```

注意编译器要打开C\+\+11支持，如果你的编译器不支持C\+\+11，那我很好奇你是怎么把bgfx编译成功的。  
`-lpthread`、`-lGL`和`-lX11`是bgfx依赖的库，分别是POSIX线程库、OpenGL库和X11库。

如果没有错误报出，运行`exec`就能看到以下窗口：

```shell
./exec
```

![helloworld](http://git.oschina.net/riteme/blogimg/raw/master/learn-bgfx/learn-bgfx-1.png)

如果你出现了什么意外，下面贴出了完整的程序用于对照：

```cpp
#include <cstdint>  // uint32_t

#include "bgfx/bgfx.h"
#include "common/common.h"

int _main_(int argc, char *argv[]) {
    uint32_t width = 1280;
    uint32_t height = 720;
    uint32_t debug = BGFX_DEBUG_TEXT;
    uint32_t reset = BGFX_RESET_VSYNC;

    bgfx::init();
    bgfx::reset(width, height, reset);
    bgfx::setDebug(debug);
    bgfx::setViewClear(
        0,
        BGFX_CLEAR_COLOR | BGFX_CLEAR_DEPTH,
        0xFFFFFFFF,
        1.0f,
        0
    );

    while (not entry::processEvents(width, height, debug, reset)) {
        bgfx::setViewRect(0, 0, 0, width, height);

        bgfx::touch(0);

        bgfx::dbgTextClear();
        bgfx::dbgTextPrintf(0, 0, 0x4F, "Hello, world!");
        bgfx::dbgTextPrintf(0, 1, 0x4F, "width = %d, height = %d", width, height);

        bgfx::frame();
    }

    bgfx::shutdown();
}
```

至此，我们的第一个bgfx程序就完成了。解决了编译的问题，就可以继续学习使用bgfx了。
