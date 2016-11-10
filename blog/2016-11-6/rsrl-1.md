---
title: RSRL开发记录（一）
create: 2016.11.6
modified: 2016.11.6
tags: RSRL
---

# RSRL开发记录（一）
深觉自己姿势水平还是太低，许多东西并没有学到家就准备搞东西，`ne2d`就是一个典型的例子吧。虽然以后可能还会继续，但是现在先写个软渲染器来熟悉一些基础知识。

项目开在了GitHub和Git@OSC上，欢迎围观：
GitHub: <https://github.com/riteme/RSRL>
Git@OSC: <http://git.oschina.net/riteme/RSRL>

所谓乎开发记录，就是记录一点有点价值的东西，各位随意看看。

## 颜色运算
[Color.h](http://git.oschina.net/riteme/RSRL/blob/master/include/Color.h) & [Color.cpp](http://git.oschina.net/riteme/RSRL/blob/master/source/Color.cpp)

常见的屏幕颜色有四个分量：红($\mathrm{R}$)、绿($\mathrm{G}$)、蓝($\mathrm{B}$)和透明度($\mathrm{A}$)。通常这四个分量用`uint8_t`来记录，范围就是$0$至$255$。在计算机图形学中为了方便插值，通常都是用浮点数来存储的，范围为$0.0$至$1.0$。

计算一个颜色的反色可以用以下公式：
$$
\mathrm{R}^\prime = 1 - \mathrm{R} \\
\mathrm{G}^\prime = 1 - \mathrm{G} \\
\mathrm{B}^\prime = 1 - \mathrm{B}
$$

这里我们不考虑透明度。

另一个比较重要的就是Alpha混合，就是将两个颜色按照透明度混合，通常是这样计算的：
$$
\mathrm{R}^\prime = \mathrm{R}_1 \cdot \mathrm{A}_1 + \mathrm{R}_2 \cdot \mathrm{A}_2 \cdot (1 - \mathrm{A}_1) \\
\mathrm{G}^\prime = \mathrm{G}_1 \cdot \mathrm{A}_1 + \mathrm{G}_2 \cdot \mathrm{A}_2 \cdot (1 - \mathrm{A}_1) \\
\mathrm{B}^\prime = \mathrm{B}_1 \cdot \mathrm{A}_1 + \mathrm{B}_2 \cdot \mathrm{A}_2 \cdot (1 - \mathrm{A}_1) \\
\mathrm{A}^\prime = 1 - (1 - \mathrm{A}_1) \cdot (1 - \mathrm{A}_2)
$$

其中$\{\mathrm{R}_1,\;\mathrm{G}_1,\;\mathrm{B}_1,\;\mathrm{A}_1\}$是前景色，$\{\mathrm{R}_1,\;\mathrm{G}_1,\;\mathrm{B}_1,\;\mathrm{A}_1\}$是后景色。
同时，这个公式可以实现颜色的叠加顺序不同，最终的结果也会有所不同。

## 向量与矩阵
[Math.h](http://git.oschina.net/riteme/RSRL/blob/master/include/Math.h) & [Math.cpp](http://git.oschina.net/riteme/RSRL/blob/master/source/Math.cpp)

这里不在介绍什么是向量和矩阵了，这里至介绍一下为什么要使用矩阵。

首先我们的可能需要缩放一个向量，这可以使用矩阵来表示：
$$
\left[
\begin{matrix}
S_X & 0 & 0 \\
0 & S_Y & 0 \\
0 & 0 & S_Z
\end{matrix}
\right]
\cdot
\left(
\begin{matrix}
X \\
Y \\
Z
\end{matrix}
\right)
$$

如果是旋转，那么这样也可以（下面示例的是绕Z轴旋转）：
$$
\left[
\begin{matrix}
\cos\alpha & -\sin\alpha & 0 \\
\sin\alpha & \cos\alpha & 0 \\
0 & 0 & 1
\end{matrix}
\right]
\cdot
\left(
\begin{matrix}
X \\
Y \\
Z
\end{matrix}
\right)
$$

对于绕X轴和绕Y轴的旋转可以类似的构造。
很多其它的线性变换都可以用矩阵来表示。当我们想进行多个变换的时候，我们可以使用矩阵乘法来变为一个矩阵，这样就加速了复杂的变换。
但是平移向量出了一点意外，因为3维的矩阵无法表示平移变化。
为了统一它们，平移变化被加上了一维，使用四维矩阵来表示之：
$$
\left[
\begin{matrix}
1 & 0 & 0 & D_X \\
0 & 1 & 0 & D_Y \\
0 & 0 & 1 & D_Z \\
0 & 0 & 0 & 1
\end{matrix}
\right] \cdot
\left(
\begin{matrix}
X \\
Y \\
Z \\
1
\end{matrix}
\right)
$$

是不是非常巧妙？虽然向量和矩阵都变成了四维，但是这样我们就可以将所有的线性变换都用矩阵表示，并且可以利用矩阵乘法来加速变换。这也就是为什么矩阵在计算机图形学中十分重要的原因之一了。
