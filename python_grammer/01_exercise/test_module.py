# print(res)

# 语法1: 导入时间模块
# import time
# print("开始")
# time.sleep(1)  # 让程序睡眠1秒
# print("结束")

# 语法2: 导入时间模块中的sleep方法
# from time import sleep
#
# print("开始")
# sleep(1)
# print("结束")

# 语法3: 模块别名
# import time as tt

# tt.sleep(2)
# print("hello")

# 功能别名
# from time import sleep as sl

# sl(2)
# print("hello")

from test_func import add

print(add(1, 1))

from test_func import div

# from test_func import *
print(div(9, 3))

