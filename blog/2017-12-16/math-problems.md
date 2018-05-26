---
title: 数学问题杂记
create: 2017.12.16
modified: 2018.5.26
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

事实上，对于任意的**正无理数** $\alpha$ 和 $\beta$，只要满足 $1/\alpha + 1/\beta = 1$，集合 $A = \left\{\left\lfloor \alpha k \right\rfloor \mid k \in \mathbf{N}^+\right\}$ 和集合 $B = \left\{\left\lfloor \beta k \right\rfloor \mid k \in \mathbf{N}^+\right\}$ 就会是一个正整数的划分。具体的证明方法与上面类似。

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

### 2018.2.17

#### 问题描述

证明，对于任意的**整数** $n$ 和**正整数** $m$，满足：
$$
\left\lceil {n \over m} \right\rceil = \left\lfloor {n + m - 1 \over m} \right\rfloor
$$

#### 解决方案

直接证明这个问题并不是特别困难，因为右边就是 $1 + \lfloor n/m - 1/m \rfloor$，然后分情况讨论 $n/m$ 是否为整数就可以得到结论。这里就不详细说了。

另外一种方法比较有意思，考虑将 $n$ 表示为 $m\lfloor n/m \rfloor + n \bmod m$ 的形式，然后上式左右同减 $\lfloor n/m \rfloor$ 可以得到：
$$
\begin{aligned}
& \left\lceil {n \over m} \right\rceil = \left\lfloor {n + m - 1 \over m} \right\rfloor \\
\Leftrightarrow \  & \left\lceil {n \over m} \right\rceil - \left\lfloor {n \over m} \right\rfloor = \left\lfloor {m\lfloor n/m \rfloor + n \bmod m + m - 1 \over m} \right\rfloor  - \left\lfloor {n \over m} \right\rfloor \\
\Leftrightarrow \  & \left[\frac{n}m \not\in \mathbf{Z} \right] = \left\lfloor {n \over m} \right\rfloor + \left\lfloor {n \bmod m + m - 1 \over m} \right\rfloor  - \left\lfloor {n \over m} \right\rfloor \\
\Leftrightarrow \  & [n \bmod m \neq 0] = [n \bmod m + m - 1 \geqslant m] \\
\Leftrightarrow \  & [n \bmod m > 0] = [n \bmod m > 0]
\end{aligned}
$$
从而证明了等式。

### 2018.4.4

#### 问题描述

（IMO 2012 预选题 **C2**）

在 $\{1,2,...,n\}$ 中最多能选出多少对**不相交**的二元组 $(a, b)$，满足 $a + b \leqslant n$，并且任意两对的元素之和不同？

如，当 $n = 6$ 时，可以找出 $2 + 4 = 6$ 和 $1 + 3 = 4$，并且最多也只能找出两对。

#### 解决方案

首先考虑上界，假设找到了 $m$ 对，则选出来的数字之和至少是：
$$
\sum_{k=1}^{2m}k = m(2m + 1)
$$
而每对的和两两不同，意思是数字之和至多为：
$$
\sum_{k = 0}^{m-1}(n-k) = mn - {m(m-1) \over 2}
$$
根据这两个界限，可知：
$$
m \leqslant {2n - 1 \over 5} \Leftrightarrow m \leqslant \left\lfloor {2n - 1 \over 5} \right\rfloor
$$
现在我们来尝试构造，使得正好能选出 $\lfloor (2n - 1)/5 \rfloor$ 对二元组。为了更方便地考虑这个问题，首先构建一个直观一点的模型。设第 $k$ 个二元组（$1 \leqslant k \leqslant m$）为 $(a_k, b_k)$，以及 $c_k = a_k + b_k$。尝试 $a_k = k$ 以及 $c_k = n - k + 1$ 的情况（也就是选取的最小的 $m$ 个数字和最大的 $m$ 个和，因为这样看起来成功率高一些），建立一个表格，如下图所示，其中每一个在第 $x$ 行第 $y$ 列的单元格上的数字为 $c_y - a_x$，代表 $b_k$ 的候选值：

![imo-2012-c2-n11](https://gitee.com/riteme/blogimg/raw/master/math-2017-6/imo-2012-c2-n11.svg)

<center>(**Fig.1.** $n = 11$，$m = 4$ 时的情况。 左边一竖列从上至下为 $a_1..a_m$，最上面一横排从左至右为 $c_m..c_1$，中间 $16$ 个单元格代表的是 $b_k$ 的候选值。图中给出了一种构造方案，即 $1 + 8 = 9$，$2+9=11$，$3+5=8$ 和 $4+6=10$，这也是最优的方案之一)</center>

观察这个表格，一个重要的信息就是每一个从左上至右下的斜列（后简称斜列）上的数字是一样的。正如上图中所展示的，我们需要从中间 $m^2$ 个单元格中圈出 $m$ 个数字作为 $b_1..b_m$。当然这是有讲究的。由于不能选相同的数字，所以**每一行、每一斜列均只能圈一个**；因为和要两两不同，所以**每一竖列也只能圈一个**。同时我们注意到左下角可能会有和 $a_1..a_m$ 相同的区域，姑且称其为 “禁区”，因为这个里面的数字也不能圈。如果这些条件均满足了，那么不难发现我们得到了一个合法方案。

根据上面的限制，格子中究竟写了什么数字已经不再重要了。现在的麻烦主要在于左下角的 “禁区”，它导致我们不能随意选择。因此，在构造的时候，要尽可能远离那个区域，也就是左下角要尽可能留出空白。为了探究规律，手玩一下 $m$ 较小的情况：

![imo-2012-c2-m16](https://gitee.com/riteme/blogimg/raw/master/math-2017-6/imo-2012-m1-6.svg)

<center>(**Fig.2.** $m$ 为 $1..6$ 时的最优解？)</center>

上图中 $m = 6$ 的规律已经体现得很明显了。记第 $x$ 行第 $y$ 列为 $(x, y)$。我们从 $(1, 2)$ 开始，设当前处在 $(x, y)$ 处，则下一步移动到 $(x+1,y+2)$ 处。如果 $y + 2 > m$，则移动到 $(x + 1, 1)$ 处。这有点类似于象棋中的 “跳马”。

这样构造出来的方案显然是满足要求的，但是我们还需要考察 $m$ 的最大值，因为随着 $m$ 的增大，“禁区” 的范围也会扩大。由于我们的 “马步” 走法的直线的斜率小于 “禁区” 边界的斜率，所以只需考虑第 $1$ 列中的情况。在表格中 $(x, y)$ 上的数字为 $n - m - x + y$，易知最左列中 “禁区” 最高点是**倒数**第 $3m - n$ 个格子，而在这一列中，我们选取的位置是**倒数**第 $\lceil m/2 \rceil$ 个格子，所以：
$$
\begin{aligned}
& 3m - n < \left\lceil {m\over 2} \right\rceil \\
\Leftrightarrow \: & 3m - n < \frac{m}2 \\
\Leftrightarrow \: & m < {2n \over 5} \\
\Leftrightarrow \: & m \leqslant \left\lceil{2n \over 5}\right\rceil - 1 = \left\lceil{2n - 5\over 5}\right\rceil \\
\end{aligned}
$$
虽然我们得到的结果与之前不同，但实际上 $\lceil (2n - 5) / 5 \rceil = \lfloor (2n - 1) / 5 \rfloor$，这是因为：
$$
\begin{aligned}
&\left\lceil {2n - 5 \over 5} \right\rceil = \left\lfloor {2n - 1 \over 5} \right\rfloor \\
\Leftrightarrow \: & \left\lceil {2n - 5 \over 5} \right\rceil \leqslant {2n - 1 \over 5} < \left\lceil {2n - 5 \over 5} \right\rceil + 1 \\
\Leftrightarrow \: & \left\lceil {2n - 1 \over 5} - \frac45 \right\rceil \leqslant \left\lfloor {2n - 1 \over 5} \right\rfloor \leqslant {2n - 1 \over 5} < {2n \over 5} \leqslant \left\lceil {2n \over 5} \right\rceil
\end{aligned}
$$
最后一行最左边的小于等于号是通过分 $(2n - 1) / 5$ 是否为整数的两种情况讨论得来的：当它是整数时取等，否则其小数部分不大于 $4/5$，所以不等式成立。综上，答案就是 $\lceil (2n - 5) / 5 \rceil = \lfloor (2n - 1) / 5 \rfloor$。

### 2018.5.19

#### 问题描述

(1) 给定自然数 $n​$，计算 $\newcommand{up}[1]{\left\lceil #1 \right\rceil}\newcommand{dw}[1]{\left\lfloor #1 \right\rfloor} \sum_{k=1}^\infty 2^k\lfloor n/2^k + 1/2\rfloor^2​$。

(2) 给定实数 $x$，定义 $\newcommand{\dis}[1]{\lVert #1 \rVert} \dis{x} = \min\{\up{x} - x,\ x - \dw{x}\}$ 即 $x$ 离最近的整数的距离，计算 $\sum_{k \in \mathbf{Z}} 2^k \lVert x / 2^k \rVert^2$。

#### 解决方案

(1) 计算这个和的思路有点非常规，考虑递推的方法，设 $S_n$ 为上面的和式。考虑到任意自然数 $n$ 均可被唯一分解为 $2^p \cdot q$（$q$ 是奇数），当 $k = p + 1$ 时：
$$
\begin{aligned}
\left\lfloor {n \over 2^k} + \frac12 \right\rfloor & = \left\lfloor {q + 1 \over 2} \right\rfloor = {q + 1 \over 2} \\
\left\lfloor {n - 1 \over 2^k} + \frac12 \right\rfloor & =  \left\lfloor {q + 1 \over 2} \right\rfloor - 1 = {q - 1 \over 2}
\end{aligned}
$$
所以 $S_n$ 和 $S_{n - 1}$ 中第 $k$ 项之差为 $2^k \cdot q = 2n$，而其余项中 $n / 2^k$ 得不到像上面 $q$ 这样的奇数，两者结果相同。所以 $S_n = S_{n - 1} + 2n = n^2 + n$。

(2) 第二问实际上除了形式与第一问类似，其实没有多少关联......

为了方便书写和探究，记函数 $f(x)$ 为我们需要计算的式子。写个程序瞎试一下其实会发现 $f(x) = x \ (x \geqslant 0)$。此外由于平方的原因，$f(-x) = f(x)$，不难推测 $f(x) = \lvert x \rvert$。

难的是如何证明猜出来的结论。首先无论 $k$ 趋向于正无穷还是负无穷，级数总是收敛的，故对于所有的 $x$，$f(x)$ 总存在。由于 $f(-x) = f(x)$，因此我们可以只用考虑 $x \geqslant 0$ 的情况。另外可以注意到 $f(2x) = 2f(x)$。令 $f(x) = l (x) + r(x)$，将 $f(x)$ 中 $k \leqslant 0$ 的项放入 $l(x)$ 中，其余的放入 $r(x)$ 中，分开处理这两部分。

对于 $l(x)$，由于 $1/2^k$ 当 $k \leqslant 0$ 时均为整数，所以 $\lVert x / 2^k \rVert = \lVert (x + 1) /2^k \rVert$，即 $l(x + 1) = l(x)$。因为 $\lVert x \rVert \leqslant 1/2$，所以 $l(x) \leqslant \sum_{k = 0}^\infty 2^k / 4 = 1/2$。

对于 $r(x)$，$k > 0 \Rightarrow 2^k \geqslant 2$，$0 \leqslant x < 1$ 时，$\lVert x / 2^k \rVert$ 和 $\dis{(x+1)/2^k}$ 都可以简单地化简出来。此时 $r(x) = \sum_{k=1}^\infty x^2/2^k = x^2 < 1$，而 $r(x + 1) = (1-x)^2/2 + \sum_{k=2}^\infty (x+1)^2/2^k = x^2 + 1$。即 $r(x + 1) = r(x) + 1$。综上，当 $0 \leqslant x < 1$ 时 $f(x + 1) = f(x) + 1$。

是否有更一般的结论呢？对于任意自然数 $n$，$f(x + n) = f(x) + n$ 能否被证明？考虑到 $f(2x) = 2f(x)$，因此尝试将 $n$ 设为 $2^mq + r$ 的形式，其中 $m \geqslant 1$，$r$ 为 $0$ 或 $1$ 从而使得 $m$ 的条件可以满足。对 $n$ 使用归纳法，当 $n = 0,\ 1$ 时显然，之后 $f(x + n) = 2^mf((x+r)/2^m + q)$，由于 $q < n$ 且 $x + r < 2 \leqslant 2^m$ 根据归纳假设，之前的式子等于 $2^mf((x+r)/2^m) + 2^mq = f(x + r) + n - r = f(x) + n$。

根据以上结论，再结合 $f(0) = 0$，我们已经可以得到对于任意整数 $n$，$f(n) = \lvert n \rvert$。接下来的步骤非常巧妙的利用了夹逼原理：还是假设 $x \geqslant 0$，对于任意正整数 $m$，我们有：
$$
\begin{aligned}
f(x) & = 2^{-m}f(2^mx) \\
& = 2^{-m}\dw{2^mx} + 2^{-m}f(\{2^mx\})
\end{aligned}
$$
现在是时候来证明我们的猜想了：
$$
\begin{aligned}
0 \leqslant \lvert f(x) - x \rvert & = \lvert 2^{-m}\dw{2^mx} - x + 2^{-m}f(\{2^mx\}) \rvert \\
& \leqslant 2^{-m}\lvert \dw{2^mx} - 2^mx \rvert + 2^{-m}f(\{2^mx\}) \\
& < 1\cdot 2^{-m} + (1/2 + 1) \cdot 2^{-m} = 5/2 \times 2^{-m}
\end{aligned}
$$
当 $m$ 趋近于无穷大时，右式趋近于 $0$。因此不难得到 $f(x) = \lvert x \rvert$ 的结论。