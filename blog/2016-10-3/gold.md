---
title: 无尽的黄金
create: 2016.10.3
modified: 2016.10.3
tags: Problems
---

[TOC]
# 无尽的黄金 (gold.cpp/in/out)
时间限制：2s / 空间限制：512MB / 打开`-O2`优化

## 题目描述
探险家Lunk发现了一个藏在大山深处的洞穴。经过五天五夜的探索，Lunk在洞中发现了一个非常神奇的地方。这里有一个不断生成黄金的小口，**每分钟**可以取出一个黄金，不然这个黄金就会**马上消失**。取出的黄金自然会变成Lunk的了。贪婪的资本家绝对不会错过这个发财的大好时机，Lunk想要取走大量的黄金。
然而在这旁边却立着一个牌子，上面写着：

> Hello, Lunk,
>
> 恭喜你，你非常机智地发现了这个奇妙的地方，我早已知道你到底想干什么。不如我们来玩个游戏，你可随意取走黄金，但是**任意连续**的$K$分钟内，你不可以取走过多的黄金，否则，你将找不到出去的路。
> 
> Best wishes
> <div style="text-align: right">XL</div>

这让Lunk感到十分害怕，它担心自己一不留神就会触犯的这个可怕的规则。但是贪婪的资本家是不会放弃的，Lunk想知道究竟有多少种取走黄金的方法（可以全都不取），使得自己不会葬身于山洞之中。
Lunk现在还有一些时间，希望你能够快速给出答案。

## 输入格式
每个数据仅一行，包含三个整数$T$，$K$和$C$。
$T$表示Lunk还剩下的时间，单位为分钟。
$K$和$C$表示Lunk在任意连续的$K$分钟内**至多**取走$C$个黄金。

## 输出格式
输出一行一个整数，表示Lunk取走黄金的方案数。由于答案可能非常大，所以请将答案对$1073741824$取模。

## 样例输入
```
2 2 2
```

## 样例输出
```
3
```

## 样例解释
只要Lunk不把所有黄金取走就好了，显然有三种取法。

## 数据限制
本题采用**捆绑测试**，共$10$个子任务，$20$个数据点。每个数据点分值为$5$分，每个子任务的分值为其所有数据点分值之和。
每个子任务和数据点约定如下：

<table width="100%" border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse;table-layout:fixed">
<tbody><tr height="18" style="height:13.50pt;">
    <th class="xl65" height="18" width="72" style="height:13.50pt;width:54.00pt;text-align: center" x:str=""><strong>子任务编号</strong></th>
    <th width="72" style="width:54.00pt;text-align: center" x:str=""><strong>数据编号</strong></th>
    <th width="72" style="width:54.00pt;text-align: center" x:str=""><strong>$T$的限制</strong></th>
    <th width="72" style="width:54.00pt;text-align: center" x:str=""><strong>$K$的限制</strong></th>
    <th width="72" style="width:54.00pt;text-align: center" x:str=""><strong>$C$的限制</strong></th>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td height="18" style="height:13.50pt;text-align: center;line-height:24px" x:num="">1</td>
    <td style="text-align: center" x:num="">1</td>
    <td style="text-align: center" x:str="">$\le 10^2$</td>
    <td style="text-align: center" x:str="">$= 2$</td>
    <td style="text-align: center" x:str="">$= 2$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td height="18" style="height:13.50pt;text-align: center;line-height:24px" x:num="">2</td>
    <td style="text-align: center" x:num="">2</td>
    <td style="text-align: center" x:str="">$\le 10^2$</td>
    <td style="text-align: center" x:str="">$= 3$</td>
    <td style="text-align: center" x:str="">$= 3$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td height="36" rowspan="2" style="height:27.00pt;border-right:none;border-bottom:none;text-align: center;line-height:64px" x:num="">3</td>
    <td style="text-align: center" x:num="">3</td>
    <td style="text-align: center" x:str="">$\le 10^2$</td>
    <td style="text-align: center" x:str="">$\le 5$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td style="text-align: center" x:num="">4</td>
    <td style="text-align: center" x:str="">$\le 10^2$</td>
    <td style="text-align: center" x:str="">$\le 5$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td height="36" rowspan="2" style="height:27.00pt;border-right:none;border-bottom:none;text-align: center;line-height:64px" x:num="">4</td>
    <td style="text-align: center" x:num="">5</td>
    <td style="text-align: center" x:str="">$\le 10^3$</td>
    <td style="text-align: center" x:str="">$\le 5$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td style="text-align: center" x:num="">6</td>
    <td style="text-align: center" x:str="">$\le 10^3$</td>
    <td style="text-align: center" x:str="">$\le 5$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td height="36" rowspan="2" style="height:27.00pt;border-right:none;border-bottom:none;text-align: center;line-height:64px" x:num="">5</td>
    <td style="text-align: center" x:num="">7</td>
    <td style="text-align: center" x:str="">$\le 10^5$</td>
    <td style="text-align: center" x:str="">$\le 5$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td style="text-align: center" x:num="">8</td>
    <td style="text-align: center" x:str="">$\le 10^5$</td>
    <td style="text-align: center" x:str="">$\le 5$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td height="36" rowspan="2" style="height:27.00pt;border-right:none;border-bottom:none;text-align: center;line-height:64px" x:num="">6</td>
    <td style="text-align: center" x:num="">9</td>
    <td style="text-align: center" x:str="">$\le 10^5$</td>
    <td style="text-align: center" x:str="">$\le 8$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td style="text-align: center" x:num="">10</td>
    <td style="text-align: center" x:str="">$\le 10^5$</td>
    <td style="text-align: center" x:str="">$\le 8$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td height="36" rowspan="2" style="height:27.00pt;border-right:none;border-bottom:none;text-align: center;line-height:64px" x:num="">7</td>
    <td style="text-align: center" x:num="">11</td>
    <td style="text-align: center" x:str="">$\le 10^9$</td>
    <td style="text-align: center" x:str="">$\le 5$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td style="text-align: center" x:num="">12</td>
    <td style="text-align: center" x:str="">$\le 10^9$</td>
    <td style="text-align: center" x:str="">$\le 5$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td height="36" rowspan="2" style="height:27.00pt;border-right:none;border-bottom:none;text-align: center;line-height:64px" x:num="">8</td>
    <td style="text-align: center" x:num="">13</td>
    <td style="text-align: center" x:str="">$\le 10^9$</td>
    <td style="text-align: center" x:str="">$\le 8$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td style="text-align: center" x:num="">14</td>
    <td style="text-align: center" x:str="">$\le 10^9$</td>
    <td style="text-align: center" x:str="">$\le 8$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td height="36" rowspan="2" align="center" style="height:27.00pt;border-right:none;border-bottom:none;text-align: center;line-height:64px" x:num="">9</td>
    <td style="text-align: center" x:num="">15</td>
    <td style="text-align: center" x:str="">$\le 10^{18}$</td>
    <td style="text-align: center" x:str="">$\le 5$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td style="text-align: center" x:num="">16</td>
    <td style="text-align: center" x:str="">$\le 10^{18}$</td>
    <td style="text-align: center" x:str="">$\le 5$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td height="72" rowspan="5" align="center" style="height:54.00pt;border-right:none;border-bottom:none;text-align: center;line-height:140px" x:num="">10</td>
    <td style="text-align: center" x:num="">17</td>
    <td style="text-align: center" x:str="">$\le 10^{18}$</td>
    <td style="text-align: center" x:str="">$\le 8$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td style="text-align: center" x:num="">18</td>
    <td style="text-align: center" x:str="">$\le 10^{18}$</td>
    <td style="text-align: center" x:str="">$\le 8$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td style="text-align: center" x:num="">19</td>
    <td style="text-align: center" x:str="">$\le 10^{18}$</td>
    <td style="text-align: center" x:str="">$\le 8$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
   <tr height="18" style="height:13.50pt;">
    <td style="text-align: center" x:num="">20</td>
    <td style="text-align: center" x:str="">$\le 10^{18}$</td>
    <td style="text-align: center" x:str="">$\le 8$</td>
    <td style="text-align: center" x:str="">$\le K$</td>
   </tr>
</tbody>
</table>
    
对于$100\%$的数据，均保证$1 \le T \le 10^{18}$，$1 \le K \le 8$，$0 \le C \le K$。
