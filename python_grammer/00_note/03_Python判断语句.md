# 目录
![目录](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699014783430-aef4d614-0a15-4c6f-83ad-d533d6734643.png#averageHue=%23fcfaf9&clientId=u12739c1b-a6e3-4&from=paste&height=202&id=ub23f21c9&originHeight=253&originWidth=470&originalType=binary&ratio=1.25&rotation=0&showTitle=true&size=26625&status=done&style=shadow&taskId=u3ac659fe-bacb-4de9-bafe-3d023de895f&title=%E7%9B%AE%E5%BD%95&width=376 "目录")
# 布尔类型和比较运算符
## 布尔类型（bool）

1. `Ture`表示真，本质是1；`false`表示假，本质是0；
2. 布尔类型不仅可以自行定义，同时也可以通过计算得来：
   1. 自行定义：`b1 = Ture`
   2. 计算得来：`b2 = 10 > 5`
## 比较运算符
![比较运算符](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699014134099-5e7cd0aa-1f63-4893-b8ad-f8a02b3cc7b2.png#averageHue=%23ddcdca&clientId=u12739c1b-a6e3-4&from=paste&height=204&id=u2112502c&originHeight=255&originWidth=693&originalType=binary&ratio=1.25&rotation=0&showTitle=true&size=78862&status=done&style=none&taskId=u9ea97051-c425-4593-a1e0-2e623c22348&title=%E6%AF%94%E8%BE%83%E8%BF%90%E7%AE%97%E7%AC%A6&width=554.4 "比较运算符")
# `if`语句的基本格式

1. 判断语句的结果，必须是布尔类型`True`或`False`

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699014263047-e9c2cb5d-9ca1-4ee8-9c64-c1edc75d987d.png#averageHue=%23f0ede5&clientId=u12739c1b-a6e3-4&from=paste&height=168&id=u0a5e6c6a&originHeight=210&originWidth=359&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=52109&status=done&style=none&taskId=u83e56e4a-a82a-47a8-9da3-87bf98ff9bc&title=&width=287.2)

2. 归属于`if`判断的代码语句块，需在前方填充4个空格缩进（**Python通过缩进判断代码块的归属关系**）

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699014343493-f4d5618d-40c5-4c44-aa3e-2d3dcba04fa8.png#averageHue=%23f0f3e9&clientId=u12739c1b-a6e3-4&from=paste&height=163&id=uf8670dd7&originHeight=204&originWidth=476&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=81420&status=done&style=none&taskId=u901ee2e1-323d-41f4-b417-39d720ed9e9&title=&width=380.8)
# `if else`语句

1. 格式

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699014423928-8ff58eb0-66c9-4242-9493-d689fb2dfaaf.png#averageHue=%23ebebeb&clientId=u12739c1b-a6e3-4&from=paste&height=223&id=uaed24973&originHeight=279&originWidth=262&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=41249&status=done&style=none&taskId=ub51cfe27-3635-4b9a-865c-b6c0ed7762e&title=&width=209.6)

2. `else`后不要判断条件，且和`if`代码块一样，`else`的代码块同样需要4个空格作为缩进

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699014588428-fda2ca0c-acd9-4314-9186-b1e0e12c3781.png#averageHue=%23eff1e7&clientId=u12739c1b-a6e3-4&from=paste&height=150&id=u7f66df3e&originHeight=187&originWidth=523&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=86602&status=done&style=none&taskId=u70501407-3795-47fd-a58b-90bd5508458&title=&width=418.4)‘
# `if elif else`语句

1. 格式：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699014634402-2af6a21f-1bdc-4117-8183-9e4d8290bbf5.png#averageHue=%23e8e7df&clientId=u12739c1b-a6e3-4&from=paste&height=212&id=u70e823d9&originHeight=265&originWidth=255&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=86205&status=done&style=none&taskId=ua890e5ad-02d4-441d-b12c-6f4e361c211&title=&width=204)

2. 判断是互斥且有顺序的

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699014666392-9126b8a1-1e32-4a0d-ae3a-7ec1a031210e.png#averageHue=%23fdeeed&clientId=u12739c1b-a6e3-4&from=paste&height=178&id=ua81ed305&originHeight=281&originWidth=753&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=151779&status=done&style=none&taskId=u2ffb67c4-2582-4d1d-8c23-7e8eba8d62d&title=&width=477.20001220703125)

3. 空格缩进同样不可以省略

![image.png](https://cdn.nlark.com/yuque/0/2023/png/27258908/1699014690029-0f630455-718c-4434-b679-9c068b1dda70.png#averageHue=%23ebf0e4&clientId=u12739c1b-a6e3-4&from=paste&height=158&id=ud12550c0&originHeight=198&originWidth=422&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=86039&status=done&style=none&taskId=ud8c69d78-4883-40d9-a3ac-c534ec364d7&title=&width=337.6)

