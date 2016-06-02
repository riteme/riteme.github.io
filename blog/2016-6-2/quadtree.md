---
title: 点分四叉树 (Point Quadtree)
create: 2016.6.2
modified: 2016.6.2
tags: 四叉树
      划分树
      数据结构
---

[TOC]
# 点分四叉树 (Point Quadtree)
点分四叉树是一种二维平面上的划分树，可以用于快速统计平面上的点的信息。
下图展现了一棵四叉树。其中箭头表示树中的边，矩形表示一个点所管辖的范围。
![quadtree](http://git.oschina.net/riteme/blogimg/raw/master/quadtree/quadtree.png)

## 原理
考虑下面的问题：

> 给你平面上$n$个点，然后不断的询问一个矩形范围内有多少个点。

通常大家会想到用二维线段树或是各种奇怪的分治算法。这当然是可以的。
这个问题恰好是为四叉树设计的。

基本的思路就是将平面切分，当然这里不是二分[^binary-split]，而是将四分。我们每次以一个点作为平面的中心来将平面划分。这样利用分治的思想可以快速维护一些点上的信息。

[^binary-split]: 当然有进行二分的树，具体参见[$k$-d tree](https://en.wikipedia.org/wiki/K-d_tree)

## 建树
从上面的图可以看出，我们每次会选择一个点来划分，同时我们以这个点为根节点，然后将其它的点分发到四个子平面内。然后对四个子平面进行递归处理。这样就可建立一棵四叉树。
当然，我们选择的这个点要尽可能使四个子平面中点数接近。这样就防止树过高。直接判断哪个点使四个子平面的点数最接近并没有比较好的算法。通常的做法就是将点按照一维进行排序后取中。可以证明，这样选择后的四叉树的期望树高为$O(\log n)$。
当然，对点的排序可以在建树前完成，因为在建树的过程中，分发点是不会打乱顺序的。
为了方便统计信息，我们需要知道一个节点所管辖的真正的范围。通过将所有的点扫描一遍就可以得出这个范围。

由此我们可以得到建树的基本流程：

```
// 对于每个树节点x，x.point是其表示的点，x.rectangle是其实际管辖的范围
// x.NE、x.NW、x.SE、x.SW表示四个方位的子平面
// 建树前先对点集排序

function BUILD-QUADTREE(P):  // P是点集
    if |P| = 0:  // 如果没有点
        return nil
    
    x = allocate a new node
    if |P| = 1:
        x.point = P[0]
        x.rectangle = { x.point.x, x.point.x, x.point.y, x.point.y }
        
        return x
    
    p = P[|P| / 2]  // 选取最中间的点
    midx = p.x, midy = p.y  // 切分线
    minx = INFTY, max = -INFTY, miny = INFTY, maxy = -INFTY  // 实际管辖的边界
    let Q1, Q2, Q3, Q4 be empty sets  // 四个子平面的点集
    for u in P:
        minx = min(minx, u.x)
        maxx = max(maxx, u.x)
        miny = min(miny, u.y)
        maxy = max(maxy, u.y)
        
        if u != p:  // 分发点至四个子平面
            if u in Q1.rectangle:  // 在第一个子平面中
                Q1.append(u)
            else if u in Q2.rectangle:
                Q2.append(u)
            else if u in Q3.rectangle:
                Q3.append(u)
            else
                Q4.append(u)
    
    // 更新树节点
    x.point = p
    x.rectangle = { minx, maxx, miny, maxy }
    x.NE = BUILD-QUADTREE(Q1)
    x.NW = BUILD-QUADTREE(Q2)
    x.SE = BUILD-QUADTREE(Q3)
    x.SW = BUILD-QUADTREE(Q4)
    
    return x
```

建树的总时间复杂度为$O(n\log n)$。因为树高是$O(\log n)$的。
你也许会好奇作为四叉树却不是$O(\log_4 n)$，那是因为可能存在所有点的某一维全部相同的情况。
如果有所有点都一样的情况，会导致树的退化。解决办法就是剔除重复点，从而保证树高。

经过对随机分布的点的测试，四叉树的树高保持在$O(\log n)$：
![quadtree-height](http://git.oschina.net/riteme/blogimg/raw/master/quadtree/quadtree-average-height.png)

同时可以得知四叉树的空间复杂度为$\Theta(n)$，因为每个点都会被用一次。

## 查询与修改
在建立完树以后，进行查询或修改就十分简单了。许多操作可以借鉴线段树，因为每个节点都管理了一段区间。

这里以我们开始问题为例：我们需要查询一个矩形内有多少个点。
对于此，在考虑时只要判断三种情况：

* 查询的矩形与所管辖矩形相离：对答案没有贡献
* 所管辖矩形在查询的矩形之中：该所管辖的矩形内的点都会被算上
* 查询的矩形与所管辖矩形相交：首先计算自己在不在矩形中，然后分治到四个子平面，最中会变为第一和第二中情况

因此我们对于每个节点，只需统计其管辖范围内有多少个点即可。这一任务可以$\Theta(1)$完成，我们将其存入`x.count`。
整个算法的流程是十分清晰的。下面是查询的伪代码：

```
function QUERY(x, rect):  // x表示当前的节点，rect是查询的矩形
    if x =  nil:
        return 0
    if x.rectangle is out of rect:  // 在矩形外
        return 0
    if x.rectangle is in rect:  // 在矩形内
        return x.count
    else:  // 相交
        answer = QUERY(x.NE, rect) + QUERY(x.NW, rect) + QUERY(x.SE, rect) + QUERY(x.SW, rect)  // 分治
        
        if x.point in rect:  // 判断自己在不在矩形内
            return answer + 1
        else:
            return answer
```

实际上，我们不仅可以查询矩形中的点数，还可以计算各种范围内的点数！我们只需要修改所管辖的矩形与范围的关系的函数即可。

对于修改操作，也是一样的思路，只是将考虑贡献变为考虑影响即可。这里就不给出具体的做法了。

## 动态插入与删除
当然我们会希望能够动态插入点。事实上你可以离线所有的操作来预处理出将要插入的所有的点，然后建树，这样就避免的了动态操作的烦恼。
当然如果被强制在线了，我们也有解决办法，那就是利用替罪羊树[^scapegoat-tree]的思想。制定一个子树不平衡的标准，然后在不平衡的子树处利用`BUILD-QUADTREE`来重建。需要注意的是`BUILD-QUADTREE`的时间复杂度为$O(n\log n)$的，而不是$\Theta(n)$。因此均摊时间复杂度一般是$O(\log^2 n)$的。

[^scapegoat-tree]: [替罪羊树](https://en.wikipedia.org/wiki/Scapegoat_tree)

## 扩展至高维
作为平面上的划分树，它是需要四叉的。如果想利用同样的思想来应用到三维中，就会需要八叉树[^octtree]。
当然不足之处就是代码量会大幅度增加。因此这种树不太适合高维度的操作。
当然利用一些离线操作方法可以使数据的维度降低。我们可以通过排序使一维有序，同时也可以利用一类按时间分治的思想来对一维分治，这样就成功的降下两维。至此，在允许离线的情况下，四叉树可以轻松对付四维的数据。

[^octtree]: 具体参见[Octree](https://en.wikipedia.org/wiki/Octree)
