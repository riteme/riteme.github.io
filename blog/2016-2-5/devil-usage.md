---
title: DevIL快速入门
create: 2016.2.5
modified: 2016.2.5
tags: C/C++
      DevIL
      OpenGL
---
[TOC]
# DevIL快速入门
[DevIL](http://openil.sourceforge.net/)全名是“Developer's Image Library”，它是一个多功能的图像库，能过很方便地载入、修改和保存图片。
其原名是OpenIL，后来是因为SGI的要求才改名为DevIL[^devil-rename]。

[^devil-rename]: 官方说法在[这里](http://openil.sourceforge.net/about.php)

本文主要介绍DevIL载入和保存图片的功能。DevIL虽然有处理图片的功能，但并不够强，不如使用[Boost.GIL](http://www.boost.org/doc/libs/develop/libs/gil/doc/index.html)，
因此不介绍DevIL处理图片的功能。

## 特点
DevIL具有几个非常好的特性：

* 支持包括PNG，JPG，TGA等30多种图片格式。  
* 与OpenGL类似的API风格。  
* 十分轻巧  
* 有许多辅助函数（ilut）

## 安装
理论上安装DevIL不会很艰难。对于Ubuntu 用户而言，可以直接使用下列命令来安装：

```shell
sudo apt-get install libdevil-dev
```

具体的下载、编译、安装的页面[在此](http://openil.sourceforge.net/download.php)。

## 初始化
接下来正式介绍如何使用DevIL。首先，我们需要添加头文件：

```cpp
#include <IL/il.h>
```

一般情况下，动态链接的DevIL会自动加载，不必调用特定的函数。但在某些情况下可能不会。因此，为了兼容性，我们最好手动载入：

```cpp
// 在程序开始的地方
ilInit();
```

仅仅一行代码，并没有什么关系。

## 加载图片
DevIL中使用了和OpenGL一样的对象创建方式。为了加载图片，我们首先要创建一个图片对象：

```cpp
ILuint image = 0;
ilGenImages(1, &image);
assert(image != 0);  // 检查是否创建成功
```

也许你会发现第二行非常熟悉，确实和OpenGL中创建缓冲区的调用长得非常像，因此很多使用OpenGL的开发者能很快上手。

当然，你如果觉得这还麻烦了，可以只创建一个：

```cpp
ILuint image = ilGenImage();
```

就像OpenGL一样，需要绑定当前的图片对象。绑定后，所有的操作都是在此图片对象上的，除非解绑：

```cpp
ilBindImage(image);

// ...

ilBingImage(0);  // 解绑图片对象
```

绑定好图片对象后，就可以直接使用`ilLoad`函数来加载图片了：

```
ilLoad(IL_PNG, "sample.png");
```

上面的`IL_PNG`是指定图片格式为PNG。  
当然，可以使用更简单的`ilLoadImage`：

```cpp
ilLoadImage("sample.png");
```

使用`ilLoadImage`就不需要手动指定图片格式了，DevIL会自动检测。

我们可以使用`ilGetError`来查看错误。如果加载过程中没有出错，`ilGetError`会返回`IL_NO_ERROR`。

```cpp
assert(ilGetError() == IL_NO_ERROR);
```

[[[注意]]]
当你不需要再使用图片对象时，应及时使用`ilDeleteImage`删除：

```
ilDeleteImage(image);       // 删除单个图片对象
ilDeleteImages(1, &image);  // 当然也可以批量删除
```
[[[#]]]

## 创建材质
加载完图片后，还只是将数据托管在DevIL内部。为了能够将数据提供给OpenGL或DirectX来创建材质，我们使用`ilGetData()`。

同时，我们还需获取图片的相关的信息，如宽度、高度、图片存储格式等等，这些都可以使用`ilGetInteger`来获取。

下面是在OpenGL中创建材质的过程：

```cpp
ilBindImage(image);                               // 绑定当前图片对象
GLint    width  = ilGetInteger(IL_IMAGE_WIDTH);   // 获取图片宽度
GLint    height = ilGetInteger(IL_IMAGE_HEIGHT);  // 获取图片高度
GLenum   format = ilGetInteger(IL_IMAGE_FORMAT);  // 获取图片像素格式
ILubyte *ptr    = ilGetData();                    // 获取图片数据的指针
ilBindImage(0);

// 创建材质
glTexImage2D(GL_TEXTURE_2D, 0, format, width, height, 0, format, GL_UNSIGNED_BYTE, ptr);
```

[[[提示]]]
DevIL中可以获取很多图片的信息，除了宽度、高度和像素格式外，还可以获取色深（<code>IL_IMAGE_DEPTH</code>）、
图片数据的大小（<code>IL_IMAGE_SIZE_OF_DATA</code>）、BPP（”Bytes Per Pixel“，每个像素所占字节数，<code>IL_IMAGE_BPP</code>或<code>IL_IMAGE_BYTES_PER_PIXEL</code>）、
Bit Per Pixel（每个像素所占位数，<code>IL_IMAGE_BITS_PER_PIXEL</code>）、图片格式（<code>IL_IMAGE_TYPE</code>）、
水平/竖直平移量（<code>IL_IMAGE_OFFX</code>和<code>IL_IMAGE_OFFY</code>）、图片原点（<code>IL_IMAGE_ORIGIN</code>）、
颜色通道数（<code>IL_IMAGE_CHANNELS</code>）等。
[[[#]]]

[[[提示]]]
在上面的示例中，图片的像素格式被直接传到OpenGL的函数中是可以的，因为DevIL对应的值和OpenGL规定的是一样的，不会有问题。<br/>
对于DirectX，需要手写<code>switch</code>来切换。
[[[#]]]

## 保存图片
DevIL中保存图片很简单，只需要先绑定图片对象，指定保存路径就可直接保存。DevIL会自动通过文件后缀名来确定图片格式。

```cpp
ilBindImage(image);
ilSaveImage("output.png");
ilBindImage(0);
```

可是我们并没有对图片做什么处理啊，保存它有什么用？确实，我们不会去用DevIL来做什么特效。但有一个场景却很常用，就是保存截图。

对于OpenGL，DevIL的工具库`ilut`已经帮我们做到了这一点。我们可以非常简单的写出保存截图的函数：

```cpp
#define ILUT_USE_OPENGL  // 通知ilut使用OpenGL
#include <IL/ilut.h>

// 保存截图
bool TakeScreenshot(const std::string &filepath) {
    ILuint image = ilGenImage();    
    ilBindImage(image);

    ilutGLScreen();                // 将当前OpenGL的颜色缓冲区的数据复制到image中
    ilSaveImage(filepath.data());  // 保存图片

    ilBindimage(0);
    ilDeleteImage(image);          // 记得释放图片对象

    return ilGetError() == IL_NO_ERROR;
}
```

没错，`ilutGLScreen`帮我们做了一切。只是非常可惜，截图的函数是OpenGL专属的。

但它是怎么工作的呢？我在GitHub上找到其源码，其过程非常简短。
下面是[GitHub](https://github.com/LuaDist/libdevil/blob/master/src-ILUT/src/ilut_opengl.c#L725)上的源码：

```cpp
//! Takes a screenshot of the current OpenGL window.
ILboolean ILAPIENTRY ilutGLScreen()
{
    ILuint  ViewPort[4];

    ilutCurImage = ilGetCurImage();
    if (ilutCurImage == NULL) {
        ilSetError(ILUT_ILLEGAL_OPERATION);
        return IL_FALSE;
    }

    glGetIntegerv(GL_VIEWPORT, (GLint*)ViewPort);

    if (!ilTexImage(ViewPort[2], ViewPort[3], 1, 3, IL_RGB, IL_UNSIGNED_BYTE, NULL))
        return IL_FALSE;  // Error already set.
    ilutCurImage->Origin = IL_ORIGIN_LOWER_LEFT;

    glPixelStorei(GL_PACK_ALIGNMENT, 1);
    glReadPixels(0, 0, ViewPort[2], ViewPort[3], GL_RGB, GL_UNSIGNED_BYTE, ilutCurImage->Data);

    return IL_TRUE;
}
```

我们来简要分析下这个过程在干什么。

首先是获取当前绑定的图片对象：

```cpp
ilutCurImage = ilGetCurImage();
if (ilutCurImage == NULL) {  // 检查并报错
    ilSetError(ILUT_ILLEGAL_OPERATION);
    return IL_FALSE;
}
```

然后获取当前OpenGL视图的信息：

```cpp
ILuint  ViewPort[4];

// ...

glGetIntegerv(GL_VIEWPORT, (GLint*)ViewPort);
```

此时，`ViewPort`中存储的分别是原点的X坐标和Y坐标，以及视图的宽度和高度。

根据获取来的视图信息，就需要调整图片的参数：

```cpp
// ilTexImage分别设置的是图片的宽度、高度、BPP、颜色通道数量、像素格式和数据格式
// 最后一个参数是图片数据的指针，但是图片数据要在之后读取，因此这里填nullptr
if (!ilTexImage(ViewPort[2], ViewPort[3], 1, 3, IL_RGB, IL_UNSIGNED_BYTE, NULL))
    return IL_FALSE;  // 设置失败
```

然后是从OpenGL的颜色缓冲中读取数组：

```cpp
// 因为OpenGL的原点是在左下角，而屏幕坐标的原点却在左上角，因此此处做点调整
ilutCurImage->Origin = IL_ORIGIN_LOWER_LEFT;

// 更改数据的内存对齐，避免读出来的数据格式不对
glPixelStorei(GL_PACK_ALIGNMENT, 1);

// 读出数据
glReadPixels(0, 0, ViewPort[2], ViewPort[3], GL_RGB, GL_UNSIGNED_BYTE, ilutCurImage->Data);
```

那么此时截图的方法已经出来了。对于DirectX，只需先创建图片对象并重设其参数，
然后读出颜色数据到图片中，最后保存即可。不过我不怎么熟悉DirectX，因此这里并没有给出DirectX的截图代码了。

## 结尾
从上面的文章我们已经了解了DevIL库，并且能够运用到实际工程中了。

事实上类似的库还有很多，例如[SOIL](http://www.lonesock.net/soil.html)和[FreeImage](http://freeimage.sourceforge.net/)。
如果你只是专注于一种格式，也许像[libpng](http://www.libpng.org/pub/png/libpng.html)和[libjpg](http://www.ijg.org/)更适合你。

因此在实际中，需要我们酌情选择合适的库来提高自己的开发效率。
