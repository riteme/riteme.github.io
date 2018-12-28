---
title: 习题解答
create: 2018.12.29
modified: 2018.12.29
tags: xxl
template: simple
---

已知 $0 < a < b \in \mathbb R$，求：

$$ \lim_{n \rightarrow \infty} \prod_{k = 0}^n {a + k \over b + k} $$

**答案：** $0$

**解 1：**（来自 xxl）

![xxl's solution](https://gitee.com/riteme/blogimg/raw/master/other/xxl-solution.jpeg)

**解 2：** $\prod_{k = 0}^n (a + k) = \Gamma(n + a + 1) / \Gamma(a)$，再利用 Stirling 近似~~暴力分析~~。

$$
\Gamma(n + 1) = \sqrt{2\pi n}\left({n \over \mathrm e}\right)^n\color{silver}\left(1 + \mathrm O\left(\frac1n\right)\right)
$$

<center>斯特林近似公式</center>