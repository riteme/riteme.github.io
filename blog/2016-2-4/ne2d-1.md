---
title: 正式开始编写ne2d
create: 2016.2.4
modified: 2016.2.12
tags: C/C++
      ne2d
      图形
---
# 正式开始编写ne2d
![ne2d v0.2.2](http://git.oschina.net/riteme/blogimg/raw/master/ne2d/ne2d-start-1.png)

一直想找个好点的2D渲染引擎，但看了很多似乎都不合胃口，也许有点挑剔。之前看到的bgfx似乎也有点操蛋，毕竟操作上还是麻烦了点。
因此，**趁着时间还多，多造点轮子，学点东西**。索性开始自己做个适合的2D渲染引擎。

之前这个自制的渲染引擎[ne2d](https://github.com/riteme/ne2d)一直处于极其不稳定状态，动辄几千行代码的改动。
今天总算有个大致框架了。目前计划做成一个单纯的2D渲染引擎，不打算管平台相关的代码。
只要能够提供OpenGL上下文就能使其工作。

目前这个工程才刚刚起步，暂时还没法使用。

这里记录下目前的想法和进度：

基本功能：  

* [x] OpenGL 3.3 core profile  
* [x] Alpha支持
* [x] Layer抽象，支持图层深度
* [x] RenderObject，所有渲染对象实例化
* [ ] Sprite绘制材质
* [ ] 矩阵变换（使用[glm](https://github.com/g-truc/glm)）
* [ ] TrueType字体（SDL_ttf or raw Freetype?）

计划中的功能：  

* [ ] 动画
* [ ] `*.layout`文件载入图层（JSON or XML?）
* [ ] 自定Shader
* [ ] 粒子系统

至于不处理平台相关的代码，因为我觉得SDL做得比我好，我个人也是很喜欢SDL的接口风格的（只是SDL在渲染方面似乎并不怎么样...）。
所以所有的窗口创建、OpenGL上下文创建、事件管理......这些东西都交给SDL吧！当然你喜欢glfw也是可以的。

最后把GitHub repo放一下吧：

* [ne2d](https://github.com/riteme/ne2d): **理论上**是稳定版  
* [ne2d/develop](https://github.com/riteme/ne2d/tree/develop): **理论上**是最新版  
* [ne2d/unstable](https://github.com/riteme/ne2d/tree/unstable): ***激进***版

另外，欢迎有兴趣的同志**一起开发**！
