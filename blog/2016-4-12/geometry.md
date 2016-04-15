---
title: 平面计算几何
create: 2016.4.12
modified: 2016.4.12
tags: 数学
      计算几何
---
[TOC]
# 平面计算几何
## 1 线段
下图中展示了一条**无向线段**$AB$。

![segment-1](http://git.oschina.net/riteme/blogimg/raw/master/geometry/segment-1.svg)

一般来说，我们所见的线段都是不定方向的。但在计算几何中，我们会借助**向量**这一强大的工具，因此我们需要将线段表示成**有向线段(Directed Segment)**的形式。如下图所示：

![segment-2](http://git.oschina.net/riteme/blogimg/raw/master/geometry/segment-2.svg)

事实上，有向线段就是一个向量。在上面，线段$AB$被向量$\vec{AB}$所替代。  
同样，我们也可以用相反的向量$\vec{BA}$来表示$AB$。

## 2 叉积
### 2.1 定义
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

### 2.2 几何解释
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

但是显然这样的公式对于计算机而言需要大量的浮点数运算，所以用这个公式计算叉积精度可能不高。  
但是这个公式可以改为下面的形式：
$$ \alpha = \sin^{-1}\left({p_1 \times p_2 \over |p_1| \cdot |p_2|}\right) \tag{2.3}$$

这样我们可以利用这个公式来计算两个向量间的夹角。

如果两个向量的起点都不在原点时，该怎么计算这个有向面积呢？  
这其实相当简单，我们将两个向量的公共起点作为原点，然后运用**向量减法**来计算相对向量，然后就可以计算了。

### 2.3 计算面积
下面我们将利用叉积来计算**简单多边形**的面积。  
首先，简单多边形时多边形中没有边相交的多边形。注意包括**凸多边形**以及令人讨厌的**凹多边形**。

首先从平行四边形入手。

![area](http://git.oschina.net/riteme/blogimg/raw/master/geometry/cross-product-1.svg)

这是之前的图。虽然向量的叉积算出来时有向面积，但是我们只用取绝对值，就是平行四边形的面积了。  
对于三角形，通过对称的方法可以构造出平行四边形。因此三角形就是叉积的绝对值的一半。

先来看一下正方形：

![area](http://git.oschina.net/riteme/blogimg/raw/master/geometry/area-1.svg)

显然，它的面积是$1$。  
但现在要你用向量的方法来计算，该怎么办?

我们的正方形是用一组向量来表示的($\vec{AB}$、$\vec{BC}$、$\vec{CD}$和$\vec{DA}$)，并且按照逆时针排列，这样就指定了顶点的顺序。  
然后我们按照下面的流程来计算面积：

1. 在平面内任选一点作为原点。  
2. 按照有向边的顺序依次计算叉积并累积求和，最后的结果除以$2$就是多边形的面积。

现在我们来演示一次：

![area](http://git.oschina.net/riteme/blogimg/raw/master/geometry/area-2.svg)

**选定原点**，平面内任意一个点都可以。这里选择的是$O$点。

![area](http://git.oschina.net/riteme/blogimg/raw/master/geometry/area-3.svg)

**计算叉积**，首先是$\vec{AB}$，我们计算的是$\vec{OA} \times \vec{OB} = -1 $。

![area](http://git.oschina.net/riteme/blogimg/raw/master/geometry/area-4.svg)

然后是$\vec{BC}$，$\vec{OB} \times \vec{OC} = 2$。

![area](http://git.oschina.net/riteme/blogimg/raw/master/geometry/area-5.svg)

之后是$\vec{CD}$，$\vec{OC} \times \vec{OD} = 2$。

![area-4](http://git.oschina.net/riteme/blogimg/raw/master/geometry/area-6.svg)

最后是$\vec{DA}$，$\vec{OD} \times \vec{OA} = -1$。  
将叉积结果累加起来并除以$2$，得到$ S_{ABCD} = 1$。  
算法得到了正确结果。

事实上，这个算法就是简单多边形的面积算法。那么，为什么这样计算是正确的呢？

我们首先来考虑$\vec{AB}$和$\vec{BC}$。

![area](http://git.oschina.net/riteme/blogimg/raw/master/geometry/area-7.svg)

这两个向量从$O$的角度来看，它们是相反的方向，并且它们叉积出来的结果是异号的。  
我们可以发现，${\vec{OA} \times \vec{OB} \over 2}$就是$-S_{\triangle OBA}$，${\vec{OB} \times \vec{OC} \over 2}$就是$S_{\triangle OBC}$，$S_{\triangle OBC}-S_{\triangle OBA} = S_{\triangle ABC}$。因此这一对边就可以计算出这个正方形一半的面积。对于另一半，也是如此。  
因此，我们发现，这个算法时先计算这个多边形与选定的原点构成的更大的多边形的面积：

![area](http://git.oschina.net/riteme/blogimg/raw/master/geometry/area-8.svg)

上图就是线计算了$S_{OCDEFG}$。这几条边的叉积之和为正数。

然后计算不属于多边形的部分：

![area](http://git.oschina.net/riteme/blogimg/raw/master/geometry/area-9.svg)

上图中就是计算$S_{OCBAG}$，而这几条边的叉积之和是负数。因此相加后就只剩下多边形的面积了。  
又因为叉积计算的是平行四边形的面积，所以最后要除以$2$。
