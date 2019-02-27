### 2019.2.27
#### 问题描述
已知正整数 $a$、$b$ 互质且 $a > b$，以及正整数 $m$、$n$。证明：

$$
\gcd(a^n - b^n,\ a^m - b^m) = a^{\gcd(n,\ m)} - b^{\gcd(n,\ m)}
$$

#### 解决方案
涉及到 gcd 的计算时，Euclid 算法是一个好思路。假设 $n \geqslant m$，那么我们需要计算 $(a^n - b^n) \bmod (a^m - b^m)$。尝试关于 $a$ 做一下长除法：

$$
\phantom{0000000} a^{n-m} + a^{n - 2m}b^m + a^{n - 3m}b^{2m} + \cdots \newline
a^m - b^m /\overline{a^n - b^n\phantom{0000000000000000000000000}} \newline
\underline{a^n - a^{n - m}b^m}\phantom{000000000000} \newline
a^{n - m}b^m - b^n\phantom{000} \newline
\phantom{000}\underline{a^{n - m}b^m - a^{n - 2m}b^{2m}} \newline
\phantom{0000000000000000}a^{n - 2m}b^{2m} - b^n \newline
\phantom{0000000000000000000000}\underline{a^{n - 2m}b^{2m} - a^{n - 3m}b^{3m}} \newline
\phantom{0000000000000000000000000000000000000}a^{n - 3m}b^{3m} - b^n \newline
\phantom{000000000000000000000000000}\cdots
$$

算了几项后就不难看出 $a^n - b^n = (a^m - b^m)(a^{n-m}+a^{n-2m}b^m+\cdots+a^rb^{n-m-r}) + a^rb^{n-r}-b^n$，这里 $r = n \bmod m$。所以原式等于 $\gcd(a^rb^{n-r}-b^n,\ a^m - b^m) = \gcd(b^{n-r}(a^r-b^r),\ a^m - b^m)$。可惜的是带着一个 $b^{n-r}$，没能直接达成目标。

不过目前为止我们还没用过 $a$ 与 $b$ 互质这个条件。试想如果 $b^{n-r}$ 与 $a^m - b^m$ 互质，那么就可以直接去掉它。注意到 $b^{n - r}$ 实际上就是 $b^{m\lfloor n/m \rfloor}$，不妨写作 $b^{km}$。考虑 $\gcd(b^{km},\ a^m - b^m)$，对 $b^{km}$ 关于 $b$ 做长除法，可以得到 $b^{km} = (a^m - b^m)\left(-b^{(k - 1)m} - a^mb^{(k - 2)m} - \cdots - a^{(k - 1)m}\right) + a^{km}$，故：

$$
\gcd(b^{km},\ a^m - b^m) = \gcd(a^{km},\ a^m - b^m)
$$

由于上面两式相等，记做 $d$，那么 $d\mid a^{km}$ 并且 $d\mid b^{km}$，这等价于 $d \mid \gcd(a^{km},\ b^{km})$，而 $a$ 与 $b$ 互质，故 $d = 1$，因此在原式中可以去掉 $b^{n - r}$，从而得以递归完成证明。