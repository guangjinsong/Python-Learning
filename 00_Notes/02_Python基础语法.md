# 常用的值类型
![常用的值类型](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091912786.png "常用的值类型")
# 注释

1. 简介：在程序中对程序代码进行解释说明的文字；
2. 作用：注释不是程序，不能被执行，只是对程序代码进行解释说明，让别人可以看懂程序代码的作用，从而大大增强程序的可读性；
3. 分类：
   1. 单行注释：`# 注释`
   2. 多行注释：`""" 注释 """`
# 变量

1. 简介：在程序运行时，能储存计算结果或能表示值的抽象概念。简单来说，变量就是程序运行时，记录数据的；
2. 格式：**变量名称 = 变量的值**
# 数据类型
## 简介
![三种数据类型](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091912435.png "三种数据类型")
## type()的使用
![type()的使用](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091912641.png "type()的使用")

1. 简介：查看变量的数据类型
2. 用法：`type(var)`
# 数据类型转换
## 简介

1. 数据类型之间，在特定的场景下，是可以相互转换的，如字符转数字，数字转字符串等；
2. 常见的数据类型转换：
   1. 从文件中读取的数字，默认是字符串，我们需要转换成数字类型；
   2. `input()`语句输出默认结果是字符串，若需要其他类型也需要转换；
   3. 将数字转换成字符串以写出到外部系统。
## 常见转换语句

1. `int(x)`：将`x`转换成一个整数；
   1. `x`如果是浮点数，那么会丢失小数部分，丢失精度；

![image.png](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091912301.png)

   2. `x`如果是字符串
      1. 字符串的内容全为数字，则转换成整数；

![image.png](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091912810.png)

      2. 字符串的内容含有非数字的字符，则报错。

![image.png](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091912882.png)

2. `float(x)`：将`x`转换成一个浮点数；
   1. 转换规则可参考`int()`
3. `str(x)`：将对象转换成字符串。
   1. 任何类型都可以通过`str()`转换成字符串。
# 标识符命名规则与规范
## 规则

1. **内容限定：**
   1. 标识符命名中只允许出现：①英文、②中文、③数字、④下划线这四类元素，其余任何内容都不被允许；
   2. 不推荐使用中文；
   3. 数字不可以开头
2. **大小写敏感：**
   1. 例如`andy`和`Andy`是两个标识符；
3. **不可使用关键字：**
   1. 关键字如下：

![image.png](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091912637.png)
## 变量命名规范

1. 见名知意；
   1. 例，年龄：`age = 10`。
2. 下划线命名法；
   1. 例，人的名字：`first_name = "张三"`。
3. 英文字母全小写。
   1. 例，名字：`name = "sgj"`。
# 运算符
## 算术运算符

1. `+`：加；

2. `-`：减；

3. `*`：乘；

4. `/`：除；

5. `//`：取整除；

6. `%`：取余；

7. `**`：指数

   ![image.png](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091912146.png) 

 
## 赋值运算符

1. `=`
## 复合运算符
![复合运算符](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091913704.png "复合运算符")
# 字符串
## 字符串定义方式
![字符串定义方式](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091913674.png "字符串定义方式")

1. 双引号
2. 单引号
3. 三引号：可以写多行。**注意，如果没有变量接收，那么就是用**`**""" """**`**引起来的就是多行注释。**

![image.png](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091913080.png)
## 字符串的引号嵌套

1. **可以使用转义字符**`**\**`**来将引号解除引用，变成普通字符串；**
2. 单引号定义法，可以内含双引号；
3. 双引号定义法，可以内含单引号。
## 字符串拼接

1. 多个字符串字面量可以通过`+`来拼接成一个字符串；

![image.png](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091913342.png)

2. 字符串不可以与其他非字符串变量或字面量拼接。

![image.png](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091913600.png)
## 字符串格式化
### 方法一：%s、%f、%d

1. `%s`：将内容转换成字符串，放入占入位置。注意，使用`%s`变量也可以是整数或浮点数，这时是没有精度控制的，整数和浮点数会先转换成字符串，然后再拼接；

![image.png](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091913463.png)

2. `%d`和`%f`：以数字原本的面貌拼接进去，有精度控制；

![image.png](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091913400.png)
### 方法二：`f "{var} {var}"`

1. 不理会类型，且不做精度控制；
2. 适合对精度没有要求的时候快速使用

![image.png](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091913046.png)
## 表达式格式化
![表达式格式化](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091913105.png "表达式格式化")
## 精度控制
![规则](https://cdn.nlark.com/yuque/0/2023/png/27258908/1698842950273-9302dc01-fd6b-4e58-b8e6-0c3ec59d7130.png#averageHue=%23fcfaf9&clientId=u219bcbdd-810d-4&from=paste&height=432&id=u4121a1bc&originHeight=540&originWidth=1438&originalType=binary&ratio=1.25&rotation=0&showTitle=true&size=191245&status=done&style=shadow&taskId=u24dcccea-047e-4fb4-9380-43775bb3382&title=%E8%A7%84%E5%88%99&width=1150.4 "规则")
![示例](https://dawn1314.oss-cn-beijing.aliyuncs.com/typoraimg/202311091913547.png "示例")
