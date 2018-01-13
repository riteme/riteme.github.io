---
title: 数学问题杂记
create: 2017.12.16
modified: 2018.1.13
tags: 数学
---

[TOC]
# 数学问题杂记

这里放些我见到过的比较有意思的数学题吧。本文会不定期更新。所有问题的标题都是记录到博客上的时间。

### 2017.6.14

#### 问题描述

给你一个无限长度的空白的尺子，问最少在上面画多少个刻度，使得可以量出 $1$ 到 $10$ 每一个整数长度？
假设一共画了 $n$ 个刻度，每个刻度到最左边的刻度的距离为 $a_1,\; a_2, \;..., \;a_n$，那么称一个长度 $x$ 为可测量的当且仅当存在一对 $i, \;j$，满足 $a_i - a_j = x$。

#### 解决方案

首先我们可以 xjb 试一试，$7$ 个点的方案是非常 naïve 的：

![p1](https://git.oschina.net/riteme/blogimg/raw/master/math-2017-6/p1.svg) 

通过一番尝试，我们可以构造出 $6$ 个点的方案：

![p2](https://git.oschina.net/riteme/blogimg/raw/master/math-2017-6/p2.svg) 

当然，因为没有长度限制，所以更长的方案我也构造出来过。总而言之，$6$ 个点的方案不是非常困难。构造上面这个方案时，我先画了一个原点，然后向右走一步，画一个点，继续走两步，画一个点。随后回到原点左边四格的位置画一个点。然后钦定最右边的为 $10$，将 $0$ 刻度画出来。此时发现 $9$ 不存在，所以将 $1$ 也点上。

那么现在问题来了，$5$ 个点的方案能否找出来？

理论上，$5$ 个点两两配对刚好 $10$ 对，给人一种可以构造的感觉。不过很可惜，$5$ 个点的方案是不存在的，这一结论可以使用计算机暴力得出。

下面给出一个不需要任何暴力的证明：

1. 由于 $5$ 个点两两配对一共 $10$ 对，所以所有点对之间的距离刚好是 $1$ 到 $10$，即不存在两个不同的点对之间的距离相同。由此可以推出，最远的两个点之间的距离为 $10$，所以我们可以先钦定刻度 $0$ 和刻度 $10$ 上有两个点。
2. 剩下还有 $3$ 个点，它们将长度为 $10$ 的线段分为 $4$ 段，这四段的长度总和要为 $10$，而 $10$ 的四拆分只有 $10 = 1 + 2 + 3 + 4$，所以这四段的长度构成 $1$ 至 $4$ 的一个排列。
3. 根据第一点，我们知道 $1$ 不能与 $2$ 或 $3$ 相邻，因为那样相邻的两段的长度之和就会与单独的长度为 $3$ 或 $4$ 的一段冲突，因此 $1$ 只能与 $4$ 相邻，并且 $1$ 只能在第一位或者最后一位。这样 $2$ 和 $3$ 必须相邻。又因为 $1+4 = 2+3$，所以我们推出矛盾，故不存在 $5$ 个点的方案。

到此处，我们已经可以回答上面的问题了，最少使用 $6$ 个刻度。

### 2017.6.14

#### 问题描述

对于 $n$ 个非负实数 $x_1, \;x_2, \;...,\;x_n$，证明：

$$
x_1x_2\cdots x_n \leqslant \left( \frac{x_1 + x_2 + \cdots x_n}n \right)^n
$$

即基本不等式。

#### 解决方案

我是在《具体数学》一书的习题上看到的，居然可以用反向归纳法，只能表示我这种菜鸡根本想不出来。

首先 $n = 1$ 时显然，就不再考虑了。

其次，根据初中知识，$(x_1 + x_2)^2 - 4x_1 x_2 = (x_1 - x_2)^2 \geqslant 0$，我们可以得到 $n = 2$ 时的结论。

接下来就比较机智了，首先如果对于 $n$ 成立，那么对于 $2n$ 也成立。我们可以考虑 $2n$ 时的不等式，是这样子的（现在还不成立）：
$$
x_1x_2\cdots x_{2n} \leqslant \left({x_1 + x_2 + \cdots x_{2n} \over 2n}\right)^{2n}
$$

设 $n$ 个变量 $y_1, \;y_2, \;..., \;y_n$ 和 $z_1, \;z_2$。我们令：
$$
x_{i + (j - 1)n} = y_i z_j \;\;\;\; (1 \leqslant i \leqslant n, \; j = 1, \;2)
$$

所以之前的不等式可以变为：
$$
(y_1y_2\cdots y_n)^2(z_1z_2)^n \leqslant \left( {y_1 + y_2 + \cdots y_n \over n} \right)^{2n} \left( {z_1 + z_2 \over 2} \right)^{2n}
$$

由于：
$$
\begin{aligned}
y_1y_2\cdots y_n &\leqslant \left( {y_1 + y_2 + \cdots + y_n \over n} \right)^n \\
z_1z_2 &\leqslant \left( {z_1 + z_2 \over 2} \right)^2
\end{aligned}
$$

都成立，所以对于 $2n$ 时基本不等式也成立。

最后一步就是反向数学归纳法证明。假设现在 $n$ 是成立的，那么需要证明 $n - 1$ 也是成立的。这个证明非常简单，只需要令 $x_n$ 为 $E = \left(\sum_{k=1}^{n-1}x_k\right) / (n - 1)$，就可以发现：
$$
\begin{aligned}
x_1x_2\cdots x_{n-1}E &\leqslant \left( {x_1 + x_2 + \cdots + x_{n - 1} + E \over n} \right)^n \\
x_1x_2\cdots x_{n-1}E &\leqslant \left( {(n - 1)E + E \over n} \right)^n \\
x_1x_2\cdots x_{n-1}E &\leqslant E^n \\
x_1x_2\cdots x_{n-1} &\leqslant E^{n-1} \\
x_1x_2\cdots x_{n-1} &\leqslant \left( {x_1 + x_2 + \cdots + x_{n - 1} \over n - 1} \right)^{n - 1}
\end{aligned}
$$

因此对于 $n - 1$ 也是成立的。

最后综合一下，如果要想证明 $n > 2$ 成立，只需要从 $m = 2$ 开始，倍增 $m$ 直到 $m \geqslant n$，然后反向归纳到 $n$ 即可。因此基本不等式对于所有正整数 $n$ 均成立。

### 2017.12.16

#### 问题描述

（哥德巴赫-欧拉定理）

(1) （《具体数学》第二章习题 31）证明：

$$
\sum_{j=2}^\infty\sum_{k=2}^\infty \frac1{j^k} = 1
$$

(2) （《具体数学》第二章习题 35）设集合 $P = \{m^n \mid m,\;n \geqslant 2,\;m,\;n\in \mathbf{N}\}$，因此我们知道：

$$
P = \{4,\;8,\;9,\;16,\;25,\;27,\;32,\;36,\;...\}
$$

证明：

$$
\sum_{k \in P} {1 \over k - 1} = 1
$$

#### 解决方案

(1) 第一问使用几何级数即可：
$$
\begin{aligned}
\sum_{j=2}^\infty\sum_{k=2}^\infty {1\over j^k} & = \sum_{j=2}^\infty \left({1 \over 1 - \frac1j} - 1 - \frac1j\right) \\
& = \sum_{j=2}^\infty \left(\frac1{j-1} - \frac1j\right) \\
& = 1
\end{aligned}
$$
(2) 考虑到 (1) 计算出的答案是 $1$，这在隐隐约约之中指引着我们去寻找 (1) 和 (2) 之间的联系。

经过一番考虑，我们发现如果分子分母同除 $k$ 会有奇效：
$$
{1 \over k - 1} = \frac1k \cdot {1 \over 1 - \frac1k} = \frac1k\sum_{j=0}^\infty {1 \over k^j} = \sum_{j=1}^\infty {1 \over k^j}
$$
所以原式变身为：
$$
\sum_{k \in P}\sum_{j=1}^\infty \frac1{k^j}
$$
十分巧妙的是，我们可以找出一种一一对应的关系，满足 $p^q = k^j$，其中 $p,\;q \geqslant 2$ （即 (1) 中的下标 $j$ 和 $k$），而 $k \in P,\;j\geqslant 1$ （上面那个式子的下标）。

根据 $P$ 的定义，设 $k = m^n$。在这里，我们可以要求 $m \notin P$，因为如果 $m \in P$，那么意味着 $m$ 又可以被表示成 $a^b$ 的形式，这时我们只需令 $m = a$ 并且使 $n$ 乘上 $b$ 就可以了。所以具体对应方案如下：

1.  当 $j > 1$ 时，我们显然可以直接令 $p = k$ 以及 $q = j$，就可以满足要求。
2.  当 $j = 1$ 时，由于 $k = m^n$，所以我们还是可以令 $p = m$ 而 $q = n$。

为了证明这是双射，所以我们还需要从另一个方向来对应：

1.  若 $p \in P$，则 $k = p$ 并且 $j = q$，这是因为 $k \in P$。
2.  若 $p \notin P$，则 $k = p^q$，此时 $j = 1$。从这里可以看出我们要求 $m \notin P$ 的好处。

至此，我们就成功证明了 (2) 中的等式。

### 2018.1.7

#### 问题描述

证明：对于任意的正整数 $n$，均可被表示为 $\left\lfloor \sqrt2 k \right\rfloor$ 或 $\left\lfloor (2 + \sqrt2)k \right\rfloor$ 中的有且仅有一种形式，其中 $k$ 也是正整数。

换句话说，集合 $A = \left\{\left\lfloor \sqrt2 k \right\rfloor \mid k \in \mathbf{N}^+\right\}$，$B = \left\{\left\lfloor (2 + \sqrt2) k \right\rfloor \mid k \in \mathbf{N}^+ \right\}$，证明 $A \cap B = \varnothing$ 并且 $A \cup B = \mathbf{N}^+$，就像把正整数集划分为两半一样。

#### 解决方案

这个思路确实比较有趣，我们尝试证明，对于任意的正整数 $n$，集合 $A$ 中不大于 $n$ 的元素个数 $a$ 与集合 $B$ 中不大于 $n$ 的元素个数 $b$ 之和等于 $n$。如果得到了这个结论，原命题就很容易说明了。

先考虑集合 $A$:
$$
\begin{aligned}
a & = \sum_k  \left[1 \leqslant \left\lfloor \sqrt2 k \right\rfloor \leqslant n \right] \\
& = \sum_k  \left[1 \leqslant \sqrt2 k < n + 1\right] \\
& = \left\lceil {n + 1 \over \sqrt2} \right\rceil - \left\lceil {1 \over \sqrt2} \right\rceil \\
& = \left\lceil {n + 1 \over \sqrt2} \right\rceil - 1
\end{aligned}
$$
同理可得：
$$
\begin{aligned}
b & = \left\lceil {n + 1 \over 2 + \sqrt2} \right\rceil - 1 = \left\lceil {(2 - \sqrt2)(n + 1) \over 2} \right\rceil - 1 \\
& = n + 1 + \left\lceil -{\sqrt2(n + 1) \over 2} \right\rceil - 1 \\
& = n - \left\lfloor {n + 1 \over \sqrt2} \right\rfloor
\end{aligned}
$$
因此：
$$
a + b = n - 1 + \left\lceil {n + 1 \over \sqrt2} \right\rceil - \left\lfloor {n + 1 \over \sqrt2} \right\rfloor \tag{1}
$$
我们知道，对于任意实数 $r$：
$$
\lceil r \rceil - \lfloor r \rfloor  = \begin{cases}
0 &  (r \in \mathbf{N}) \\
1 &  (\text{otherwise})
\end{cases}
$$
而 $(n+1) / \sqrt2$ 一定是无理数，故 $(1)$ 式中的取上整减取下整的部分恒为 $1$，即 $a + b = n$。

### 2018.1.13

#### 问题描述

求下面这个递推式的通项公式：
$$
\begin{aligned}
R(1) & = 4  \\
R(n + 1) & = 3R(n) + 2^{n-1}-4n ~~~~(\forall n > 1)
\end{aligned}
$$

#### 解决方案

这里主要是记录一下 Repertoire Method 这种方法，不过现在我还不知道该怎么翻译这个名称...

这个方法基于一个简单的观察：如果设
$$
\begin{aligned}
R(1) & = a \\
R(n + 1) & = 3R(n) + b\cdot 2^{n-1} + c\cdot  n + d
\end{aligned}
$$
我们会发现：
$$
\begin{aligned}
R(1) & = a \\
R(2) & = 3a + b + c + d \\
R(3) & = 9a + 5b + 5c + 4d \\
R(4) & = 27a + 19b + 18c + 13d \\
R(5) & = 81a + 65b + 58c + 40d \\
&\cdots
\end{aligned}
$$
可以猜测，$R(n)$ 的通项公式可以被写成以下形式：
$$
R(n) = a\cdot f(n) + b \cdot g(n) + c\cdot h(n) + d \cdot \varphi(n)
$$
其中 $f(n)$、$g(n)$、$h(n)$ 和 $\varphi(n)$ 都是关于 $n$ 的简单函数。运用数学归纳法，不难证明可以一直保持这种形式。

我们现在的目标就是求出这四个函数。接下来的步骤就比较投机了，我们可以猜测当 $a$、 $b$、$c$、$d$ 取不同值的时候 $R(n)$ 可能的形式，我们可以假设 $R(n) = 1$，尝试找出是否有对应的值。根据递推的等式，可以列出：
$$
\begin{cases}
1 = a \\
1 = 3 \times 1 + b \cdot 2^{n-1} + c\cdot n + d
\end{cases}
$$
不难发现：$a = 1$ 以及 $d = -2$，其余两个变量只能为 $0$。回代到 $R(n)$ 的通项公式中：
$$
R(n) = f(n) - 2\varphi(n) = 1
$$
我们明白，如果能按照类似的方式找到 $4$ 个这样的方程，我们就可以把四个函数全部都解出来。现在继续尝试一些其它的函数。考虑到递推式中有 $n$ 这种东西，可以尝试当 $R(n) = n$ 时的情况：
$$
\begin{cases}
0 = a \\
n + 1 = 3n + b \cdot 2^{n-1} + c\cdot n + d
\end{cases}
$$
可以解出 $a = 1,\;c = -2,\;d = 1$。因此 $f(n) - 2h(n) + \varphi(n) = n$。

根据同样的想法，尝试一下 $R(n) = 2^n$：
$$
\begin{cases}
2 = a \\
2^{n+1} = 3 \times 2^n + b \cdot 2^{n-1} + c\cdot n + d
\end{cases}
$$
此时 $a = 2,\;b = -2$，同时我们有 $f(n) - g(n) = 2^{n-1}$。

此外注意到第二个递推式中 $R(n)$ 前的系数是 $3$，说明通项公式中应该是有 $3^n$ 这种东西的。于是尝试 $R(n) = 3^n$：
$$
\begin{cases}
3 = a \\
3^{n + 1} = 3^{n+1} + b \cdot 2^{n-1} + c\cdot n + d
\end{cases}
$$
So easy, $a = 3$，并且可以直接知道 $f(n) = 3^{n - 1}$。

现在 $4$ 个方程集齐了，只需要解下面这个方程组：
$$
\left\{
\begin{aligned}
f(n) - 2\varphi(n) & = 1 \\
f(n) - 2h(n) + \varphi(n) & = n \\
f(n) - g(n) &= 2^{n-1} \\
f(n) & = 3^{n - 1}
\end{aligned}
\right.
$$
不难解出：
$$
\left\{
\begin{aligned}
f (n) & = 3^{n - 1} \\
g(n) & = 3^{n-1} - 2^{n - 1}\\
h(n) & = \frac14 3^n - \frac12 n - \frac14 \\
\varphi(n) & = \frac12 3^{n - 1} - \frac12
\end{aligned}
\right.
$$
现在来解决原问题。原问题中，$a = 4,\;b = 1,\;c = -4,\;d = 0$，所以 $R(n) = 4f(n) + g(n) - 4h(n) = 2\times 3^{n-1} - 2^{n-1}+2n+1$。纵观整个过程，Repertoire Method 并不简单，甚至有点繁琐，但仍不失为探究问题的一种好思路。