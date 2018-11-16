### 2018.11.16

#### 问题描述

已知实数域上的 Thomae Function $f(x)$ 为：
$$
f(x) = \begin{cases}
1/p & x \in \mathbf Q,\ x = q/p,\ p \in \mathbf N^+,\ q \in \mathbf Z \\
0 & x \in \mathbf R \backslash \mathbf Q
\end{cases}
$$
证明：$f(x)$ 处处不可微。

#### 解决方案

对于一元函数，可导和可微是等价的。由于这个函数在有理点不连续[^discontinuous-at-rationals]，故只需要考虑对于**无理数** $a$，下面这个极限：
$$
\lim_{x\rightarrow a} {f(x) - f(a) \over x - a} \xlongequal{a \text{ irrational}} \lim_{x \rightarrow a} {f(x) \over x - a}
$$
是否存在。不失一般性，假定 $a \geqslant 0$，小于 $0$ 的情况的讨论是类似的。稍作尝试估计都会觉得不存在。首先，对于趋近于 $a$ 的无理数列 $\{x_n\}$，显然：
$$
\lim {f(x_n) \over x_n - a} = 0
$$
为了证明极限不存在，我们需要再构造一个趋近于 $a$ 的实数列 $\{y_n\}$，使得类似的极限**不为** $0$。考虑构造一个有理数列？首先，所谓趋近于 $a$ 就是对任意小的 $\varepsilon > 0$，从某一项开始都有 $|y_n - a| < \varepsilon$。设 $y_n = q/p > a $，那么上面这个极限就可以写成：
$$
\lim {1/p \over q/p - a}
$$
如果 $0 < q/p - a \leqslant 1/p$，那么若其有极限，则极限至少不小于 $1$，我们的目的就达成了。而我们总能找到这样的 $p$，满足 $1/p < \varepsilon$。同时，$q$ 只需要满足 $ap < q \leqslant ap + 1$。这样令 $q = \lceil ap \rceil$ 就 OK 了。于是我们就构造出了这样的有理数列。所以 $f(x)$ 处处不可导，同时也处处不可微。

[^discontinuous-at-rationals]: 证明可以查看 Wikipedia：<https://en.wikipedia.org/wiki/Thomae%27s_function#Properties> "$f$ is discontinuous at all rational numbers, dense within the real numbers"。虽然这个命题 Wikipedia 上也证明了，但是这里稍微初等一些。