---
title: 莫比乌斯反演
create: 2016.8.18
modified: 2016.8.18
tags: 数学
      组合数学
      莫比乌斯反演
---

[TOC]
# 莫比乌斯反演
> 我把《组合数学》抄了一遍，免得我记不住......

## 偏序集
这里的莫比乌斯反演是从关联代数的角度来介绍的。首先介绍一个基础的概念：偏序集。
它通常写作$(X_n,\;\le)$，其中$X_n$是一个有限或者无限的集合，$\le$是代指偏序关系，而**不是特指小于等于符号**。
所谓偏序关系，就是指$a,\;b,\;c \in X_n$并且$a \le b,\;b \le c$，有$a \le c$的性质的关系。
这种偏序关系一般是比较符$\le$、集合的$\subseteq$符号和整除$\;\mid\;$。

## 卷积
对于定义在偏序集$(X_n,\;\le)$上的二元函数$f(x,\;y)$，我们假定当$x \not\le y$时，$f(x,\;y)$均为$0$，这样是为了方便我们之后的讨论。
考虑偏序集$(X_n, \le)$上的二元函数$f(x,\;y)$和$g(x,\;y)$，定义它们的卷积为：
$$
(f \times g)(x,\;y) = \sum_{x \le z \le y} f(x,\;z)g(z,\;y) \tag{2.1}
$$

这个卷积满足结合律：
$$
(f \times g) \times h = f \times (g \times h) \tag{2.2}
$$

注意，这个卷积**不一定[^possible]满足交换律**。

[^possible]: 在偏序集$(X_n,\;\mid\;)$上简化后的卷积 (即狄利克雷卷积)，会满足交换律。

以及三种强行定义的莫名其妙的函数：
$\delta$ (delta) 函数：
$$
\delta(x,\;y) = [x = y] \tag{2.3}
$$

任意函数卷$\delta$函数均会得到原函数。

$\zeta$ (zeta) 函数：
$$
\zeta(x,\;y) = [x \le y] \tag{2.4}
$$

以及莫比乌斯$\mu$函数是定义为$\zeta$函数的**逆函数**，即：
$$
\mu \times \zeta = \zeta \times \mu = \delta \tag{2.5}
$$

展开卷积可得：
$$
\begin{align}
\delta = \mu \times \zeta \Longrightarrow \delta(x,\;y) & = \sum_{x \le z \le y} \mu(x,\;z)\zeta(z,\;y) \\
& = \sum_{x \le z \le y} \mu(x,\;z)
\end{align}
$$

因此，当$x \neq y$时：
$$
\mu(x,\;y) = - \sum_{x \le z \lt y} \mu(x,\;z) \tag{2.6}
$$

## 莫比乌斯反演公式
> **(莫比乌斯反演公式)**
> 对于有限偏序集$(X_n,\;\le)$上的两个函数$F(x,\;y)$和$G(x,\;y)$，如果：
> $$ G(x,\;y) = \sum_{x \le z \le y} F(x,\;z) \tag{3.1}$$
> 
> 那么：
> $$F(x,\;y) = \sum_{x \le z \le y} G(x,\;z)\mu(z,\;y)  = (G \times \mu)(x,\;y) \tag{3.2}$$

**证明** 首先将式子展开：
$$
\begin{align}
F(x,\;y) & = \sum_{x \le z \le y} G(x,\;z)\mu(z,\;y) \\
& = \sum_{x \le z \le y} \mu(z,\;y) \sum_{x \le m \le z} F(x,\;m)
\end{align}
$$

我们使用$\zeta$函数来表示上下界，于是式子改写为以下形式：
$$
\sum_{x \le z \le y} \mu(z,\;y) \sum_{m \in X_n} F(x,\;m)\zeta(x,\;m)\zeta(m,\;z)
$$

改变求和的枚举顺序，先枚举$m$，其值依然不变：
$$
\sum_{m \in X_n} \sum_{x \le z \le y} \zeta(m,\;z)\mu(z,\;y)\zeta(x,\;m)F(x,\;m)
$$

由于当$m \lt x$的时候$\zeta(x,\;m)$为$0$，因此只用考虑$m \ge x$。
并且当$m \ge x$时，$z \ge m$必需成立。
因此可以改写下界：
$$
\sum_{m \in X_n} \sum_{m \le z \le y} \zeta(m,\;z)\mu(z,\;y)F(x,\;m)
$$

然后变成了卷积的形式：
$$
\begin{align}
\sum_{m \in X_n} F(x,\;m) \sum_{m \le z \le y} \zeta(m,\;z)\mu(z,\;y) & = \sum_{m \in X_n} F(x,\;m) \delta(m,\;y) \\
& = F(x,\;y)
\end{align}
$$

当$m = y$时，$\delta(m,\;y)$才为$1$，所以综上所述：
$$
F(x,\;y) = \sum_{x \le z \le y} G(x,\;z)\mu(z,\;y) \tag{3.2}
$$

## 偏序集直积
对于两个偏序集$(A,\;\le_1)$和$(B,\;\le_2)$，它们的直积$C = A \times B = (A \times B,\;\le)$也是偏序集，其中的元素为$(x,\;y)\;\;(x \in A,\;y \in B)$。其关系$\le$的定义如下：
$$
(x_1,\;y_1) \le (x_2,\;y_2) \Longleftrightarrow x_1 \le_1 x_2 \land y_1 \le_2 y_2
$$

对于偏序集的直积，我们有以下定理：

> 设$A$和$B$的莫比乌斯函数分别为$\mu_1$和$\mu_2$，那么$C$的莫比乌斯函数满足：
> $$\mu((x_1,\;y_1),\;(x_2,\;y_2)) = \mu_1(x_1,\;x_2)\mu(y_1,\;y_2) \tag{4.1}$$

**证明** 对于$(x_1,\;y_1) \not\le (x_2,\;y_2)$和$(x_1,\;y_1) = (x_2,\;y_2)$的情况，上式显然成立。
假设对于满足$(x_1,\;y_1) \le (u,\;v) \lt (x_2,\;y_2)$的二元组均满足，那么有：
$$
\begin{align}
\mu((x_1,\;y_1),\;(x_2,\;y_2)) & = - \sum_{(x_1,\;y_1) \le (u,\;v) \lt (x_2,\;y_2)} \mu((x_1,\;y_1),\;(u,\;v)) \\
& = - \sum_{(x_1,\;y_1) \le (u,\;v) \lt (x_2,\;y_2)} \mu_1(x_1,\;u)\mu_2(y_1,\;v) & (\text{根据归纳假设}) \\
& = - \sum_{x_1 \le_1 u \lt_1 x_2} \sum_{y_1 \le_2 v \lt_2 y_2} \mu_1(x_1,\;u)\mu_2(y_1,\;v) & (\text{分别枚举}) \\
& =  - \sum_{x_1 \le_1 u \le_1 x_2} \sum_{y_1 \le_2 v \le_2 y_2} \mu_1(x_1,\;u)\mu_2(y_1,\;v) \\
&\;\;\;\, + \mu_1(x_1,\;x_2)\sum_{y_1 \le_2 v \le_2 y_2} \mu_2(y_1,\;v) \\
&\;\;\;\, + \mu_2(y_1,\;y_2)\sum_{x_1 \le_1 u \le_1 x_2} \mu_1(x_1,\;u) \\
&\;\;\;\, + \mu_1(x_1,\;x_2)\mu_2(y_1,\;y_2) & (\text{扩展上界})
\end{align}
$$

由于：
$$
\begin{align}
0
& = \sum_{y_1 \le_2 v \le_2 y_2} \mu_2(y_1,\;v) \\
& = \sum_{x_1 \le_1 u \le_1 x_2} \mu_1(x_1,\;u)  \\ 
& = \sum_{x_1 \le_1 u \le_1 x_2} \sum_{y_1 \le_2 v \le_2 y_2} \mu_1(x_1,\;u)\mu_2(y_1,\;v) 
\end{align}
$$

所以定理成立。

## 在$(X_n,\;\le)$上的莫比乌斯函数
注意这里的是真正的小于等于号了......
这个比较智障，分析一下就好了：
对于$y = x$，我们有：
$$
\mu(x,\;y) = \mu(x,\;x) = 1
$$

对于$y = x + 1$，我们有：
$$
\mu(x,\;y) = \mu(x,\;x + 1) = -\mu(x,\;x) = -1
$$

对于$y = x + 2$，我们有：
$$
\mu(x,\;y) = \mu(x,\;x + 2) = -\left[\mu(x,\;x) + \mu(x,\;x + 1)\right] = 0
$$

不难发现，对于$y \gt x + 1$的函数值就全都变为$0$了。
总结一下就是：
$$
\mu(x,\;y) = 
\begin{cases}
1 & (y = x) \\
-1 & (y = x + 1) \\
0 & (\text{otherwise})
\end{cases}
\tag{5.1}
$$

## 在$(X_n,\;\subseteq)$上的莫比乌斯函数
> 试证明：
> 偏序集$(X_n,\;\subseteq)$的莫比乌斯函数是：
> $$\mu(A,\;B) = (-1)^{|B| - |A|} \tag{6.1}$$

运用归纳法证明：
首先对于$A = B$，显然成立：
$$
\mu(A, B) = \mu(A, A) = 1 = (-1)^0
$$

假设对于$|B| - |A| \le k$均成立，尝试证明对于$|B| - |A| = k + 1$也成立：
$$
\begin{align}
\mu(A,\;B) & = -\sum_{A \subseteq C \subset B} \mu(A,\;C) \\
& = -\sum_{A \subseteq C \subset B} (-1)^{|C| - |A|} \\
& = -\sum_{i = 0}^{k} {k + 1 \choose i}(-1)^i \\
& = -\left[(1 - 1)^{k + 1} - (-1)^{k + 1} \right] \\
& = (-1)^{k + 1} \\
& = (-1)^{|B| - |A|}
\end{align}
$$

## 在$(X_n,\;\mid)$上的莫比乌斯函数
首先我**不会**证这玩意：
$$
a \mid b \Longrightarrow \mu(a,\;b) = \mu(1,\;\frac{b}a) \tag{7.1}
$$

不管了......
反正它是对的......

由于有上面的式子，所以我们只用关心$\mu(1,\;n)$。
首先可以递归计算：
$$
\mu(1,\;n) = -\sum_{a \mid n,\;a\neq n} \mu(1,\;a)
$$

考虑对$n$进行质因数分解：
$$
n = p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_m^{\alpha_m}
$$

对于$n$的任意一个因子$d$都有：
$$
d = p_1^{\beta_1}p_2^{\beta_2}\cdots p_m^{\beta_m} \;\;\;\; (0 \le \beta_i \le \alpha_i)
$$

相当于可以看作$m$个大小为$\alpha_1 + 1,\;\alpha_2 + 1,\;\dots,\;\alpha_m + 1$的偏序集的直积的结果。
于是可以得到：
$$
\mu(1,\;n) = \prod_{i=1}^m\mu(1,\;p_i^{\alpha_i}) \tag{7.2}
$$

注意到，对于$\varphi(p) = p - 1$：
$$
\mu(1,\;1) = 1 \\
\mu(1,\;p) = -\mu(1,\;1) = -1 \;\; \\
\mu(1,\;p^2) = -\left[ \mu(1,\;1) + \mu(1,\;p) \right] = 0 \\
\dots
$$

总结一下就是：
$$
\mu(1,\;p^k) = 
\begin{cases}
1 & (k = 0) \\
-1 & (k = 1) \\ 
0 & (\text{otherwise})
\end{cases}
\tag{7.3}
$$

运用直积，可以知道：
$$
\mu(1,\;n) = 
\begin{cases}
1 & (n = 1) \\
(-1)^k & (n = p_1p_2\cdots p_k, \;\;\varphi(p_i) = p_i - 1) \\
0 & (\text{otherwise})
\end{cases}
\tag{7.4}
$$

为了方便，通常把$\mu(1,\;n)$记作$\mu(n)$，就变成常见的莫比乌斯函数了。

据此，我们可以证明莫比乌斯函数是积性函数，即：
$$
a \bot b \Longrightarrow \mu(ab) = \mu(a)\mu(b) \tag{7.5}
$$

**证明**：
1. 如果$a$、$b$中有一者为$1$，结论显然成立。
2. 如果$a$、$b$中有一者不为素数连乘的形式，它们的积也一定不会是素数连乘的形式，故等于$0$。
3. 此时假设$a$、$b$都是素数连乘的形式，又因为$a$与$b$互质，所以它们的素因子中没有相同的。设$a = p_1p_2\cdots p_m$和$b = q_1q_2\cdots q_n$所以可以知道$\mu(ab) = (-1)^{n + m} = \mu(a)\mu(b)$。

## 反演示例：容斥原理
设$S$为有限集，$A_1,\;A_2,\;\dots,\;A_n$是$S$的子集，$K \subseteq \{1,\;2,\;\dots,\;n\}$。
定义函数$F(K)$计数$s$**同时**满足下列条件：
$$
s \not\in \bigcup_{i \in K} A_i \\
s \in \bigcap_{i \not\in K} A_i
$$

即：
$$
F(K) = \left| \bigcap_{i \not\in K} A_i - \bigcup_{i \in K} A_i \right| \tag{8.1}
$$

如何脑补这个函数？可以想象成是用$K$把$S$中的很多东西挖走了，然后剩下的集合再求交集。
对于此，再定义函数$G(K)$：
$$
G(K) = \sum_{L \subseteq K} F(L) \tag{8.2}
$$

这货居然计数的是：
$$
G(K) = \left| \bigcap_{i \not\in K} A_i \right| \tag{8.3}
$$

如何脑补其正确性？可以想象是一个智障用$K$把本来属于它们交集的东西挖去了，然后又一个一个吐出来，于是就还原了原本的交集......
根据莫比乌斯反演公式可以知道：
$$
G(K) = \sum_{L \subseteq K} F(K) \Longrightarrow F(K) = \sum_{L \subseteq K} (-1)^{|K| - |L|} G(L)
$$

所以取$K = \{1,\;2,\;\dots,\;n\}$可以得到：
$$
F(K) = \sum_{L \subseteq K} (-1)^{n - |L|} G(L) \tag{8.4}
$$

这个时候的$F(K)$计数的东西有了新的含义：
$$
F(K) = \left|\bigcup_{i \in K} A_i\right| = \left|\bigcap_{i \in K} \overline{A}_i \right| \tag{8.5}
$$

用$F(K)$和$G(K)$本身的含义来替换，就可以得到**容斥原理** (感觉好神奇)：
$$
\left|\bigcap_{i = 1}^n \overline{A}_i \right| = \sum_{K \subseteq \{1,\;,2,\;,\dots,\;n\}} (-1)^{|K|} \left| \bigcap_{i \in K} A_i \right| \tag{8.6}
$$

## 反演示例：$\varphi(n)$通项公式
欧拉$\varphi(n)$函数计数的是不大于$n$的与$n$互质的正整数个数。
对于欧拉$\varphi$函数，我们有如下的定理：
$$
n = \sum_{d \mid n} \varphi(d) \tag{9.1}
$$

有两种证明方法：
第一种考虑不与$n$互质的数，如果存在一个数$d$与$n$不互质，那么必有$\gcd(d, n) = a \gt 1$，换言之$\gcd(d / a, n / a) = 1$，所以一个数不与$n$互质，那么必定与$n$的一个因子互质。所以上式成立。

另一种是使用归纳法证明：
首先考虑$1$，是显然成立的。
然后考虑质数$p$，$\varphi(1) + \varphi(p) = p$，所以也是成立的。
考虑质数$p$的幂$p^k$，它的因子有$1,\;p,\;p^2,\;\dots,\;p^k$，由于：
$$
\varphi(p^k) = (p - 1)p^{k-1} \;\;\;\; (\varphi(p) = p - 1)
$$

所以我们对其进行等比数列求和：
$$
\begin{align}
\sum_{d \mid n} \varphi(d) & = 1 + (p - 1)\sum_{i=0}^{k-1} p^i \\
& = 1 + (p - 1) \cdot {1 - p^k \over 1 - p} \\
& = 1 + p^k - 1 \\
& = p^k
\end{align}
$$

故对质数的幂也成立。
假设对于一个数$c$，所有小于$c$的数均成立，那么选取$n$的两个互质的因子$a$、$b$使得$ab = c$，那么有：
$$
\sum_{n \mid a} \varphi(n) \sum_{m \mid b} \varphi(m) = a \cdot b = c
$$

下面证明$\sum_{n \mid a} \varphi(n) \sum_{m \mid b} \varphi(m) = \sum_{d \mid c} \varphi(d)$，即可证明原式：
$$
\begin{align}
\sum_{n \mid a} \varphi(n) \sum_{m \mid b} \varphi(m) & = \sum_{n \mid a}\sum_{m \mid b}\varphi(n)\varphi(m) & (\text{改变枚举顺序}) \\
& = \sum_{n \mid a}\sum_{m \mid b} \varphi(nm) & (\text{由于}n \bot m) \\
& = \sum_{nm \mid ab} \varphi(nm) & (\text{由于}a \bot b) \\
& = \sum_{d \mid c} \varphi(d) & (\text{等价代换}) \\
& = c
\end{align}
$$

注意到$(9.1)$式是一个明显的莫比乌斯反演的形式。根据莫比乌斯反演公式，我们可以得到：
$$
\begin{align}
\varphi(n) & = \sum_{d \mid n} d \cdot \mu(d,\;n) \\
& = \sum_{d \mid n} d \cdot \mu(1,\;n / d) \\
& = \sum_{d \mid n} d \cdot \mu(n / d) \\
& = \sum_{d \mid n} \mu(d) \cdot n/d
\end{align}
$$

考虑一下$\mu$函数的取值，对于因子$1$，和式中的结果为$n$。对于由素数相乘的因子，这些素因子必定来自$n$。而其它情况就都为$0$。
设$n = p_1^{k_1}p_2^{k_2}\cdots p_m^{k_m}$。
因此可以得到下面的式子：
$$
\varphi(n) = n\left[1 - \sum \frac1{p_i} + \sum \frac1{p_ip_j} - \cdots + (-1)^{m}\sum \frac1{\prod_{i=1}^m p_i} \right] \tag{9.2}
$$

这恰好是下面的式子展开的形式：
$$
\varphi(n) = n\prod_{i=1}^m \left( 1 - \frac1{p_i} \right) \tag{9.3}
$$

因此：
$$
\varphi(n) = n\prod_{p \mid n,\;\varphi(p) = p - 1} \left( 1 - \frac1p\right) \tag{9.4}
$$

## 反演示例：多重集合的循环排列
> 我们有一个多重集合$\{\infty \cdot 1,\;\infty \cdot 2,\;\dots,\;\infty \cdot k\}$。易知长度为$n$的全排列数为$k^n$。
> 现在对于两个排列$A$和$B$，如果$A$通过"旋转" (即将最后一个变成第一个，并且把之前的全部后移) 能变成$B$，那么$A$和$B$是等价的。
> 换言之，最小表示法相同的排列是等价。
> 求不同的长度为$n$的**循环排列**数量。

对于这个计数问题，我们记$h(n)$为长度为$n$时的答案，$f(n)$为长度为$n$并且**旋转**$n$次才会变为原排列 (即循环节长度为$n$) 的排列的数量。显然，一个排列的循环节长度$m$必须满足$m \mid n$。
那么可以知道：
$$
h(n) = \sum_{d \mid n} \frac{f(d)}d \tag{10.1}
$$

由于循环节长度小于$n$的排列都可以由循环节不断重复而得来。因此我们设：
$$
g(n) = \sum_{d \mid n} f(d)
$$

$g(n)$就计数了所有长度为$n$的排列数量。
所以：
$$
g(n) = k^n \tag{10.2}
$$

根据莫比乌斯反演公式可得：
$$
\begin{align}
f(n) & = \sum_{d \mid n} g(d)\mu(n/d) \\
& = \sum_{d \mid n} k^d\mu(n/d)
\end{align}
\tag{10.3}
$$

带入$h(n)$的计算公式可得：
$$
h(n) = \sum_{d \mid n} \frac1d \sum_{e \mid d} k^e\mu(d/e) \tag{10.4}
$$

由于$e \mid d$并且$d \mid n$，所以我们设$n = rd,\;d = me$，所以$n = rem$，这样将方便我们变换公式：
$$
\begin{align}
\sum_{d \mid n} \frac1d \sum_{e \mid d} k^e\mu(d/e) & = \sum_{e \mid n} k^e \sum_{m \mid (n/e)} \frac1{me}\mu(m) \\
& =\sum_{e\mid n} \frac{k^e}n \sum_{r \mid (n/e)} r\cdot\mu(\frac{n}e/r)
\end{align}
$$

由于：
$$
\varphi(n) = \sum_{d \mid n} d \cdot \mu(n/d)
$$

所以：
$$
h(n) = \frac1n \sum_{d \mid n} k^d \varphi(n/d) \tag{10.5}
$$

## 莫比乌斯函数示例：最大公约数
除了莫比乌斯反演公式，莫比乌斯函数本身的性质也是很好的。
考虑下面一个问题：

> 给定$n$和$m$，求$\gcd(x,\;y)\;\;(1 \le x \le n,\;1 \le y \le m)$为**素数**的二元组$(x,\;y)$个数。

换言之，我们要求的是这个：
$$
\sum_{x=1}^n\sum_{y=1}^m \left[\varphi(\gcd(x,\;y)) = \gcd(x,\;y) - 1\right] \tag{11.1}
$$

首先，我们可以换个思路，就是枚举最大公约数的答案：
$$
\sum_{\varphi(p) = p - 1}^{\min\{n,\;m\}}\sum_{x=1}^n\sum_{y=1}^m \left[ \gcd(x,\;y) = p \right] \tag{11.2}
$$

由于$\gcd(x,\;y) = p \Longrightarrow \gcd(x/p,\;y/p) = 1$，所以就变成了枚举互质的数的对数：
$$
\sum_{\varphi(p) = p - 1}^{\min\{n,\;m\}}\sum_{x=1}^{\left\lfloor \frac{n}p\right\rfloor}\sum_{y=1}^{\left\lfloor \frac{m}p \right\rfloor} \left[ \gcd(x,\;y) = 1 \right] \tag{11.3}
$$

由于莫比乌斯函数有这样的性质：
$$
\sum_{d \mid n} \mu(d) = [n = 1] \tag{11.4}
$$

所以可以使用莫比乌斯函数来测试一个数是否为$1$：
$$
\sum_{\varphi(p) = p - 1}^{\min\{n,\;m\}}\sum_{x=1}^{\left\lfloor \frac{n}p\right\rfloor}\sum_{y=1}^{\left\lfloor \frac{m}p \right\rfloor} \sum_{d \mid \gcd(x,\;y)} \mu(d) \tag{11.5}
$$

因为$d \mid \gcd(x,\;y)$当且仅当$d \mid x$并且$d \mid y$，所以可以变成这样：
$$
\sum_{\varphi(p) = p - 1}^{\min\{n,\;m\}}\sum_{x=1}^{\left\lfloor \frac{n}p\right\rfloor}\sum_{y=1}^{\left\lfloor \frac{m}p \right\rfloor} \sum_{d \mid x \,\land\, d \mid y} \mu(d) \tag{11.6}
$$

现在东西越来越多了，是时候考虑简化一下了。
首先对于一堆和式的一个技巧就是**调整枚举顺序**。
尝试先枚举$d$，这样合法的$d$就可以直接计算了：
$$
\sum_{\varphi(p) = p - 1}^{\min\{n,\;m\}} \sum_{d=1}^{\min\{n,\;m\}} \left\lfloor \frac{n}{dp} \right\rfloor \left\lfloor \frac{m}{dp} \right\rfloor \mu(d) \tag{11.7}
$$

其实这个式子已经可以用来计算答案了。因为两个向下取整的乘积最多有$O(\sqrt{n} + \sqrt{m})$个不同的取值，左边枚举的素数约为$O({n \over \ln n})$个，故根据此公式计算的时间复杂度为$O({n (\sqrt{n} + \sqrt{m}) \over \ln n})$。
然而我们可以做得更快一些。
设$T = dp$，现在改成先枚举$T$：
$$
\sum_{T = 1}^{\min\{n,\;m\}} \left\lfloor \frac{n}T \right\rfloor \left\lfloor \frac{m}T \right\rfloor \sum_{p \mid T,\;\varphi(p) = p - 1} \mu(T / p) \tag{11.8}
$$

这样左边就可以在$O(\sqrt{n} + \sqrt{m})$的时间内进行枚举。
枚举大概是这样的一个过程：

```
lastpos = 0
i = 1
while i <= min(n, m):
    lastpos = min(n / (n / i), m / (m / i))
    # Do something...
    i = lastpos + 1
```

我们企图能使右边快速计算。因此我们来研究一下右边这个玩意。
设：
$$
g(x) = \sum_{p \mid x,\;\varphi(p) = p - 1} \mu(p) \tag{11.9}
$$

考虑使用线性筛来计算$g(x)$。

1. 当$x = 1$时，$g(x) = 0$。
2. 当$x$为素数时，$g(x) = -1$。
3. 在线性筛的处理过程中，设当前数为$i$，枚举到的素数为$p$，我们将要计算$g(ip)$：
    1. 当$\mu(i) = 0$时，说明$i$的质因数分解中至少存在一个一个素因子的次数大于$1$。
       在这种情况下，除非**只有一个**素因子的次数为$2$，其它均为$1$，否则无论如何$g$的函数值都为$0$。
       假设只存在一个素因子的次数为$2$，记这个素因子为$f(i)$。
        1. 若$p \mid i$，那么将会导致无论是哪个素因子，$\mu$函数的值都为$0$。因此$g$函数的值为$0$。
        2. 若$p \not\mid i$，那么就只有除以$f(i)$时会有值，此时的值为$\mu(i / f(i) \cdot p)$。
    2. 当$\mu(i) \neq 0$时，意味着$i$将是多个素数之积。同样我们来考虑两种情况：
        1. 若$p \mid i$，那么就只有$p$的次数为$2$，此时$g(ip) = \mu(i)$。
        2. 若$p \not\mid i$，那么$\mu(ip)$依然不为$0$。假设$i$有$r$个素因子，那么$g(i) = r(-1)^{r-1}$，并且$g(ip) = (r + 1)(-1)^r = -r(-1)^{r-1} + (-1)^{r+1}$，这意味着它们符号相反且绝对值差$1$。这样就可以直接计算。

经过一番分类讨论，我们总算成功地找到了预处理$g(x)$的方法。
在这中间有一个问题还亟待解决，就是我们需要计算$f(x)$，事实上它也可以用线性筛计算。
假设存在这样的素因子$p$，就记$f(x) = p$。如果$x$还是多个素数相乘，就记$f(x) = 1$。否则记作$0$，又称为"没救了"。这样就只有$f(x) \gt 1$时才有我们需要的结果。

1. 当$x = 1$或$x$为质数时，$f(x) = 1$。
2. 每次往一个数$i$加入一个素数$p$时，需要考虑下面的情况：
    1. 若$f(i) = 0$，那么没救了。
    2. 若$p \mid i$，并且$f(i) = 1$，那么$ip$将不再是素数连乘的形式，此时可以记下$f(ip) = p$。如果$f(i) > 1$，那么它没救了。
    3. 若$p \not\mid i$，那么$f$函数值不会改变。

这样就可以欢快地计算$f$函数啦~
回到之前的问题，我们能够计算$g(x)$函数后，预处理出它的前缀和，就可以在前面伪代码中展示的迭代过程计算答案了。时间复杂度是$O(\sqrt{n} + \sqrt{m})$。
