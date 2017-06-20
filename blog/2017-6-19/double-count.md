---
title: 双重计数的简单应用
create: 2017.6.19
modified: 2017.6.19
tags: 图计数
      组合数学
---

[TOC]
# 双重计数的简单应用
## 什么是双重计数
双重计数就是就是计数同一个事物考虑两种计算方式，得到两个看上去没有联系的表达式相等，从而得到优美的公式的一种方法。通常也被称作“多重计数”或者“双计数”。

## 应用
### 组合恒等式
大小为$n$的集合的所有子集数是$2^n$的，因为集合中的每个元素可以选择选或者不选。另一方面，它的子集数目同时也是$\sum_{k=0}^n {n \choose k}$，于是我们可以得到经典的组合恒等式：
$$
\sum_{k=0}^n {n \choose k} = 2^n \tag{2.1}
$$

这应该是双计数最基础的运用了吧。

我们递推组合数时经常会用到这样的公式：
$$
k{n \choose k} = n{n - 1 \choose k - 1} \tag{2.2}
$$

证明它十分简单，只需要将组合数公式展开约分即可。但是形象的组合证明也许更好，因此我们来考虑二元组$(A,\;x)$的数量，其中要求满足$x \in A$。我们从两个方面来考虑：

1. 如果先计数集合$A$，再计数$x$：集合$A$的数量为${n \choose k}$，从中选出一个元素的方案数为$k$，所以总方案数为$k{n \choose k}$。
2. 如果先计数$x$，再计数$A$：首先$x$有$n$种选法，然后考虑从剩下的$n - 1$个元素里面来选出$k - 1$个元素，即可得到一个大小为$k$的子集$A$。因此总方案数为$n{n - 1 \choose k - 1}$。

由于我们计数的是同一个东西，所以$(2.2)$式成立。

### Burnside定理
Burnside定理的证明本身就是一个巧妙的双计数，具体的证明过程就不在这里展出，各位可以参考网上的相关资料或者[这篇博客](/blog/2016-12-19/burnside.html)。

### 无标号的有根树计数
无标号的有根树表示我们所计数的树是有一个固定的根节点，但是同构的树只能算一个。为了方便，我们令$n$个无标号节点的有根树的数量为$t(n)$。例如，下面的三棵树中：

![tree-sample](https://git.oschina.net/riteme/blogimg/raw/master/double-count/tree-sample.svg)

蓝色的节点是根节点，第一棵树和第二棵树虽然本质上一模一样，但是由于树根的不同，所以算作不同的树。而第三棵树和第一棵数仅仅只是子树顺序的调动，由于节点没有编号，所以认为与第一棵树是同构的。

如何计数这样的东西？首先有一个明显的特征就是树根是固定的，而每一棵子树又是一棵有根树，所以我们来考虑递推：设$f(n, \;m)$表示$n$个节点，其中最大的子树大小为$m$的方案数，通过枚举大小为$m$的子树的个数$k$可以做如下递推：
$$
f(n,\;m) = \sum_{1 \leqslant mk < n} {k + t(m) - 1 \choose k} \sum_{i = 1}^{m - 1} f(n - mk, \;i)　\tag{2.3}
$$

而$t(n) = \sum_{k = 1}^{n - 1} f(n,\;k)$，所以利用一些递推技巧，不考虑算术的复杂度，我们可以在$O(n^2\ln n)$的时间内计算出$t(n)$。

现在我们来考虑使用双计数的技巧，尝试计数二元组$(T, \;x)$的方案数，其中$T$是一棵有根树，而$x$是将$T$按照最小表示法[^id]标号之后一个非树根的节点编号，现在来考虑两个方面：

1. 考虑先计数$T$，后计数$x$：总共的$T$共有$t(n)$个，其中非根节点数量为$n - 1$个，故总方案数为$(n - 1)t(n)$。
2. 考虑先计数$x$，后计数$T$：首先假定$x$在一个大小为$m$的某个子树中，这样的子树一共有$t(m)$种，而子树上的$x$有$m$种，所以一共有$mt(m)$种。然后注意到跟它相同的子树可能不止一个，而我们的$x$都要枚举到。当$x$在第一棵上这样的子树时，方案数为$t(n - m)$，在第二棵时，方案数为$t(n - 2m)$......所以我们可以得知方案数为$\sum_{1 \leqslant km < n} t(n - km)$。由于$x$在不同的大小的子树中，所以总方案数为$\sum_{m = 1}^{n - 1}mt(m)\sum_{1\leqslant km<n}t(n-km)$

[^id]: 显然我们可以对比较小的（例如大小为$1$）大小相同的不同的有根树都给个编号，然后更大的有根树可以按照先子树大小后子树编号来对它树根的子树排序，因此就可以继续给更大的子树编号。

联立两式相等，我们可以得知：
$$
t(n) = \frac1{n-1}\sum_{m = 1}^{n - 1}mt(m)\sum_{1\leqslant km<n}t(n-km) \tag{2.4}
$$

通过枚举$T = mk$，递推式可以变为：
$$
t(n) = \frac1{n-1}\sum_{T = 1}^{n - 1} t(n - T) \sum_{m \mid T} mt(m) \tag{2.5}
$$

这样就可以方便的在$O(n^2)$时间递推计算$t(n)$了，也可以通过进一步的变形从而利用FFT算法来加速计算。当然有关利用生成函数来计算类似问题的可以[参考这里](http://debug18.com/posts/calculate-the-number-of-structural-isomers-for-alkanes-ii/)。

### 无标号的无向连通简单图计数
上述方法可以继续套用到无向图上来，首先我们设$n$个没有标号的无向简单图数量为$h(n)$，连通图数量为$f(n)$，以及非连通图数量为$g(n)$。$n = 0..5$的几个数值如下[^zero-graph]：
$$
\begin{aligned}
f: &1, 1, 1, 2, 6, 21, ... \\
g: &0, 0, 1, 2, 5, 13, ... \\
h: &1, 1, 2, 4, 11, 34, ...
\end{aligned}
$$

[^zero-graph]: 我们认为大小为$0$的图是存在的，并且它是连通的。

关于$h$的计算，可以使用Polya计数法来得出（只可惜这种方法并不高效），具体的方法可以[参见这里](/blog/2016-12-19/burnside.html#_4)。由于非连通图是由一些连通块构成的，很像我们在无标号有根树中的子树，所以我们接下来考虑计算关于$g$的递推关系。

首先，我们考虑计数二元组$(G, \;x)$的数量，类似的，$G$是一张非连通图，而$x$是将$G$编号后的一个节点$x$。同样，我们考虑两个方面：

1. 先计数$G$后计数$x$：显然方案数为$ng(n)$。
2. 先计数$x$后计数$G$：考虑$x$在一个大小为$t$的连通块中，按照类似的方法，我们可以得知这样的$x$有$tf(t)$种。另外，我们还需要枚举它是$G$中第几个这样的连通块，这样的方案数是$\sum_{1 \leqslant kt \leqslant n} h(n - kt)$种。

所以，我们得到：
$$
g(n) = \frac1n\sum_{t = 1} tf(t) \sum_{1\leqslant kt \leqslant n} h(n - kt) \tag{2.6}
$$

因此知道了$h(n)$的值，同时就可以将$f(n)$和$g(n)$都计算出来。

然而，我并没有找到更好的计算$h(n)$的办法，希望如果有大神知道能够告诉我一声！