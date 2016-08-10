---
title: 最近公共祖先(LCA)
create: 2016.2.1
modified: 2016.2.1
tags: 算法
      LCA
---
[TOC]
# 最近公共祖先(LCA)
## 1 概述
### 1.1 什么是LCA？
下面是一棵有根树，注意不一定是二叉树。

![Sample Tree](http://git.oschina.net/riteme/blogimg/raw/master/lca/sample-tree.png)

我们先定义深度函数$ d(u): u \text{到根的最短距离} $。

例如，在上图中$ d(1)=0,\,d(3)=1,\,d(9)=3$

我们再定义一个函数$ LCA(u, v) $表示节点$ u $和$ v $的最小公共祖先。

其定义为：
$$ LCA(u,v):u和v的所有祖先p中,d(p)最大 $$

举个例子：$ LCA(5,6)=3,\,LCA(7,6)=3,\,LCA(1,8)=1 $

应该很简单吧。

### 1.2 有什么卵用？
一个简单的例子，计算完LCA后，可以在$ \Theta (1) $的时间内算出任意两点的距离。

还是下面这个图解释：

![Sample Tree With Weight](http://git.oschina.net/riteme/blogimg/raw/master/lca/sample-tree-weighted.png)

上面的树边上带了权重，两点之间的距离就是两点间的简单路径上的边权之和。

例如$ distance(1,1)=0,\,distance(2,3)=3,\,distance(7,6)=6$

如果用DFS或BFS来计算的话，需要$ O(n) $的时间复杂度。

如果先预处理LCA，就只需$ \Theta (1) $的时间。

先不考虑是如何算出LCA的，先讲下如何快速求距离。

上图中，`dist`数组表示节点到树根的距离，在图中已经计算出来。
这个数组很好计算，根据下面的公式直接将树BFS一遍即可，其中$ u $是$ v $的父节点，$w[u, v]$表示$ u $到$ v $的边权。
$$ dist[v] = dist[u] + w[u,v] \tag{1.1}$$

那么两点之间的距离$ distance(u,v) $的计算非常简单：
$$ distance(u,v) = dist[u] + dist[v] - 2 \times dist[LCA(u, v)] \tag{1.2} $$

可以想象成是Link这个人从$ u $先走到根节点，再从根节点走到$ v $。由于从根节点到$ LCA(u,v) $走了两遍，因此Link走的总路程，减去这一段来回走的即可。

### 1.3 预备知识
因为LCA的算法中会用到并查集，但我们还没学，因此并查集的实现不会过多纠结，我们只需知道并查集提供的几个函数即可。

并查集提供查询和连接操作：

```python
def find(u) -> int
def union(u, v) -> void
```

* `find`函数会返回节点`u`所在的集合编号，如果`find(a) == find(b) `则表示`a`和`b`处在一个集合中。

* `union`函数会将`u`和`v`所在的集合并起来，即使`u`和`v`处在一个集合中。

后面会提到**在线**和**离线**的概念，只要知道离线是**先将所有操作读入后**再作处理就行了。

## 2 LCA算法
计算LCA的算法有很多，这里介绍三个。

### 2.1 朴素算法
朴素算法是最简单的了，按照国际惯例，先放图：

![Sample Tree](http://git.oschina.net/riteme/blogimg/raw/master/lca/sample-tree.png)

朴素算法的做法如下：

> 1. 先将两个结点调为同一深度
> 2. 将两个结点同时上调，直到这两个结点到达同一位置时，此时即为LCA

伪代码如下：

```python
def Plain_LCA(u, v):
    if d(u) < d(v):
        swap(u, v)  # 始终保持u所处的深度较深

    while d(u) != d(v):
        u = father(u)  # 将u上调

    # 将u和v同时上调
    while u != v:
        u = father(u)
        v = father(v)

    # 最后会使u == v，即他们到达了LCA
    return u
```

### 2.2 离线算法：Tarjan-LCA
朴素算法很简单，大多数情况下能很快算出LCA。

然而在计算$ LCA(4,6) $时，需要从树的底部走到根节点。

因此朴素算法的时间复杂度为$ O(n) $，很容易TLE。

因此我们的前人想出了机智的Tarjan-LCA算法！

Tarjan-LCA算法比较难理解，最好的理解方法是手动模拟一下。
先放出伪代码：

```python
def Tarjan_LCA(u):
    # ancestor数组表示一个集合的公共祖先
    # 如anscestor[i]表示标号为i的集合中所有结点的公共祖先。
    # marked数组表示结点是否被处理过

    anscestor[find(u)] = u

    for v in u.children:  # 遍历u的儿子节点
        Tarjan_LCA(v)
        union(u, v)
        anscestor[find(u)] = u

    marked[u] = true

    # query数组表示查询操作，保存的是(x, y)，表示要计算LCA(x, y)
    for (x, y) in query:
        if y == u and marked[x] == True:
            LCA(x, y) = LCA(y, x) = anscestor[x]
```

这个算法的进行类似于DFS，是个递归调用的过程。
因为DFS总是先将小的子树遍历完，因此`anscestor`数组中的祖先都是尽可能小的。

拿一棵较小的子树作为示例：

![Sample Subtree](http://git.oschina.net/riteme/blogimg/raw/master/lca/sample-tree-2.png)

一开始先DFS到`7`处。

![Step 1](http://git.oschina.net/riteme/blogimg/raw/master/lca/tarjan-1.png)

处理到`7`时还并没有什么结点被处理过，只好默默的回到5。

![Step 2](http://git.oschina.net/riteme/blogimg/raw/master/lca/tarjan-2.png)

`5`处将`7`和自己相连，形成集合`{5, 7}`，`5`是这个集合的公共祖先。

![Step 3](http://git.oschina.net/riteme/blogimg/raw/master/lca/tarjan-3.png)

现在DFS到`9`。

![Step 4](http://git.oschina.net/riteme/blogimg/raw/master/lca/tarjan-4.png)

假设我们询问了$ LCA(7,9) $，那么在处理`9`时，会发现`7`被处理过了，**`7`所在的集合的公共祖先为`5`**。
而`9`是从`5`递归下来的，因此**`9`与`7`的公共祖先中有`5`**。
又因为DFS会尽可能的处理较小的子树，因此**`5`将会是$ LCA(7, 9) $**。

剩下的步骤都是一样的，大家可以自己手推一下。

为了方便理解，大家可以将Tarjan-LCA算法换个说法：
> 一个熊孩子Link从一棵有根树的最左边最底下的结点灌岩浆，Link表示很讨厌这种倒着长的树。
> 岩浆会不断的注入，直到注满整个树...
> 
> 如果岩浆灌满了一棵子树，Link发现树的另一边有一棵更深的子树，Link会先去将那棵子树灌满。
>
> 岩浆只有在迫不得已的情况下才会向上升高，找到一个新的子树继续注入。
>
> 机(yu)智(chun)的Link发现了找LCA的好方法，即如果两个结点都被岩浆烧掉时，他们的LCA即为那棵子树上岩浆最高的位置。

Tarjan-LCA算法能在$ \Theta (n + q) $时间内计算出所有询问的LCA，其中$ q $为询问总数。
这得益于并查集的高效。
同样我们也能以此算出所有点对的LCA。

### 2.3 在线算法：倍增法
Tarjan-LCA算法速度很快，效果也很好，但有一个致命的问题...

就是内存占用。

首先它需要离线操作，如果空间比较紧且操作较多时，显然不合适。

另外，如果要处理任意结点对的LCA，就需要一个巨大的二维数组来存储，这意味着如果$ n > 10000 $此算法将报废。

但如果用朴素算法，就又太慢了...

这时，倍增法就来拯救世界了。

倍增法能以$ \Theta (\log n) $的时间复杂度和$ \Theta (n \log n) $的空间复杂度内完成LCA的计算。

相比与Tarjan-LCA的$ \Theta (n^2) $的空间复杂度，能节省更多的空间。
并且它是在线算法，弥补了LCA算法的不足。

倍增法运用了动态规划的思想，并利用二进制达到了$ \Theta (\log n) $的时间复杂度。

#### 2.3.1 预处理
倍增法首先需要计算一个`f`数组，其含义为：
$$ f[i, j] : 离节点i相距2^j的父节点 $$

换言之
$$ distance(i, f[i, j]) = 2^j \tag{2.1} $$

![Sample Tree](http://git.oschina.net/riteme/blogimg/raw/master/lca/sample-tree.png)

又是这个图。我们将树上的每一条边的长度都视为1，那么$ f[7, 0] = 5,\,f[7, 1] = 3 ... $，
因此节点$ 5 $到$ 7 $的距离为$ 1 = 2^0 $，节点$ 3 $到$ 7 $的距离为$ 2 = 2^1 $。
由此我们可以观察到`f`数组的一个特点：$ f[i, 0] $就是$ i $的父节点。

为了算出`f`数组，我们有如下的状态转移方程：
$$ f[i,j] = f[f[i, j - 1], j - 1] \tag{2.2} $$

如何理解这个转移方程呢？

我么设$ u = f[i,j],\,v=f[i, j-1] $，

那么，根据$ (2.1) $式可得：

$$
\begin{align}
distance(i, v) & = 2^{j-1} \\
distance(i, u) & = 2^j \\
distance(v, u) & = distance(i, u) - distance(i, v) \\
&                = 2^j-2^{j-1} \\
&                = 2^{j-1} \times 2 - 2^{j-1} \times 1 \\
&                = 2^{j-1} \\
&                \Rightarrow u = f[v, j - 1] \\
&                \Rightarrow u = f[f[i, j-1],j-1]
\end{align}
$$

即证明$ (2.2) $式。

利用得到的状态转移方程，我们可以在$ \Theta (n \log n) $的时间内推出`f`数组。

```python
# 初始化f[i, 0]
for i in [1, n]:
    f[i, 0] = father(i)

# 计算整个f数组
for j in [1, log(n)]:
    for i in [1, n]:
        f[i, j] = f[f[i, j - 1], j - 1]
```

#### 2.3.2 在线算法
得到了`f`数组后，倍增法也就完成了50%了，剩下的任务就是计算LCA。

事实上，倍增法计算LCA的过程与朴素算法一样，也是要先调制同一深度，再同时上调。
而巧妙的是倍增法利用算出的`f`数组来加速提升的过程，使得节点的上升的距离可以达到$ 2^j $，而不是一格一格往上调。

思路已经很清晰了，然而难在如何运用`f`数组。

下面的伪代码展示了倍增法求LCA的过程：

```python
def Double_LCA(u, v):
    if d(u) < d(v):
        swap(u, v)  # 始终保持u所处的深度较深

    # 将u上调dist个距离
    dist = d(u) - d(v)
    for i in [0, log(n)]:
        if (1 << i) & dist  # KEY #1
            u = f[u, i]

    if u == v:
        return u  # 特判此时u, v是否在同一位置，如果是，u和v都站在LCA上

    # 将u和v同时上调
    for i from log(n) to 0:
        if f[u, i] != f[v, i]:  # KEY #2
            u = f[u, i]
            v = f[v, i]

    # 最后会使u和v成为LCA的子节点
    return f[u, 0]
```

在代码中有两处比较奇特的地方，被注释打上了`KEY`。

先看`KEY #1`，这里的代码是尝试将$ u $与$ v $调制统一高度，而这里出现的位运算令人十分费解。

首先我们思考一下二进制：
对于一个二进制数$ k $，设其从右往左数的第$ i $位为$ k_i $，则当$ k_i = 1 $时，$ k - 2^i $的第$ i $位为$ 0 $。

例如，对于二进制数$ 110010_{(2)} $，第$ 2 $位为$ 1 $，$ 2^2 = 10_{(2)} $，$ 110010_{(2)} - 10_{(2)} = 110000_{(2)} $，我们发现这个二进制数的第$ 2 $位变成了$ 1 $。

利用这个特性，我们可以逐位将一个二进制数减成$ 0 $。

在上面的代码中，就这样逐步上调节点$ u $，并使最后的深度差`dist`变为$ 0 $。
下面有一张样例：

![Sample #1](http://git.oschina.net/riteme/blogimg/raw/master/lca/double-1.png)

再来看`KEY #2`，此时$ u $和$ v $处在同一深度上，$ j $从大到小逐一测试。

我们试图使$ u $和$ v $尽可能靠近LCA，但又不直接到达LCA。

如果说$ 2^j $的距离上，$ u $和$ v $的父节点相同，则这个父节点是它们的公共祖先，如果跳上去就有可能超过LCA了，因此忽略。

如果说$ 2^j $的距离上，$ u $和$ v $的父节点不同，则$ f[u, j] $和$ f[v, j] $的LCA也是$ u $和$ v $的LCA，因此可以将$ u $和$ v $上移至该位置，不影响结果。

因为这两个节点到LCA的深度差可以被分解成多个$ 2 $的幂之和，因此我们有办法逐步将它们上移至LCA的位置。

但是为了方便判断是否跳的太远，我们不让它们最后跳到LCA的位置，而是跳到LCA的儿子节点处。

此时其父节点就是LCA。

下面有一张样例：

![Sample #2](http://git.oschina.net/riteme/blogimg/raw/master/lca/double-2.png)

至此，倍增法就结束了。

以上三种算法是比较常见的求LCA的算法。似乎二叉树还有一种分治的LCA算法，我没有做过多了解了。
