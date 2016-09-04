---
title: 极限与导数
create: 2016.6.23
modified: 2016.6.24
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
f^\prime(x) &= \lim_{\Delta x \rightarrow 0} {f(x + \Delta x) - f(x) \over \Delta x} \\
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
$$ \left[{f(x) \over g(x)} \right]^\prime = {f^\prime(x)g(x) - f(x)g^\prime(x) \over g^2(x)} \; (g(x) \neq 0) $$

复合函数：
$$ [f(g(x))]^\prime = f^\prime(g(x)) \cdot g^\prime(x) $$

一些基本函数的导函数就放这里了，当我们要求一个特定函数的导函数时，可以利用上面的规则，然后根据导函数表来计算。下面只有$x$是变量。
$$ c^\prime = 0 $$

$$ x^\prime = 1 $$

$$ (x^\alpha)^\prime = \alpha x^{\alpha - 1} $$

$$ (\text{e}^x)^\prime = e^x $$

$$ (a^x)^\prime = a^x\ln a $$

$$ (\ln x)^\prime = \frac1x $$

$$ (\log_a x)^\prime = \frac1{x\ln a} $$

$$ \sin^\prime x = \cos x $$

$$ \cos^\prime x = -\sin x $$

$$ \tan^\prime x = \frac1{\cos^2 x} $$

$$ \cot^\prime x = -\frac1{\sin^2 x} $$

## 对数求导法
上面的求导公式已经能够应对大部分基本函数的求导了，但是对于下面的函数：
$$ f(x) = x^{1/x} $$

该如何求导呢？
这就要用到对数来进行求导。

我们知道，对于一个函数$f(x)$：
$$ [\ln f(x)]^\prime = \ln^\prime f(x) \cdot f^\prime(x) $$

换言之：
$$ f^\prime(x) = {[\ln f(x)]^\prime \over \ln^\prime f(x)} \tag{1}$$

利用这一点，我们就可以对$f(x) = x^{1/x}$求导。
首先，为了方便我们设：
$$ y = x^{1/x} $$

由于两者相等，所以两者的对数也应相等：
$$ \ln y = \ln x^{1/x} = \frac1x\ln x $$

将两边对$x$求导。注意按照$(1)$式，左式需要乘上$y^\prime$两者才能相等。
$$ {y^\prime \over y} = {\ln x - 1 \over x^2} $$

于是我们可以得到：
$$ y^\prime = {\ln x - 1 \over x^2}y = {\ln x - 1 \over x^2}x^x = f^\prime(x) $$

这样我们就完成了求导。
既然都对这个函数求过导了，我们来验证一下它的一个性质。
将$\text{e}$代入导函数：
$$
\begin{align}
f^\prime(\text{e}) & = {\ln \text{e} - 1 \over \text{e}^2}\text{e}^{1/\text{e}} \\
& = {1 - 1 \over \text{e}^2} \\
& = 0
\end{align}
$$

因此我们发现$x = \text{e}$是这个函数的极值点。
但究竟是极大值还是极小值呢。设$h > \text{e}$，则：
$$
f^\prime(\text{e} + h) = {\ln (\text{e} + h) - 1 \over (\text{e} + h)^2}(\text{e} + h)^{1/(\text{e} + h)}
$$

因为$(\text{e} + h)^2$和$(\text{e} + h)^{1/(\text{e} + h)}$都大于$0$，因此只要看分子的符号。
由于自然对数函数是单调递增的，易知分子是大于$0$的。故$f^\prime(\text{e} + h) > 0$。同理，当$0 < h < \text{e}$时，$f^\prime(\text{e} - h) < 0$。
这样我们就证明了这是一个极大值点。
事实上，我们可以证明这个导函数的单调性，从而得知这是最大值。

## 后记
有关微积分的教材这里我推荐一本：Ron Larson的<font style="font-family: Georgia">*Calculus*</font>。
这本教材的比较像我们的数学教科书，不是像某些教科书一样不停的放出各种定理......
用于自学是非常适合的~~~
