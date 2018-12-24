---
title: 计算分拆数的一种方法
create: 2017.10.1
modified: 2017.10.1
tags: 分拆数
      组合数学
      FFT
---

[TOC]

# 计算分拆数的一种方法

## 原始问题

给定 $n$，要求计算 $p(n)$ 和 $q(n)$，其中 $p(n)$ 表示 $n$ 的分拆方案总数，$q(n)$ 表示 $n$ 的不使用重复元素的分拆方案总数。

例如 $p(4) = 5$，因为有以下几种分拆方案：
$$
\begin{aligned}
4 & = 4 \\
4 & = 3 + 1 \\
4 & = 2 + 2 \\
4 & = 2 + 1 + 1 \\
4 & = 1 + 1 + 1 + 1
\end{aligned}
$$
而 $q(4) = 2$，因为在上面只有前两种没有出现重复元素。

为了方便，这里将与数字相关的基本运算的时间复杂度均视为常数时间。

## 基本思路

主要还是利用[双计数的套路](/blog/2017-6-19/double-count.html)，对于 $p(n)$，容易得知：
$$
np(n) = \sum_{k=1}^n k \sum_{t=1}^{\lfloor n / k \rfloor} p(n - kt)
$$
对于 $q(n)$，双计数貌似就没法直接使用了。但是我们可以证明[^origin]：

[^origin]: 这里也有下面两个证明：<https://math.stackexchange.com/q/54976>

>   将 $n$ 拆分为不同的部分的方案数等于将 $n$ 拆分为各部分都是奇数的方案数。

**证明 $1$：** 考虑构造双射。

由于每个数 $n$ 都可以被唯一表示为 $2^k \cdot t$ 的形式，其中 $t$ 是奇数。利用这一点可以沟通上述两种拆分方法。

1.  给定一个每个部分不同的拆分方案，构造一个新的拆分方案：对于每个数 $n = 2^k \cdot t$，在新方案中加入 $2^k$ 个 $t$。易知新方案中的每个部分都是奇数。
2.  从上面给出的新方案还原原来的方案：统计每个奇数 $t$ 的出现次数 $c$，并将其表示为二进制，即 $c = c_0c_1...{c_p}_{(2)}$。对于 $0 \leqslant k \leqslant p$，如果 $c_k = 1$，那么表示原方案中有一个数为 $2^k \cdot t$。

举个例子，如 $6 = 1 + 2 + 3$，按照上述方法转为全部都是奇数的方案就是 $6 = 1 + 1 + 1 + 3$，这里 $1$ 出现了 $3 = 11_{(2)}$ 次，所以知道原方案中有 $2^0 \times 1 = 1$ 和 $2^1 \times 1 = 2$ 这两个数。

**证明 $2$：** 利用生成函数直接证明。据说是欧拉当时给出的证明。

根据几何级数，我们知道：
$$
\begin{aligned}
1 + x^k & = \sum_{k = 0}^\infty x^k - x^{2k}\sum_{k = 0}^\infty x^k \\
& = {1 - x^{2k} \over 1 - x^k} \;\;\;\; (|x| < 1)
\end{aligned}
$$
注意到分子部分总是偶数次幂。因此设 $o(n)$ 表示将 $n$ 分为每个部分均为奇数的方案数，则：
$$
\begin{aligned}
\sum_{k = 0}^\infty q(k)x^k & = \prod_{k = 1}^\infty (1 + x^k) \\
& = \prod_{k = 1}^\infty {1 - x^{2k} \over 1 - x^k} \\
& = {1 - x^2 \over 1 - x}{1 - x^4 \over 1 - x^2}{1 - x^6 \over 1 - x^3}{1 - x^8 \over 1 - x^4}\cdots \\
& = \prod_{k = 0}^\infty {1 \over 1 - x^{2k + 1}} \\
& = \prod_{k = 0}^\infty \left(\sum_{j = 0}^\infty x^{j(2k + 1)} \right) = \sum_{k = 0}^\infty o(k)x^k
\end{aligned}
$$

即 $q(n)$ 的生成函数与 $o(n)$ 是一样的，从而证明它们相等。

现在回到原来的问题，由于只是要求每个部分都是奇数，所以可以再一次运用双计数：
$$
nq(n) = \sum_{k = 1}^n (k \bmod 2) k \sum_{t = 1}^{\lfloor n / k \rfloor} q(n - kt)
$$
现在令 $T = kt$ 换元，我们可以得到：
$$
nq(n) = \sum_{T = 1}^n q(n - T) \sum_{k | T} (k \bmod 2)k
$$
令 $c(n) = \sum_{k | n} (k \bmod 2)k$，即 $n$ 的所有奇数因子之和，并且易知 $c(0) = 0$，所以上面的式子可以简化为：
$$
nq(n) = \sum_{k = 0}^n c(k)q(n - k)
$$
变成了一个卷积的形式。$c(1)$ 到 $c(n)$ 显然可以在$O(n \ln n)$ 的时间内计算出来，此外使用 “分治 + FFT” 就可以在 $O(n \log^2 n)$ 的时间内计算 $q(1)$ 到 $q(n)$ 所有的值。上述推导过程对于 $p(n)$ 来讲是一样的。

## 实现

下面的程序实现了计算 $q(0)$ 到 $q(n)$ 所有的值在模 $998244353$ 意义下的值：

```c++
#include <cstring>

#include <algorithm>
#include <iostream>

using namespace std;

#define NMAX 400000
#define MOD 998244353
#define G 3

typedef long long i64;

inline i64 qpow(i64 a, int b) {
    i64 r = 1;
    for (; b; a = a * a % MOD, b >>= 1)
        if (b & 1) r = r * a % MOD;
    return r;
}

inline i64 inv(i64 x) {
    return qpow(x, MOD - 2);
}

inline void add(i64 &a, i64 b) {
    a += b;
    if (a >= MOD) a -= MOD;
    else if (a < 0) a += MOD;
}

inline int nxtp(int n) {
    int r = 1;
    for (; r < n; r <<= 1);
    return r;
}

void fft(i64 *a, int n, bool in = false) {
    static i64 b[NMAX + 10];
    memcpy(b, a, sizeof(i64) * n);
    for (int i = 0, k = 0, j; i < n; k |= j, i++) {
        a[i] = b[k];
        for (j = n >> 1; k & j; k ^= j, j >>= 1); 
    }

    for (int s = 2; s <= n; s <<= 1) {
        int l = s >> 1;
        i64 wn = qpow(G, in ? MOD - (MOD - 1) / s - 1 : (MOD - 1) / s);
        for (int i = 0; i < n; i += s) {
            i64 w = 1;
            for (int j = i; j < i + l; j++) {
                i64 t = a[j + l];
                a[j + l] = (a[j] - w * t) % MOD;
                a[j] = (a[j] + w * t) % MOD;
                w = w * wn % MOD;
            }
        }
    }

    if (in) {
        i64 d = inv(n);
        for (int i = 0; i < n; i++) {
            a[i] = a[i] * d % MOD;
        }
    }
}

static int n;
static i64 q[NMAX + 10], c[NMAX + 10];

void initialize() {
    ios::sync_with_stdio(false);
    
    cin >> n;
    q[0] = 1;

    for (int i = 1; i <= n; i += 2) {
        for (int j = i; j <= n; j += i) {
            add(c[j], i);
        }
    }
}

static i64 a[NMAX + 10], b[NMAX + 10];

void solve(int l, int r) {
    if (l == r) {
        if (l) q[l] = q[l] * inv(l) % MOD;
        return;
    }

    int m = (l + r) >> 1;
    solve(l, m);

    int alen = m - l + 1, blen = r - l + 1;
    int len = nxtp(blen - 1);

    memset(a, 0, sizeof(i64) * len);
    memset(b, 0, sizeof(i64) * len);
    memcpy(a, q + l, sizeof(i64) * alen);
    memcpy(b, c, sizeof(i64) * blen);

    fft(a, len);
    fft(b, len);
    for (int i = 0; i < len; i++) {
        a[i] = a[i] * b[i] % MOD;
    }
    fft(a, len, true);

    for (int i = alen; i < blen; i++) {
        add(q[m + i - alen + 1], a[i]);
    }

    solve(m + 1, r);
}

int main() {
    initialize();

    solve(0, n);

    for (int i = 0; i <= n; i++) {
        cout << q[i] << " ";
    }
    cout << "\n";

    return 0;
}
```
