# 空列表
li = list()
# print(li)

# 普通列表
my_list1 = ["sgj", "cb"]
# print(my_list1[0])
# print(my_list1[1])

# 列表中的元素存储不同数据类型的元素
my_list2 = ["it", 123, True]

# 嵌套列表
my_list3 = [[1, 2, 3], [4, 5, 6]]
# print(my_list3[0][0])
# print(my_list3[0][1])
# print(my_list3[0][2])

my_list4 = ["s", "g", "j", "s"]
i1 = my_list4.index("s")
# print(i1)  # 返回第一与之相等的下标

# 修改
my_list4[2] = "e"
# print(my_list4)

# 插入
my_list4 = ["s", "g", "j", "s"]
my_list4.insert(1, "sgj")
# print(my_list4)

# 追加
# 方式1
my_list5 = ["s", "g", "j", "s"]
# my_list5.append([1, 2, 3])
# print(my_list5)

# 方式2
str1 = "string"
my_list5.extend(str1)
# print(my_list5)


# 删除
my_list6 = [1, 2, 3, 4, 5, 1]

# remove
my_list6.remove(1)
# print(my_list6)

# del
del my_list6[0]
# print(my_list6)

# pop
my_list6.pop(0)
# print(my_list6)

# clear
my_list6.clear()
# print(my_list6)


# 统计
my_list7 = [1, 1, 1, 4, 5, 1]
print(my_list7.count(1))
print(len(my_list7))
