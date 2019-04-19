### 2019.4.19
#### 问题描述

证明：对于正整数 $n$ 和 $m$，

(1) 若 $n^k \equiv 1 \pmod m$，则 $n \perp m$。

(2) 若 $n^ p \equiv n^q \equiv 1 \pmod m$，则 $n^{\gcd(p,\ q)} \equiv 1 \pmod m$。

(3) 若 $n^{m - 1} \equiv 1 \pmod m$ 以及对于所有 $m - 1$ 的质因子 $p$ 满足 $n^{(m - 1)/p} \not\equiv 1 \pmod m$，则 $m$ 为质数。

#### 解决方案

(1) 非常简单，使用 Euclid 算法即可：
$$
\gcd(n^k,\ m) = \gcd(1,\ m) = 1
$$
而 $\gcd(n,\ m) \mid \gcd(n^k,\ m)$，所以 $\gcd(n,\ m) = 1$，即 $n$ 与 $m$ 互质。

(2) 类似的，可以利用所谓更相减损术。假设 $p > q$，则
$$
n^p \equiv n^q \ ⇒ \ n^q(n^{p - q} - 1) \equiv 0 \ ⇒ \ n^{p - q} \equiv 1 \pmod m
$$
此时保持条件 $n^{p - q} \equiv n^q \equiv 1 \pmod m$，因此一直进行下去直到有 $n^{\gcd(p,\ q)} \equiv 1 \pmod m$ 即可。

(3) 前面两个实际上是帮助解决 (3) 的简单结论。首先我们就可以通过第一个条件得知 $n \perp m$，包括 $n$ 的任意幂次都与 $m$ 互质。可这和 $m$ 为质数有什么关系？试想如果 $n^k$ 可以遍历 $1$ 到 $m - 1$ 每一个数，那就可以得到这些数都与 $m$ 互质，从而推出 $m$ 为质数。考虑到幂次在模 $m$ 意义下有循环节，因此我们只考虑 $n^1$ 到 $n^{m - 1}$，因此我们需要这些幂次两两之间互不相同。

假设存在 $1 \leqslant j < k < m$ 有 $n^j \equiv n^k \pmod m$，那么就有 $n^j(1 - n^{k - j}) \equiv 1 \pmod m$，也即 $n^{k - j} \equiv 1 \pmod m$，而这里 $1 \leqslant k - j \leqslant m - 2$。换句话说，对于 $1$ 到 $m - 2$ 中的幂次 $k$，不能有 $n^k$ 与 $1$，也就是 $n^{m - 1}$，同余。考虑反证法，如果存在这样的 $k$，那么就有 $n^k \equiv n^{m - 1} \equiv 1 \pmod m$，此时根据 (2) 中的结论，设 $d = \gcd(k,\ m - 1)$，那么 $n^d \equiv 1 \pmod m$。这一步的巧妙之处在于利用 $d$ 这个 $m - 1$ 的因子与第二个条件相沟通。因为 $k < m - 1$，于是 $d$ 至少与 $m - 1$ 相差了某个素因子 $p$，于是推出 $n^{(m - 1)/p}$ 是 $n^d$ 的整幂次，从而同余 $1$，与题设条件相违背，从而完成证明。