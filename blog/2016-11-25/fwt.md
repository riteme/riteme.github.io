---
title: 位运算卷积与FWT
create: 2016.11.25
modified: 2018.2.12
tags: 位运算卷积
      FWT
---

[TOC]
# 位运算卷积与 FWT
几行代码里隐藏数学真是高深莫测，只有勇者才能够发现这绝妙的规律。

## 位运算卷积
普通的卷积 (即多项式乘法) 是这个样子：

$$
C_i = \sum_{j + k = i} A_j \cdot B_k \;\;\;\;\forall \; j, k \in [0, n)
\tag{1.1}
$$

而位运算卷积就是将加号变为了**二元位运算**，就是这样：

$$
C_i = \sum_{j \oplus k = i} A_j \cdot B_k \;\;\;\;\forall \; j, k \in [0, n)
\tag{1.2}
$$

其中 $\oplus$ 指代任意二元位运算符号，如异或 (就是记做 $\oplus$)、与运算 ($\land$) 和或运算 ($\lor$) 等等。

注意到，在多项式乘法中，如果两个多项式的界为 $A$ 和 $B$，那么答案的界就是 $A + B - 1$。而在位运算卷积中，却是 $2^{\left\lceil\log_2\max\{A,B\}\right\rceil}$。而且对于两个输入向量而言，末尾添加几个 $0$ 是不会对答案产生影响的[^tailing-zero]。因此，像在快速傅里叶变换中一样，假定输入的向量大小一致且均为 $2$ 的幂，设这个大小为 $n$。

在下文中，向量 $A = (a_0, a_1, ..., a_k)$ 的倒置 $A^T​$ 为：
$$
A^T = \left[\begin{matrix}
a_0 \\
a_1 \\
\vdots \\
a_k
\end{matrix}\right] \tag{1.3}
$$

为了方便，矩阵 $M$ 与向量 $A = (a_0, a_1, ..., a_k)$ 相乘表示线性变换时，简写为 $MA$，代表 $(MA^T)^T$。

[^tailing-zero]: 当然需要保证添加完 $0$ 后结果的界不变。数值上不会有影响。

## 特殊情况
为了探寻规律，我们以**异或**为例，手动计算一下 $n$ 很小时的情况。

### $n = 2^0$
当输入两个数时，结果会是一个数。由于 $0 \oplus 0 = 0$，所以：

$$
C_0 = A_0 \cdot B_0
\tag{2.1}
$$

So easy, 也没什么意思。

### $n = 2^1$
输入两个向量 $A = (a_0, a_1)$ 和 $B = (b_0, b_1)$。得到的结果 $C$ 是：

$$
C = (a_0 b_0 + a_1 b_1, a_0 b_1 + a_1 b_0)
\tag{2.2}
$$

不如大胆的尝试一下，能否通过某种变换，从而能够使用更简单的点积来计算呢，就像下面这个样子：

$$
TA \cdot TB = TC
\tag{2.3}
$$

这里 $T$ 表示变换，同时他还需要一个逆变换从而使得我们能够得到 $C$。我们可以从线性代数的角度来考虑这个问题，那么我们希望 $T$ 能够是一个线性变换，这样我们就可以用矩阵来表示之。

那么意味着我们要找到一个矩阵 $T$，满足：

$$
T
\left[
\begin{matrix}
a_0 \\
a_1
\end{matrix}
\right]
\cdot
T
\left[
\begin{matrix}
b_0 \\
b_1
\end{matrix}
\right]
=
T
\left[
\begin{matrix}
a_0 b_0 + a_1 b_1 \\
a_0 b_1 + a_1 b_0
\end{matrix}
\right]
\tag{2.4}
$$

首先这个线性变换只在二维向量空间上进行的，所以 $T$ 应该是一个 $2 \times 2$ 的矩阵，于是设：

$$
T =
\left[
\begin{matrix}
m & n \\
p & q
\end{matrix}
\right]
\tag{2.5}
$$

那么之前是一个两个向量的点积式，于是我们可以列出两个方程来表示：

$$
\begin{cases}
\begin{aligned}
(ma_0 + na_1)(mb_0 + nb_1) & = m(a_0 b_0 + a_1 b_1) + n(a_0 b_1 + a_1 b_0) \\
(pa_0 + qa_1)(pb_0 + qb_1) & = p(a_0 b_0 + a_1 b_1) + q(a_0 b_1 + a_1 b_0)
\end{aligned}
\end{cases}
\tag{2.6}
$$

于是你发现第一个方程和第二方程没有区别......好吧，那就只研究第一个方程，将其暴力拆开是这样的：

$$
m^2a_0 b_0 + mna_0 b_1 + mna_1 b_0 + n^2a_1 b_1 = ma_0 b_0 + na_0 b_1 + na_1 b_0 + ma_1 b_1
\tag{2.7}
$$

一个二元二次方程，有很多解了啦，但是我们只需要一个。最简单的解法[^zero]就是对应的项的系数相同。

[^zero]: 为什么不直接将$m$和$n$设为$0$？因为那样太naïve了，你得到的$T$是零矩阵。

也就是说：

$$
m^2 = m \Longrightarrow m = 1
\tag{2.8}
$$

然后就是：

$$
n^2 = 1 \Longrightarrow n = \pm 1
\tag{2.9}
$$

然后发现 $n$ 的这两个取值都可以满足 $mn = n$。那么对于 $p$ 和 $q$ 是同理的，因此 $T$ 的一种形式是这样的：

$$
\left[
\begin{matrix}
1 & \pm 1 \\
1 & \pm 1 \\
\end{matrix}
\right]
\tag{2.10}
$$

不过我们不能够全部填 $1$，因为我们在一开始的要求是 $T$ 要有逆变换，但是全是 $n = q$ 的矩阵不满秩，所以没有逆矩阵。因此，我们只有两种选择。

对于其逆矩阵，我在这里帮你们算出来了：

$$
\left[
\begin{matrix}
1 & -1 \\
1 & 1 \\
\end{matrix}
\right]^{-1}
=
\left[
\begin{matrix}
0.5 & 0.5 \\
-0.5 & 0.5 \\
\end{matrix}
\right] \\
\left[
\begin{matrix}
1 & 1 \\
1 & -1 \\
\end{matrix}
\right]^{-1}
=
\left[
\begin{matrix}
0.5 & 0.5 \\
0.5 & -0.5 \\
\end{matrix}
\right]
\tag{2.11}
$$

实在记不住就爆枚一下矩阵吧，这样的 $\pm 1$ 矩阵没几个，试一试就好......

### $n = 2^m \;\; (m \geqslant 2)$
现在来考虑更复杂的情况。

跟前面一样的思想，我们企图找到 $T_m$，满足：

$$
T_mA \cdot T_mB = T_mC
\tag{2.12}
$$

我们已经知道 $T_0 = 1$ 并且求出了 $T_1$。

基于这样一个事实：

$$
a \oplus b = c \Longrightarrow
a[i] \oplus b[i] = c[i]
\tag{2.13}
$$

这里 $a[i]$ 表示 $a$ 的二进制表示中的第 $i$ 位。这说明二进制运算有一个重要的性质就是其每一位可以分开运算。

这有什么好处呢？我们先考虑最高位，这样将输入向量分为两部分：

$$
A = (A_0, A_1) \\
B = (B_0, B_1)
\tag{2.14}
$$

下标为 $0$ 的表示最高位为 $0$，下标为 $1$ 的表示最高位为 $1$。实际上，就是将向量切成了两半。

对于结果 $C = (C_0, C_1)$ 而言，在不考虑最高位的情况下，$A_0$、$A_1$、$B_0$ 和 $B_1$ 任意求卷积都是可以对 $C_0$ 和 $C_1$ 有贡献的 (卷积后一个向量加法累计贡献)。但是此处我们需要考虑最高位，那么就会有一定的限制，也就是下标的运算结果的限制。

不难发现，这实际上退化为了 $n = 2$ 的情况，这里用之前的方法来表示：

$$
T_1
\left[
\begin{matrix}
T_{m-1} A_0 \\
T_{m-1} A_1
\end{matrix}
\right]
\cdot
T_1
\left[
\begin{matrix}
T_{m-1}B_0 \\
T_{m-1}B_1
\end{matrix}
\right]
=
T_1
\left[
\begin{matrix}
T_{m-1}C_0 \\
T_{m-1}C_1
\end{matrix}
\right]
\tag{2.15}
$$

对于逆变换也是一样。

于是可以得知：

$$
T_m = T_1
\left[
\begin{matrix}
T_{m-1} \\
T_{m-1}
\end{matrix}
\right]
\tag{2.16}
$$

但实际上已经没有意义啦！因为 $(2.15)$ 就是一个分治计算的过程，并且它的复杂度是：

$$
T(n) = 2T(n / 2) + \Theta(n) = \Theta(n\log n)
\tag{2.17}
$$

于是我们获得了 FWT 算法[^fwt-name]！

[^fwt-name]: 有时也称 FWHT。

## FWT 算法
前面 BB 了一大段，现在来梳理一下：

1. 我们计算 $TA$ 和 $TB$。
2. 然后答案就是 $T^{-1}(TA \cdot TB)$。

如何计算 $TA$ 和 $T^{-1}A$？根据 $(2.15)$ 式，我们先要按最高位分成两个向量，对于每一个子向量，递归计算其经过变换后的结果。然后根据 $T_1$ 来合并结果。

以异或运算为例，假设我们钦定了使用这个矩阵作为我们的变换：

$$
T =
\left[
\begin{matrix}
1 & 1 \\
1 & -1 \\
\end{matrix}
\right]
\tag{3.1}
$$

那么合并的过程就是这样[^other-forms]：

$$
TA = (TA_0 + TA_1, TA_0 - TA_1)
\tag{3.2}
$$

你只用按照矩阵的形式来计算就可以了。
对于逆变换，就是这样合并：

$$
T^{-1} A = \left({T^{-1}A_0 + T^{-1}A_1 \over 2}, {T^{-1}A_0 - T^{-1}A_1 \over 2}\right)
\tag{3.3}
$$

[^other-forms]: 由于我们已经得到了矩阵，所以这个变换是线性变换，你可以有其它的写法。

## 具体实现
为了方便理解，在这里给出用 Python 编写的 FWT 算法，依然是异或的例子。

### 递归形式
递归形式简单粗暴，容易编写。

```python
import numpy

def fwt(X):
    """正变换，返回TX
    X: 输入向量
    """

    if len(X) == 1:
        return X

    m = len(X) // 2
    A0 = fwt(X[:m])
    A1 = fwt(X[m:])
    return numpy.array(*(A0 + A1), *(A0 - A1))

def rfwt(X):
    """逆变换，返回T^{-1}X
    X: 输入向量
    """

    if len(X) == 1:
        return X

    m = len(X) // 2
    A0 = rfwt(X[:m])
    A1 = rfwt(X[m:])
    return numpy.array(*((A0 + A1) / 2), *((A0 - A1) / 2))

def product(A, B):
    """计算卷积
    A, B: 输入向量
    """

    TA = fwt(A)
    TB = fwt(B)
    TC = TA * TB
    return rfwt(TC)

# 调用
print(product(
    numpy.array([1, 2, 3, 4]),
    numpy.array([2, 3, 3, 3])
))  # [29, 28, 27, 26]
```

### 迭代形式
与快速傅里叶变换类似，FWT 也可以改写为迭代的版本，具体的原理可以参见快速傅里叶变换的实现：

```python
import copy
import numpy

def iterative_fwt(X):
    A = copy.deepcopy(X)
    s = 2
    while s <= len(X):
        for i in range(0, len(X), s):
            for j in range(0, s // 2):
                tmp = A[i + j]
                A[i + j] += A[i + j + s // 2]
                A[i + j + s // 2] = tmp - A[i + j + s // 2]
        s *= 2

    return A

def iterative_rfwt(X):
    A = copy.deepcopy(X)
    s = 2
    while s <= len(X):
        for i in range(0, len(X), s):
            for j in range(0, s // 2):
                tmp = A[i + j]
                A[i + j] = (A[i + j] + A[i + j + s // 2]) / 2
                A[i + j + s // 2] = (tmp - A[i + j + s // 2]) / 2
        s *= 2

    return A
```

当然这里给出版本不是常数上效率最高的，大家可以根据实际情况改写代码。

## 其他的位运算

之前一直在讨论异或，没有关注与运算和或运算。因为它们的推导过程是一样的。这里就不重复其过程了。

对于与运算而言：
$$
T =
\left[
\begin{matrix}
1 & 1 \\
0 & 1 \\
\end{matrix}
\right] \\
T^{-1} =
\left[
\begin{matrix}
1 & -1 \\
0 & 1 \\
\end{matrix}
\right]
\tag{5.1}
$$

对于或运算而言：
$$
T =
\left[
\begin{matrix}
1 & 0 \\
1 & 1 \\
\end{matrix}
\right] \\
T^{-1} =
\left[
\begin{matrix}
1 & 0 \\
-1 & 1 \\
\end{matrix}
\right]
\tag{5.2}
$$

实现它们的位运算卷积就只用修改合并的过程即可。

## 其他运用

### 子集和

现在是时候来看一下**或卷积**了，按照之前方法，求出或卷积变换的一种形式。这里我们关注的是 $(5.2)$ 中的变换。FWT 算法运行过程中，是从低位到高位的顺序进行合并的。我们还是按照某一位来划分序列 $A = (A_0, A_1)$，那么 $TA$ 就是 $(A_0, A_0 + A_1)$，不难发现，原来的 $A_1$ 部分加上了 $A_0$，也就是相当于一个集合里面少了一个元素的集合的值被加了过来，这些集合都是自己的子集。因此，这样的 FWT 算法实际上计算的是下面这个东西：
$$
H(S) = \sum_{T \subseteq S} A(T) \tag{6.1}
$$
这就是**子集和变换**。同时利用 $T^{-1}$，我们可以根据 $H$ 来算出 $A$。关系运算符 "$\subseteq$" 是偏序，根据莫比乌斯反演[^mobius]，我们得知逆 FWT 算的是：
$$
\begin{aligned}
A(S) & = \sum_{T \subseteq S} \mu(T)H(S - T) \\
& = \sum_{T \subseteq S} (-1)^{|T|}H(S - T)
\end{aligned} \tag{6.2}
$$
即**逆子集和变换**。计算它们的时间复杂度都是 $\Theta(n \log n)$。

[^mobius]: 可以参见[我的博客](/blog/2016-8-18/mobius.html)。

### 子集卷积

利用或卷积，我们可以干些更有趣的事情，那就是子集卷积：对于两个向量 $F= (f_0, f_1, ..., f_{n-1})$ 和 $G = (g_0, g_1, ..., g_{n-1})$，它们的子集卷积 $H = F \times G$ 为：
$$
H(S) = \sum_{T \subseteq S} F(T)G(S - T) \tag{7.1}
$$
记 $k = \Theta(\log n)$，如果直接两边同时枚举计算，其复杂度为 $\Theta(n^2)$。如果先枚举 $S$，再枚举 $S$ 的子集 $T$，那么实际上我们只枚举了 $\sum_{j = 0}^k \binom{k}j 2^j = (1 + 2)^k = 3^k$ 次。为了能够降低复杂度，我们可以尝试使用 FWT 算法。容易看出，或卷积与子集卷积最为相似。我们可以把子集卷积等价地写成下面的形式：
$$
H(S) = \sum_{X \subseteq S} \sum_{Y \subseteq S} [X \cup Y = S][X \cap Y = \varnothing] F(X)G(Y) \tag{7.2}
$$
而或卷积可以等价地写成这样的形式：
$$
H(S) = \sum_{X \subseteq S} \sum_{Y \subseteq S} [X \cup Y = S] F(X)G(Y) \tag{7.3}
$$
与子集卷积相比，只是少了一个交集为空的条件。为了能够解决这个条件，我们可以从集合的大小下手。主要原因是大小只有 $\Theta(\log n)$ 种，并且 $|A \cup B| \leqslant |A| + |B|$（当且仅当 $A$ 与 $B$ 无交集时取等），这样一来就可以按照大小分类进行 FWT。

具体的做法如下，首先令：
$$
F_k(S) = \begin{cases}
F(S) & (|S| = k) \\
0 & (\text{otherwise})
\end{cases} \tag{7.4}
$$
类似的方法定义 $G_k$、$H_k$。令元素个数为 $k = \Theta(\log n)$，枚举 $i$ 和 $j$ 满足 $i + j = l$，将 $F_i$ 和 $G_j$ 进行或卷积后贡献给 $H_l$，最后将 $H_0$ 到 $H_k$ 全部加起来就是子集卷积后的 $H$。这里需要注意的是，$F_i$ 和 $G_j$ 的卷积不必每次都做 FWT 和逆 FWT 变换，就像多项式乘法一样，经过 FWT 之后的序列之间的点积就是原序列的卷积，序列之间的加法还是原序列的加法。因此最终的复杂度是 $\Theta(2^k k^2) = \Theta(n \log^2 n)$。

下面是我的 Python 2 实现：

```python
n = int(raw_input())
assert n & (n - 1) == 0, 'Argument "n" must be a power of 2.'

f = map(int, raw_input().split())
g = map(int, raw_input().split())

def fwt(X):
    if len(X) == 1:
        return X

    m = len(X) >> 1
    A, B = fwt(X[:m]), fwt(X[m:])
    for i in xrange(m):
        A.append(A[i] + B[i])
    return A

def rfwt(X):
    if len(X) == 1:
        return X

    m = len(X) >> 1
    A, B = rfwt(X[:m]), rfwt(X[m:])
    for i in xrange(m):
        A.append(B[i] - A[i])
    return A

def cnt(x):
    r = 0
    while x:
        x ^= x & (-x)
        r += 1
    return r

def add(A, B):
    return [A[x] + B[x] for x in xrange(len(A))]

def mul(A, B):
    return [A[x] * B[x] for x in xrange(len(A))]

def show(X):
    print ' '.join(map(str, X))

k = cnt(n - 1) + 1
F = [[0] * n for i in xrange(k)]
G = [[0] * n for i in xrange(k)]
H = [[0] * n for i in xrange(k)]

# 按照大小分组
for i in xrange(n):
    c = cnt(i)
    F[c][i] = f[i]
    G[c][i] = g[i]

# 提前进行 FWT
for i in xrange(k):
    F[i] = fwt(F[i])
    G[i] = fwt(G[i])

# 卷积部分
for i in xrange(k):
    for j in xrange(k - i):
        print i, j
        H[i + j] = add(H[i + j], mul(F[i], G[j]))

for i in xrange(k):
    H[i] = rfwt(H[i])

# 计算结果
R = [0] * n
for i in xrange(n):
    c = cnt(i)
    R[i] = H[c][i]

show(R)
```