---
title: 极限与导数
create: 2016.6.23
modified: 2016.6.23
tags: 数学
      极限
      导数
---

[TOC]
# 极限与导数
最近学了一些基础微积分，这里稍微记录一下。

## 极限
极限可以当做是一个函数$f(x)$的$x$无限趋近于某一个常数或无穷远处时，函数数值所逼近的一个值。
例如，对于函数$f(x) = {2x \over x + 1}$，当$x$趋近于无穷大时，$f(x)$无限趋近于$2$。我们将此记成这样子：
$$
\lim_{x \rightarrow \infty} f(x) = 
\lim_{x \rightarrow \infty} {2x \over x + 1} = 
2
$$

求极限需要会一点代数技巧，我反正是老是求不出......

极限有一些方便的性质：
当然，这些等式的左边都是存在极限的。
$$ \lim_{x \rightarrow c} a \cdot f(x) = a \cdot \lim_{x \rightarrow c} f(x) $$

对于两个函数$f(x)$和$g(x)$之间极限的关系：（当然$f(x)$和$g(x)$都要存在极限）
$$ \lim_{x \rightarrow c} [f(x) + g(x)] = \lim_{x \rightarrow c} f(x) + \lim_{x \rightarrow c} g(x) $$

$$ \lim_{x \rightarrow c} [f(x) - g(x)] = \lim_{x \rightarrow c} f(x) - \lim_{x \rightarrow c} g(x) $$

$$ \lim_{x \rightarrow c} f(x) \cdot g(x) = \lim_{x \rightarrow c} f(x) \cdot \lim_{x \rightarrow c} g(x) $$

$$ \lim_{x \rightarrow c} {f(x) \over g(x)} = {\lim_{x \rightarrow c} f(x) \over \lim_{x \rightarrow c} g(x)} \; (\lim_{x \rightarrow c} g(x) \neq 0)$$

简而言之，极限这东西可以加减乘除。

## 导数
对于函数$f(x)$而言，它在$x_0$处的导数是这么定义的：
$$ \lim_{\Delta x \rightarrow 0} {f(x_0 + \Delta x) - f(x_0) \over \Delta x} $$

从几何意义上讲，这个值可以视为是$f(x)$的图像在$x_0$处的切线的斜率。
当然不是所有的函数都是可以求导数的，只有在那一段上是连续的函数时，才会有导数。
连续的函数$f(x)$在其定义域内的每一点上都可以计算导数，意味着每一个$x$都会对应一个导数，这样就形成了一个函数关系。我们将这个函数叫作导函数，记作$f^\prime(x)$。

如何求导函数呢？根据导数的定义，我们将$x_0$换为$x$，然后求极限就好了。然而说的轻巧，实际上很多都比较难以求出，因此早有先人为我们把各种导函数算好了。

举一个典型的例子$f(x) = x^2$。按照求导数的方法：
$$
\begin{align}
f^\prime(x) &= \lim_{\Delta x \rightarrow 0} {f(x - \Delta x) - f(x) \over \Delta x} \\
&= \lim_{\Delta x \rightarrow 0} {(x + \Delta x)^2 - x^2 \over \Delta x} \\
&= \lim_{\Delta x \rightarrow 0} {\Delta x^2 + 2x\Delta x \over \Delta x} \\
&= \lim_{\Delta x \rightarrow 0} (\Delta x + 2x) \\
&= 2x
\end{align}
$$

事实上，对于幂函数$f(x) = x^\alpha$，其导函数为$f^\prime(x) = \alpha x^{\alpha - 1}$。

导数与导数之间存在运算关系，有了这些运算关系，我们就可以方便地进行求导。
类似于线性的性质：
$$ [a \cdot f(x) + b \cdot g(x)]^\prime = a \cdot f^\prime(x) + b \cdot g^\prime(x) $$

两个导数相乘：
$$ [f(x)g(x)]^\prime = f^\prime(x)g(x) + f(x)g^\prime(x) $$

两个导数相除：
$$ \left[{f(x) \over g(x)} \right]^\prime = {f^\prime(x)g(x) + f(x)g^\prime(x) \over g^2(x)} \; (g(x) \neq 0) $$

复合函数：
$$ [f(g(x))]^\prime = f^\prime(g(x)) \cdot g^\prime(x) $$

一些基本函数的导函数就放这里了，当我们要求一个特定函数的导函数时，可以利用上面的规则，然后根据导函数表来计算。下面只有$x$是变量。
$$ c^\prime = 0 $$

$$ x^\prime = 1 $$

$$ (x^\alpha)^\prime = \alpha x^{\alpha - 1} $$

$$ (\text{e}^x)^\prime = e^x $$

$$ (a^x)^\prime = a^x\ln a $$

$$ (\ln x)^\prime = \frac1x $$

$$ (\log_a x) = \frac1{x\ln a} $$

$$ \sin^\prime x = \cos x $$

$$ \cos^\prime x = -\sin x $$

$$ \tan^\prime x = \frac1{\cos^2 x} $$

$$ \cot^\prime x = -\frac1{\sin^2 x} $$

大致就这么多了~
