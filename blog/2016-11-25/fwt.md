---
title: 位运算卷积与FWT
create: 2016.11.25
modified: 2016.11.25
tags: 位运算卷积
      FWT
---

[TOC]
# 位运算卷积与FWT
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

其中$\oplus$指代任意二元位运算符号，如异或 (就是记做$\oplus$)、与运算 ($\land$) 和或运算 ($\lor$) 等等。

注意到，在多项式乘法中，如果两个多项式的界为$A$和$B$，那么答案的界就是$A + B - 1$。而在位运算卷积中，却是$2^{\left\lceil\log_2\max\{A,B\}\right\rceil}$。而且对于两个输入向量而言，末尾添加几个$0$是不会对答案产生影响的[^tailing-zero]。因此，像在快速傅里叶变换中一样，假定输入的向量大小一致且均为$2$的幂，设这个大小为$n$。

[^tailing-zero]: 当然需要保证添加完$0$后结果的界不变。数值上不会有影响。

## 特殊情况
为了探寻规律，我们以**异或**为例，手动计算一下$n$很小时的情况。

### $n = 2^0$
当输入两个数时，结果会是一个数。由于$0 \oplus 0 = 0$，所以：

$$
C_0 = A_0 \cdot B_0
\tag{2.1}
$$

So easy, 也没什么意思。

### $n = 2^1$
输入两个二元组$A = (a_0, a_1)$和$B = (b_0, b_1)$。得到的结果$C$是：

$$
C = (a_0 b_0 + a_1 b_1, a_0 b_1 + a_1 b_0)
\tag{2.2}
$$

不如大胆的尝试一下，能否通过某种变换，从而能够使用更简单的点积来计算呢，就像下面这个样子：

$$
TA \cdot TB = TC
\tag{2.3}
$$

这里$T$表示变换，同时他还需要一个逆变换从而使得我们能够得到$C$。我们可以从线性代数的角度来考虑这个问题，那么我们希望$T$能够是一个线性变换，这样我们就可以用矩阵来表示之。

那么意味着我们要找到一个矩阵$T$，满足：

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

首先这个线性变换只在二维向量空间上进行的，所以$T$应该是一个$2 \times 2$的矩阵，于是设：

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

一个二元一次方程，有很多解了啦，但是我们只需要一个。最简单的解法[^zero]就是对应的项的系数相同。

[^zero]: 为什么不直接将$m$和$n$设为$0$？因为那样太naive了，你得到的$T$是零矩阵。

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

然后发现$n$的这两个取值都可以满足$mn = n$。那么对于$p$和$q$是同理的，因此$T$的一种形式是这样的：

$$
\left[
\begin{matrix}
1 & \pm 1 \\
1 & \pm 1 \\
\end{matrix}
\right]
\tag{2.10}
$$

不过我们不能够全部填$1$，因为我们在一开始的要求是$T$要有逆变换，但是全是$n = q$的矩阵不满秩，所以没有逆矩阵。因此，我们只有两种选择。

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

实在记不住就爆枚一下矩阵吧，这样的$\pm 1$矩阵没几个，试一试就好......

### $n = 2^m \;\; (m \geqslant 2)$
现在来考虑更复杂的情况。

跟前面一样的思想，我们企图找到$T_m$，满足：

$$
T_mA \cdot T_mB = T_mC
\tag{2.12}
$$

我们已经知道$T_0 = 1$并且求出了$T_1$。

基于这样一个事实：

$$
a \oplus b = c \Longrightarrow
a[i] \oplus b[i] = c[i]
\tag{2.13}
$$

这里$a[i]$表示$a$的二进制表示中的第$i$位。这说明二进制运算有一个重要的性质就是其每一位可以分开运算。

这有什么好处呢？我们先考虑最高位，这样将输入向量分为两部分：

$$
A = (A_0, A_1) \\
B = (B_0, B_1)
\tag{2.14}
$$

下标为$0$的表示最高位为$0$，下标为$1$的表示最高位为$1$。实际上，就是将向量切成了两半。

对于结果$C = (C_0, C_1)$而言，在不考虑最高位的情况下，$A_0$、$A_1$、$B_0$和$B_1$任意求卷积都是可以对$C_0$和$C_1$有贡献的 (卷积后一个向量加法累计贡献)。但是此处我们需要考虑最高位，那么就会有一定的限制，也就是下标的运算结果的限制。

不难发现，这实际上退化为了$n = 2$的情况，这里用之前的方法来表示：

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

但实际上已经没有意义啦！因为$(2.15)$就是一个分治计算的过程，并且它的复杂度是：

$$
T(n) = 2T(n / 2) + \Theta(n) = \Theta(n\log n)
\tag{2.17}
$$

于是我们获得了FWT算法！

## FWT算法
前面BB了一大段，现在来梳理一下：

1. 我们计算$TA$和$TB$。
2. 然后答案就是$T^{-1}(TA \cdot TB)$。

如何计算$TA$和$T^{-1}A$？根据$(2.15)$式，我们先要按最高位分成两个向量，对于每一个子向量，递归计算其经过变换后的结果。然后根据$T_1$来合并结果。

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
A = (TA_0 + TA_1, TA_0 - TA_1)
\tag{3.2}
$$

你只用按照矩阵的形式来计算就可以了。
对于逆变换，就是这样合并：

$$
A = \left({TA_0 + TA_1 \over 2}, {TA_0 - TA_1 \over 2}\right)
\tag{3.3}
$$

[^other-forms]: 由于我们已经得到了矩阵，所以这个变换是线性变换，你可以有其它的写法。

## 具体实现
为了方便理解，在这里给出用Python编写的FWT算法，依然是异或的例子。

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
与快速傅里叶变换类似，FWT也可以改写为迭代的版本，具体的原理可以参见快速傅里叶变换的实现：

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
\tag{5.1}
$$

对于或运算而言：

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
\tag{5.2}
$$

实现它们的位运算卷积就只用修改合并的过程即可。
