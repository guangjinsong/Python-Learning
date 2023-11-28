# 文件的读取
# 打开文件
f = open("D:/GitHub/Python-Learning/python_grammer/00_note/07_文件操作.md", "r", encoding="UTF-8")
# f = open("D:/GitHub/Python-Learning/python_grammer/00_note/07_文件操作1.md", "r", encoding="UTF-8")   # 如果文件不存在, 则会报: No such file or directory: 'D:/GitHub/Python-Learning/python_grammer/00_note/07_文件操作1.md'

# read(num): 读固定字节
content1 = f.read(10)
print(content1)

# 读一行
content2 = f.readline()
print(content2)

# 读全部
content3 = f.readlines()
print(content3)

# for
for line in f:
    print(line)

# with open
with open("D:/GitHub/Python-Learning/python_grammer/00_note/07_文件操作.md", "r", encoding="UTF-8") as  ff:
     content4 = ff.readline()
     print(content4)

# 关闭文件
f.close()

# 文件的写入
with open("D:/GitHub/Python-Learning/python_grammer/00_note/07_test.md", "w") as fff:
    fff.write("hel")
    fff.flush()

# 文件的追加
with open("D:/GitHub/Python-Learning/python_grammer/00_note/07_test.md", "a") as ffff:
    ffff.write("hel")
    ffff.flush()
