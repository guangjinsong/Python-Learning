# `while`循环的基础语法
![格式](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699015024345-21e58740-b8fe-4e58-a032-622db9c927a5.png#averageHue=%23eae9e9&clientId=ub4be4896-eed3-4&from=paste&height=112&id=u093ae69f&originHeight=140&originWidth=233&originalType=binary&ratio=1.25&rotation=0&showTitle=true&size=23160&status=done&style=shadow&taskId=u58d8a6ff-4ce3-4655-b753-ad3bc98eecf&title=%E6%A0%BC%E5%BC%8F&width=186.4 "格式")

# `for`循环的基础语法
## 基本使用

1. 格式：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699015187681-5fc39200-cd27-425b-b8e7-7f2312791d7d.png#averageHue=%23f5f2d4&clientId=ub4be4896-eed3-4&from=paste&height=42&id=uf96adf90&originHeight=52&originWidth=219&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=10812&status=done&style=shadow&taskId=u3752a94e-4f84-4995-ba70-b9b4c4db3bf&title=&width=175.2)

2. 示例：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699015214499-bc163659-17ac-46a6-bc9f-ab220bb343ae.png#averageHue=%23fbf8dc&clientId=ub4be4896-eed3-4&from=paste&height=189&id=ub754a00e&originHeight=236&originWidth=392&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=31942&status=done&style=shadow&taskId=uaac5f4d3-c680-4e74-8d3d-68307c3536f&title=&width=313.6)

3. 总结：
   1. `for`循环处理数据的方式：从待处理数据集中逐个去除数据复制给临时变量
   2. 同`while`循环不同，`for`循环是无法定义循环条件的，只能从被被处理的数据集中一次取出内容进行处理。所以理论上讲，Python循环无法构建无限循环（被处理的数据即不可能无限大）
   3. 待处理数据集，严格来说，称之为：可迭代类型。即，内容可以一个一个依次取出的一种类型，包括：
      1. 字符串
      2. 列表
      3. 元组......
## `range()`

1. 语法
   1. `range(num)`：创建一个从`0`开始，到`num`结束的数字序列（不含`num`）
   2. `range(num1, num2)`：创建一个从`num1`到`num2`结束的数字序列（不含`num2`）
   3. `range(num1, num2, step)`：创建一个`num1`到`num2`结束，数字之间的步长为`step`为准（`step`默认为`1`）的数字序列（不含`num2`）
2. 总结：
   1. 上面获得数字序列的范围为`num1<= x < num2`
## 变量作用域

1. 在编程规范上，临时变量的作用域只限定在`for`循环内部
2. 如果在`for`循环外部访问临时变量，实际上是可以访问到的，但是在编程规范上是不允许、不建议这么做的
3. 如果实在需要在循环外访问访问循环内的临时变量，可以在循环外预先定义

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699016515206-75f565c0-6669-484e-b753-fa78dcb927f2.png#averageHue=%23f2f1eb&clientId=ub4be4896-eed3-4&from=paste&height=98&id=u68d68b36&originHeight=123&originWidth=241&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=18293&status=done&style=shadow&taskId=ud3c20370-1939-466a-8878-9e9503c1946&title=&width=192.8)
# `continue`和`break`

1. `continue`：它所在的临时循环中断
2. `break`：直接结束所在循环
