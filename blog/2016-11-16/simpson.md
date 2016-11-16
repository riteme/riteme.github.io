---
title: 辛普森积分法
create: 2016.11.16
modified: 2016.11.16
tags: 辛普森积分法
---

[TOC]
# 辛普森积分法
辛普森积分法是一种快速求函数定积分的方法。与普通的直线拟合方法相比，辛普森积分法采用的是二次函数来拟合函数，而效果十分显著。

## 用抛物线拟合
假设我们有三个不重合的点，那么可以唯一确定一个抛物线经过这三个点。如下图所示：

![quadratic](http://git.oschina.net/riteme/blogimg/raw/master/simpson/simpson1.svg)

辛普森积分法就是在积分区间$[a,\;b]$上去三个点$a$、$b$和$m = (a + b) / 2$，计算其原函数的在此处的值，然后用抛物线来拟合原函数，即使用该二次函数的积分值代替原函数的积分值，达到近似积分的效果。

如何计算这个二次函数？我们自然可以解三元三次方程组，但更方便的方法是拉格朗日差值公式：
$$
g(x) = {(x - m)(x - b) \over (a - m)(a - b)}f(a) + {(x - a)(a - b) \over (m - a)(m - b)}f(m) + {(x - a)(x - m) \over (b - a)(b - m)}f(b)
$$

其中$f(x)$是原函数，$g(x)$是拟合后的函数。下文中$f$和$g$也表示同样的意义，不再复述。

## 二次函数的积分
有了二次函数后，计算其积分是十分简单的事，但是这一切还不够完美。下面我们将推导出一个更简单的公式。

设：
$$
g(x) = Ax^2 + Bx + C \\
m = \frac{(a + b)}2 \\
f(a) = g(a), \; f(m) = g(m), \; f(b) = g(b)
$$

那么：
$$
\int_a^b f(x) \;\mathrm{d}x \approx \int_a^b (Ax^2 + Bx + C)\;\mathrm{d}x
$$

所以：
$$
\int_a^b (Ax^2 + Bx + C)\;\mathrm{d}x = \frac{A}3(b-a)^3 + \frac{B}2(b-a)^2 + C(b-a)
$$

因为：
$$
b^3 - a^3 = (b^2 + ab + a^2)(b-a)\\
b^2 - a^2 = (b+a)(b-a)
$$

所以之前的式子可变为：
$$
{b-a \over 6}[2A(b^2 + ab + a^2) + 3B(b+a) + 6C]
$$

调整可得：
$$
{b-a \over 6}\left[(Aa^2 + Ba + C) + (Ab^2 + Bb + C) + 4A\left({b+a \over 2}\right)^2 + 4B\left({b+a \over 2}\right) + 4C\right]
$$

于是就是：
$$
\int_a^b f(x) \;\mathrm{d}x \approx {b - a \over 6}(f(a) + 4f(m) + f(b))
$$

这就是辛普森法则。

## 辛普森积分
下面将用Python简单实现一下辛普森积分，首先我们需要一个计算积分的函数：

```python
def sample(f, a, b):
    """用二次函数近似计算函数f的积分
    f: 函数
    a: 积分下界
    b: 积分上界
    """

    return (b - a) * (f(a) + 4.0 * f((a + b) * 0.5) + f(b)) * 0.5
```

然后就是对`f`分成`n`段，每一段使用二次函数近似计算：

```python
def simpson(f, a, b, n = 1000):
    """计算定积分
    f: 原函数
    a: 积分下界
    b: 积分上界
    n: 划分的区间数
    """

    delta = (b - a) / n
    result = 0

    for i in range(0, n):
        left = a + i * delta
        right = left + delta
        result += sample(f, left, right)

    return result
```

用它来试着算一下圆周率：
```python
In [1]: simpson(lambda x : 2.0 * sqrt(1 - x**2), -1, 1, 100000)
Out[1]: 3.1415926390691236
```

可以发现分为$100000$个区间就获得了$7$位的精度。事实上，如果你将`sample`换为直线的拟合，你将只能得到$6$的精度。

## 自适应辛普森积分
然而控制区间个数不是一个控制答案精度的好办法，通常我们将使用特定的$\varepsilon$来控制精度误差。

如何让算法知道应当继续细分来达到特定精度呢？通常的方法就是将当前区间分为两半，用这两半的拟合值与当前计算的值做差。如果小于$\varepsilon$，那么我们就认为精度达到了要求。否则我们就递归下去，计算两个子区间的积分。注意，此时$\varepsilon$也应当缩小，从而避免累积的误差超过了$\varepsilon$。

这样我们就将得到一个递归算法，具体实现如下：

```python
def _adaptive_simpson(f, a, b, eps, current):
    """递归过程
    f: 原函数
    a: 积分下界
    b: 积分上界
    eps: 精度
    current: [a, b]的定积分近似值，用于减少计算量
    """

    mid = (a + b) * 0.5
    leftans = sample(f, a, mid)
    rightans = sample(f, mid, b)

    if abs(leftans + rightans - current) < eps:  # 如果达到要求
        return current
    else:  # 否则将递归下去计算
        return (_adaptive_simpson(f, a, mid, eps * 0.5, leftans) +
                _adaptive_simpson(f, mid, b, eps * 0.5, rightans))

def adaptive_simpson(f, a, b, eps):
    """自适应辛普森积分
    f: 原函数
    a: 积分下界
    b: 积分上界
    eps: 精度
    """

    return _adaptive_simpson(f, a, b, eps, sample(f, a, b))
```

我将其与线性拟合的算法对比了一下速度。他们共用一个递归的框架，只是`sample`函数有二次函数拟合和直线拟合两种：

直线拟合：

```python
In [1]: %time adaptive_simpson(sin, 0, 1000, 0.00001)
CPU times: user 5.58 s, sys: 0 ns, total: 5.58 s
Wall time: 5.58 s
Out[1]: 0.4376209161316862
```

二次函数拟合：

```python
In [26]: %time adaptive_simpson(sin, 0, 1000, 0.00001)
CPU times: user 60 ms, sys: 0 ns, total: 60 ms
Wall time: 59.6 ms
Out[26]: 0.43762092534838204
```

可见辛普森积分法是相当迅速的。

## 异常情况
由于是使用二次函数拟合，所以辛普森积分法对光滑的函数效果较好。但下面集中情况需要谨慎考虑：

* 上下震荡十分剧烈的函数（如$y = \sin(1/x)$）不适用，事实上这种函数一般都不好积。
* 突变的函数（如$y = |x|$，在$x = 0$处无导数）不适用。

对于存在没有导数的点的函数，通常的解决方法就是从这些点分开，然后就可以分段计算了。
