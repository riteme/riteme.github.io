---
title: 二端串并联图相关
create: 2019.1.30
modified: 2019.2.7
tags: 图论
      串并联图
      点双连通分量
      ZJOI
---

[TOC]

# 二端串并联图相关

> 实际上是 ZJOI2016 Day2 T3 电阻网络的题解 -.-

常见的电阻网络一般都会画成这种样子：

![](https://riteme.site/blogimg/resist/network-1.svg)

<center class="figcaption">某个电阻网络</center>

为了方便描述，在图论中，通常用边表示电阻，点表示接线柱，如下图所示：

![](https://riteme.site/blogimg/resist/network-2.svg)

<center class="figcaption">对应的图</center>

在电阻网络中，有一类最为特殊：它们仅使用串联和并联连接而成，并且带有源点和汇点[^sink-and-source]，称为**二端串并联图**（**T**wo-**T**erminal **S**eries-**P**arallel **G**raphs，**TTSPG**）。形式化地讲，仅包含一条边的图是二端串并联图；给定两个二端串并联图，将其中一个图的汇点和另外一个图的源点合并后的图是二端串并联图（串联操作）；给定两个二端串并联图，将源点与源点合并，汇点与汇点合并，得到的图也是二端串并联图（并联操作）。

![from Wikipedia](https://upload.wikimedia.org/wikipedia/commons/d/da/Series_parallel_composition.svg)

<center class="figcaption">串联与并联（图片来自 Wikipedia [[1]](#ref-1)）</center>

[^sink-and-source]: 这里只讨论无向图，故源点和汇点可以互换。为了方便直接称其为端点。

一个有趣的事实是，串并联图都是平面图（这一结论不难由定义使用归纳法得出），并且有许多给出平面画法的算法。此外，串并联图与 SPQR 树 [[2]](#ref-2) 和三连通分量密切相关（虽然我并不会它们…）。由于串并联图是平面图，故边数与点数是同级别的。

## 图的识别

“给定一张无向图，判断这张图是否是可由串联和并联操作得到。”这是一个经典问题。首先，这个问题有一个很模糊的地方，就是它并没告诉你源点和汇点是什么。简单起见，我们先规定一对有效的源汇点，尝试按照定义来拆解原图。首先，如果原图中有割点，那么显然割点都是依靠串联操作拼接而来的，

![](https://riteme.site/blogimg/circuit/series-1.svg)

<center class="figcaption">拆解串联的示意图。紫色节点为端点（源汇点），蓝色节点为割点。每个虚线圈内均为一个判定子问题</center>

此时需要保证图中所有的点双连通分量需呈链状分布，否则原图不可能是**二端**串并联图。所以此时将图按照割点位置切开，从而划为多个子问题。去除割点后，接下来则需要按照并联的方式进行拆分了。不过这个拆分有点小麻烦，毕竟不可能总是下面左图那种简单的情形，只需要将端点发出的边拆开即可，

![](https://riteme.site/blogimg/circuit/parallel-1.svg)

<center class="figcaption">拆解并联的示意图。除紫色外，同种颜色的节点属于同一个子问题。紫色的端点在每个子问题中都会出现</center>

多数情况下我们无法直接知道两条端点发出的边究竟会不会划到同一个子问题内，如右图所示。不过我们知道，子图在合并端点之前，相互之间是不连通的。换句话说，删去端点后，图中每个连通块代表一个子问题，这时就能正确拆分了。

实话讲，这个算法不仅需要规定端点，而且不好快速实现。上面是从拆解的角度来看待串并联图，实际上，从生成的角度来看，会更加简单。除了一开场给出的定义外，二端串并联图还有下面这个等价的定义：

> 从仅含一条边的图开始，执行若干次操作，操作有下列两种：
>
> 1. （串联）选择一条边 $u - v$，增加一个新点 $x$，将原来的边 $u - v$ 替换为 $u - x - v$。
> 2. （并联）选择一条边 $u - v$，增加一条重边 $u - v$。

![](https://riteme.site/blogimg/circuit/alternative-definition.svg)

<center class="figcaption">串联与并联</center>

如何证明等价性？只需要将上图的箭头倒过来看就可以明白了：简单的串联缩成一条边，简单的并联也缩成一条边，如此往复，只要是串并联图，最终都会退化为一条边；反之，反向执行所有操作，即可得到原图。于此同时，判定串并联图的方法就出来了：找到图中一个度数为 $2$ 的点进行缩点，并删去所有重边，不断执行这个过程直到找不到度数为 $2$ 的点。如果最后仅剩下一条边，则为串并联图。不难发现，最后留下的边的端点，也是原串并联图的端点。这个算法结合队列和哈希表实现难度不大，时空复杂度为 $\Theta(n)​$。

## 扩展定义

从现实角度来讲，上面的定义不太科学。主要在于，图中的点双连通分量需在同一条链上。现实中，当端点接入电源时，电阻网络有些部分实际上并无电流，如下图所示。

![](https://riteme.site/blogimg/circuit/bctree-1.svg)

<center class="figcaption">为了方便展示，将原图转为了对应的圆方树（Block-Cut Tree）。紫色节点为端点，灰色部分是没有电流流过的部分</center>

那么对于特定的端点，这些无关的部分无论长成什么样，都不会影响电阻网络的电学属性。因此，判断串并联图之前，先找出所有端点间的简单路径会经过的节点，记为点集 $V'$，然后在原图关于 $V'$ 的导出子图上定义串并联图，这类图称为扩展二端串并联图。此时判定算法就需要提前删去无效节点。

## 结构树

用图来表示电阻网络相当直观，但是实际用起来并不方便，因为我们并不能直接从图中得知整个电阻网络是如何构建起来的。二端串并联图的结构树（Parse Tree[^parse-tree]）是将原图拆解的递归过程保存下来的树结构。树中一共有三种节点，分别为**串联节点**、**并联节点**和**边节点**，其中边节点仅代表原图中的一条边。

![](https://riteme.site/blogimg/circuit/parse-1.svg)

<center class="figcaption">二端串并联图的结构树示意图。左图为原图，其中紫色节点（$1$ 和 $5$）为端点；右图为对应的结构树，红色节点表示并联节点，蓝色节点表示串联节点，灰色节点表示边节点。树上每个节点均对应一条边，但只有边节点才对应原图中的边，其余节点对应虚边。结构树上每个子树均对应原图中一个串并联子图</center>

[^parse-tree]: 实际上结构树是没有 R 节点的 SPQR 树，故有些地方也称为 SPQ 树。一张点双连通的无向图是二端串并联图当且仅当其 SPQR 树中不存在 R 节点 [[2]](#ref-2)。

之前提到的两种识别串并联图的算法都可以用于获取结构树。第一种算法相当于自顶向下生成这棵树，而第二种算法，缩点算法，是自底向上逐渐合并成结构树。实现细节这里就不啰嗦了，只需要注意第二种算法过程中需要合并两个串联或者并联的节点，时空复杂度为 $\Theta(n)$。

为了更直观地表示图的结构，串联节点和并联节点绘制时通常会对应一个 “框架”（Skeleton）。串联节点对应一条链，称其为串联路径（为了方便，边节点可以视为特殊的串联节点，故单独的一条边也可以称为串联路径）；并联节点对应由几条重边构成的图。框架内的每条边代表该节点的一个儿子。

![](https://riteme.site/blogimg/circuit/parse-2.svg)

<center class="figcaption">先前的例子中的结构树的另外一种画法</center>

值得注意的是串联节点的父亲肯定是并联节点，并联节点的父亲肯定是串联节点，以及所有边节点都是叶子节点。此外，如果图中没有割点，根节点就必为并联节点，否则为串联节点。

## 【ZJOI2016】电阻网络

> 给定一张 $n$ 个点 $m$ 条边的无向图，问有多少种选择端点的方法，使得这张图是扩展二端串并联图。
>
> $n,\ m \leqslant 10^5$

既然是要求扩展的定义，那么免不了求点双连通分量。首先，对于特定的端点，在点双树上，这两个端点间会经过几个点双连通分量。若这对端点合法，则经过的每个点双连通分量内，端点（或者割点）到割点之间必须是二端串并联子图。这样就把问题分解到点双连通分量里了。

![](https://riteme.site/blogimg/circuit/valid-1.svg)

<center class="figcaption">一个合法方案的示意图</center>

现在我们考虑：对于一张点双连通的图，给定两个端点，如何快速判断这张图是否是二端串并联图？线性的做法非常简单，在缩点算法里，缩点时避免对给定的端点执行操作，如果最后能得到一条边则为串并联图。原题肯定不能直接用这种算法。不过结构树实际上保存了缩点算法的整个过程，因此可以考虑用这棵树来加速。

假设现在得到了结构树，对于树上任意一棵子树，这棵子树以及删去该子树得到的树均可以分别缩为一条边。那么对于端点 $a$ 和 $b$，不难发现如果 $a$ 和 $b$ 可以放到某条串联路径上，则这对端点是合法的（下图 (a) ）。其它情况下，我们将会逐一验证为不合法。考虑 $a$ 和 $b$ 处于两个不同的串联路径上，分别对应 $u$ 和 $v$ 两个串联节点[^series-node]。设 $p$ 为 $u$ 和 $v$ 在结构树上的最近公共祖先，假设 $p$ 不是根节点，分以下几种情况考虑：

1. $p = u$ 或 $p = v$。
2. $p \neq u,\ v$ 且 $p$ 为并联节点。
3. $p \neq u,\ v$ 且 $p$ 为串联节点。

具体的验证过程在下面这张图中的 (b)、(c)、(d) 给出。

![](https://riteme.site/blogimg/circuit/proof-1.svg)

<center class="figcaption">$a$ 与 $b$ 在树中的几种情况。　**(a)** $a$ 与 $b$ 在同一条串联路径上，此时执行缩点算法得到一个环。　**(b)** $a$ 与 $b$ 在不同的串联路径上，其中一个串联节点是另外一个节点的祖先。注意 $p$ 中走向另一个端点的边的顶点不是端点，否则 1) 若两个串联节点之间只有一个并联节点，则实际上退化为第一种情况；2) 若两个串联节点间有多个节点，则顶部的端点可以下移，直到变成第一种情况或者是第二种情况。蓝色边为子树 $p$ 之外的部分缩成的边，黄色边为 $p$ 到下端子树之间的部分缩成的边，红色边为下端子树缩成的边，绿色边为 $p$ 中除了下端子树之外的子树缩成的边　**(c)** $a$ 与 $b$ 在不同的串联路径上，最近公共祖先 $p$ 为并联节点。　**(d)** $a$ 与 $b$ 在不同的串联路径上，最近公共祖先 $p$ 为串联节点。</center>

[^series-node]: 注意这里的 $u$ 和 $v$ 不是唯一的，只保证 $u \neq v$。

前面之所以要求 $p$ 不是根节点，是因为上图 (c) 这种情况中，若 $p$ 为根节点且只有两个分岔，则给定的端点是合法的。为了避免，我们首先特判掉简单的环状图，这样保证图中存在度数大于 $2$ 的节点。然后在缩点算法中，优先缩原图中度数为 $2$ 的点，这样就可以保证根节点的分岔数至少为 $3$。综上，我们可以得出，一对端点合法的充要条件是这对端点可以放在同一条串联路径上。

至此，这道题最关键的一点已经完成了。接下来的任务就是根据这个性质在结构树和原图的点双树上做 DP 即可，这个过程这里就不赘述了。时空复杂度为 $\Theta(n)$。

## 后记

我没有在网上搜到这道题的题解，所以写了这篇博客。最开始做这道题时一脸懵逼，想查资料却不知道该搜什么关键词。然而我大胆地猜想题面中的图一定是从什么地方蒯来的……于是用 Google 的 Search by Image 找到了 Wikipedia……才知道原来是个这么厉害的玩意……

对拍时数据不够强结果 WA 了 $5$ 个点，之后采取先生成一棵树，再按照定义生长出串并联图的办法造出了一些强一点的数据后才调过了。

我的代码在 LOJ 上拿了第一，在 UOJ 上拿了倒数第一 QAQ

## 参考资料

<span id="ref-1">[1].</span> "[*Series-parallel graph*](https://en.wikipedia.org/wiki/Series-parallel_graph)", Wikipedia
<span id="ref-2">[2].</span> "[*SPQR tree*](https://en.wikipedia.org/wiki/SPQR_tree)", Wikipedia
