---
title: 数学问题杂记
create: 2017.12.16
modified: 2018.1.8
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