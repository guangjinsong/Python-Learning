def mysum():
    return 1


def check_age(age):
    if age > 18:
        return "adult"
    return None


res = check_age(5)
if not res:
    print("未成年, 不可进入")

# 暂时不赋予变量具体值
name = None


# 文档说明
def add(x, y):
    """
    函数说明
    :param x: 相加的数字1
    :param y: 相加的数字2
    :return:  返回相加的结果
    """
    # 函数体
    return x + y


i1 = add(1, 2)
