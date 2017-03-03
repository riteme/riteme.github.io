---
title: 无向图最小割
create: 2017.2.12
modified: 2017.2.12
tags: 最小割
      网络流
      图论
      组合优化
---

[TOC]
# 无向图最小割
## 基本定义
对于一张无向带权图$G = (V, E, w)$，将点集$V$分为两个不相交的集合$S$和$T$，满足$S \cup T = V$，那么称$C = (S, T)$是图$G$的一个**割**。**割的权值**定义为两个端点不在同一集合内的边的权值之和，记做$W(C)$：

$$
W(C) = \sum_{u \in S, v \in T, (u, v) \in E} w(u, v)
\tag{1.1}
$$

对于指定的$s$和$t$，如果存在一个割$C = (S, T)$满足$s \in S, t \in T$或者$s \in T, t \in S$，那么称这个割为**$s$-$t$割**。

对于一张图，权值最小的割称为**最小割**。多数情况下，最小割不是唯一的。

例如，在下图中：

![graph-example](https://git.oschina.net/riteme/blogimg/raw/master/mincut/graph-example.svg)

$(\{2\}, \{1,3,4,5,6\})$和$(\{4\}, \{1,2,3,5,6\})$均是最小割，其权值为$3$。而$(\{1,2,3\}, \{4,5,6\})$是一个$1$-$6$最小割，其权值为$51$。

为了方便，我们对于任意的不相交集合$U$、$V$，要求$U \cup V \subseteq V$，定义它们之间的权值为：

$$
W(U, V) = \sum_{u \in U, v \in V, (u, v) \in E} w(u, v)
\tag{1.2}
$$

换言之。权值是横跨$U$和$V$的边的权值之和。

现在来考虑一个比较浅显的定理：

> 对于任意四个不相交集合$S_1$、$T_1$、$S_2$和$T_2$，满足$S_1 \cup T_1 \cup S_2 \cup T_2 \subseteq V$，那么一定有：
> $$ W(S_1, T_1) + W(S_2, T_2) \leqslant W(S_1 \cup S_2, T_1 \cup T_2) \tag{1.3}$$

**证明**：
$$
\begin{aligned}
& W(S_1 \cup S_2, T_1 \cup T_2) = W(S_1, T_1) + W(S_1, T_2) + W(S_2, T_1) + W(S_2, T_2) \\
& \because W(S_1, T_2), W(S_2, T_1) \geqslant 0\\
& \therefore W(S_1 \cup S_2, T_1 \cup T_2) \geqslant W(S_1, T_1) + W(S_2, T_2)
\end{aligned}
$$

## 求解$s$-$t$最小割
利用最大流最小割定理，一个图的$s$-$t$最小割实际上就是将原图建成一个源点为$s$，汇点为$t$的网络上的最大流，因此可以采用各种最大流算法来解决。这里不再详细介绍。

## 求解全局最小割
所谓全局最小割就是无向图本身的最小割，没有限定$s$和$t$。考虑到一个$s$-$t$最小割可能成为全局最小割，所以可以想出以下的过程：

> 1. 令$i = 1, w_0 = \infty$。
> 2. 如果$|V| \leqslant 1$，返回$\min\{w_0, w_1, \dots, w_{n - 1}\}$。
> 3. 随便选定两个点$s$和$t$，求出其$s$-$t$最小割，记权值为$w_i$。
> 4. 将$s$和$t$合并，即将$E$中的每条边的$t$改成$s$，并从$V$中删去$t$。
> 5. $i = i + 1$，跳回第二步。

这样做的理由是：假设全局最小割为$(S, T)$，那么分两种情况：

1. 如果$s$和$t$分别在$S$和$T$中，那么$s$-$t$的最小割就是全局最小割。
2. 如果$s$和$t$同在$S$或$T$内，那么将$s$和$t$合并为一个点后，不会影响割的权值。

这样我们可以在$\Theta(n)$次网络流内求出最小割。但是由于网络流算法时间复杂度比较高，所以这并不是一个很优的过程。

考虑到在第三步中，我们实际上并不关心$s$和$t$是谁，我们只在意得到一个$s$-$t$最小割。那么是不是可以实现一个更加高效的方法来求出任意一个$s$-$t$最小割呢？

现在来考虑以下这个算法：

```javescript
function ST-MINCUT(G):
    assert |V| > 1

    A = {}
    B = V
    s = 0
    t = 0
    while |B| > 0:
        p = 0
        for u in B:
            if W(A, {u}) > W(A, {p}):  // Assume that W(A, 0) = 0
                p = u
        
        A = A ∪ p
        B = B - {p}
        s = t
        t = p
    
    return (s, t)
```

该算法会返回一个二元组$(s, t)$，表示$(V - {t}, {t})$是一个$s$-$t$最小割。
下面我们将证明这是对的：

> 设$s$和$t$为`ST-MINCUT`中$A$集合倒数第二个加入的点和最后加入的点，那么$(V - \{t\}, \{t\})$是一个$s$-$t$最小割。

**证明**[^mistake]：
我们令$S^\prime = V - \{t\}$、$T^\prime = \{t\}$。对于图中任意一个$s$-$t$割$C = (S, T)$，假设$t \in T$并且$s \in S$。设$t^\prime = v_i$为$T$中除了$t$之外最后被加入$A$的点。令$V_i = \{v_1, v_2, \dots, v_i\}$。此外我们注意到$V_i$实际上是`ST-MINCUT`算法在$G$关于$V_i$的导出子图上的运行结果。
这几个集合内的点的一种可能如下表所示：

$$
\begin{matrix}
S        & = &     & v_2 &          & \dots  & s &   \\
T        & = & v_1 &     & t^\prime &        &   & t \\
S^\prime & = & v_1 & v_2 & v_3      & \dots  & s &   \\
T^\prime & = &     &     &          &        &   & t \\
\end{matrix}
$$

进行归纳假设，对于$|V| = 2$的图，以上结论显然成立。现在假设对于$|V| \lt n$的图均满足，尝试证明对于$|V| = n$的图也满足。

现在我们要证明$W(S^\prime, T^\prime) \leqslant W(S, T)$，就可以得出算法的正确性。首先注意到：

$$
W(S, T) \geqslant W(V_i \cap S, V_i \cap T) + W(V_{n - 1} - V_{i - 1}, \{t\})
\tag{3.1}
$$

以及：

$$
W(S^\prime, T^\prime) = W(V_{i - 1}, \{t\}) + W(V_{n - 1} - V_{i - 1}, \{t\})
\tag{3.2}
$$

根据归纳假设，我们有：

$$
W(V_{i - 1}, \{t^\prime\}) \leqslant W(V_i \cap S, V_i \cap T)
\tag{3.3}
$$

考虑到算法的$A$变为$V_{i - 1}$时，选择了$t^\prime$而不是$t$加入$A$集合，那么说明：

$$
W(V_{i - 1}, \{t\}) \leqslant W(V_{i - 1}, \{t^\prime\}) \leqslant W(V_i \cap S, V_i \cap T)
\tag{3.4}
$$

综上可知：
$$
\begin{aligned}
W(S^\prime, T^\prime) & = W(V_{i - 1}, \{t\}) + W(V_{n - 1} - V_{i - 1}, \{t\}) \\
& \leqslant W(V_i \cap S, V_i \cap T) + W(V_{n - 1} - V_{i - 1}, \{t\}) \\
& \leqslant W(S, T)
\end{aligned}
$$

[^mistake]: 这个证明是原论文中的证明方式，个人认为其中有一些不妥之处，因为在最后一步时，好像忽略了$w(t^\prime, t)$，导致不等式会不成立。不知道是不是个人的理解上的偏差还是确实有误，如果有看过原证明的大神希望能指点我一下。

这样，我们可以通过执行$\Theta(n)$次`ST-MINCUT`算法来找出全局最小割。`ST-MINCUT`的直接实现是$\Theta(n^2)$的，如果使用二叉堆这种数据结构来实现，那么可以做到$\Theta((n + m) \log n)$的复杂度。这个算法就是Stoer-Wanger算法。
