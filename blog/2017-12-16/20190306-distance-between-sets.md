### 2019.3.6
#### 问题描述
在 $n$ 维 Euclidean 空间 $\mathbb R^n$ 上，定义一个点 $x$ 到一个点集 $A$ 之间的距离 $\lambda(x,\ A)$ 为：

$$
\lambda(x,\ A) = \inf\{|x - y|:\ y \in A\}
$$

类似的，对于 $\mathbb R^n$ 中的两个点集 $A$ 和 $B$，定义两个集合间的距离 $\lambda(A,\ B)$ 为：

$$
\lambda(A,\ B) = \inf\{|x - y|:\ x \in A,\ y \in B\} = \inf\{\lambda(x,\ B):\ x \in A\}
$$

考虑当 $A$ 与 $B$ 有交集时，显然 $\lambda(A,\ B) = 0$；现假设 $A \cap B = \varnothing$：

(1) 此时 $\lambda(A,\ B)$ 是否恒大于 $0$?

(2) 若 $A$、$B$ 均为闭集，则 $\lambda(A,\ B)$ 是否恒大于 $0$？

(3) 若 $A$ 为紧集，$B$ 为闭集，则 $\lambda(A,\ B)$ 是否恒大于 $0$？

#### 解决方案
(1) 两个开区间 $(1,\ 2)$ 和 $(2,\ 3)$ 不相交，但是取 $x_k → 2^-$ 和 $y_k → 2^+$ 得到 $|x_k - y_k| → 0$。

(2) 在 (1) 中因为开集不包含自己的聚点，因此只要有公共聚点，就会导致集合间的距离可以无限靠近。然而即使要求没有公共聚点，集合间的距离依然可以无限靠近，毕竟集合间在无限远处的行为没有限定。在实数轴上可能难以想象反例，不过在二维 Euclidean 空间中，考虑 $A = \{(x,\ y):\ y \geqslant 1/x,\ x > 0\}$ 和 $B = \{(x,\ y):\ y \leqslant -1/x,\ x > 0\}$，当 $x → +\infin$ 时两个集合的边界不断靠近，不难得出这两个集合间的距离为 $0$。

在实数轴上也有反例。首先回顾一下：**离散集也是闭集**。这样一来，令 $A = \mathbb Z$，$B = \{n + 1/n:\ n \in \mathbb Z\}$，当 $n → +\infin$ 时可以看出 $A$、$B$ 间的距离为 $0$。

(3) 更进一步，当我们限定 $A$ 为有界闭集时，等价于当 $A$ 是紧集时，以上两个漏洞就钻不了啦，此时可以证明 $\lambda(A,\ B) > 0$。

如果从紧集的开覆盖定义出发，我们会联想到闭集的补集是开集，这样这条路就通了。考虑 $B$ 的补集 $\complement B$：对任意 $\complement B$ 中的点 $x$，总存在 $\delta(x) > 0$，满足以 $x$ 为圆心，半径为 $\delta(x)$ 的开邻域 $\mathcal O(x,\ \delta(x))$ 完全在 $B$ 之外。于是构造 $\mathcal C = \{\mathcal O(x,\ \delta(x) / 2):\ x \in \complement B\}$ 为 $\complement B$ 的一个开覆盖。这里半径减半是为了方便之后留出 $A$ 与 $B$ 之间的间距做的准备。由于 $A \cap B = \varnothing$，所以 $A \subset \complement B$，故 $\mathcal C$ 也是 $A$ 的开覆盖，因此存在一个有限子覆盖 $C$。取 $\delta = \min\{\delta(x):\ \mathcal O(x,\ \delta(x)/2) \in C\}$，考虑任意 $A$ 中的点 $y$，总存在开邻域 $\mathcal O(x,\ \delta(x)/2) \in C$ 盖住了 $y$，那么显然 $\mathcal O(y,\ \delta(x)/2) \subset \mathcal O(x,\ \delta(x))$，而后者与 $B$ 无交集，故 $\lambda(y,\ B) \geqslant \delta(x)/2 \geqslant \delta/2$，因此有 $\lambda(A,\ B) = \inf\{\lambda(y,\ B):\ y \in A\} \geqslant \delta/2 > 0$。

直接用紧集的定义给人一种强行证明的感觉。实际上，我们还可以从连续函数的角度出发，那就是考虑 $A \mapsto \mathbb R$ 的多元函数 $f(x) = \lambda(x,\ B)$。我们知道紧集上的连续函数必能取到最值，假如 $\xi \in A$ 是最小值点，则 $f(x) \geqslant f(\xi) = \lambda(\xi,\ B) > 0$，直接就完成了证明。连续意味着当两个点无限接近时，函数值也会无限逼近。因此，考虑 $A$ 中的两个点 $x_1$、$x_2$：

![](https://gitee.com/riteme/blogimg/raw/master/math-problems/20190306-1.svg)

<center class="figcaption">在 $\mathbb R^2$ 中的距离示意图</center>

如上图，考虑取 $B$ 中任意一点 $P$，那么有 $f(x_1) \leqslant |x_1 - P|$ 以及 $f(x_2) \leqslant |x_2 - P|$，此时将两个函数值与两条边关联起来了。在 $\triangle Px_1x_2$ 中：

$$
|x_1 - x_2| \geqslant \big||x_1 - P| - |x_2 - P|\big|
$$

对不等式两边同时枚举 $P \in B$ 求下确界，得到：

$$
|x_1 - x_2| \geqslant \left|\inf_{P \in B}|x_1 - P| - \inf_{P \in B}|x_2 - P|\right| = |f(x_1) - f(x_2)|
$$

因此 $f(x)$ 满足 Lipschitz 连续条件，故 $f(x)$ 连续。