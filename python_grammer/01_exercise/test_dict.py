# 数据的获取
dict1 = {1: "blue", 2: "red", 3: "gold"}
print(dict1[1])  # output: blue
print(dict1[2])  # output: red
print(dict1[3])  # output: gold

# 字典的嵌套
dict2 = {"张三": {"语文": 99, "数学": 98},
         "李四": {"语文": 93, "数学": 92},
         "王五": {"语文": 95, "数学": 92}
         }

# keys()
keys = dict2.keys()
print(keys)  # dict_keys(['张三', '李四', '王五'])
print(type(keys))  # <class 'dict_keys'>

# for
for key in keys:
    print(f"学生: {key}, 分数:{dict2[key]}")

# len()
print(len(dict2))  # output: 3

# 获取嵌套字典的内容
print(dict2["张三"])  # output: {'语文': 99, '数学': 98}
print(dict2["李四"]["语文"])  # output: 93

