# Equation（v0.1）
## 项目介绍（建设中）
- 使用简单
- 可以解简单的方程 *（后面考虑更复杂的）*
- 安全可靠
## 安装第三方库
- 在该目录下命令行运行：`pip install -r 
## 如何使用
- Python **3.10** 及以上版本
- 示例代码：
  ```python
  from equation import *
  e1 = OneOne() #一元一次方程
  e1.give("a+b=2",ignore=("b"),value=("1")) #等同于e1.give("a+1=2")
  print(e1.get())
  ```
## 最后
本项目主要开发者是一个初中生，项目中有很多史山代码，如果您对本仓库感兴趣，期待您的修改。