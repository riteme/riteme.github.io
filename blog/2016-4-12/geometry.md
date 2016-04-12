---
title: 平面计算几何
create: 2016.4.12
modified: 2016.4.12
tags: 数学 计算几何
---
# 平面计算几何
[TOC]

## 1 线段
下图中展示了一条**无向线段**$AB$。

![segment-1](http://git.oschina.net/riteme/blogimg/raw/master/geometry/segment-1.svg)

一般来说，我们所见的线段都是不定方向的。但在计算几何中，我们会借助**向量**这一强大的工具，因此我们需要将线段表示成**有向线段(Directed Segment)**的形式。如下图所示：

![segment-2](http://git.oschina.net/riteme/blogimg/raw/master/geometry/segment-2.svg)

事实上，有向线段就是一个向量。在上面，线段$AB$被向量$\vec{AB}$所替代。  
同样，我们也可以用$\vec{BA}$来表示。

接下来，我们将研究非常基础的问题：**判定线段是否相交**。  
这件工作对于人类来说是非常简单的，然而我们要能设计出一个算法来实现。  
首先我们会有一个$\Theta(1)$的时间内判定两条线段是否相交的算法，于是我们就可以在$\Theta(n^2)$的时间内来判定$n$条直线内是否有线段相交。  
之后，我们将改进这一算法，使得在$\Theta(n\log n)$的时间内来完成这一任务。

## 2 叉积
对于两个向量$p_1$和$p_2$，它们的**叉积(Cross Product)**$p_1 \times p_2$的定义如下：
$$
p_1 \times p_2 = 
\begin{vmatrix}
x_1 & x_2 \\
y_1 & y_2
\end{vmatrix} = 
x_1y_2 - x_2y_1
\tag{2.1}
$$

上面的定义使用了行列式，初学者可能感到迷糊。好在叉积有着很好的几何解释。

下图中，向量$p_1$和向量$p_2$的叉积$p_1 \times p_2$就是它们和与$p_1$平行的向量$p_3$和与$p_2$平行的向量$p_4$所围成的平行四边形$ABCD$的**有向面积**。

![cross-product-1](http://git.oschina.net/riteme/blogimg/raw/master/geometry/cross-product-1.svg)

为什么会是有向面积呢？你可以自己造个数据来算一下，你会发现$p_1 \times p_2 = -p_2 \times p_1$。

我们发现，叉积结果的符号与$p_1$和$p_2$的相对位置关系有很大联系：

* 当$p_2$在$p_1$的**顺时针方向**时，$ p_1 \times p_2 \lt 0$。  
* 当$p_2$在$p_1$的**逆时针方向**时，$ p_1 \times p_2 \gt 0$。  
* 当$p_2$与$p_1$**共线（方向相同或相反）**时，$ p_1 \times p_2 = 0$。

利用这些性质，我们可以完成许多有趣的事情。

同时，利用上面的图像，我们可以探究出叉积公式的另外一种形式：

![cross-product-2](http://git.oschina.net/riteme/blogimg/raw/master/geometry/cross-product-2.svg)

在前面的基础上，我们作$ BE \bot p_2 $，那么平行四边形$ABCD$的面积又可以表示为：
$$ S_{ABCD} = |p_2| \cdot |BE| $$

又因为：
$$ |BE| = |p_1| \sin \alpha $$

因此：
$$ p_1 \times p_2 = |p_1|\cdot|p_2|\sin \alpha \tag{2.2} $$

但是显然这样的公式对于计算机而言需要大量的浮点数运算，所以用这个公式计算叉积精度可能不高。但是这个公式可以改为下面的形式：
$$ \alpha = \sin^{-1}\left({p_1 \times p_2 \over |p_1| \cdot |p_2|}\right) \tag{2.3}$$

这样我们可以利用这个公式来计算两个向量间的夹角。

如果两个向量的起点都不在原点时，该怎么计算这个有向面积呢？  
这其实相当简单，我们将两个向量的公共起点作为原点，然后运用**向量减法**来计算相对向量，然后就可以计算了。
