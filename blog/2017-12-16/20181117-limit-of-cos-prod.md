### 2018.11.17

#### 问题描述

已知 $\varphi$ 为任意实数，求：
$$
\lim_{n\rightarrow\infty} \prod_{k = 1}^n \cos{\varphi \over 2^k}
$$

#### 解决方案
首先你需要跳出 $\cos$ 的怪圈，想到 $\sin$ 的倍角公式：
$$
\sin x = 2\cos \frac{x}2 \sin \frac{x}2
$$

于是你发现可以继续展开下去，得到一堆 $\cos$ 相乘：
$$
\sin x = 2^n\cos \frac{x}2 \cos \frac{x}4 \cdots \cos \frac{x}{2^n} \sin \frac{x}{2^n}
$$

所以我们求的极限就是：
$$
\lim_{n\rightarrow\infty} \prod_{k = 1}^n \cos{\varphi \over 2^k} = \lim_{n\rightarrow\infty} {\sin \varphi \over 2^n \sin \frac{\varphi}{2^n}}
$$
当然上面这里要求 $\varphi/2^n \neq 0$。首先当 $n$ 足够大时，$|\varphi / 2^n| < \pi / 2$，这样就只剩 $\varphi = 0$ 的情况了。而若 $\varphi = 0$，原来那个极限等于 $1$，之后我们就默认其不为 $0$。由于 $\varphi / 2^n \rightarrow 0$，利用 $x \sim \sin x$ ($x \rightarrow 0$)，所以：
$$
\lim_{n\rightarrow\infty} {\sin \varphi \over 2^n \sin \frac{\varphi}{2^n}} = \lim_{n \rightarrow \infty} {\sin \varphi \over 2^n \frac{\varphi}{2^n}} = {\sin \varphi \over \varphi}
$$
