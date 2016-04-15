---
title: 最小费用最大流
create: 2016.2.2
modified: 2016.2.2
tags: 算法
      网络流
      最小费用流
      图论
---
[TOC]
# 最小费用最大流
之前一直想不明白最小费用流，今天翻了很多资料才理解了，在此做点记录。

## 最小费用流
我们首先定义流$f$的费用$w(f)$为：
$$
w(f) = \sum_{(u,v)\in f} w(u,v)f(u,v)
$$

那么最小费用（可行）流就是指一个在所有同流量的流中费用最小的流。

## 最小费用最大流问题
在给定的流网络$G$中，若$(u,v)\in E$，则$c(u,v)$表示其容量，$w(u,v)$表示其**单位流费用**。设$f$为其中的可行流，最小费用最大流问题就是要求在使$f$为最大流的情况下，其总费用$w(f)$最小。

## 增广路算法
本文中我们只讨论增广路算法。最小费用流还有消圈法和神奇的ZKW算法。

增广路算法有一个贪心的基本思想：已知一个最小费用流$f$，在流网络中找出一条费用最小的增广路对其增广得到$f^,$，那么$f^,$也是最小费用流。
这个结论是显而易见的，因为原流费用最小，增广出来的新流费用也最小，那么总费用也是最小的。

因此，寻找最小费用最大流的思路就出来了：

1. 初始化零流$f$  
2. 寻找费用最小的增广路，如果没有则表明$f$已为最大流  
3. 增广流$f$，跳至第二步

在上面的步骤中，第二步是关键。

我们首先要确定费用最小的衡量标准。首先考虑一条增广路会对流增加多少的费用。

假设$p$是一条增广路，其瓶颈边（即剩余容量最小的边）的容量为$c_{min}$，那么增加的费用就是所有边所产生的费用之和：

$$w(p) = \sum_{(u,v)\in p} w(u,v)c_{min} = c_{min}\sum_{(u,v)\in p} w(u,v)$$

由于我们要保证每一步都是最小费用流，而流的大小并不在意，因为最后肯定能达到最大流。
故我们不在乎每次流的增量$c_{min}$，而只要使单位费用之和最小即可。

因此我们把每条弧的单位费用作为其边权，然后寻找一条从源点到汇点的最短路，这样就能使单位费用之和最小。

## 实现细节
现在我们来尝试实现增广路算法，首先我们定义边的结构体：

```python
# 表示有向边
class DirectedEdge(object):
    u:int                      # 出发点
    v:int                      # 进入点
    capacity:int               # 容量
    flow:int                   # 现有流量
    cost:int                   # 单位流费用
    reverse_edge:DirectedEdge  # 表示其在残留网络中的反向边
```

我们添加一个函数，计算边的的剩余流量：

```python
def r(edge:DirectedEdge):
    return edge.capacity - edge.flow
```

在残留网络中，如果剩余容量为0,它就已经不存在了。
我们使`G`为一个有向边链表的数组，表示从某个点出发的边集合。

现在思考下残留网络中反向边的费用。反向边本意是为了最大流算法能重新调整整个流，让算法能够“反悔”，
因此我们给反向边的费用为`-cost`，能够与之前的选择抵消。这样导致出现了负边，因此找最短路不能使用Dijkstra算法，

为了方便，我们添加一个`add_edge`函数来添加边：

```python
def add_edge(u:int, v:int, capacity:int, cost:int):
    e  = DirectedEdge(u, v, capacity,  cost, flow=0)         # 初始为零流
    re = DirectedEdge(v, u, capacity, -cost, flow=capacity)  # 注意是反向边

    # 设置反向边
    e.reverse_edge = re
    re.reverse_edge = e

    G[u].append(e)
    G[v].append(re)
```

这样就可方便的添加边

最好采用Bellman Ford算法，这里使用其改进版SPFA算法：

```python
dist:int[]             = [INFTY...]  # 距离数组
edge_to:DirectedEdge[] = [None...]   # 前趋边数组

def SPFA(s:int, t:int):
    q:queue
    q.push(s)
    dist[s] = 0

    while q not empty:
        u:int = q.pop()

        for edge in G[u]:
            if r(edge) == 0:  # 如果剩余容量为0,这条边就不存在
                continue

            # 松弛操作
            v:int = edge.v
            if dist[v] > dist[u] + edge.cost:
                dist[v]    = dist[u] + edge.cost
                edge_to[v] = edge  # 更新前趋边

                if v not in q:
                    q.push(v)
```

接下来就可以写最小费用最大流算法了：

```python
s:int  # 源点
t:int  # 汇点

def compute_maxflow():
    answer:int = 0

    while True:
        SPFA(s, t)  # 寻找增广路

        if dist[t] == INFTY:  # 如果没有增广路，s到t的距离就不会更新
            return

        minflow:int = INFTY  # 瓶颈边容量

        # 寻找瓶颈边
        x:int = t
        while edge_to[x] is not None:
            minflow = min(minflow, r(edge_to[x]))

            x = edge_to[x].u

        # 增广
        x = t
        while edge_to[x] is not None:
            DirectedEdge e = edge_to[x]

            answer += minflow * e.cost  # 更新总费用
            e.flow += minflow
            e.reverse_edge.flow -= minflow

            x = edge_to[x].u

    return answer
```

至此，增广路算法就结束了。现在总结下其中涉及到的关键：  
1. 贪心选择：每次寻找费用最少的增广路  
2. 反向边边权：是相反的  
3. SPFA: 寻找最短路
