---
title: 秩平衡树(Rank Balanced Tree)
create: 2016.4.10
modified: 2016.4.11
tags: 数据结构
      平衡二叉树
      Rank-Tree
      Treap
      Splay
      并查集
      贼爷我真的错了
---
[TOC]
# 秩平衡树(Rank Balanced Tree)
> riteme: “这是并查集和Treap的杂交品种。”  
> tplink: “贼式二叉树！”  
> ruanxz: “ZY！”

## 1 秩
### 1.1 树的秩高
这里先介绍**"秩"**的概念。我们定义一棵**二叉树**的秩为从为**从根节点开始**到**其叶节点**中**最长的一条树链**上结点的个数。  
对于空结点$nil$，它的秩为$0$。
$$ nil.\text{rank} = 0 \tag{1.1} $$

那么对于任意非空节点$x$，它的秩可以如下定义：
$$ x.\text{rank} = \max\{x.\text{left}.\text{rank}, x.\text{right}.\text{rank}\} + 1 \tag{1.2}$$

树的秩我们使用`UPDATE`函数来维护：

```
function UPDATE(h):
    h.rank = max(h.left.rank, h.right.rank) + 1
```

现在我们来看一棵二叉搜索树。

![tree-example](http://git.oschina.net/riteme/blogimg/raw/master/rank-tree/binary-tree.png)

上图中，`a`的秩为$1$，`e`的秩为$2$，`c`的秩为$3$，根节点`j`的秩为$6$。

### 1.2 按秩合并
在并查集的优化方法中有一个是**启发式按秩合并**。做法是将秩小的树接在秩大的树下面，这样就可以尽可能避免树的高度的暴涨。同样，在秩平衡树中，也要利用到这种思想。

## 2 旋转
众所周知，二叉搜索树的旋转操作可以保持树的有序性，同时可以通过旋转的组合来实现许多操作。因此我们先实现左旋(`LEFT-ROATE`)和右旋(`RIGHT-ROTATE`)。  
左旋是将左子树旋转上来顶替自己的位置，右旋类似。  
旋转时要确保左子树或右子树不是$nil$。

```
function LEFT-ROTATE(h):
    ASSERT h.left != nil
    
    x = h.left
    h.left = x.right
    x.right = h
    
    UPDATE(h)
    UPDATE(x)
    
    return x  // 使用左子树来替代原来的节点

function RIGHT-ROTATE(h):
    ASSERT h.right != nil
    
    x = h.right
    h.right = x.left
    x.left = h
    
    UPDATE(h)
    UPDATE(x)
    
    return x  // 使用右子树来替代原来的节点
```

例如，要对节点`x`进行左旋转时，我们这样调用：

```
x = LEFT-ROTATE(x)
```

## 3 普通秩平衡树
> P: 并查集 x Treap  
> -> F1: “贼式二叉树”

秩平衡树的样子与二叉搜索树并没有什么区别。  
普通的秩平衡树的实现非常简单。它将利用秩的信息来使树保持平衡。

### 3.1 查询
查询中没有对树的形状的修改，因此什么特殊的操作都不要。  
故查询操作和普通的二叉搜索树是一样的。

```
function QUERY(h, key):
    if h = nil:
        return nil  // 没有查找到
    
    if key < h.key:
        return QUERY(h.left, key)  // 结果在左子树中
    else if key > h.key:
        return QUERY(h.right, key)  // 结果在右子树中
    else:
        return h  // 命中节点
```

### 3.2 平衡
准确的说，这个操作并**不能维护平衡**，而只是能使树向平衡的方向发展。  
进行平衡的依据就是**树的秩**。当左右子树的秩差距太大，我们就要采取行动来使其减小差距。

首先我们设定一个秩的差距的最大容忍值$t$。这个值是一个正整数，并且值选取的愈小树就会变得愈平衡。当$t=1$时，秩平衡树大多数情况下就是完全平衡的二叉树。  
在普通的秩平衡树中，我们一般选定为$1$：

```
TOLERANCE = 1
```

设定这个值的意义在于定义了平衡的触发标准。如果左右子树的秩的差距大于$t$，那么就要减小差距。  
减小差距的方法就是将树根通过旋转的方式进入秩较小的子树中，这样使得秩较小的子树的秩增加，秩较大的子树的秩减小。  
于是我们得到了一个大致的平衡代码：

```
function BALANCE(h):
    if h.left.rank > h.right.rank and
       h.left.rank - h.right.rank > TOLERANCE:   // 左子树的秩过大
        h = LEFT-ROTATE(h)
    else if h.left.rank < h.right.rank and
            h.right.rank - h.left.rank > TOLERANCE:   // 右子树的秩过大
        h = RIGHT-ROTATE(h)
    
    UPDATE(h)  // 更新节点
    return h  // 返回调整后的节点
```

实际上，这样还不足够。

考虑下面的情况：

![balance-situation-1](http://git.oschina.net/riteme/blogimg/raw/master/rank-tree/rank-tree-balance-1.png)

现在我们要平衡`b`节点。左子树的秩比右子树大。倘若按照上面的方法进行调整，将会得到下面的结果：

![balance-situation-2](http://git.oschina.net/riteme/blogimg/raw/master/rank-tree/rank-tree-balance-2.png)

呃...你会发现并没有什么变化。  
其原因在于左子树的右儿子的秩太大，导致旋转过去之后没有太大效果。  
这样导致中间的子树的**深度下移一位**。加之它本来就秩比较大，如此一来这个平衡就毫无作用。  
然而，如果左子树的连个儿子如果秩是一样的，就不会有太大的影响，因为这样就只会导致秩的差距为$1$。倘若右儿子的秩更小，就不会有这样的问题。

为了解决这个问题，我们考虑使左子树右儿子的秩**减小**，这样就不会因为中间的子树而导致无用的平衡。

首先我们将左子树的右儿子通过**右旋**上移，这样使得右儿子的秩减小：

![balance-situation-3](http://git.oschina.net/riteme/blogimg/raw/master/rank-tree/rank-tree-balance-3.png)

然后再进行**左旋**操作，完成平衡：

![balance-situation-4](http://git.oschina.net/riteme/blogimg/raw/master/rank-tree/rank-tree-balance-4.png)

这时左右子树的秩的差距就减小了。

同样，对于右子树的平衡操作也是类似的处理方法。这里就不再多说。具体的可以参考实现伪代码。

完整的平衡代码如下：

```
function BALANCE(h):
    if h.left.rank > h.right.rank and
       h.left.rank - h.right.rank > TOLERANCE:   // 左子树的秩较大
        if h.left.right.rank > h.left.left.rank:  // 如果左子树的右儿子的秩较大
            h.left = RIGHT-ROTATE(h.left)

        h = LEFT-ROTATE(h)
    else
    if h.left.rank < h.right.rank and
       h.right.rank - h.left.rank > TOLERANCE:   // 右子树的秩较大
        if h.right.left.rank > h.right.right.rank:  // 如果右子树的左儿子的秩较大
            h.right = LEFT-ROTATE(h.right)

        h = RIGHT-ROTATE(h)
    
    UPDATE(h)  // 更新节点
    return h  // 返回调整后的节点
```

这个平衡操作运用到了类似于并查集中“路径压缩”的思想。在并查集中可以直接全部接在根节点处，从而极大的提高了效率。但限于二叉树的性质，平衡操作只能使每个节点的秩尽可能的小。

### 3.3 插入
插入与普通的二叉搜索树差不多，只是在最后回溯的时候维护树的平衡。  
因此我们可以很快的写出插入操作：

```
function INSERT(h, key):
    if h = nil:
        return new node with key
        
    if key < h.key:
        h.left = INSERT(h.left, key)
    else if key > h.key:
        h.right = INSERT(h.right, key)
    
    return BALANCE(h)  // 最后要进行平衡
```

### 3.4 删除
与插入类似，删除的代码和二叉搜索树的保持一致，只要最后记得进行平衡即可。  
这里我们采用将被删除节点下沉的方法来进行删除：

```
function REAL-REMOVE(h):  // 删除指定的节点
    if h.left != nil and h.right != nil:
        // 如果有两个非空子树就继续下沉
        // 尽量往秩小的子树中下沉，同时将另一棵子树的秩尽量减小
        // 从而达到平衡的目的
        if h.left.rank > h.right.rank:
            h = LEFT-ROTATE(h)
            h.right = REAL-REMOVE(h->right)
        else:
            h = RIGHT-ROTATE(h)
            h.left = REAL-REMOVE(h->left)
    else:
        // 如果只有一个子树，就可以直接删除，将唯一的子树顶替自己的位置
        // 如果没有子树，说明是叶节点，返回nil
        next = nil
        if h.left != nil:
            next = h.left
        else:
            next = h.right
        
        delete h  // 删除
        return next

    return BALANCE(h)

function REMOVE(h, key):
    if key < h.key:
        h.left = REMOVE(h.left, key)
    else if key > h.key:
        h.right = REMOVE(h.right, key)
    else:
        return REAL-REMOVE(h)  // 找到指定的节点后进行删除

    return BALANCE(h)
```

### 3.5 时间复杂度
如果$t$选取得当，秩平衡树将是非常平衡的。因此操作都是$O(\log n)$的：

| 操作   | 时间复杂度            |
|:------:|:---------------------:|
| 平衡   | $\Theta(1)$           |
| 查询   | $O(\log n)$           |
| 插入   | $O(\log n)$           |
| 删除   | $O(\log n)$           |

在实际效率上，秩平衡树比Treap略快，与伸展树相比常数稍大一些。在查询操作很多的时候，秩平衡树比较占优势。

## 4 可合并秩平衡树
> F1: “贼式二叉树” x 可持久化Treap  
> -> F2: “可合并秩平衡树”

如果只是一棵单纯BST，未免太过无聊......  
现在各种BST都玩出花出来了，然而在这之中支持区间操作的BST却非常少。据我所知还只有**可持久化Treap**和**伸展树**。  
那秩平衡树能不能也支持区间操作呢？

一种思路是类似于伸展树的做法：将区间变为开区间，然后将区间的两个端点上浮，然后就可以截取区间了。秩平衡树可以进行上浮，上浮时不考虑树的平衡。当区间用完后，再将上浮的顶点依次下沉，同时维护平衡，这样就可以实现区间操作。  
事实上，如果这样进行处理，有着诸多的缺点：

* 又要增加上浮和下沉操作，并且这两个操作并不简单，**代码量**急剧增长。  
* 如果有**懒惰标记**之类的东西，难以正确处理。  
* **常数**变大，尽管理论上时间复杂度都是$O(\log n)$。

但是...又不是不能写，毕竟我是写过的，所以我才会知道这些。  
这样写出来的秩平衡树能比可持久化Treap快，但与伸展树相比差距较大。

另一种思路就是类似于可持久化Treap的做法：将树从第$k$小的位置拆开，然后又合并......  
可合并秩平衡树就是这种做法。

接下来我们会继续用到秩平衡树的`BALANCE`操作，同时将增加两个基本操作：`SPLIT`和`MERGE`，表示拆分和合并。以及一个辅助操作`RANK`[^rank]来查找第$k$小的节点，这样我们就可以利用这些操作来实现各种各样的操作。

[^rank]: 这里的英文解释为“排名”，不是秩。

### 4.1 拆分
拆分操作是将树从第$k$小的节点处拆成$[1, k]$和$[k+1, n]$的两棵子树。  
因为需要计算排名，所以每个节点都要记录一个$\text{size}$，表示子树中节点的个数，即子树的大小。同样，空节点的大小为$0$：
$$ nil.\text{size} = 0 \tag{4.1} $$

对于每个节点$x$，它的大小定义如下：
$$ x.\text{size} = x.\text{left}.\text{size} + x.\text{right}.\text{size} + 1 \tag{4.2} $$

此时我们将在`UPDATE`函数中维护树的大小：

```
function UPDATE(h):
    h.size = h.left.size + h.right.size + 1
    h.rank = max(h.left.rank, h.right.rank) + 1
```

拆分操作时先沿着寻找第$k$小的树链不断的将树切开，然后在回溯的时候进行拼装。这是一个递归的过程。  
假设我们在对子树$x$进行拆分，我们考虑下面两种情况：

* 如果$k \le x.\text{left}.\text{size}$，那么说明第$k$小的节点**在左子树中**，因此只需要将左子树拆开，拆开后的左边是$[1, k]$的子树，右边是大于$k$的子树。  
* 如果$k \ge x.\text{left}.\text{size}$，那么说明左子树**完全小于$k$**，**子树的根必定不大于$k$**，因此可以确定左子树和树根都在$[1,k]$的范围内。但我们不确定右子树中是否有在这个范围内的。如果有，则它在右子树中的排名为$k-x.\text{left}.\text{size} - 1$，因此我们将右子树按照这个值进行拆分，那么**拆开的左边属于$[1,k]$**。

这个过程非常简单，代码实现也是如此：

```
function SPLIT(h, k):
    if h = nil:
        return (nil, nil)  // 如果是空树，那么不需要拆分
    
    if k <= h.left.size:  // 情况1
        a, b = SPLIT(h.left, k)  // 拆分左子树
        h.left = b               // b不属于[1, k]
        UPDATE(h)
        
        return (a, h)
    else:                 // 情况2
        a, b = SPLIT(h.right, k - h.left.size - 1)  // 拆分右子树
        h.right = a                                 // a属于[1, k]
        UPDATE(h)
        
        return (h, b)
```

### 4.2 合并
之前我们把树给拆开了，用完了当然还要还回去，因此我们必然需要合并操作。  
同时我们注意到，拆分时我们并**没有维护平衡**，因此平衡的重任就交给了合并。

进行合并时，我们必须保证合并的左子树必须**完全小于**合并的右子树，即左子树的最大值必须小于右子树的最小值。  
合并时要遵循按秩合并的思想，始终选取秩较大的子树作为树根。然后将另一棵子树与树根的对应儿子继续进行合并。  
这是一个递归向下的过程。在回溯的时候，使用`BALANCE`操作进行平衡。  
如果我们在合并两棵子树$a$和$b$，其中$a$完全小于$b$。由于二叉搜索树的有序性，合并只会出现两种情况：

* $a$作为树根，$a.\text{right}$与$b$继续合并。  
* $b$作为树根，$a$和$b.\text{left}$继续合并。

作为特例，如果$a$和$b$中有一个是空树，那么就没有必要合并了。

合并的伪代码如下：

```
function MERGE(a, b):
    if a = nil:
        return b
    if b = nil:
        return a
    
    ASSERT max(a) < min(b)  // a < b
    if a.rank > b.rank:  // 按秩合并
        a.right = MERGE(a.right, b)
        UPDATE(a)
        
        return BALANCE(a)  // 最后进行平衡
    else:
        b.left = MERGE(a, b.left)
        UPDATE(b)
        
        return BALANCE(b)
```

### 4.3 排名
由于`SPLIT`操作需要排名$k$，而一般的调用是给定节点的键，因此我们需要一个能将节点在树中的排名计算出来的算法。  
因此`RANK`操作也成为了非常重要的操作之一。

利用节点储存的子树大小值，我们可以快速算出一个节点的排名。

这个操作也是一个递归操作的过程：

* 如果指定的节点在**左子树**，我们直接在左子树中继续查询。  
* 如果指定的节点在**右子树**，我们查询它在右子树中的排名，然后加上左子树和树根的大小。  
* 如果**直接命中**，那么直接计算排名，其排名为左子树的大小加$1$。  
* 对于没有命中的空节点，排名的意义在于查询一个新节点插入树后的排名。为此，对于空节点，我们视为它的排名为$1$。

根据上面的讨论，我们可以写出查询排名的操作：

```
function RANK(h, key):
    if h = nil:
        return 1
    
    if key < h.key:
        return RANK(h.left, key)
    else if key > h.key:
        return RANK(h.right, key) + h.left.size + 1
    else:
        return h.left.size + 1
```

当然，我们希望这个操作越快越好。现代绝大部分的语言的编译器/解释器...都能够对尾递归进行优化。上面的`RANK`操作可以被我们改为尾递归，从而充分利用优化的优势：

```
function RANK(h, key, offest = 0):  // 利用offest进行尾递归优化
    if h = nil:
        return 1 + offest
    
    if key < h.key:
        return RANK(h.left, key, offest)
    else if key > h.key:
        return RANK(h.right, key, offest + h.left.size + 1)
    else:
        return h.left.size + 1 + offest
```

如果没有优化，也没有关系，因为能尾递归的函数，基本上都可以写成迭代的形式：

```
function RANK(h, key):
    offest = 0
    
    while h != nil:                          // 向左走
        if key < h.key:
            h = h.left
        else if key > h.key:                 // 向右走
            offest += h.left.size + 1
            h = h.right
        else:
            return h.left.size + 1 + offest  // 直接命中
    
    return offest + 1  // 最后没有命中
```

### 4.4 时间复杂度
显然时间复杂度是我们最关心的。通过`BALANCE`操作，秩平衡树在合并过程中能够维持很好的平衡。  
因此对于所有的操作，递归深度不会超过$O(\log n)$。因此时间复杂度都是$O(\log n)$的。

| 操作   | 时间复杂度            |
|:------:|:---------------------:|
| 拆分   | $O(\log n)$           |
| 合并   | $O(\log n)$           |
| 排名   | $O(\log n)$           |

### 4.5 衍生操作
有了`SPLIT`、`MERGE`和`RANK`三大利器，我们就可以随心所欲的进行各种操作了。下面将对一些操作进行说明，大家可以在此基础上开发更多操作。

#### 4.5.1 查询
这个实际上没有必要动用拆分和合并，直接查就好。

#### 4.5.2 插入
设要插入的节点的排名为$k$，那么先将树拆分为$[1, k-1]$和$[k, n]$两部分，然后依次合并。

```
function INSERT(h, key):
    x = new node with key
    
    k = RANK(h, key)
    a, b = SPLIT(h, k - 1)
    
    return MERGE(MERGE(a, x), b)
```

#### 4.5.3 删除
设要删除的节点的排名为$k$，那么将树拆分为$[1,k-1]$、$[k+1,n]$和被删除的节点三部分，然后只将左右合并即可。

```
function REMOVE(h, key):
    k = RANK(h, key)
    a1, a2 = SPLIT(h, k - 1)
    b1, b2 = SPLIT(a2, 1)
    
    delete b1  // 删除节点
    
    return MERGE(a1, b2)
```

#### 4.5.4 第k小
直接拆就好了。

```
function KTH(h, k):
    a1, a2 = SPLIT(h, k - 1)
    b1, b2 = SPLIT(a2, 1)
    
    MERGE(a1, MERGE(b1, b2))
    return b1
```

#### 4.5.5 截取区间
这才是区间操作的关键吧...  
但是我们只要拆拆合合就搞定了...  
最后要记得合并就好了。

```
function SLICE(h, left, right):
    a1, a2 = SPLIT(h, left - 1)
    b1, b2 = SPLIT(a2, right - left + 1)
    
    return b1
```

### 4.6 总结
在实际的测试中，秩平衡树的表现非常不错，比可持久化Treap快了很多，并且在区间操作上能和伸展树不相上下。  
但是，与可持久化Treap相比，因为依赖于`BALANCE`操作，所以就**无法进行可持久化**了。

最后我们重新来考虑$t$这个容忍值的选取。在之前普通的秩平衡树中，我们认为$1$是最好的。而现在就未必。如果数据完全随机，我们其实并不需要平衡。但这样在极端数据的情况下，不平衡容易退化为一条链。但是过多的平衡会影响常数。因此，$t$可以稍微取大一点，但不能太大。一般情况下，最好选择$2$到$6$中的值。
