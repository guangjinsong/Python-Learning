str1 = "sgjqxy"
print(str1.index("qxy")) # output: 4

str2 = "123153412345"
str3 = str2.replace("12", "--")
print(str2)  # output: 123153412345
print(str3)  # output: --31534--345

str4 = "123 456"
str5 = str4.split(" ")
print(str5)  # output: ['123', '456']

str6 = "sr12456rs"
print(str6.strip("sr"))  # output: 12456

str7 = "12345126"
print(str7.count("12"))  # output: 2

str8 = "12A & a 45126"
print(len(str8))  # output: 13

str9 = "sgj"
index = 0
while index < len(str9):
    print(str9[index])
    index += 1

for i in str9:
    print(i)


str10 = "1234567"
str11 = str10[1:4]  # 下标1开始，下标4（不含）结束，步长1
str12 = str10[:]  # 从头开始，到最后结束，步长1
str13 = str10[::2]  # 从头开始，到最后结束，步长2
str14 = str10[:4:2]  # 从头开始，到下标4（不含）结束，步长2
print("str11 : " + str11)  # output: str11 : 234
print("str12 : " + str12)  # output: str12 : 1234567
print("str13 : " + str13)  # output: str13 : 1357
print("str14 : " + str14)  # output: str13 : 13

str15 = "12345"
str16 = str15[::-1]  # 从头（最后）开始，到尾结束，步长-1（倒序）
str17 = [1, 2, 3, 4, 5]
str18 = str17[3:1:-1]  # 从下标3开始，到下标1（不含）结束，步长-1（倒序）
str19 = (1, 2, 3, 4, 5)
str20 = str19[:1:-2]  # 从头（最后）开始，到下标1(不含)结束，步长-2（倒序）
print(str16)  # output: 54321
print(str18)  # output: [4, 3]
print(str20)  # output: (5, 3)