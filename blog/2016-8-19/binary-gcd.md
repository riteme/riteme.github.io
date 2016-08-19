---
title: 二进制GCD
create: 2016.8.19
modified: 2016.8.19
tags: 数学
      GCD
---

[TOC]
# 二进制GCD
在算导上发现了一个有趣的算法，有氧环境下可以拿来卡卡常.....

## 算法原理
下面将考虑计算$\gcd(a,\;b)$，假定$a \ge b$：

1. 如果$a$、$b$都是**偶数**，那么易知：
$$
\gcd(a,\;b) = 2\gcd(a / 2,\;b / 2)
$$
2. 如果$a$是**偶数**，$b$是**奇数**，那么有：
$$
\gcd(a,\;b) = \gcd(a / 2, b)
$$
3. 如果$a$是**奇数**，$b$是**偶数**，那么有：
$$
\gcd(a,\;b) = \gcd(a,\;b / 2)
$$
4. 如果$a$、$b$都是**奇数**，那么有：
$$
\gcd(a,\;b) = \gcd((a - b) / 2, b)
$$

这些结论都是比较容易证明的，这里就略去了。
由于**减法的速度比取模快** (减法速度基本与加法一致)，同时除以$2$和乘以$2$可以使用**位运算**来代替，并且每次折半可以保证复杂度，所以理论上这个算法是非常快的。
但是需要注意，欧几里德算法是上界$O(\log(\min\{a,\;b\}))$，而此算法类似于快速幂，是**上下界**$\Theta(\log(\min\{a,\;b\}))$。
但这并不影响它的效率。在我的机子上 (使用Clang 3.6.0) 实测，在编译器打开`-O2`优化下比欧几里德算法快。
但是在没有开`-O2`优化时，因为**常数问题速度变慢**许多。

## 算法实现
下面展示一个基本实现：

```
function BINARY-GCD(a, b):
    if a < b:  # 要保证 a >= b
        SWAP(a, b)
    if b == 0:
        return a
    if a & 1:
        if b & 1:
            return BINARY-GCD((a - b) >> 1, b)
        else:
            return BINARY-GCD(a, b >> 1)
    else:
        if b & 1:
            return BINARY-GCD(a >> 1, b)
        else:
            return BINARY-GCD(a >> 1, b >> 1) << 1
```

注意到欧几里德算法里面是**尾递归**，编译器可以依此做优化。
而上面给出的代码里面并不是这种形式。
但是我们可以稍微修改一下，就可以将其改为尾递归形式：

```
function TAIL-BINARY-GCD(a, b, shift = 0):  # 记录一个shift表示答案乘了几个2
    if a < b:
        SWAP(a, b)
    if b == 0:
        return a << shift  # 将shift的记录的2算入答案
    if a & 1:
        if b & 1:
            return TAIL-BINARY-GCD((a - b) >> 1, b, shift)
        else:
            return TAIL-BINARY-GCD(a, b >> 1, shift)
    else:
        if b & 1:
            return TAIL-BINARY-GCD(a >> 1, b, shift)
        else:
            return TAIL-BINARY-GCD(a >> 1, b >> 1, shift + 1)  # 计数器加1
```

在编译器优化的帮助下，这份代码跑得更快。

此外，二进制GCD另一个巨大的优势就是在需要**高精度**的场合下，不但降低时间复杂度也减低了编程难度 (毕竟**不需要高精度取模**)，所以在这种情况下是一个非常好的算法。
