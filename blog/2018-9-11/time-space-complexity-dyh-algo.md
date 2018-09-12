---
title: 杜教筛的时空复杂度分析
create: 2018.9.11
modified: 2018.9.11
tags: 时空复杂度
      杜教筛
      数论
---

[TOC]
# 杜教筛的时空复杂度分析

## 背景

杜教筛是 OI 界中一种常用的计算积性函数前缀和的技巧：对于积性函数 $f(n)$，设其前缀和为 $F(n) = \sum_{k = 1}^n f(k)$。选定辅助函数 $g(n)$，尝试计算 $f \times g$ 的前缀和：
$$
\begin{aligned}
\sum_{k = 1}^n (f \times g)(k) &= \sum_{k = 1}^n \sum_{d \mid k} f\left({k \over d}\right)g(d) \\
&= \sum_{d = 1}^n g(d) \sum_{k = 1}^{\lfloor n / d \rfloor} f(k) = \sum_{k = 1}^n g(k)F\left(\left\lfloor{n \over k}\right\rfloor\right)
\end{aligned}
$$
将 $g(1)F(n)$ 移出来，得到：
$$
F(n) = \frac1{g(1)}\left(\sum_{k = 1}^n(f \times g)(k) - \sum_{k = 2}^ng(k)F\left(\left\lfloor{n \over k}\right\rfloor\right)\right)
$$

关键在于 $\lfloor n / k \rfloor$ 的不同取值只有 $\Theta(\sqrt n)$ 个。如果我们可以：

1. 快速计算 $\sum_{k = 1}^n (f \times g)(k)$。
2. 快速计算 $\sum_{k = 1}^n g(k)$。

那么利用哈希表，我们就可以以比较低的时空复杂度计算 $F(n)$。

## 具体分析

考虑一个具体的例子：计算欧拉函数 $\varphi(n)$ 的前缀和。因为 $\sum_{d \mid n} \varphi(d) = n$，所以选取 $g(n) = 1$ 作为辅助函数。那么可以得到 $\varphi(n)$ 的前缀和 $\Phi(n) = \sum_{k = 1}^n \varphi(k)$ 为：
$$
\Phi(n) = {n(n + 1) \over 2} - \sum_{k = 2}^n \Phi\left(\left\lfloor {n \over k} \right\rfloor\right)
$$
定义 $R(n) = \{\lfloor n / k \rfloor: 2 \leqslant k \leqslant n,\,k \in \mathbf N\}$，即对于 $x \in R(n)$，$\Phi(x)$ 是需要递归计算的前缀和。

**引理 1**　$\forall n,\,m \in \mathbf N \geqslant 1$，若 $m \leqslant \sqrt n$，则 $\lfloor n / \lfloor n / m \rfloor \rfloor = m$。

**证明**　令 $k = \lfloor n / m \rfloor$，则 $mk \leqslant n < m(k + 1)$，那么 $m \leqslant n / k < m(k + 1) / k$，若要 $\lfloor n / k \rfloor = m$，则需要 $m(k + 1) / k \leqslant m + 1$，因此 $m + m / k \leqslant m + 1$ 即 $m \leqslant \lfloor n / m \rfloor$，这等价于 $m^2 \leqslant n$，即 $m \leqslant \sqrt n$。<span style="float: right">$\blacksquare$</span>

**引理 2**　对于任意**连续单增**函数 $f(x)$，并且满足：
$$
f(x) \in \mathbf Z \Longrightarrow x \in \mathbf Z
$$
则 $\lfloor f(x) \rfloor = \lfloor f(\lfloor x \rfloor) \rfloor$，以及 $\lceil f(x) \rceil$ = $\lceil f(\lceil x \rceil) \rceil$。

这个引理来自 *Concrete Mathematics* [[1]](#ref-1) 的 (3.10)，这里就不再证明。

**引理 3**　令正整数 $a,\,b$ 为常数，则对于正整数 $x$，有 $\lfloor\lfloor x / a \rfloor / b \rfloor = \lfloor x / ab \rfloor$。

**证明**　令 $f(x) = \lfloor x / b \rfloor$，运用引理 2 即可。<span style="float: right">$\blacksquare$</span>

**定理 1**　$\forall n \in \mathbf N \geqslant 1$，记 $s = \lfloor \sqrt n \rfloor$，$A = \{1,\,2,\,3,\,...,\,s\}$，$B = \{\lfloor n / 2 \rfloor,\,...,\,\lfloor n / s \rfloor\}$，则 $R(n) = A \cup B$ 并且 $|R(n)| = 2\sqrt n + \Theta(1)$。

**证明**　对于 $x \in A$，根据引理 1，$\lfloor n / \lfloor n / x \rfloor \rfloor = x$，所以 $x \in R(n)$。

对于 $x \in R(n)$ 并且 $x > s$，$n / x \leqslant s$，意思是在 $R(n)$ 的定义中能够得到 $x$ 的 $k \in [2,\,s]$，所以 $S \ \backslash\ A \subseteq B$。根据 $B$ 的定义，$B \subseteq S$，由此可得出 $S = A \cup B$。

对于 $1 \leqslant x < y \leqslant s$，$n / x - n / y \geqslant n/(y - 1) - n / y > 1$，所以 $\lfloor n / x \rfloor \neq \lfloor n / y \rfloor$，所以 $|R(n)| = 2\sqrt n + \Theta(1)$。<span style="float: right">$\blacksquare$</span>

**定理 2**　对于任意正整数 $n$，$\forall m \in R(n)$，有 $R(m) \subseteq R(n)$。

**证明**　因为 $m \in R(n)$，所以可设 $m = \lfloor n / a \rfloor$。对于 $z \in R(m)$，有 $z = \lfloor m / b \rfloor$，根据引理 3，可知 $z = \lfloor  n / ab \rfloor$。因为 $a,\,b > 1$，且 $a \leqslant n$，$b \leqslant n / a$，所以 $1 < ab \leqslant n$，所以 $z \in R(n)$。<span style="float: right">$\blacksquare$</span>

定理 2 揭示了这个技巧的巧妙所在：只需要对每个 $m \in R(n)$ 和 $m = n$ 计算 $\Phi(m)$ 即可。此外，计算 $\Phi(n)$ 时单独还需要 $\Theta(\sqrt n)$ 的枚举，因此总的枚举次数为：
$$
\begin{aligned}
\sum_{k = 1}^{\lfloor \sqrt n \rfloor} \sqrt k + \sum_{k = 1}^{\lfloor \sqrt n \rfloor} \sqrt{n \over k} = \Theta\left( \int_1^{\sqrt n} \left(\sqrt x + \sqrt{n \over x}\right) \mathrm dx \right) = \Theta(n^{3/4})
\end{aligned}
$$
当然空间复杂度是 $\Theta(\sqrt n)​$。一般都还会采取预处理的方法来继续优化这个算法：利用线性筛算出前 $S > \sqrt n​$ 个前缀和，那么时间复杂度变为：
$$
S + \sum_{k = 1}^{\lfloor n / S\rfloor} \sqrt{n \over k} = \Theta\left( S + \int_1^{n/S} \sqrt{n \over x} \mathrm{d}x \right) = \Theta\left(S + {n \over \sqrt S}\right)
$$
取 $S = n^{2/3}$ 可以得到最优时间复杂度 $\Theta(n^{2/3})$。注意此时空复杂度相同。

## 后记

之所以会写这篇博客，主要是我第二次看杜教筛的资料的时候，终于想通了它的时间复杂度分析，也就上面这一堆东西。但实际上和任之洲的集训队论文 [[2]](#ref-2) 相比，只多出了一个简单的定理 2。没有意识到这一点之前，我一直无法理解为什么那两个和式就可以代表杜教筛的时间复杂度。另外，更重要的一点就是看到了 tangjz 的[《浅谈一类积性函数的前缀和》](https://blog.csdn.net/skywalkert/article/details/50500009)中的分析，个人认为那是在自欺欺人，稍有用心的人就会发现其中描述时间复杂度的 $T(n)$ 忽略了记忆化这个操作。所以我才想写一个详细一点的分析，希望对大家有帮助。

## 参考资料

<span id="ref-1">[1]</span>. Ronald L. Graham, Donald E. Kunth, Oren Patashnik, 2002, *Concrete Mathematics* (2th edition), 978-7-111-10576-3
[2]. 任之洲，2016，《积性函数求和的几种方法》，2016 年信息学奥林匹克中国国家队候选队员论文
