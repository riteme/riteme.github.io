---
title: 【NOI2016】“循环之美” 无脑解法
create: 2017.5.18
modified: 2017.5.18
tags: NOI
      数论
      题解
---

[TOC]
# 【NOI2016】“循环之美” 无脑解法
## 题意
给定$n, m, k$，求出所有满足$1 \leqslant x \leqslant n,\; 1 \leqslant y \leqslant m$的正整数中，$x / y$是纯循环小数的个数。**数值相同的只算一次**。

$n,\;m$均不超过$10^9$，$k$不超过$2000$。

## 题解
网上一般的解法都是推一大堆式子，然后经过一些讨论最后得出使用杜教筛的做法。
接下来要给的是一个xjb算法，各位听听就好。

### 初步转化
首先，如果$x / y$是纯循环小数，那么$1 / y$也是纯循环小数。
考虑小数循环节的计算方式，实际上和$k^x \pmod{y}$的循环节是一样的。由于我们知道$k^0 \equiv 1 \pmod{y}$，所以一定存在一个$L > 0$满足$k^L \equiv 1 \pmod{y}$。这样就可得知$k \cdot k^{L - 1} = 1 + cy$。利用扩展欧几里得算法我们可以知道当$k$和$y$不互质时，是不会有解的。
综上，我们要求的就是：
$$
\sum_{i = 1}^n \sum_{j = 1}^m [\gcd(i, j) = 1][\gcd(j, k) = 1]
$$

### 具体分析
看到之后，我发现如果没有后面那个$j$和$k$的互质条件，则是一个简单的莫比乌斯函数前缀和的计算，可以使用杜教筛，这里就不多讲。现在考虑$j$要和$k$互质，看到计数想容斥，我们自然去找不与$k$互质的$j$，那么设$\gcd(j, k) = d$。首先$d > 2$，其次$d$是$j$和$k$的一个公因子，所以我们枚举$d$的倍数即可。同时注意一个$j$可能被多个因子所减去，所以需要使用莫比乌斯函数作为容斥系数。因此**需要减去的部分**为：
$$
\sum_{d \mid k} \mu(d) \sum_{j = 1}^{\lfloor m / d \rfloor} \sum_{i = 1}^n [\gcd(dj, i) = 1]
$$

由于$\gcd(dj, i) = 1$等价于$\gcd(j, i) = 1$并且$\gcd(d, i) = 1$，所以上式变为：
$$
\sum_{d \mid k, d > 1} \mu(d) \sum_{j = 1}^{\lfloor m / d \rfloor} \sum_{i = 1}^n [\gcd(j, i) = 1][\gcd(i, d) = 1]
$$

我们机智的发现后面那两个求和就是原问题的“**数据规模减小版**”......
所以设$f(n, m, k)$表示我们的答案，那么可以得到DP转移式：
$$
f(n, m, k) = \sum_{i = 1}^n\sum_{j = 1}^m [\gcd(i, j) = 1] - \sum_{d \mid k, d > 1} \mu(d) f\left(\left\lfloor \frac{m}d \right\rfloor, n, d\right)
$$

很像杜教筛？我直接拿去用个哈希表来记忆化搜一下，好像最坏的数据也只访问了$30000$左右个状态......这么优美的一道题就这样过了......
复杂度不会算......

### 具体实现
[UOJ Submission #159233](http://uoj.ac/submission/159233)

```c++
// #define NDEBUG

#include <cassert>
#include <cstdio>
#include <cstring>
#include <climits>

#include <vector>
#include <algorithm>

using namespace std;

#define KMAX 2000
#define S 5000000
#define MOD 116099

typedef long long i64;

template <typename TPolicy>
struct HashTable {
    typedef typename TPolicy::TKey TKey;
    typedef typename TPolicy::TVal TVal;
    typedef pair<TKey, TVal> Data;

    vector<Data> bucket[MOD];

    int get_pos(int key) {
        int pos = key % MOD;
        return pos < 0 ? pos + MOD : pos;
    }

    void insert(TKey key, TVal val) {
        bucket[get_pos(TPolicy::hash(key))].push_back(Data(key, val));
    }

    bool query(TKey key, TVal &val) {
        int pos = get_pos(TPolicy::hash(key));

        for (auto e : bucket[pos]) {
            if (e.first == key) {
                val = e.second;
                return true;
            }
        }

        return false;
    }
};

struct PrePolicy {
    typedef int TKey;
    typedef int TVal;

    static int hash(int x) {
        return x;
    }
};

static int c[S + 10];
static int p[S + 10];
static HashTable<PrePolicy> mu;

int pre(int n) {
    if (n <= S)
        return p[n];

    int ret = 1;
    if (mu.query(n, ret))
        return ret;

    for (int i = 2, last = 2; i <= n; i = last + 1) {
        last = n / (n / i);
        ret -= (last - i + 1) * pre(n / i);
    }

    mu.insert(n, ret);
    return ret;
}

struct Key {
    int n, m, k;

    bool operator==(const Key &b) const {
        return n == b.n && m == b.m && k == b.k;
    }
};

struct DpPolicy {
    typedef Key TKey;
    typedef i64 TVal;

    static int hash(const TKey &x) {
        return (x.n ^ x.m) * x.k;
    }
};

static vector<int> d[KMAX + 10];
static HashTable<DpPolicy> mem;

i64 dp(int n, int m, int k) {
    if (n == 0 || m == 0)
        return 0;

    Key key = {n, m, k};
    i64 ret = 0;
    if (mem.query(key, ret))
        return ret;

    for (int i = 1, last = 1; i <= n && i <= m; i = last + 1) {
        last = min(n / (n / i), m / (m / i));
        i64 sum = pre(last) - pre(i - 1); 
        ret += sum * (n / i) * (m / i);
    }

    for (int i : d[k]) {
        ret += c[i] * dp(m / i, n, i);
    }

    mem.insert(key, ret);
    return ret;
}

static int n, m, k;
static bool marked[S + 10];
static int prime[S + 10], cnt;

void initialize() {
    scanf("%d%d%d", &n, &m, &k);

    c[1] = p[1] = 1;
    for (int i = 2; i <= S; i++) {
        if (!marked[i]) {
            c[i] = -1;
            prime[++cnt] = i;
        }

        p[i] = p[i - 1] + c[i];
        for (int j = 1; i * prime[j] <= S; j++) {
            int p = prime[j];
            marked[i * p] = true;

            if (i % p == 0) {
                c[i * p] = 0;
                break;
            } else
                c[i * p] = -c[i];
        }
    }

    for (int i = 2; i <= k; i++) {
        for (int j = 2; j <= i; j++) {
            if (c[j] && i % j == 0)
                d[i].push_back(j);
        }
    }
}

int main() {
    // freopen("cyclic.in", "r", stdin);
    initialize();
    printf("%lld\n", dp(n, m, k));

    return 0;
}
```
