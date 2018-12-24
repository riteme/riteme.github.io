---
title: 指数与原根笔记
create: 2017.3.8
modified: 2017.3.8
tags: 数论
      原根
---

[TOC]
# 指数与原根笔记
这里大部分定理的证明方法摘自《初等数论》第三版。

## 指数
令$\delta_m(a)$为满足下面等式的最小**正整数$d$**，称为模$m$下$a$的**指数**：
$$
a^d \equiv 1 \pmod{m}
$$

容易知道，如果$a$与$m$不互质，那么这样的正整数$d$不存在。因此下面均认为$a \bot m$。

> **定理1** 设$d_0 = \delta_m(a)$，对于任意满足
> $$ a^d \equiv 1 \pmod{m} $$
> 
> 的$d$，均满足$d_0 \mid d$。

**证明** 如果存在$d$满足该等式但$d_o \nmid d$，我们可以知道：
$$
a^{d - d_0} \equiv 1 \pmod{m}
$$

对于$d - d_0$，如果$d - d_0 < d_0$，那么违背了$d_0$的定义，假设不成立。如果$d - d_0 \geqslant d_0$，那么可以将$d$换为$d - d_0$继续以上过程，同样得到假设不成立。
另一方面，如果$d_0 \mid d$，那么最后得到$a^0 \equiv 1 \pmod{m}$，此时依然满足$d_0$的定义，所以$d_0 \mid d$。

根据欧拉定理我们知道：
$$
a^{\varphi(m)} \equiv 1 \pmod{m} \;\;\;\; \forall\; a\bot m
$$

因此可以推出：
$$
\delta_m(a) \mid \varphi(m) \tag{1.1}
$$

考虑一个数$a$和它的逆元$a^{-1}$，由于：
$$
a^d \equiv 1 \Longleftrightarrow (a^{-1})^d \equiv 1 \pmod{m}
$$

所以我们可以得到：
$$
\delta_m(a) = \delta_m(a^{-1}) \tag{1.2}
$$

下面的定理可以帮助我们快速计算一个数的幂的指数：
> **定理2** 设$k$是非负整数，则有：
> $$ \delta_m(a^k) = {\delta_m(a) \over \gcd(\delta_m(a), k)} \tag{1.3} $$

**证明** 令$\delta = \delta_m(a)$，$\delta_1 = \delta_m(a^k)$，$\delta_2 = \delta / \gcd(\delta, k)$，那么根据指数的定义，可以得到：
$$
a^{k\delta_1} \equiv 1 \pmod{m}
$$

以及
$$
a^{k\delta_2} \equiv 1 \pmod{m}
$$

根据定理1，我们可以得到：
$$
\delta \mid k\delta_1, \; \delta_1 \mid \delta_2
$$

所以可以推出：
$$
\delta_2 = { \delta \over \gcd(\delta, k) } \;\left|\; { k\delta_1 \over \gcd(\delta, k) } \right.
$$

又因为$\delta_2 \bot k / \gcd(\delta, k)$，所以$\delta_2 \mid \delta_1$。综上可以得到定理。

> **定理3**
> $$ \delta_m(ab) = \delta_m(a)\delta_m(b) \Longleftrightarrow \delta_m(a) \bot \delta_m(b) \tag{1.4} $$

**证明** 设$\delta = \delta_m(ab)$，$\delta_1 = \delta_m(a)$以及$\delta_2 = \delta_m(b)$。
**(充分性)** $\delta_m(a) \bot \delta_m(b) \Longrightarrow \delta_m(ab) = \delta_m(a)\delta_m(b)$
因为：
$$
\begin{aligned}
(ab)^\delta & \equiv 1 \equiv (ab)^{\delta_1\delta} \\
& \equiv b^{\delta_1\delta} \pmod{m}
\end{aligned}
$$

所以可以知道$\delta_2 \mid \delta_1\delta$。又因为$\delta_1 \bot \delta_2$，所以$\delta_2 \mid \delta$。同理可得$\delta_1 \mid \delta$。
因为$\delta_1 \bot \delta_2$，所以得到$\delta_1\delta_2 \mid \delta$。

另一方面，由于：
$$
(ab)^{\delta_1\delta_2} \equiv 1 \pmod{m}
$$

所以$\delta \mid \delta_1\delta_2$。综上可以得到$\delta = \delta_1\delta_2$。

**(必要性)** $\delta_m(ab) = \delta_m(a)\delta_m(b) \Longrightarrow \delta_m(a) \bot \delta_m(b)$
利用$\mathrm{lcm}(\delta_1, \delta_2)$作为中介。因为：
$$
(ab)^{\mathrm{lcm}(\delta_1, \delta_2)} \equiv 1 \pmod{m}
$$

所以可以得到$\delta = \delta_1\delta_2 \mid \mathrm{lcm}(\delta_1, \delta_2)$。又因为$\mathrm{lcm}(\delta_1, \delta_2) \mid \delta_1\delta_2$，所以可以得到两者相等。由此可以得知$\delta_1 \bot \delta_2$。

> **定理4** 如果$n \mid m$，那么$\delta_n(a) \mid \delta_m(a)$。

**证明** 令$\delta_1 = \delta_n(a)$以及$\delta_2 = \delta_m(a)$。
由于：
$$
\begin{aligned}
a^{\delta_2} & \equiv 1 & \pmod{m} \\
& \equiv 1 \equiv a^{\delta_1} & \pmod{n}
\end{aligned}
$$

所以可以推出$\delta_1  \mid \delta_2$。

> **定理5** 如果$m_1 \bot m_2$，那么$\delta_{m_1m_2}(a) = \mathrm{lcm}(\delta_{m_1}(a), \delta_{m_2}(a))$。

**证明** 令$\delta = \delta_{m_1m_2}(a)$，$\delta_1 = \delta_{m_1}(a)$以及$\delta_2 = \delta_{m_2}(a)$，
那么根据定理4，我们可以知道$\delta_1 \mid \delta$和$\delta_2 \mid \delta$。因此$\mathrm{lcm}(\delta_1, \delta_2) \mid \delta$。
由于：
$$
\begin{aligned}
a^{\mathrm{lcm}(\delta_1, \delta_2)} \equiv 1 \pmod{m_1} \\
a^{\mathrm{lcm}(\delta_1, \delta_2)} \equiv 1 \pmod{m_2}
\end{aligned}
$$

同时成立，并且$m_1 \bot m_2$，所以可以得到$a^{\mathrm{lcm}(\delta_1, \delta_2)} \equiv 1 \pmod{m_1m_2}$，所以$\delta \mid \mathrm{lcm}(\delta_1, \delta_2)$。所以可以推出$\delta = \mathrm{lcm}(\delta_1, \delta_2)$。

> **推论** 如果$m_1, m_2, \dots, m_k$两两互质，那么：
> $$ \delta_{\prod_{i=1}^k m_i}(a) = \mathrm{lcm}(\delta_{m_1}(a), \delta_{m_2}(a), \dots, \delta_{m_k}(a)) \tag{1.5} $$

## 原根
如果一个数$a$满足$\delta_m(a) = \varphi(m)$，那么$a$是$m$的一个**原根**。
一个数$m$存在原根当且仅当$m = 1, 2, 4, p^a, 2p^a$，其中$p$是奇素数。
当$m$有原根$g$时，所有与$m$互质的数均可以用$g$的某次幂来表示。换句话说，与$m$互质的所有的数是：
$$
g^0, g^1, \dots, g^{\varphi(m) - 1}
$$

对于一个与$m$互质的数$a$，用$\log_{m,g} a$表示模$m$意义下以原根$g$为底$a$的**离散对数**（有些地方也称为**指标**）。满足：
$$
g^{\log_{m,g}a} \equiv a \pmod{m}
$$

求解一个数的离散对数可以使用**大步小步算法** (BSGS)。大致想法就是$a$一定能表示成如下形式[^other-form]：
$$
a \equiv g^{i\sqrt{\varphi(m)} - j} \pmod{m}
$$

[^other-form]: 有另外一种形式$a \equiv g^{i\sqrt{\varphi(m)} + j} \pmod{m}$，但是这种形式最后将会需要逆元，计算过程和可推广性都不如$a \equiv g^{i\sqrt{\varphi(m)} - j} \pmod{m}$优。

相当于我们要求满足下列方程的解：
$$
a g^j \equiv g^{i\sqrt{\varphi(m)}} \pmod{m}
$$

其中$i, j \leqslant \sqrt{\varphi(m)}$，因此可以在$\Theta\left(\sqrt{\varphi(m)}\right)$的时间内求出一个解或者报告不存在解。

为了方便，没有歧义的情况下，离散对数将不会写下标。

> **定理6** 当$a$、$b$和$ab$的离散对数存在时，满足：
> $$ \log_{m,g} ab \equiv \log_{m,g} a + \log_{m,g} b \pmod{\varphi(m)} \tag{2.1}$$

**证明** 根据离散对数的定义：
$$
ab \equiv g^{\log a} \cdot g^{\log b} \equiv g^{\log a + \log b} \equiv g^{\log ab} \pmod{m}
$$

> **定理7** (离散对数换底公式)
> 如果$g$和$\hat g$是$m$的两个原根，那么：
> $$ \log_{\hat g} a \equiv \log_{\hat g} g \cdot \log_{g} a \pmod{\varphi(m)} \tag{2.2} $$

**证明** 根据离散对数的定义：
$$
\begin{aligned}
a & \equiv g^{\log_g a} \equiv (\hat g^{\log_{\hat g} g})^{\log_g a} \\
& \equiv \hat g^{\log_{\hat g} g \cdot \log_g a} \pmod{m}
\end{aligned}
$$

> **定理8** (指数与离散对数的关系)
> $$ \delta_m(a) = { \varphi(m) \over \gcd(\log_{m, g} a, \varphi(m))} \tag{2.3}$$

**证明** 由于$a \equiv g^{log_{m,g} a}$，利用定理2就可得到上式。

> **定理9** (原根的个数)
> 如果$m$存在原根，那么一定有$\varphi(\varphi(m))$个原根。

**证明** 根据原根的定义，原根$g$必须满足$\delta_m(g) = \varphi(m)$。
如果$m$存在一个原根$g$，根据$(2.3)$式，另外与$m$互质的数$a$如果是原根，必须满足$\log_g a \bot \varphi(m)$。由于$0 \leqslant \log_g a \lt \varphi(m)$，所以这样的数共有$\varphi(\varphi(m))$个。

最后来关注一个问题，如果$m$满足了存在原根的条件，如何求出它的原根？
显然，利用定理9，如果我们求出了一个原根，那么其他的原根可以通过枚举所有与$\varphi(m)$互质的数，从而很快地求出来。
但是求出一个原根似乎现在没有好的办法，但是考虑到原根有$\varphi(\varphi(m))$个，一般的最小正原根都比较小。因此一般的方法就是枚举原根并检验其正确性。检验的方法就是利用$(1.1)$式，看这个数是不是只有$\varphi(m)$次幂才是$1$，否则就不是原根。
