# 以"r"方式打开一个不存在的文件
# with open("linux.txt", 'r') as f:
#     content1 = f.read(2)
#
# print(content1)

# 捕获常规异常
try:
    # 以"r"方式打开一个不存在的文件
    with open("linux.txt", 'r') as f:
        content1 = f.read(2)
except:
    print("常规异常捕获")

# 捕获特定异常
try:
	print(name)
except NameError as e:
    print("name变量名称未定义错误")

# 捕获多个异常
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print("ZeroDivisionError错误...")

# 捕获异常并输出描述信息
try:
	print(name)
except NameError as e:
    print(e)

# 捕获所有异常
try:
    print(name)
except Exception as e:
    print(e)

# 异常else
try:
    print(1)
except Exception as e:
    print(e)
else:
    print("没有异常的时候执行的代码")

# finally
try:
    with open("test_file1.py", 'r') as f:
        f.read(4)
except Exception as e:
    f = open("test_file.py", "r")
else:
    print("无异常")
finally:
    f.close()

