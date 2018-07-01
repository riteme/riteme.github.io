---
title: 最小树形图
create: 2018.6.18
modified: 2018.6.18
tags: 图论
      数据结构
      并查集
      可并堆
      最小树形图
---

[TOC]

# 最小树形图

## 问题引入

在带权无向图中，**最小生成树**是一个广为人知的问题。对应的，在有向图中，我们也可以定义**有向生成树**（**D**irected **S**panning **T**rees，简称 DST）。在有向图 $G = (V,\ E)$ 中，我们选定一个生成树的根节点 $r$，以 $r$ 为根的有向生成树是图 $G$ 的一个子图 $T$，并且子图 $T$ 中 $r$ 到任意非 $r$ 节点 $u$ 的路径**存在且唯一**。根据树的定义，子图 $T$ 的形状就是一棵以 $r$ 为根的树，只不过所有的边都是从父亲指向儿子的有向边。所以也称为 “树形图”。

需要注意的是，并非图 $G$ 中任意一个节点都能成为某个 DST 的根。具体而言，必须要满足从 $r$ 出发能够到达其它的顶点。如果将图 $G$ 的所有强连通分量缩点，得到一张拓扑图，且拓扑图中只有一个入度为 $0$ 的点 $u$，则 $r$ 必须来自 $u$ 所代表的强连通分量中。

类比最小生成树，最小树形图就是带权有向图 $G = (V,\ E,\ w)$ 中边权总和最小的 DST，简称 MDST（**M**inimum DST）。虽然定义类似，但算法却不尽相同。因为**在有向图中，给定 DST 的根 $r$，有一些边可能不能成为任何一个 DST 的树边**[^invaild-edges]。这导致对于无向图的算法（Kruskal 算法、Prim 算法等等）都无法在有向图上算出最小树形图。

[^invaild-edges]: 例如，一棵 DST 上的所有 “返祖边”。

1965 年，朱永津和刘振宏 [[1]](#references-1) 最先提出了最小树形图时间复杂度为 $O(VE)$ 的算法。两年后，也就是 1967 年，Edmonds [[2]](#references-2) 也独立发现了同样的算法。可能 Edmonds 名气比较大，现在英文资料里面关于这个算法的叫法总少不了 Edmonds 的名字 QAQ

## 算法流程

首先，DST 有一个特点：除根节点外，其它节点的入度为 $1$。此外，DST 是不存在环的。一个非常奇怪的想法就是，对于每个非根节点，选择**入边中边权最小的**。因为这样选择之后，如果图中没有环，不难发现就构成了一棵 DST，并且显然它的边权之和也是最小的，因此直接找到了 MDST。

当然现实没有那么美好，很大概率下，这样选择会出现环。现在来考虑其中的一个环 $C$，这个环上至少有一条边是不能选的。但可能还有更多的边在真正的 MDST 中也不能选？然而事实却非常巧，注意到环 $C$ 不是一般的环，它是由边权最小的入边组成的环。我们可以证明，存在一棵 MDST，其中进入环 $C$ 的边只有一条。

![cycle-example](https://gitee.com/riteme/blogimg/raw/master/mdst/cycle.svg)

<center>**Fig.1.** 环 $C$ 的一个示意图。红色的边不是环上的边，是某棵 MDST 中的边。虚线边被红色边所取代。</center>

如上图所示，对于任意的 MDST，设为 $T$，如果只有一条进入环 $C$ 的边，那我们的目的就达成了。否则，将会有至少两条边进入。如上图所示，选择其中一个进入点 $y$（即上图中边 $u$ 和边 $v$ 进入的点），设边 $u$ 的另一个端点为 $x$。不难发现 $x$ 和 $y$ 在树 $T$ 上的 LCA（最近公共祖先）不在环 $C$ 上，所以将边 $v$ 从 $T$ 中删去，然后加入边 $u$，得到的依然是一棵 DST，设为 $T'$。而边 $u$ 是 $y$ 入边中边权最小者，即 $w(u) \leqslant w(v)$，所以 $T'$ 的边权之和不超过 $T$ 的边权之和，所以 $T'$ 也是一棵 MDST。重复此操作我们可以得到只有一条进入环 $C$ 的边的 MDST。

换句话说，我们可以只用考虑删去环 $C$ 的一条边的情况。想象一下，相当于环 $C$ 只有一条入边。这又与 DST 有相似之处。考虑将**环 $C$ 缩成一个点**，在得到的新图 $G'$ 中，图 $G'$ 中的一个 DST 可以对应我们所需要的考虑的一个 DST。这启发着我们进行一次递归的操作：假定原来我们选择了环 $C$ 中所有的边，但由于 DST 定义的要求，我们需要从中替换掉一条边 $u$，换成环 $C$ 外的一条边 $v$，此时边权之和会多增加 $w(v) - w(u)$。所以，将环 $C$ 缩为一个点 $c$ 时，设环 $C$ 中进入点 $x$ 的边为 $\mathrm{in}(x)$，对图 $G$ 中的所有边 $e:\ u \rightarrow v$ 作如下处理：

1. 如果 $u,\ v \notin C$，即环外一条边，该边保持不变。
2. 如果 $u,\ v \in C$，即内接在环上的一条边，将这条边删去。
3. 如果 $u \in C$ 而 $v \notin C$，相当于从环 $C$ 出发的边，则将 $u$ 改为 $c$。
4. 否则就是进入环 $C$ 的边，此时将 $v$ 改为 $c$，且边权变为 $w(e) - w(\mathrm{in}(v))$。

在得到的新图 $G'$ 中计算 MDST，得到 $T'$，根据 $T'$ 进入 $c$ 的边的 “前身” 就可以知道环 $C$ 中应该抛弃哪一条边了。将原图 $G$ 中的自环排除后，每次这样的操作至少可以减少一个点，所以总的时间复杂度为 $O(VE)$。

## 快速实现

我们知道，无向图中最小生成树的时间复杂度取决与排序的复杂度，即 $O(E \log E)$ 或比这更好的 $O(E + V \log V)$。相比之下，之前的算法实在是太慢了。于是伟大的 Tarjan 老爷子 [[3]](#references-3) 就出现了。Tarjan 在 1977 年提出了一个时间复杂度为 $O(E \log V)$ 的实现，他将上述算进行了调整，使用一个迭代式的过程完成了算法。首先，为了方便，我们假定带权有向图 $G$ 是强连通的。即使没有强连通，可以添加 $V$ 条边将每个点顺次连成一个环，并且每条边的边权足够大，使得它们不会出现在 MDST 中，这样就可以保证强连通。

算法开始时，选取图中任意一个点 $x$，然后选取 $x$ 的入边中边权最小的边 $e:\ u \rightarrow x$，如果 之前没有访问过 $u$，则将 $u$ 追加到 $x$ 后面，构成一条链，然后继续从 $u$ 开始执行同样的步骤。如果 $u$ 已经被访问过，说明在链中形成了一个环，此时则执行缩环操作。最后，由于强连通的特性，整张图会被缩成一个点。在此期间，我们可以存下缩环的操作结果，这用一棵树来表示：

![tree-example](https://gitee.com/riteme/blogimg/raw/master/mdst/tree.svg)

<center>**Fig.2.** 左边是一个 $4$ 个点的强连通图，右边是算法完成后所给出的树结构。首先将环 $1 \rightarrow 2 \rightarrow 3$ 缩为了点 $5$，然后将环 $5 \rightarrow 4$ 缩为了点 $6$。这棵树展示了环与环之间嵌套的关系。</center>

得到这棵树之后，我们就可以从任意合法的根节点开始展开整个 MDST 了。上述过程中缩点一般采用并查集数据结构，而为了能够既完成缩点，又能随时从某个点中抽出边权最小的入边，这里则需要可并堆来高效实现。上面说的比较粗糙，因为仔细讲起来就太细节化了。我实现了朴素的 $O(VE)$ 算法和 Tarjan 的快速算法，用 [POJ 3164](http://poj.org/problem?id=3164) 测试了下，如果细节上有问题的可以参考一下：

[$O(VE)$ 版本](https://github.com/riteme/test/blob/master/oi/Code/poj/P3164/nm.cpp)、[$O(E \log V)$ 版本](https://github.com/riteme/test/blob/master/oi/Code/poj/P3164/main.cpp)

另外，我是看的 Uri Zwick 教授 [[4]](#references-4) 的讲稿写的算法，里面的实现部分写的比较详细。

## 相关问题

上面的讨论中，MDST 的树根都是给定了的。而在有些问题中，可能没有给定树根（更类似于无向图的最小生成树了）。解决这类问题并不需要进行 $O(V)$ 次展开。我们可以给图新增一个点 $x$，向原图中每一个点连一条边权足够大的边，这样以 $x$ 为根的 MDST 中，算法只会选择一条 $x$ 的出边，毕竟选择这样的边非常不划算。而此时 $x$ 的出边所指向的点就是原问题中 MDST 的树根。

## 参考文献

<span id="references-1">[1]. Chu, Y. J.; Liu, T. H. (1965), *On the Shortest Arborescence of a Directed Graph*, Science Sinica, 14: 1396–1400</span>
<span id="references-2">[2]. Edmonds, J. (1967), *Optimum Branchings*, J. Res. Nat. Bur. Standards, 71B: 233–240, [doi](https://en.wikipedia.org/wiki/Digital_object_identifier):[10.6028/jres.071b.032](https://doi.org/10.6028%2Fjres.071b.032)</span>
<span id="references-3">[3]. R.E. Tarjan. (1977), *Finding optimum branchings*, Networks, 7:25–35<span>
<span id="references-4">[4]. Uri Zwick. (2013), [*Directed Minimum Spanning Trees*](http://www.cs.tau.ac.il/~zwick/grad-algo-13/directed-mst.pdf), Lecture notes on “Analysis of Algorithms”</span>
[5]. H.N. Gabow, Z. Galil, T.H. Spencer, and R.E. Tarjan. (1986), *Efficient algorithms for finding minimum spanning trees in undirected and directed graphs*, Combinatorica, 6:109–122
