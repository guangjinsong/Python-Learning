def test_return():
    return 1, 2


x, y = test_return()
print(x)  # output: 1
print(y)  # output: 2


# 函数简介
def add(x1, y1):
    result = x1 + y1
    return result


print(add(5, 6))  # output: 11


# 定义函数
def user_info(name, age, gender):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


# 关键字传参
# 按照顺序传参
user_info(name='sgj', age=10, gender='男')
# 不按照顺序传参
user_info(age=10, name='sgj', gender='男')
# 与位置参数混用, 位置参数必须在前, 且匹配参数顺序
user_info('sgj', age=10, gender='男')

# 位置传参
user_info('sgj', 26, "男")


# 定义函数
def user_infor(name, age, gender="男"):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


# 默认传参
user_infor("Tom", 20)
user_infor("Rose", 18, '女')


# 位置传递
# 传进的所有参数都会被args变量收集,
# 它会根据传进参数的位置合并成一个元组(tuple)
def user_info1(*args):
    print(args)


user_info1('Tom')  # output: ('Tom',)
user_info1('Tom', 18)  # output: ('Tom', 18)


# 关键字传递
def user_info2(**kwargs):
    print(kwargs)


user_info2(name="Tom", age=18, id=10)  # output: {'name': 'Tom', 'age': 18, 'id': 10}


# 匿名函数
def compute(x1, y1):
    return x1 + y1


def test_func1(compute):
    res = compute(1, 2)
    print(res)


test_func1(compute)


def test_func2(compute):
    res = compute(1, 2)
    print(res)


test_func2(lambda x1, y1: x + y)
