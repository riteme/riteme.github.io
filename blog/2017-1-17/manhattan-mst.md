---
title: 曼哈顿距离最小生成树
create: 2017.1.17
modified: 2017.1.17
tags: 最小生成树
      计算几何
---

[TOC]
# 曼哈顿距离最小生成树
## 问题
给你平面上的$n$个点，$n$个点之间两两连边，边权为两点间的曼哈顿距离，构成一张完全图。求这张完全图的最小生成树。

## 朴素算法
由于完全图的边数是$\Theta(n^2)$级别的，所以直接使用稀疏图的最小生成树算法将会得到$\Omega(n^2)$级别的算法。这是比较难以接受的。

## 平面划分
鉴于完全图边数十分之多，然而生成树上的边却只有$n - 1$条，是不是真正有用的边数也是$O(n)$级别的？

事实上确实如此，如果我们随意选择一个点作为中心$O$，用四条直线将平面划为八个对称的区域，如下图所示：

![r8](https://git.oschina.net/riteme/blogimg/raw/master/manhattan-mst/r8.svg)

上图中$R_1$到$R_8$就是被八等分出来的区域。

接下来我们将证明，对于每一个区域，只需要留下离$O$最近的点的连边，最后形成的图的最小生成树就是原图的最小生成树。

假设现在在区域$R_1$有两个点$A$和$B$，并且满足$|OA| \leqslant |OB|$。那么根据最小生成树的环切性质[^cut]，我们只需要证明$|OB| \geqslant |AB|$就可以了。在这里，$|AB|$表示$A$到$B$的曼哈顿距离。

[^cut]: 对于图上一个环，删去环上权重最大的边后的图的最小生成树与原图一致。证明在很多地方都有。

设$A(x_1, y_1)$和$B(x_2, y_2)$，我们需要考虑$4$种情况：

**情况2：**$x_1 \leqslant x_2, \;y_1 \leqslant y_2$

![situation-1](https://git.oschina.net/riteme/blogimg/raw/master/manhattan-mst/s1.svg)

此时有：
$$
|AB| = x_2 - x_1 + y_2 - y_1 \leqslant x_2 + y_2 = |OB|
$$

**情况2：**$x_2 \leqslant x_1, \;y_1 \leqslant y_2$

![situation-2](https://git.oschina.net/riteme/blogimg/raw/master/manhattan-mst/s2.svg)

此时有：
$$
|AB| = x_1 - x_2 + y_2 - y_1
$$

如果$|OB| \geqslant |AB|$，那么也就有$|OB| - |AB| \geqslant 0$，于是：
$$
\begin{aligned}
|OB| - |AB| & = x_2 + y_2 - x_1 + x_2 - y_2 + y_1 \\
& = 2x_2 - x_1 + y_1
\end{aligned}
$$

由于在区域$R_1$满足$x_1 \leqslant y_1$，所以上式大于等于$0$，即满足$|OB| \geqslant |AB|$。

**情况3：**$x_1 \leqslant x_2, \;y_2 \leqslant y_1$

![situation-3](https://git.oschina.net/riteme/blogimg/raw/master/manhattan-mst/s3.svg)

此时有：
$$
\begin{aligned}
|AB| & = x_2 - x_1 + y_1 - y_2 \\
|OB| - |AB| & = x_2 + y_2 - x_2 + x_1 - y_1 + y_2 \\
& = 2y_2 + x_1 - y_1
\end{aligned}
$$

由于$|OA| \leqslant |OB|$和$x_2 \leqslant y_2$，那么我们知道：
$$
x_1 + y_1 \leqslant x_2 + y_2 \Longrightarrow y_1 \leqslant x_2 + y_2 \leqslant 2y_2
$$

所以$|OB| \geqslant |AB|$。

**情况4：**$x_2 \leqslant x_1, \;y_2 \leqslant y_1$
![situation-4](https://git.oschina.net/riteme/blogimg/raw/master/manhattan-mst/s4.svg)

这种情况违反了$|OA| \leqslant |OB|$这个条件，故不考虑。

综上，在区域$R_1$内，只用保留离$O$最近的点的连边就可以了。

对于其它的区域，都可以通过对称或者旋转，从而变成$R_1$的情况。因此$8$个区域均满足这一性质。

这样一来，每个点只用连出$8$条边，然后在得到的图上使用稀疏图的最小生成树算法，就可得到原图的最小生成树。由于这张图的边数是$O(n)$的，所以如果我们使用Kruskal算法，我们的算法也就是$O(n \log n)$的。

一条边在上面的图中被两个端点都被计数了一次，所以最终的边数是不超过$4n$的。

## 求出最近点
上面的性质中还留下一个问题：如何求出每个区域内离$O$最近的点？

从之前的关于边数的讨论中可知，我们只用求$R_1$到$R_4$的最近点即可。此外，利用对称的性质，我们可以全部归结到在$R_1$求最近点的算法中，只需要提前做一个坐标的变换。下面也将只考虑$R_1$的算法。

考虑使用扫描线算法：将所有点按照$x$坐标升序排好序，$x$坐标相同的就按照$y$降序排序。然后从前往后扫描。我们将每个点按照$y - x$进行离散化（也就是经过该点的斜率为$1$的直线的纵截距）。对于某个点$i$而言，在以$i$为原点的$R_1$区域内点$j$满足$y_j - x_j \geqslant y_i - x_i$。而$R_1$内离$i$最近的点$j$满足$y_j + x_j$最小。因此我们可以使用简单的数据结构，如线段树或者树状数组，就可维护$[y - x, \;\infty]$内$y + x$最小的是谁，从而求得每一个点的最近点。

这个算法是$O(n \log n)$的。因此，$n$个点的最小曼哈顿生成树可以在$O(n \log n)$计算出来。

至于坐标变换，一个比较方便的顺序就是先关于$y = x$对称，也就是交换$x$和$y$。然后关于$y = 0$对称，也就是将$y$取反，然后再关于$y = x$对称。这样执行$4$次扫描线算法就可以完成构图。
