---
title: 测试
create: 2016.1.31
modified: 2016.2.1
tags: test
---
[TOC]
# pagegen.py的试炼
希望`pagegen.py`能正确工作。  

## 常规Markdown测试
# h1
## h2
### h3
#### h4
##### h5
###### h6
上面是六级标题。  
> 上面是六级标题。  
> 这是一段引用  

很好，`inline-code`和`Hello, world`：

```cpp
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
    cout << "Hello, world!" << endl;

    return 0;
}
```
别忘了Python：

```python
#!/usr/bin/env python3

if __name__ == "__main__":
    print("Hello, world!")
```

    Tab也可以直接代码
    Yeah!!!

*重要的话说三遍*  
**重要的话说三遍**  
***重要的话说三遍***  
++下划线是什么鬼++

打表A题：

| NOI | A | B | A + B |
|:---:|:-:|:-:|:-----:|
|  1  | 1 | 2 |   3   |
|  2  | 2 | 2 |   4   |
|  3  | 5 | 5 |   10  |
|  4  | 3 | 4 |   7   |

|列1    |列2     |列3    |
|:-----:|--------|:-----:|
|233333333333333   |23333333|233    |

我的GitHub: <https://github.com/riteme>  
[GitHub](https://github.com/riteme)  
我的E-mail: <riteme@qq.com>

脚注[^footnote]？  
[^footnote]: 真的行吗......

GFM breaks!
应该不在一行!
应该不在一行!!
应该不在一行!!!!!
~~deleted~~
++inserted++
--smartpants---
"a"'b'"c"'d'"e""'

## Mathjax测试: $e^{ix} = \cos x + i\sin x$
这个**应该**不得出问题......
$$ \sum_{i = 1}^{\infty} i = - {1 \over 12} \tag{1.1} $$

$$ a^2 + b^2 = c^2 \Rightarrow \triangle ABC\text{是直角三角形} \tag{1.2} $$

$$
\begin{align}
X_k & = \sum^{n - 1}_{j = 0} x_ke^{-2\pi ijk/n} \\
    & = \sum^{n - 1}_{j = 0} x_kw_n^{-jk}
\end{align}
$$

$$
\begin{align}
x_k & = \frac1n\sum^{n - 1}_{j = 0} X_ke^{2\pi ijk/n} \\
    & = \frac1n\sum^{n - 1}_{j = 0} X_kw_n^{jk}
\end{align}
$$

`$$` `$$$$` `$` `$`

行内公式`inline-math`在此$ 233 \neq 244 $233333

## 特殊语法测试
[[[FBI Warning]]]
肯定有BUG
[[[#]]]
[[[Markdown in it]]]
**STRONG**, `inline-code`.
[[[#]]]
[[[中文]]]
Not Supported...
[[[乱搞]]]
233444
[[[#]]]
233
[[[#]]]
Goodbye!
