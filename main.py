# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Hello Ewa")

print("你好，世界")

a = "\n单身猫"
b = '拒绝谈恋爱'
c = '''只要
灵魂深处
有爱的人'''
print (a)
print (b)
print (c)

name ="MJA"
birthday ="20061010"
print (f"\nmy name is {name}")
print (f"my birthday is {birthday}")

# 2月4日
d = ("\n今天是...\n\n大年初四")
e = ("\t恢复学习")
f = ("\t\t恢复运动")
g = ("我正在听：\nThings I Could Never Say to You")
print (d)
print (e)
print (f)
print (g)

#变量名不能以数字、空格开头，且大小写敏感；只能由大小写字母、数字、下划线组成。

# 2月5日
num = 66
if num %2 == 0:
    print("\nyes")
if num %2 == 1:
    print("no")
#一个数字对2取模，结果为1是奇数，为0是偶数。

# BMI 公式： 体质指数(BMI)=体重(kg)÷(身高(m)*身高(m))

# 非零非空

# 如果不是XXX，就XXX
weather = "晴天"
if weather == "晴天":
    print ("今天出去玩")
else:
    print ("今天宅在家")

#解决是否回本
bid =200
price = 300
jj= 200 * 10
sj= 300 * 8
profit = sj / jj
if profit >=0:
    print ("回本了")
else:
    print ("没有回本")

#补运费问题：超出的部分每公斤交20元的运费，
Jack = 8.5 + 6 + 8
free = 20
pay = (Jack-20) * 20
if Jack > free:
    print (f"需要交{pay}元")
else:
    print ("不需要补交运费")

#索引
a = "Iloveyou"
print ([a[0],a[1],a[5]])

# append vt 追加; (在文章后面)附加，增补; insert vt 插入; 嵌入; (在文章中)添加，加插

#2月7日

#加总
PriceList = [44,51,38,66,90]
TotalPrice = 0
for price in PriceList:
    TotalPrice = TotalPrice + price
print (TotalPrice)

#奇数偶数
Numbers =[0,1,2,3,4,5,6,7,8,9]
for OneNumber in Numbers:
    if OneNumber % 2 ==1:
        print (OneNumber)

# 神奇动物在哪里？
animals = ["bear", "python", "peacock", "kangaroo", "whale", "platypus"]
numbers = ["1st", '2nd', "3rd", "4th", "5th", "6th"]
num = [0, 1, 2, 3, 4, 5]
for i in num:
    print(f"The {numbers[i]} animal in the list is {animals[i]}")

# for 循环最大值
NumList = [83,80,18,4,88,21,96,20,40,59]
MaxNum = NumList[0]
for Num in NumList:
    if Num > MaxNum:
        print (Num)
        print (MaxNum)
        MaxNum = Num
        print (Num)
        print (MaxNum)
print (MaxNum)

#for 循环最小值
num = [83,80,18,4,88,21,96,20,40,59]
Mini = num[4]

for i in num:
    if i < Mini:
        Mini = i
print (Mini)

# 2月8日

# While 循环 +1 版本
Num = 5
while Num <=25:
    print (Num)
    Num = Num + 1

# 循环 困惑问题1
sum= 0
counter= 0
while counter < 5:
    sum = sum + counter
    counter = counter + 1
    print(sum)

#while 困惑问题 1 拆解过程：
#第二次循环：sum(1) + counter(0) ；counter(0) = 0 + 1, 结果 sum是1
#第二次循环：sum(0) +counter (1) ；counter(1)=1+1, 结果 sum是1
#第三次循环：sum(1) +counter (2) ；counter(2)=2+1, 结果 sum是3
#第四次循环：sum(3) +counter (3) ；counter(3)=3+1, 结果 sum是6
#第五次循环：sum(6) +counter (4) ；counter(4)=4+1, 结果 sum是10

#注意print的位置，只输出最后一位结果
sum= 0
counter= 0
while counter < 5:
    sum = sum + counter
    counter = counter + 1
print(sum)

#counter先自增，sum再加上counter，输出位置不同导致结果不同
sum= 0
counter= 0
while counter < 5:
    counter = counter + 1
    sum = sum + counter
print(sum)

#普通while 循环遍历
num = 0
while num < 10:
    num = num + 1
    print (num)

#从1+到50
num = 0
i = 0
while i < 51:
    num = num + i
    i = i + 1
print (num)

# 求30天内所有奇数
n = 1
while n <=30:
    if n % 2 == 1:
        print (n)
    n = n + 1


#2月9日

# 这个月有几天没有背单词？
    Record = [60, 0, 73, 139, 64, 48, 73, 63, 0, 59, 100, 121, 44, 30, 0, 0, 43, 67, 64, 51, 106, 0, 80, 0, 119, 59, 0,
              58, 100, 90]
    Count = 0
    for i in Record:
        if i > 0:
            continue
        Count = Count + 1
    print(f"这个月有{Count}天没有背单词")

# 几个人能买到牛奶？
numberlist = [2, 4, 3, 5, 2, 1, 3, 5, 2, 4]
total = 0
n = 0

for i in numberlist:
    total = total + i
    if total > 15:
        print(f"有{n}个人可以买到牛奶")
        break

    n = n + 1

# 买西瓜
melonlist = [4, 3.5, 2, 5, 6, 3, 4.7, 5.3]
n = 0
buylist = []
for i in melonlist:
    if n == 3:
        break

    if i >= 4:
        buylist.append(i)
        n = n + 1
        continue

print(buylist)

# 数有几个2
Number = (2, 5, 6, 3, 4, 2, 2, 7, 8, 2)
n = 0
for i in Number:
    if i != 2:
        continue
    n = n + 1
print (n)

#元组切片求和
Number = (2, 5, 6, 3, 4, 2, 2, 7, 8, 2)
n = 0
for i in Number[3:8]:
    n = n + i
print (n)

# 某工厂生产某产品，从中随机抽取20个产品进行质量检验。合格记为1，不合格记为0。假如这批产品中不合格的产品数超过2个，则认为这批产品未通过检验，不合格。
Quality = [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1]
Count = 0

for i in Quality:
    if i == 0:
        Count = Count + 1
    if Count > 2:
        break

if Count > 2:
    print ("不合格")
else:
    print ("合格")

# 年龄段输出：
Jack = 35
if Jack <= 44:
    print("青年人")
if 45 <= Jack <= 59:
    print("中年人")
if 60 <= Jack <= 95:
    print("老年人")
if Jack > 95:
    print("长寿老人")

#hello逆序：
string = "hello"
NewList = []
for i in string:
    NewList.append(i)

result = ""
n = 4

while n >= 0:
    result = result + NewList[n]
    n = n - 1

print(result)


#最高分是谁？
Result = {'Tony':69, 'Lihua':64, 'Rain':93, 'Jack':61, 'Xiuxiu':82, 'Peiqi':67, 'Black':77}
n = 0
for i in Result.keys():
    if Result [i] < n:
        continue
    n = Result[i]
print (n)

# 2月10日

# 循环遍历 key和value
state = {"China":"Beijing", "USA":"Washington", "Japan":"Tokyo", "England":"London"}
for i in state:
    print (i + ' ' + state[i])

    #高分图书
    Score = {"Here to Stay": 4.2, "The Secrets of Lost Stones": 4.7, "I Know Everything": 4.6, "The Rabbit Girls": 4.5,
             "Butterfly in Frost": 4.1, "Call Her Mine": 4.5, "Broken Knight": 4.8, "All the Lovely Pieces": 4.4,
             "Black Nowhere": 4.2, "The Loot": 4.6}
    n = "Here to Stay"
    k = 0
    TopTen = []
    for i in Score:
        if Score[n] < Score[i]:
            n = i
        TopTen.append(i)
    print(TopTen)
    print(f"得分最高的图书是{n}")

# 2月12日 学习内容

    # 定义一个算数的函数 类似SIZE
    def length(Height, Width):
        return 2 * (Height + Width)

    Size = length(15, 10)
    print(Size)

#函数的基本使用
    def PrintFourTimes(content):
        print(content)
        print(content)
        print(content)
        print(content)

    PrintFourTimes("China")

# 加法， 用 return实现
    def plus(a, b):
        return a + b

    c = plus(788, 1667)
    print(c)

# 生成一个比较函数
def than (a, b):
    if a > b:
        return a
    else:
        return b

c = than (18,22)
print (f"{c}比较大")

#用max选择最大数字
maxhaha = max (10,100,1000)
print (maxhaha)

# 拼接字符串
a = 'abc'
b = 'def'
print (a + b)

#原式子里面5变8
List = [5, 7, 9, 2, 1, 3, 5, 5]
n = 0
for i in List:
    if i == 5:
        List[n] = 8
    n = n + 1
print (List)


#有多少字母？
n = 'sjdkfjjdskhsjk'
num = 0
for i in n:
    num = num + 1
print (num)
#简单方法
n = 'sjdkfjjdskhsjk'
print (len(n))