---
title: 砍木棍问题
create: 2018.3.2
modified: 2018.3.2
tags: 概率论
---

[TOC]

# 砍木棍问题

## 问题描述

初始时有一根长为 $a$ 的木棍，每次会随机砍掉木棍的一段，问期望多少次后木棍的长度小于 $b$ ？

还有一种离散的版本：初始时有一个数字 $n$，每次可以随机减去一个 $[0, n]$ 内的整数，问期望多少次后变为 $0$ ？

## 离散版本

首先考虑一下我们可以手算的问题，记 $F(n)$ 表示初始时为 $n$ 的期望次数，不难得到下面的递推式：
$$
\begin{cases}
F(0) = 0 \\
F(n) = {n + 1 \over n} + \frac1n\sum_{k = 0}^{n - 1} F(k) & (n > 0)
\end{cases}
$$
上面的 $(n + 1) / n$ 是停留在 $n$ 的期望次数，也就是 $\sum_{k = 0}^\infty (1/(n + 1))^k$，因为每次都有 $1/(n + 1)$ 的概率不减小。通过差分不难解得：
$$
F(n) = 1 + H_n = 1 + \ln n + \mathrm{O}(1)
$$
其中 $H_n$ 表示调和级数。

## 原始问题

从离散版本中我们可以估计出答案应该是对数级别的。为了解决这个问题，首先将模型转化一下：每次砍掉随机的长度，可以视为随机一个 $X \in (0, 1)$，将原长度 $a$ 变为 $Xa$，问期望多少次后小于 $b$。假设是 $k$ 次后满足要求，那么可以得到 $k$ 个独立随机变量 $X_1, X_2, ..., X_k$ 与 $a$ 和 $b$ 的关系：
$$
a \prod_{j = 1}^k X_j < b
$$
也就是：
$$
\prod_{j = 1}^k X_j < \frac{b}a
$$
为了方便，令 $n = a / b$，那么上式右边变为 $< 1/n$。现在来考虑左边那个乘积，处理乘积的一个好方法就是取对数，即：
$$
\ln \prod_{j=1}^k X_j = \sum_{j=1}^k \ln Xj < -\ln n
$$
不等式两边同时算期望：
$$
\mathbf{E}\left[\sum_{j=1}^k \ln X_j\right] = \sum_{j = 1}^k \mathbf{E}[\ln X_j] < - \ln n
$$
而 $E[X_j] = \lim_{y \rightarrow 0}\int_y^1 \ln x \ \mathrm{d}x = \int_{-\infty}^0 e^x \ \mathrm{d}x = -1$，所以可知期望 $\ln n$ 次后满足不等式。因此原问题的答案就是 $\ln a/b$。

## 相关的概率问题

现在来考虑一个扩展的问题：$n$ 个独立随机变量 $X_1, X_2, ..., X_n \in [0, 1]$ 的乘积 $X = \prod_{k = 1}^n X_k$ 小于一个常数 $a \in (0, 1]$ 的概率？

首先考虑一些特殊的情况：

1.  $n = 1$ 时，显然概率就是 $a$。
2.  $n = 2$ 时，设这两个随机变量分别为 $x$ 和 $y$，那么可以看做在以原点为左下角，坐标 $(1, 1)$ 为右上角的正方形中随机投点，问这个点处于 $xy = a$ 的图像（即反比例函数）的左下方的概率。由于这个正方形的面积为 $1$，所以概率就是围出的面积，关于 $x$ 积分，即 $a + \int_a^1 a / x \ \mathrm{d}x = a - a\ln a$。

当 $n \geqslant 3$ 时没有那么好想了，但是我们可以考虑一下递推：设 $P(n, a)$ 表示这个概率（可以是关于 $a$ 的函数），仿照 $n = 2$ 的情况，我们要求的是函数 $X = a$ 在超立方体内围出的超体积。设这 $n$ 个变量中的任意一个为 $z$，考虑下面两种情况：

1.  若 $z < a$，那么 $X$ 一定小于 $a$，这种情况发生的概率为 $a$。
2.  若 $z \geqslant a$，那么 $X < a \Leftrightarrow X/z < a/z$，注意这里 $a \leqslant a/z \leqslant 1$，并且 $X/z$ 是 $n - 1$ 个独立随机变量的乘积。依此，我们可以将问题规模缩减。通过关于 $z$ 求积分，我们可以求出这种情况的概率为 $\int_a^1 P(n - 1, a/z) \ \mathrm{d}z$。

综上所述，我们可以归纳出 $P(n, a)$ 的递推式（假设 $0$ 个元素的乘积为 $1$）：
$$
\begin{cases}
P(0, a) = 0 \\
P(n, a) = a + \int_a^1 P(n - 1, a / z) \ \mathrm{d} z & (n > 0)
\end{cases}
$$
看上去并不好直接得出 $P(n, a)$ 的表达式，所以我尝试用 Mathematica 算了一下 $n \leqslant 6$ 的情况[^subscript]：

```mathematica
In[1]:= P[0, a_] := 0
		P[n_, a_] := a + Integrate[P[n - 1, a/Subscript[z, n]], {Subscript[z, n], a, 1}, Assumptions -> 0 < a < 1]
		Table[Expand[P[i, a]], {i, 6}]
Out[1]:= {a,
		  a - a Log[a],
		  a - a Log[a] + 1/2 a Log[a]^2,
		  a - a Log[a] + 1/2 a Log[a]^2 - 1/6 a Log[a]^3,
		  a - a Log[a] + 1/2 a Log[a]^2 - 1/6 a Log[a]^3 + 1/24 a Log[a]^4,
 		  a - a Log[a] + 1/2 a Log[a]^2 - 1/6 a Log[a]^3 + 1/24 a Log[a]^4 - 1/120 a Log[a]^5}
```

[^subscript]: 代码里面的定积分的积分变量用的是 `Subscript[z, n]`，主要原因是 Mathematica 是直接展开函数来计算的，如果使用 `z` 计算，积分变量会不对，因而出来的结果也会不对。

Wow! $P(n, a)$ 看上去可以表示成 $a \cdot Q(\ln a)$ 的形式，并且 $Q(x)$ 是个多项式。进一步的，我们把这个多项式的系数写出来：
$$
+1, -1, +\frac12, -\frac16,+\frac1{24},-\frac1{120},...
$$
如果对阶乘比较熟悉，不难发现 $Q(x)$ 中 $x^k$ 的系数就是 $(-1)^k / k!$。于是我们可以猜想：

$$
P(n, a) = a\sum_{k = 0}^{n - 1} \frac{(-1)^k}{k!} \ln^k a \:\:\:\: (n > 0) \tag{1}
$$
为了确认这个结论，数学归纳法应该是个比较好的选择：上面已经验证了 $1 \leqslant n \leqslant 6$ 的情况。现在假设对于任意的 $1 \leqslant k \leqslant n - 1$，$P(k, a)$ 均满足 $(1)$ 式，现在证明 $P(n, a)$ 也满足 $(1)$ 式。首先利用 $P(n, a)$ 的递推式：
$$
\begin{aligned}
P(n, a) & = a + \int_a^1 P(n - 1, a / x) \ \mathrm{d}x \\
& = a + \int_a^1 \frac{a}x\sum_{k = 0}^{n - 2} {(-1)^k \over k!} \ln^k \frac{a}x \ \mathrm{d} x \\
& = {a + \sum_{k = 0}^{n - 2} {(-1)^k \over k!} \int_a^1 \frac{a}x\ln^k \frac{a}x \ \mathrm{d}x \:\:\:\:\:\:\:\: (2)}
\end{aligned}
$$
单独考虑积分：
$$
\int \frac{a}x \ln^k \frac{a}x \ \mathrm{d} x
$$
进行换元：令 $u = \ln(a/x)$，那么可知 $\mathrm{d}u = \mathrm{d}\ln(a/x) = {\mathrm{d}(a/x) \over a/x} = -{\mathrm{d}x \over x}$，即 $-x\mathrm{d} u = \mathrm{d}x$，所以上述积分为：
$$
\begin{aligned}
\int \frac{a}x \ln^k \frac{a}x \ \mathrm{d} x & = a\int\frac1x u^k (-x \mathrm{d}u) \\
& = -a \int u^k \ \mathrm{d}u \\
& = -{au^{k + 1} \over k + 1} + C \\
& = -{a\ln^{k  + 1} (a/x) \over k + 1} + C
\end{aligned}
$$
将结果代回到 $(2)$ 中，得到：
$$
\begin{aligned}
P(n, a) & = a + \sum_{k = 0}^{n - 2} {(-1)^k \over k!} \left(- {a \ln^{k + 1} a \over k + 1}\right) \\
& = a + a\sum_{k = 0}^{n - 2} {(-1)^{k + 1} \over (k + 1)!} \ln^{k  + 1}a \\
& = a\sum_{k = 0}^{n - 1} {(-1)^k \over k!} \ln^k a
\end{aligned}
$$
所以归纳假设成立。<span style="float: right">$\blacksquare$</span>

非常有趣的事情是，这个多项式 $Q(x)$ 实际上就是 $\mathrm{e}^{-x}$ 的前 $n$ 项泰勒展开。这里我们回忆一下：
$$
\begin{aligned}
\mathrm{e}^x & = \sum_{k = 0}^\infty {x^k \over k!} \\
\mathrm{e}^{-x} & = \sum_{k = 0}^\infty {(-1)^k x^k \over k!}
\end{aligned}
$$
又一次与自然常数美妙的邂逅，也难怪它值得配上一个专用符号在各种场合大显身手。