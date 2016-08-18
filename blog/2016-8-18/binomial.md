---
title: 二项式定理及其它
create: 2016.8.18
modified: 2016.8.18
tags: 数学
      组合数学
      二项式定理
      多项式定理
      牛顿二项式定理
---

[TOC]
# 二项式定理及其它
## 二项式定理
### 基本定理
二项式定理是用于展开两数相加的幂次的公式：
$$
(x + y)^n = \sum_{k=0}^n {n \choose k} x^k y^{n-k} \tag{1.1}
$$

我们可以考虑使用组合证明。由于我们可以从$n$个括号中任意选取$k$个来组成$x^k$的项，这个方案数恰好是${n \choose k}$，剩下的$y$也是同理。因此对应的项的系数就是${n \choose k}$或${n \choose n - k}$。
下面使用归纳法证明：
当$n = 1$的时候：
$$
(x + y)^1 = x + y = \sum_{k=0}^1 {1 \choose k} x^ky^{1-k}
$$

结论显然成立。
假设对$n$成立，求证对$n + 1$成立：
$$
\begin{align}
(x + y)^{n+1} & = (x + y)(x + y)^n \\
& = (x + y)\sum_{k=0}^n {n \choose k} x^ky^{n-k} \\
& = \sum_{k=0}^n {n \choose k} x^{k+1}y^{n-k} + \sum_{k=0}^n {n \choose k} x^ky^{n-k+1} \\
& = x^{n+1} + y^{n+1} + \sum_{k=0}^{n-1} {n \choose k} x^{k+1}y^{n-k} + \sum_{k=1}^n {n \choose k} x^ky^{n-k+1} \\
& = x^{n+1} + y^{n+1} + \sum_{k=1}^{n} {n \choose k - 1} x^{k}y^{n-k+1} + \sum_{k=1}^n {n \choose k} x^ky^{n-k+1} \\
& = x^{n+1} + y^{n+1} + \sum_{k=1}^n \left[{n \choose k - 1}+{n \choose k}\right] x^ky^{n-k+1} \\
& = x^{n+1} + y^{n+1} + \sum_{k=1}^n {n+1 \choose k} x^ky^{n-k+1} \\
& = \sum_{k=0}^{n+1} {n+1 \choose k} x^ky^{n-k+1} \\
\end{align}
$$

这样就完成了我们的证明。

### 简单运用
#### 组合恒等式
将$y = 1$，我们将得到一个很常用的式子：
$$
(1 + x)^n = \sum_{k=0}^n {n \choose k} x^k \tag{1.2}
$$

令$x = 1$:
$$
\sum_{k=0}^n {n \choose k} = (1 + 1)^n = 2^n \tag{1.3}
$$

得到了组合数之和，

令$x = -1$:
$$
\sum_{k=0}^n (-1)^k {n \choose k} = 0 \tag{1.4}
$$

得到了组合数的交错和。
通过移项可以得到更进一步的结论：:
$$
{n \choose 0} + {n \choose 2} + \dots = {n \choose 1} + {n \choose 3} + \dots \tag{1.5}
$$

结合$(1.3)$可知：
$$
{n \choose 0} + {n \choose 2} + \dots = {n \choose 1} + {n \choose 3} + \dots = 2^{n-1} \tag{1.6}
$$

#### 导数
现在我们重新考虑这个式子：
$$
(1 + x)^n = \sum_{k=0}^n {n \choose k} x^k \tag{1.2}
$$

两边同时关于$x$求导：
$$
n(1 + x)^{n-1} = \sum_{k=0}^n {n \choose k} \cdot kx^{k-1} \tag{1.7}
$$

令$x = 1$：
$$
n2^{n-1} = \sum_{k=0}^n k{n \choose k} \tag{1.8}
$$

这样我们得到了一个非常有意思的式子。
运用这个式子，我们可以算出：
$$
\sum_{k=0}^n (2k+1){n \choose k} = (n+1)2^n
$$

事实上，你还可以对$(1.8)$进一步求导，从而得到$k^2$的公式。

#### 组合数的平方和
$$
\sum_{k=0}^n {n \choose k}^2 = {2n \choose n} \tag{1.9}
$$

对于这个结论，我们考虑下面的式子：
$$
(1 + x)^n(1+x)^n = (1+x)^{2n}
$$

运用二项式定理展开可得：
$$
\begin{align}
\sum_{i=0}^n {n\choose i} x^i \cdot \sum_{j=0}^n {n\choose j} x^j & = \sum_{i=0}^n\sum_{j=0}^n {n \choose i}{n \choose j} x^ix^j \\
& = \sum_{k=0}^{2n} {2n \choose k} x^k
\end{align}
$$

考虑等号两边系数同为$k$的项，一定满足下面的等式：
$$
\sum_{i=0}^n {n \choose i}{n \choose k - i} = {2n \choose k} \tag{1.10}
$$

当$k = n$时：
$$
\begin{align}
\sum_{i=0}^n {n \choose i}{n \choose n - i} & = \sum_{i=0}^n {n \choose i}{n \choose i} \\
& = \sum_{i=0}^n {n \choose i}^2 \\
& = {2n \choose n}
\end{align}
$$

这样就证明了组合数的平方和的结论。

#### 二项式定理与$\text{e}$
根据泰勒展开，我们可以知道：
$$
\text{e}^x = \sum_{n=0}^\infty \frac{x^n}{n!} \tag{1.11}
$$

令$x = 1$就可以得到$\text{e}$的无穷展开形式：
$$
\text{e} = \sum_{k=0}^\infty \frac1{k!} \tag{1.12}
$$

而我们平常所熟知的$\text{e}$的定义是这样的：
$$
\text{e} = \lim_{n \rightarrow \infty} \left(1 + \frac1n\right)^n \tag{1.13}
$$

运用二项式定理可以证明泰勒展开的结果与上面的定义等价：
$$
\begin{align}
\text{e} & = \lim_{n\rightarrow\infty} \left(1 + \frac1n\right)^n \\
& = \lim_{n\rightarrow\infty} \sum_{k=0}^n {n \choose k} \frac1{n^k} \\
& = \lim_{n\rightarrow\infty} \sum_{k=0}^n \frac1{k!} \frac{\prod_{i=n-k+1}^n i}{n^k}
\end{align}
$$

由于：
$$
\lim_{n \rightarrow \infty} \frac{\prod_{i=n-k+1}^n i}{n^k} = 1
$$

所以这一项可以去掉。于是就得到了泰勒展开的结果。

## 多项式定理
与二项式定理，这个定理并不怎么常用。
可能是形式比较复杂，不便于理论分析。
多项式定理是二项式定理的扩展：
$$
(x_1 + x_2 + \dots + x_m)^n = \sum_{k_1 + k_2 + \dots + k_m = n} {n \choose k_1\;k_2\;\dots\;k_m} x_1^{k_1}x_2^{k_2}\cdots x_m^{k_m} \tag{2.1}
$$

其中：
$$
{n \choose k_1\;k_2\;\dots\;k_m} = {n! \over k_1!k_2!\cdots k_m!}
$$

是多项式系数，同时也是多重集合的全排列数量。
组合证明方法与二项式定理类似。同时也可以从二项式定理归纳法而来。

## 牛顿二项式定理
牛顿二项式定理又称为广义二项式定理：
$$
(x + y)^\alpha = \sum_{k=0}^\infty {\alpha \choose k} x^ky^{\alpha - k} \;\;\; (\alpha \in R,\;\color{red}{0 \le \;\mid x\mid\; \lt \;\mid y\mid}) \tag{3.1}
$$

注意红色的字，这是非常重要的限制。
其中：
$$
{\alpha \choose k} = {\prod_{i=\alpha - k +1}^\alpha i \over k!}
$$

是在实数域的二项式系数。
不会那么高深的高数知识，不会证......

### 基本用途
这种形式并不常用，而另外一种形式很常用：
令$z = x/y$，那么$\color{red}{\mid z\mid \;\lt 1}$：
$$
(x + y)^\alpha = y^\alpha(z + 1)^\alpha
$$

所以：
$$
\begin{align}
(z + 1)^\alpha & = \sum_{k=0}^\alpha {\alpha \choose k} {x^ky^{\alpha-k} \over y^\alpha} \\
& = \sum_{k=0}^\alpha {\alpha \choose k} {x^k \over y^k}\cdot{y^{\alpha-k} \over y^{\alpha-k}} \\
& = \sum_{k=0}^\alpha {\alpha \choose k} z^k \\
& = (1 + z)^\alpha
\end{align}
\tag{3.2}
$$

#### 几何级数
令$\alpha = -n \; (n \in Z)$：
$$
{\alpha \choose k} = {-n \choose k} = (-1)^k{n + k - 1 \choose k}
$$

所以：
$$
\frac1{(1+z)^n} = \sum_{k=0}^\infty (-1)^k{n + k - 1 \choose k} z^k
$$

令$z = -z$：
$$
\frac1{(1-z)^n} = \sum_{k=0}^\infty {n+k-1 \choose k}z^k
$$

妙啊！讨厌的$-1$不见了！
令$n=1$：
$$
\frac1{1-z} = \sum_{k=0}^\infty z^k
$$

正是收敛几何级数。
这东西在生成函数里面很常见。
看生成函数之前一定要学好牛顿二项式定理和泰勒展开QAQ。
现在我们来求一下有限几何级数的公式。
注意$\mid z \mid \;\lt 1$：
$$
\begin{align}
\sum_{k=0}^n z^k & = \sum_{k=0}^\infty z^k - \sum_{k=n+1}^\infty z^k \\
& = \sum_{k=0}^\infty z^k - z^{n+1}\sum_{k=0}^\infty z^k \\
& = (1 - z^{n+1}) \sum_{k=0}^\infty z^k \\
& = {1 - z^{n+1} \over 1-z}
\end{align}
\tag{3.3}
$$

#### 开根运算
之前取$\alpha = -n$，从而解决了几何级数的问题。
现在取$\alpha = 1/2$，就可以将求平方根变成一个迭代的形式。
并且可以求任意幂次、任意精度的结果。
由于$z$有限制，因此需要提项，如：
$$
\sqrt{20} = \sqrt{16+4} = 4\sqrt{1 + 0.25}
$$

这样我们就获得了一个求根号的好方法。
