---
title: 2-3树与红黑树
create: 2016.3.12
modified: 2016.3.12
tags: 2-3树
      红黑树
      算法
      数据结构
---
[TOC]
# 2-3树与红黑树
## 概述
### 红黑树
红黑树[^red-black-tree-wiki]是一种平衡二叉树，其目标是为了优化二叉搜索树，防止极端情况下时间复杂度的退化。

![red-black-tree-wiki-pic](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-example.png)

[^red-black-tree-wiki]: 红黑树维基百科：<https://zh.wikipedia.org/zh-cn/%E7%BA%A2%E9%BB%91%E6%A0%91>

红黑树的背后原型其实是2-3树。因此我们将先了解什么是2-3树。

### 2-3树
2-3树[^2-3-tree-wiki]是一种阶为3的B树[^b-tree-wiki]，可以简单的理解为3叉树。2-3树最大的特点就是它一定是一棵完全3叉树，即除了叶节点外，其它的节点没有空儿子。

![2-3-tree](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-tree-example.png)

[^2-3-tree-wiki]: 2-3树（2-3-4树）维基百科：<https://zh.wikipedia.org/wiki/2-3-4%E6%A0%91>

[^b-tree-wiki]: B树维基百科：<https://zh.wikipedia.org/wiki/B%E6%A0%91>

接下来我们将探究2-3树的基本操作。之后再来观察2-3树与红黑树之间的联系。

## 2-3树？
### 树的表示
从之前给出的图中可以看出，2-3树的每个节点不一定只有一个键[^key]，同时儿子的数量也有不同。

[^key]: 键（Key）表示节点用于索引的值，同时也是确定节点在树中的位置的依据之一。

在2-3树中，共有两种节点。  
第一种是“2-节点”：

![2-node](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-2-node-example.png)

2-节点和普通的二叉查找树的节点没有什么不同。其左儿子表示比`a`小的子树，右儿子表示比`a`大的子树。

接下来是不一样的“3-节点”：

![3-node](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-3-node-example.png)

3-节点有两个键。最左边的儿子表示比`a`小的子树，**中间的儿子**表示大于`a`但小于`b`的子树，右边的儿子表示比`b`大的子树。

虽然这是2-3树，**呈现给我们看的树中是不存在“4-节点”的**。但是为了保持树的平衡性，我们将会利用4-节点来在插入和删除过程中保持树的完美平衡。下面是一个4-节点：

![4-node](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-4-node-example.png)

与3-节点类似，左边和右边的儿子分别表示小于`a`和大于`c`的子树。中间的两个儿子分别表示大于`a`且小于`b`的子树和大于`b`小于`c`的子树。

### 查询操作
2-3树具有和二叉查找树一样的有序性，使得查找操作和二叉查找树类似。  
我们先来看一棵2-3树：

![2-3-tree](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-tree-example.png)

使用和二叉查找树一样的方法，我们在向下递归这棵树的时候通过“打擂台”来确定查找的节点应该在哪棵子树中。

例如我们要查找`8`,首先和根节点`5`做比较，发现比`5`大，于是在其右子树中查找。  
接下来`7-9`这个3-节点中，我们先和`9`比较，发现比`9`小，于是**向左移一位**，与`7`比较，发现比`7`大，因此查找的节点应当在中间的子树中。  
继续深入下去，我们发现2-节点`8`就是我们要找的。

由于2-3树的完美平衡性质，因此所有查询操作均可在$ \Theta(\text{log}N) $的时间复杂度内完成。

那么问题来了，为什么2-3树具有完美平衡的性质？

### 插入操作
2-3树之所以完美平衡，关键在于插入时的维护。  
我们首先来看2-节点、3-节点以及4-节点之间如何转换。

#### 节点合并
当我们插入结点时，通常都是插入一个键，在2-3树中就是一个2-节点。  
与二叉查找树一样，我们将会在2-3树中找到一个合适位置来插入它，这个位置一定在**树的底部**。  
然而，在插入前，我们可以保证这棵2-3树是完美平衡的（空树也是如此）。在底部插入一个节点后，就会导致底部“多出”一个节点，导致2-3树不完美平衡。  
其解决方案就是把它与上面的节点相结合。  
与节点结合时，共有5种情况：

* 在一个**2-节点**的**左边**  
* 在一个**2-节点**的**右边**  
* 在一个**3-节点**的**左边**  
* 在一个**3-节点**的**中间**  
* 在一个**3-节点**的**右边**

嗯...这些情况很无聊，下面是它们的转换情况：

![2-3-tree-5-cases](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-tree-insert-5-cases.png)

合并的过程是很直观的，就是将2-节点放到了一个合适的地方。  
由于2-3树中不存在4-节点，因此不需要考虑与4-节点的合并。

#### 节点分裂
在上面的节点合并的操作中，我们发现**出现了4-节点**。然而4-节点是不能出现在最后的2-3树中的。  
因此我们需要将4-节点“肢解”，以确保这是一棵2-3树。  
通常情况下，一个4-节点可以分裂成3个2-节点：

![4-node-to-2-node](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-tree-4-node-to-2-node.png)

分裂的过程十分简单，只需要将4-叉节点从中间分开，并将中间的两个儿子分别重新接在`a`的右儿子和`c`的左儿子即可。  
但是4-节点是在插入时出现的，并且是出现在**树的底部**。我们发现这样一分裂就**导致高度加1**，直接导致树的不平衡。为了解决这个问题，我们**将`a`和`c`留在原处，把`b`向上传递，与父亲节点结合**。这样就可以避免高度的增加了。  
但是父亲节点可能是一个3-节点，**`b`向上结合时又会产生4-节点**！但是不必慌张，我们只需要**继续分解这个新生成的4-节点**即可。  
那么问题又来了，如果父亲节点是3-节点并且它是**树根**呢？

其实非常简单，我们依然可以分解4-节点，由于根节点没有父亲，因此向上传递的节点就没必要去结合了，此时**整棵树的高度加1**，保证了2-3树的完美平衡性。

#### 插入示例
下面是一个完整的插入示例，依次向一棵空的2-3树中插入`1`到`7`：

![2-3-tree-insert](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-tree-insert-example.png)

在插入节点中，找到其正确的位置需要访问$ \Theta(\text{log}N) $个节点。回溯向上调整2-3树时，每个节点处的调整时间为$ \Theta(1) $。因此，2-3树的插入操作的时间复杂度为$ \Theta(\text{log}N) $。

### 删除操作
可以看出，2-3树的插入操作是有点复杂的，然而删除操作更加麻烦。我们首先从简单的情况开始讨论。

首先，我们确定一点：**2-3树中的节点的儿子，要么都是空儿子，要么都不是空儿子**。  
原因非常简单，我们用反证法来证明：如果存在一个节点，它既有非空儿子，又有空儿子，那么非空儿子在树中所处的深度肯定大于父节点的深度，那么以这个节点为根的子树**不是完美平衡的**。又因为2-3树必须是完美平衡的，因此2-3树需要它所有的子树也是完美平衡的，故这样的节点是不存在的。  
并且可以看出，只有树的底部节点才会没有儿子。

由此，我们就可以方便的分情况讨论。

#### 删除底部节点
我们先考虑底部节点是因为这些节点不需要和它的儿子们“纠缠不清”，并且它也是我们后续删除算法的一个基础。  
首先考虑3-节点。从3-结点删除一个键非常简单，只需要将其变成一个2-节点就可以保证2-3树的完美平衡。然而删除一个2-节点就麻烦了，因为这会导致留下一个空位，而且没有合适的节点来填补它。

为了解决这个问题，我们考虑在删除之前能否将其变成一个3-节点。

答案是肯定的，我们可以通过从根节点开始的一系列变换来实现这一点。

为了在最后删除的时候的确是一个3-节点，我们必须确保在查找被删除的节点的路径上必须一直有3-节点。

假设我们在寻找待删除节点的路径上已经**处于一个3-节点处**，我们需要考虑如何保证下一步也是一个3-节点。首先，我们确定要向下递归的方向，如果在该方向上已经有一个3-节点，那么我们无需变换就可安全地递归向下。如果该方向上没有3-节点，我们就需要想办法变出一个3-节点。  
如何才能变出一个3-节点呢？一个很好的想法就是当我们有很多的节点时，我们就有很大的自由来分配这些节点。因此，我们将当前的3-节点中的一个键拿出来，和它的儿子”团聚”一下，然后确定如何“发配”这些“聚在一起”的节点。如果其中一个儿子是3-节点，那么聚合后就会**出现一个含有4个键的5-节点**！5-节点是绝对不能出现的！但是我们可以从中**取出两个键来构成一个3-节点**，剩下的两个键则用于调整局部平衡。这样就既不损害2-3树的完美平衡性，又能在希望的地方创建一个3-节点了。当然，你也可以理解成公然从左儿子或右儿子中“抢来”了一个键。  
但如果两个儿子中没有一个是3-节点，那么我们现在就只凑到了3个键，还不足以分解出3-节点。因此，我们索性将从当前节点的分离出来的键和儿子们**构成一个临时的4-节点**。没错，就是4-节点，在4-节点中删除一个键也是很容易的，并且如果不是从中删除键，我们也有办法在删除完指定的键之后的回溯过程中来**分解这个4-节点**，从而保证2-3树中不会出现不该出现的东西。

为了更清楚的说明上面这坨东西在讲什么，我放几张图解释一下：  
首先是可以从旁边“抢”节点的情况：

![2-3-tree-delete-1](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-tree-delete-1-2.png)

上图是准备向右递归之前的调整过程。首先取出`e`与它的儿子3-节点`c-d`和2-节点`f`结合生成了一个5-节点`c-d-e-f`，然后我们取出`e`和`f`在右边创建出一个3-节点，然后`d`代替原来3-节点`b-e`中`e`从而还原，然后被抢掉一个键的`c`就默默的留在原地...  
对于向左边和中间调整都是类似的做法。只是向中间递归的调整需要先判定是左边有3-节点还是右边有3-节点，从而确定被取出的键是谁。

如果这个键的儿子都是2-节点，我们从这个节点中取出一个键向下合并，却只能创造出一个临时的4-节点，无法从中提取出3-节点。因此我们将其留在那里当作是3-节点。这个4-节点等到我们删除完之后再来处理。如果要删除的键就在这个节点中，我们就不需要管了。如果这个4-节点依然保留着，只需分解它即可。下面是合并的过程：

![2-3-tree-delete-2](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-tree-delete-2.png)

但是，上面的做法都是在假设当前正处在一个3-节点处而做的。倘若根节点就不是3-节点，那该怎么办呢？

考虑到根节点的特殊性，我们可以直接将其和它的儿子合并为4-节点。

![2-3-tree-root-transformation](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/2-3-tree-root-trans-1.png)

如果根节点和它的左右儿子都是2-节点，那么我们可以直接将它和儿子们结合，变成一个3-节点。这样会导致树的局部的高度降低。然而这是在根节点处，所以这样的变化是全局性的，不会影响2-3树的完美平衡性。同时有保证向下变换时有充足的键可取。同理，这个遗留的4-节点可以日后再来将其分解掉。

这样，我们就能确保在删除操作必定是在3-节点内进行的了。于是我们完成了底部节点的删除操作。

#### 删除中间节点
然而，我们不一定会去删除底部节点，而是会删除树中央的一个节点。这样似乎问题变得很棘手。

然而我们可以将其转换为删除底部节点。我们模仿二叉搜索树的删除方式：当要被删除的节点有两个儿子时，用该节点的前趋或者后继节点来顶替它，并且将这个前趋或者后继节点删除。  
由于2-3树的非底部节点一定是有多个儿子的，因此，我们找到其后继节点，将这个后继节点的键和卫星数据[^remote-data]复制到要被删除的节点处，这样就实现了用后继节点来顶替原先节点的任务。因此我们就只需要将原来的后继节点删除即可。  
而一个节点的后继节点是它的右子树中的最小的节点，即右子树中最靠左的节点，因此它肯定没有儿子。所以我们可以使用删除底部节点的方法来删除它。

[^remote-data]: 卫星数据指存储在这个节点上的与树结构无关的数据，即这个节点的一些附加数据，例如假设每个节点表示一个人，那么性别、年龄、身高等就属于卫星数据。

#### 删除示例
为了使大家想得更明白，这里给出一个删除底部节点的示例。

首先，下面是一棵高度为4的2-3树，我们准备删除`i`：

![2-3-tree-delete-example-1](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-tree-delete-example-1.png)

从根节点开始，发现`i`在右子树中，但发现根节点自己和左右儿子都是2-节点，于是它们合并为一个4-节点：

![2-3-tree-delete-example-2](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-tree-delete-example-2.png)

接下来在新的4-节点`d-h-n`中发现右儿子为3-节点，于是直接向下搜索。

在3-节点`j-l`中我们发现`i`在其左子树中，并且左儿子不是3-节点，于是我们将`j`向下合并：

![2-3-tree-delete-example-3](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-tree-delete-example-3.png)

向下后来到4-节点`i-j-k`，发现目标`i`就在其中，我们直接将其删除：

![2-3-tree-delete-example-4](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-tree-delete-example-4.png)

删除完成，我们沿着递归向下的顺序向上回溯。回溯到根节点时，我们发现是一个4-节点，于是我们将其分解：

![2-3-tree-delete-example-5](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/23-tree-delete-example-5.png)

至此。删除操作就完成了。

对于所有的删除操作，2-3树需要$ \Theta(\text{log}N) $的时间查找节点，并且以$ \Theta(1) $的时间在每个回溯的节点处来作出适当的调整。故2-3树的删除操作是$ \Theta(\text{log}N) $的。

## 2-3树到红黑树
上面讲了那么多关于2-3树的操作，却从不提及其具体实现，是因为2-3树在实际中很少使用。  
由于其需要大量的节点变换（从2-节点到3-节点到4-节点甚至到5-节点...），这些变换在实际代码中是很复杂的。所以现在几乎没有2-3树的具体实现。  
但是由于2-3树的变化十分直观，因此前人在2-3树的理论基础上发明了红黑树。

### 变化到红黑树
红黑树是一种平衡二叉树，只有一种节点。这种节点有两个儿子，和2-3树中的2-节点对应。

![rbtree-normal-node](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-normal-node.png)

如何表示3-节点呢？我们尝试一种特殊的边：默认情况下节点的颜色均为黑色。我们将某个节点染为红色，表示它和父亲的的链接是红色的，就像下图：

![rbtree-red-node-1](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-red-node-normal.png)

当我们将红链接画平时...

![rbtree-red-node-2](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-red-node-flat.png)

我们发现它和2-3树中的3-节点极为类似！  
事实上，我们完全可以用这样的方式来表示2-3树中的3-节点。

下图是一棵典型的红黑树：

![rbtree-example-1](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-example-1.png)

如果将红链接画平，将得到一棵完美平衡的“2-3树”：

![rbtree-example-2](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-example-2.png)

从某种意义上来说，红黑树和2-3树是一种等同。

同时，为了我们的操作方便，我们对红黑树作出以下规定：

* **红黑树是二叉搜索树**。  
* **根节点必须为黑色**。毕竟根节点没有父亲。  
* **红链接必须在左侧**[^red-is-left]。将红链接统一在一个方向是为了方便其它操作。如果不统一，3-节点就有两种情况，4-节点就有5中情况，非常不利于我们判定当前是什么节点。并且，对于右边的红链接，我们可以通过二叉搜索树的旋转操作来将其变为左链接。具体的会在之后解释。  
* **不允许两个连续的红链接**。因为连续的连个红链接表示的是4-节点。当然，跟2-3树一样，插入/删除的过程中还是允许临时的4-节点。  
* **每一条树链上的黑色节点数量（称之为“黑高”）必须相等**。原因非常简单，一个黑色节点就对应着2-3树中的一个2-节点或3-节点，而2-3树是完美平衡的。  
* **空节点（NULL/None）为黑色**。这样方便将方便我们识别没有儿子的2-节点。

[^red-is-left]: 这是红黑树的一种实现。网络上有其它的实现，允许右儿子为红色。

### 查询操作
由于红黑树是二叉搜索树，因此查询操作就是二叉搜索树的查询操作。时间复杂度为$ \Theta(\text{log}N) $。

### 基本操作
在介绍红黑树的插入和删除操作前，首先介绍红黑树的一些基本操作。

#### 旋转
红黑树的旋转只有两种：顺时针旋转和逆时针旋转[^rotate-different]。  
红黑树的旋转操作是为了在保证二叉搜索树和红黑树的性质的前提下，来转换红链接的位置。  

![rbtree-rotate-1](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-rotate-1-2.png)

可以看出顺时针旋转就是将节点的左儿子提上来，将自己变做它的右儿子，将左儿子的右子树接到自己的左子树中，同时转变红链接。可以将其想象成把`4->2`这条边顺时针旋转了一下。逆时针旋转也是类似的做法。同时顺时针旋转和逆时针旋转可以视为一对逆操作，因为一次左旋和一次右旋可以变回原来的样子。

```python
# 顺时针旋转
def cw_rotate(h):
    assert h is not None and h.left is red  # h是非空节点并且左儿子为红色

    x = h.left
    h.left = x.right
    x.right = h
    x.color = h.color
    h.color = red
    
    return x  # 返回被提上来的左儿子

# 逆时针旋转
def ccw_rotate(h):
    assert h is not None and h.right is red  # h是非空节点并且左儿子为红色

    x = h.right
    h.right = x.left
    x.left = h
    x.color = h.color
    h.color = red
    
    return x  # 返回被提上来的左儿子

h = cw_rotate(h)  # 将h顺时针旋转
```

[^rotate-different]: 也称作左旋和右旋，但个人认为这样的名字晦涩并具有误导性，故使用顺时针旋转和逆时针旋转代替。

#### 反色
如同在2-3树中一样，红黑树要能够处理4-节点。  
对于4-节点，我们只有两种操作：合成一个4-节点和分解一个4-节点。

![rbtree-flip-1](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-flip-1.png)

对照一下2-3树，这个操作就显而易见了。

![rbtree-flip-2](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-flip-2-2.png)

也许你会注意到反色操作会将两个儿子的父节点变为红色，是因为在2-3树中，中间取出来的键要向上传递并结合进去。此外，反色操作会导致出现右边的红链接，然而这没有关系，因为4-节点是临时的，我们最终会通过逆时针旋转将其变为左边的红链接或者再次反色将这个4-节点分解。

```python
def flip_color(h):
    assert h.color is different from h.children.color  # h的颜色和它的儿子相反

    h.color = (h.color == RED ? BLACK : RED)
    h.left.color = (h.left.color == RED ? BLACK : RED)
    h.right.color = (h.right.color == RED ? BLACK : RED)

    return h

h = flip_color(h)  # 将h反色
```

### 插入操作
为了探究红黑树的插入操作，我们依然回到2-3树。在2-3树中，我们将新插入的节点与上面的节点合并，然后再做调整。为了表示合并，我们将**新插入的节点均设为红色**，表示与上面的节点相连接。  

然而插入后，新的红节点可能会违反我们的规定，因此需要在回溯的时候进行调整。

#### 情况一：调整右边的红链接
当我们发现某个节点的**左儿子是黑色**但**右儿子是红色**时，我们要将右边的红色链接转到左边来：

![rbtree-insert-1](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-insert-1.png)

如上图，通过对`b`**逆时针旋转**，完成了对红链接位置的纠正。  
这样做是为了方便接下来的操作。

#### 情况二：分解4-节点
在情况一中，我们要求节点的左儿子是黑色。这是因为当**左儿子和右儿子都是红色**时，就代表着一个4-节点，为此我们可以直接将其反色来分解它：

![rbtree-insert-2](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-insert-2.png)

如果该操作是在根节点上，那么整棵红黑树的黑高将会加1。

#### 情况三：连续的红色左儿子
在情况一中，我们能够把所有的右边的红色节点转到左边来，这样就好判断是否存在4-节点。除了情况二中的4-节点外，**连续的两个红色左儿子**也将表示一个4-节点：

![rbtree-insert-3](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-insert-3.png)

对此，我们的做法是将节点**顺时针旋转**，从而变为了情况二。

#### 平衡操作
上面介绍了三种插入时的情况，实际上已经将插入的所有情况都概括到了。接下来我们将实现一个平衡操作。这个平衡操作就是通过对节点的情况进行判定并作出调整。

```python
def balance(h):
    assert h is not None  # 当然不能为非空节点

    if h.right is red and h.left is not red:  # 情况一
        h = ccw_rotate(h)

    if h.left is red and h.left.left is red:  # 情况三
        h =.cw_rotate(h)

    if h.left is red and h.right is red:  # 情况二
        h = flip_color(h)

    return h  # 返回调整后的h节点
```

有了平衡操作后，我们就能直接改动一行二叉搜索树的插入代码，就能实现红黑树的插入了：

```python
def insert(h, key, value):
    # 二叉搜索树的插入实现
    
    # return h
    return balance(h)  # 插入后回溯的过程中，先平衡节点，再返回
```

这里需要注意一点，当所有操作完成以后，根节点可能变为红色，这是需要我们手动将根节点设置为黑色。  
由于`balance`操作是$ \Theta(1) $的时间复杂度，故红黑树的插入操作是$ \Theta(\text{log}N) $的时间复杂度。

### 删除操作
正如你所见，红黑树的插入写起来也并不是那么难。然而删除操作就未必。根据我们在2-3树中所讨论的，红黑树删除节点也要保证一路上都有一个3-节点或4-节点。

#### 红节点的转移
由于红黑树在向下递归的过程中只有向左边和向右两个方向，因此我们再弄两个操作：**红色左移**和**红色右移**。这两个操作用于在左儿子和右儿子处创造出一个3-节点或4-节点。

我们先讨论红色左移的情况，毕竟红色右移也是类似的做法。  
当我们要在左儿子处造一个3-节点时，首先肯定**左儿子不是3-节点**。那么按照2-3树的做法，我们要么是从右儿子借一个节点，要么就是把自己“献身”。

第一种情况是右儿子不是3-节点，我们直接在左儿子处创建4-节点：

![rbtree-delete-1](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-delete-1.png)

上面就是利用了**反色操作**。  
另一种情况是右儿子是一个3-节点，那么操作就有点复杂了：

![rbtree-delete-2](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-delete-2.png)

和2-3树一样，我们将`b`合并创建出一个5-节点。然后我们发现右儿子的左儿子是红色的，即右儿子为3-节点。为此，我们通过两次旋转操作将代替节点`b`的节点`c`旋转到曾经`b`的位置。最后我们分裂这个5-节点，此时左儿子已经是一个3-节点。

这样我们就能把红色左移给写出来了：

```python
def move_red_to_left(h):
    assert h is red and h.left is not red  # 左儿子必须为黑色，同时当前必须是红色

    h = flip_color(h)  # 与儿子节点结合

    if h.right.left is red:  # 如果右儿子为3-节点
        # 通过两次旋转将替代者上移至h处
        h.right = cw_rotate(h.right)
        h = ccw_rotate(h)
        
        h = flip_color(h)  # 分裂5-节点

    return h
```

同样红色右移也是一样的做法。先是节点结合，然后根据情况进行调整。

```python
def move_red_to_left(h):
    assert h is red and h.right is not red

    h = flip_color(h)

    if h.left.left is red:
        h = cw_rotate(h)  # h的左儿子就是替代者
        
        h = flip_color(h)

    return h
```

#### 处理根节点
和2-3树一样，根节点可能为2-节点。为了方便处理，我们可以把根节点也看作是一个3-节点：

![rbtree-root-1](http://git.oschina.net/riteme/blogimg/raw/master/rbtree-and-2-3-tree/rbtree-root-1-2.png)

上图中，`a`是真正的根节点，而$ \infty $是一个想象的节点，实际上不存在。这样根节点就变成了一个3-节点。  
并且，对于这个3-节点，无论红色左移和红色右移都不会关系到$ \infty $，因此这样不会导致问题。  
实际中，我们直接**将根节点设为红色即可**。当删除操作完成后，**再把根节点设为黑色**。

#### 真正的删除
解决了红色节点的转移的工作，删除操作也就变得清晰了。下面将介绍删除操作该如何进行。

红黑树的删除过程和二叉搜索树类似。首先都要在树中找到这个节点，然后再着手处理。  
对于红黑树，它的节点也是**要么都是空儿子，要么就没有空儿子**。

* **对于没有儿子的节点**，在保证向下递归的红色节点的变换完成之后，如果它是红节点，我们可以直接将其删除。如果不是红节点，那么它的左儿子必定是红色节点，因为我们保证它会在一个3-节点或4-节点中，并且我们的红色转移操作都是创建红链接在左的节点。这样我们可以直接将其**顺时针旋转**，使其**变为红色节点**，然后直接删除。  
* **对于有儿子的节点**，我们模仿二叉搜索树中的做法：在它的右子树中找到最小的节点来替代它的位置，然后在右子树中将这个节点删除即可。

下面是红黑树的删除操作的参考实现：

```python
# 获取后继节点
def min_node(h):
    assert h is not None

    if h.left is not None:  # 一直沿左链接寻找
        return min_node(h.left)
    else:
        return h

def delete(h, key):
    assert h is not None  # 确认不是一棵空树

    if key < h.key:  # 在左子树中
        if h.left is black and h.left.left is black:  # 如果左儿子不是3-节点
            h = move_red_to_left(h)

        h.left = delete(h.left, key)
    else:  # 在右子树中或已经找到
        if h.left is red:
            h = cw_rotate(h)  # 将左边的红链接变为右边的红链接

        if key == h.key and h.right is None:  # 如果已经查找到并且没有儿子
            del h  # 直接删除
            return None

        if h.right is black and h.right.left is black:  # 如果右儿子不是3-节点
            h = move_red_to_right(h)

        if key == h.key:  # 如果已经查找到但有儿子
            x = min_node(h.right)  # 找到后及节点

            # 交换键值和卫星数据
            h.key = x.key
            h.data = x.data

            h.right = delele(h.right, x.key)  # 在右子树中删除后继
        else:  # 如果没有命中，则继续往右边寻找
            h.right = delete(h.right, key)

    return balance(h)  # 完成删除后平衡当前的子树
```
