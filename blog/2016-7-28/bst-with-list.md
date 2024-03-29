---
title: 平衡树套链表
create: 2016.7.28
modified: 2016.7.28
tags: 数据结构
      平衡树
      链表
---

[TOC]
# 平衡树套链表
## 前言
> 这是一个闲得卵疼的产物

有时候我们希望能够在一个序列上快速遍历，然而这个序列却又是动态的，因此会考虑到平衡树来维护序列。
然而普通平衡树查找前趋后继是比较麻烦的，除了Splay有一个很简单直观的方法[^splay-way]，其它平衡树都要与父亲节点纠缠一番。
然而最关键的是，它们查询前趋后继还不是$\Theta(1)$的时间，最坏情况下是$O(\log n)$的。

[^splay-way]: 将当前节点Splay至根，然后就不用讨论父亲节点了。

因此考虑将链表"挂载"在平衡树上，可以将查找前趋后继的时间复杂度降为$\Theta(1)$，并且只需要在插入和删除时每个节点付出$\Theta(1)$的代价。同时顺序遍历节点的代码将与普通链表一样。这样在动态维护凸包等一些复杂的平衡树应用中做到一些优化。

想必强者[^sbk]看完前言已经脑补出这玩意了。

[^sbk]: [LinkSBK](http://link-arthur.github.io/)

## 插入
实际上我们就是需要在插入节点时同时记录一个节点的前趋和后继。
由于新插入的节点一定是在树的底部，因此我们需要考虑的情况很少。

这时有两种情况，一种是插入到左儿子：

![left-node](https://riteme.site/blogimg/bst-with-list/insert-1.png)

那么新插入的节点必定是其父亲的前趋。这个过程可以看作是往链表中插入一个元素。

同样，对于插入到右儿子，情况也是类似的：

![right-node](https://riteme.site/blogimg/bst-with-list/insert-2.png)

因此，对于每个新插入的节点，只需要花费$\Theta(1)$的时间来记录前趋后继。

## 旋转
许多平衡树 (Treap、Splay等) 都是以旋转操作来进行平衡的。然而平衡的时候是否要维护链表信息呢？
实际上根本不需要，因为旋转操作不会影响平衡树的有序性，所以对于每个节点而言，它的前趋后继是不会变化的，所以没有必要改动信息。

## 删除
有了前面的基础，删除操作其实很自然了。实际上就是最后要真正删除节点时，将链表上的指针重设。如果你写过链表的删除 (这东西很简单)，在平衡树上也就是一样的了。

## 应用
这个东西实际上只是一个小技巧，它可以用来简便一些代码，尤其是维护动态凸包这种要不停地向左向右访问节点的东西。如果我们使用的是循环链表，就可从任意一个节点开始循环遍历每一个节点。
