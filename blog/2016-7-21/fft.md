---
title: 有关多项式的算法
create: 2016.7.21
modified: 2016.7.21
tags: 多项式
      FFT
---

[TOC]
# 有关多项式的算法
## 多项式
一个度数为$n$的多项式为最高项的次数为$n - 1$的多个$x$的幂次与对应系数之积的和，通常用大写字母表示多项式。
如，下式是一个度数为$4$的多项式。将$x^2$的系数设为$0$就可消除这一项。
$$ A(x) = 3x^3 + 2x + 1 $$

用$\text{degree}(A)$来表示一个多项式的度数。一个多项式中会含有$\text{degree}(A)$项。

通常有两种表示多项式的方法：**系数表达**和**点值表达**。
系数表达即按照从低次项到高次项[^ordering]的顺序将每个项的系数放入一个向量中。如上面的多项式$A(x)$还可以表示成这样：
$$ \hat A(x) = (1,\;0,\;2,\;3) $$

[^ordering]:当然也可以从高次到低次，视情况选择方便的表示方法。

点值表达，顾名思义就是给定一些点，计算出多项式在这些点的值。
计算多项式在一个点$x_0$处的值可以用秦九韶算法[^huola]:
$$ A(x_0) = a_0 + x_0(a_1 + x_0(a_2 + \dots + x_0(a_{n-2} + x_0a_{n-1})\dots)) \tag{1.1}$$

这样可以在$\Theta(\text{degree}(A))$的时间内计算一个点处的值。

[^huola]: 也称作霍纳法则。

计算$n$个不同的点$x_0,\;x_1,\dots,\;x_{n-1}$处的值$y_0,\;y_1,\dots,\;y_{n-1}$，于是可以将多项式表示成$n$个二元组，二元组的第一项是选取的点$x_i$，第二项是该点计算出的值$y_i$。
因此之前的多项式可以表示成以下的形式：
$$ \hat A(x) = \{(0,\;1),\;(1,\;6),\;(2,\;29),\;(3,\;88)\} $$

可以证明，如果选择的求值点互不相同，那么一个含有$n$个元素点值表达会有唯一的度数为$n$的多项式。
因为点值表达可以用下面的矩阵方程表示出来：
$$
\left[
\begin{matrix}
1 & x_0 & x_0^2 & \cdots & x_0^{n-1} \\
1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots\\
1 & x_{n-1} & x_{n-1}^2 & \cdots & x_{n-1}^{n-1} \\
\end{matrix}
\right]
\left(
\begin{matrix}
a_0 \\
a_1 \\
\vdots \\
a_{n-1}
\end{matrix}
\right)
=\left(
\begin{matrix}
y_0 \\
y_1 \\
\vdots \\
y_{n-1}
\end{matrix}
\right)
\tag{1.2}
$$

方程左边的矩阵是一个**范德蒙德矩阵**，其行列式的值为：
$$
\prod_{0 \le i < j < n} (x_j - x_i)
$$

因此只要$x_0,\;x_1,\;\dots,\;x_{n-1}$中没有相同的值，该矩阵的行列式就不会为$0$。
这意味着它一定会有一个**逆矩阵**，从而可以将方程右边的列向量乘以逆矩阵，就可以得到原多项式的系数向量。

## 多项式加法
多项式加法是很简单的，只需要将对应次数的项的系数相加即可。
如果是点值表达，则需要两个多项式的采样点是一样的，然后对应点的值才可以直接相加减，最后得到的是新的多项式的点值表达。
两个多项式$A(x)$和$B(x)$的加法可以在$\Theta(\max\{\text{degree}(A),\;\text{degree}(B)\})$的时间内完成。

## 多项式乘法
如果采用系数表达，我们可以暴力地将多项式乘开然后合并同类项，这样可以在$O(\text{degree}(A) \cdot \text{degree}(B))$的时间内完成。然而这个复杂度并不妙。
相反，如果采用点值表达，则只需要$\Theta(\max\{\text{degree}(A),\;\text{degree}(B)\})$的时间，因为我们只要将对应采样点的值相乘就会得到新多项式的点值表达。
然而，点值表达方式并没有系数表达更有用。考虑能否利用点值表达的多项式乘法线性时间来加快系数表达的多项式乘法。
一个直接的方法就是先对原多项式在$\text{degree}(A) + \text{degree}(B)$个点[^sampling-points]处采样，然后做完点值表达的乘法之后，又进行插值操作，这样就可以得到系数表达的结果了。

[^sampling-points]: 因为新的多项式的度数为$\text{degree}(A) + \text{degree}(B)$。

然而并没有什么很快的采样/插值算法，但是使用快速傅立叶变换可以在$\Theta(n\log n)$的时间内完成采样和插值。

### 复数
**快速傅立叶变换**是用于快速计算**离散傅立叶变换 (DFT)**的结果的算法。由于DFT涉及到复数的运算，因此这里先扯一点复数的基本知识。
首先定义单位复数根$i = \sqrt{-1}$，可以将其想象成是垂直于实数轴的一个单位向量，因此所有的复数都是由$a + bi$这种形式给出的，其中$a$是实部，$b$是虚部。
单位复数根与自然对数的底数$\text{e}$有着相当密切的关系，下面的公式就是欧拉公式：
$$ \text{e}^{xi} = \cos x + i\sin x \tag{3.1.1}$$

为了证明这个等式，首先考虑一下$i$的幂次的规律：
$$
\begin{align}
& i^0 = 1,\; i^1 = i,\; i^2 = -1,\; i^3 = -i \\
& i^4 = 1,\; i^5 = i,\; i^6 = -1,\; i^7 = -i \\
& \dots
\end{align}
$$

我们注意到$i$的幂次是一个长度为$4$的循环节。考虑$\text{e}$的无限展开式：
$$
\begin{align}
\text{e}^{xi} & = \sum_{n=0}^{\infty} {x^ni^n \over n!} \\
& = 1 + xi - \frac{x^2}{2} - \frac{x^3}{6}i + \dots \\
& = \sum_{n = 2k,\;k \in \mathbf{N}}^{\infty} (-1)^k{x^n \over n!} + i\sum_{n = 2k + 1,\;k \in \mathbf{N}}^{\infty} (-1)^k{x^n \over n!}
\end{align}
$$

和式左边就是$\cos x$的无限展开形式，而右边就是$\sin x$形式。
因此：
$$ \text{e}^{xi} = \cos x + i\sin x $$

为了方便之后的公式书写，这里定义$n$次单位复数根为：
$$
\omega_n = \text{e}^{2\pi i/n}
\tag{3.1.2}
$$

从几何的角度来讲，相当于将一个周角均分成$n$份，从每一个角度发出一个单位长度的向量。
$\omega_8$的每一个幂次在平面上的情况如下图，注意$\omega_8^0 = 1$。

![w_8](http://git.oschina.net/riteme/blogimg/raw/master/fft/w.svg)

### DFT
接下来介绍DFT。标准的DFT是作用在一个长度为$n$复数序列$\{x_0,\;x_1,\;x_2,\;\dots,\;x_{n-1}\}$，将其变换为另一个复数序列$\{X_0,\;X_1,\;X_2,\;\dots,\;X_{n-1}\}$，其定义如下：
$$
X_k = \sum_{j=0}^{n-1} x_j\omega_n^{-jk}
\tag{3.2.1}
$$

我们当然可以从$\{X_0,\;X_1,\;X_2,\;\dots,\;X_{n-1}\}$得到$\{x_0,\;x_1,\;x_2,\;\dots,\;x_{n-1}\}$，即逆DFT：
$$
x_k = \frac1n\sum_{j=0}^{n-1}X_j\omega_n^{jk}
\tag{3.2.2}
$$

如何可以得到这个逆DFT公式呢？可以将DFT的过程视为一次矩阵乘法：
$$
\left[
\begin{matrix}
1 & 1 & 1 & \cdots & 1 \\
1 & \omega_n & \omega_n^2 & \cdots & \omega_n^{n-1} \\
1 & \omega_n^2 & \omega_n^4 & \cdots & \omega_n^{2(n-1)} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \omega_n^{n-1} & \omega_n^{2(n-1)} & \cdots & \omega_n^{(n-1)(n-1)}
\end{matrix}
\right]
\left(
\begin{matrix}
x_0 \\
x_1 \\
x_2 \\
\vdots \\
x_{n-1}
\end{matrix}
\right)
= \left(
\begin{matrix}
X_0 \\
X_1 \\
X_2 \\
\vdots \\
X_{n-1}
\end{matrix}
\right)
\tag{3.2.3}
$$

设等式左边的矩阵为$V$，下面将证明其逆矩阵$V^{-1}$的元素$[V^{-1}]_{jk} = \omega_n^{-jk} / n$：
因为
$$
[VV^{-1}]_{jk} = \sum_{c=0}^{n-1}(\omega_n^{jc})({\omega_n^{-ck} \over n}) = \frac1n\sum_{c=0}^{n-1}(\omega_n^{j-k})^c
\tag{3.2.4}
$$

由于几何级数的求和对复数也适用，所以：
$$
\begin{align}
\sum_{j=0}^{n-1}(\omega_n^k)^j & = {(\omega_n^k)^n - 1 \over \omega_n^k - 1} \\
& = {(\omega_n^n)^k - 1 \over \omega_n^k - 1} \\
& = 0
\end{align}
$$

注意，只有在$n \not\mid k$时上式成立。当$n \mid k$时，$\omega_n^k = 1$。
于是$V \cdot V^{-1}$中只有$j = k$的位置为$1$，其余元素均为$0$，即单位矩阵。所以$V^{-1}$确实是$V$的逆矩阵。

### FFT
如果根据DFT的定义来计算，需要$\Theta(n^2)$的时间。可以利用复数的一些特殊性质，我们可以在$\Theta(n\log n)$的时间内计算DFT及逆DFT，这就是快速傅立叶变换 (FFT)。
下面为了讨论方便，假设所有的给FFT处理的序列长度都是$2$的某次幂。
快速傅立叶变换是基于分治思想的。算法首先将序列分为两部分，一部分的元素的下标为偶数，另一部分为奇数：
$$
\begin{align}
A & = \{x_0,\;x_1,\;x_2,\;x_3,\;x_4,\;x_5,\;x_6,\;x_7\} \\
A^{[0]} & = \{x_0,\;x_2,\;x_4,\;x_6\} \\
A^{[1]} & = \{x_1,\;x_3,\;x_5,\;x_7\}
\end{align}
$$

可以注意到，下标为偶数就是下标的二进制表示的最后一位为$0$ (它们放入$A^{[0]}$)，奇数就是为$1$ (放入$A^{[1]}$)。
分成两部分后，对于每一部分递归求解。然后尝试将这两部分合并，得到原序列的DFT。
考虑假设我们获得了变换后的$A^{\prime[0]}$和$A^{\prime[1]}$。
$$
\begin{align}
A^{\prime[0]}(x) &= \sum_{j=0}^{n/2-1}A^{[0]}_jx^j \\
A^{\prime[1]}(x) &= \sum_{j=0}^{n/2-1}A^{[1]}_jx^j
\end{align}
$$

因此：
$$
A(x) = A^{\prime[0]}(x^2) + xA^{\prime[1]}(x^2) \tag{4.3.1}
$$

将单位复数根带入：
$$
\begin{align}
A^{\prime[0]}(\omega_n^{2k}) + \omega_n^kA^{\prime[1]}(\omega_n^{2k}) &= A(\omega_n^k) \\
A^{\prime[0]}(\omega_n^{2k}) - \omega_n^kA^{\prime[1]}(\omega_n^{2k}) &= A^{\prime[0]}(\omega_n^{2k}) + \omega_n^{k + n/2}A^{\prime[1]}(\omega_n^{2k}) \\
&= A^{\prime[0]}(\omega_n^{2k + n}) + \omega_n^{k + n/2}A^{\prime[1]}(\omega_n^{2k + n}) \\
&= A(\omega_n^{k+(n/2)})
\end{align}
$$

由此我们获得了如何将两部分合并为一部分的方法。
对于逆变换，可以使用同样的方法，只是单位复数根的次数的符号恰好相反，并且最后需要对每一个数除以$n$。

### FFT实现
#### 递归式FFT
递归实现FFT的过程非常简单，首先判断序列长度是否为$1$，如果为$1$则直接返回。
否则按照下标的奇偶性分为两部分，然后递归求解。
最后合并这两部分的结果。

```
function RECURSIVE-FFT(x, reverse = False):
    if x.length == 1:  # 如果长度为1
        return x
    
    将序列分为a[0]和a[1]
    a'[0] = RECURSIVE-FFT(a[0])
    a'[1] = RECURSIVE-FFT(a[1])
    
    X = [0..x.length - 1]
    if reverse:  # 如果是逆变换
        w_n = exp(0 + (-2 * pi / n)i)
    else:
        w_n = exp(0 + (2 * pi / n)i)
    w = 1
    for k in [0, x.length / 2 - 1]:
        t = w * a'[1][k]
        X[k] = a'[0] + t
        X[x.length / 2 + k] = a'[0] - t
        w *= w_n
    
    return X
```

#### 迭代式FFT
与递归式FFT相比，效率更高的是无需递归的迭代式。
首先考虑求值的顺序。对于一个下标而言，它的二进制表示实际上已经决定了它将要移动的路径。
即从低位开始，如果是$0$则向左运动，否则向右运动，然后检查其高位。
更进一步，观察划分完之后的序列，把每一个下标所对应的二进制翻转过来，这恰好是递增的顺序。
因此我们可以实现一个从高位到低位的加法器，从而计算下一个元素该是谁。
这个算法被称作雷德算法 (Rader's algorithm)。

```
function RADER(x):
    n = x.length
    
    X = [0..n - 1]
    X[0] = x[0]
    rev = 0
    for i in [1, n - 1]:
        k = n / 2
        while k < rev:
            rev -= k
            k /= 2
        rev += k
        X[rev] = x[k]
    
    return X
```

这样就可以按照顺序进行合并，第一次每$2$个进行合并，然后每$4$个进行合并， ...，最后就是整体进行合并。

```
function ITERATIVE-FFT(x):
    x = RADER(x)
    
    n = x.length
    s = 2
    while s <= n:
        if reverse:  # 如果是逆变换
            w_n = exp(0 + (-2 * pi / n)i)
        else:
            w_n = exp(0 + (2 * pi / n)i)
        for i in [0, n] by s:
            left = i
            right = i + s - 1
            mid = (left + right) / 2
            w = 1
            for k in [0, mid - 1]:
                t = w * x[mid + k]
                x[mid + k] = x[left + k] - t
                x[left + k] = x[left + k] + t
                w *= w_n
        s *= 2
    
    return x
```

### 多项式乘法
前面讲了那么多DFT，那多项式乘法与DFT有什么关系呢？
事实上，在多项式上采样实际上就是一次DFT的过程。
获得了点值表达之后，就可以在$\Theta(n)$的时间内完成乘法。
最后进行一遍逆DFT可以得到结果！
时间复杂是$\Theta(n\log n)$的，$n$是两个多项式的度数和。

需要注意的是，上面的FFT需要序列长度为$2$的幂，解决方式就是将补$0$来完成。
实际实现中，需要注意$\text{e}$的复数幂，即单位复数根的计算十分缓慢，因此对于递归式的FFT，需要先预处理每一层的单位复数根。
