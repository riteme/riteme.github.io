### 2018.1.13

#### 问题描述

求下面这个递推式的通项公式：
$$
\begin{aligned}
R(1) & = 4  \\
R(n + 1) & = 3R(n) + 2^{n-1}-4n ~~~~(\forall n > 1)
\end{aligned}
$$

#### 解决方案

这里主要是记录一下 Repertoire Method 这种方法，不过现在我还不知道该怎么翻译这个名称...

这个方法基于一个简单的观察：如果设
$$
\begin{aligned}
R(1) & = a \\
R(n + 1) & = 3R(n) + b\cdot 2^{n-1} + c\cdot  n + d
\end{aligned}
$$
我们会发现：
$$
\begin{aligned}
R(1) & = a \\
R(2) & = 3a + b + c + d \\
R(3) & = 9a + 5b + 5c + 4d \\
R(4) & = 27a + 19b + 18c + 13d \\
R(5) & = 81a + 65b + 58c + 40d \\
&\cdots
\end{aligned}
$$
可以猜测，$R(n)$ 的通项公式可以被写成以下形式：
$$
R(n) = a\cdot f(n) + b \cdot g(n) + c\cdot h(n) + d \cdot \varphi(n)
$$
其中 $f(n)$、$g(n)$、$h(n)$ 和 $\varphi(n)$ 都是关于 $n$ 的简单函数。运用数学归纳法，不难证明可以一直保持这种形式。

我们现在的目标就是求出这四个函数。接下来的步骤就比较投机了，我们可以猜测当 $a$、 $b$、$c$、$d$ 取不同值的时候 $R(n)$ 可能的形式，我们可以假设 $R(n) = 1$，尝试找出是否有对应的值。根据递推的等式，可以列出：
$$
\begin{cases}
1 = a \\
1 = 3 \times 1 + b \cdot 2^{n-1} + c\cdot n + d
\end{cases}
$$
不难发现：$a = 1$ 以及 $d = -2$，其余两个变量只能为 $0$。回代到 $R(n)$ 的通项公式中：
$$
R(n) = f(n) - 2\varphi(n) = 1
$$
我们明白，如果能按照类似的方式找到 $4$ 个这样的方程，我们就可以把四个函数全部都解出来。现在继续尝试一些其它的函数。考虑到递推式中有 $n$ 这种东西，可以尝试当 $R(n) = n$ 时的情况：
$$
\begin{cases}
0 = a \\
n + 1 = 3n + b \cdot 2^{n-1} + c\cdot n + d
\end{cases}
$$
可以解出 $a = 1,\;c = -2,\;d = 1$。因此 $f(n) - 2h(n) + \varphi(n) = n$。

根据同样的想法，尝试一下 $R(n) = 2^n$：
$$
\begin{cases}
2 = a \\
2^{n+1} = 3 \times 2^n + b \cdot 2^{n-1} + c\cdot n + d
\end{cases}
$$
此时 $a = 2,\;b = -2$，同时我们有 $f(n) - g(n) = 2^{n-1}$。

此外注意到第二个递推式中 $R(n)$ 前的系数是 $3$，说明通项公式中应该是有 $3^n$ 这种东西的。于是尝试 $R(n) = 3^n$：
$$
\begin{cases}
3 = a \\
3^{n + 1} = 3^{n+1} + b \cdot 2^{n-1} + c\cdot n + d
\end{cases}
$$
So easy, $a = 3$，并且可以直接知道 $f(n) = 3^{n - 1}$。

现在 $4$ 个方程集齐了，只需要解下面这个方程组：
$$
\left\{
\begin{aligned}
f(n) - 2\varphi(n) & = 1 \\
f(n) - 2h(n) + \varphi(n) & = n \\
f(n) - g(n) &= 2^{n-1} \\
f(n) & = 3^{n - 1}
\end{aligned}
\right.
$$
不难解出：
$$
\left\{
\begin{aligned}
f (n) & = 3^{n - 1} \\
g(n) & = 3^{n-1} - 2^{n - 1}\\
h(n) & = \frac14 3^n - \frac12 n - \frac14 \\
\varphi(n) & = \frac12 3^{n - 1} - \frac12
\end{aligned}
\right.
$$
现在来解决原问题。原问题中，$a = 4,\;b = 1,\;c = -4,\;d = 0$，所以 $R(n) = 4f(n) + g(n) - 4h(n) = 2\times 3^{n-1} - 2^{n-1}+2n+1$。纵观整个过程，Repertoire Method 并不简单，甚至有点繁琐，但仍不失为探究问题的一种好思路。