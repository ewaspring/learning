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

<<<<<<< HEAD

#2月16日 学习心得


pida = lambda x:x*2
print (pida(3))

#我最喜欢的书
def favorite_book(title):
    print (f"My favorite book is {title}")

favorite_book('Harry Potter')

#计算5！
def factorial(num):
    result = 1
    while num > 0:
        result = result * num
        num = num - 1
    return result

print (factorial(5))

#计算汇率
dollar = lambda x:x/6.681
pound = lambda x:x/8.8162
yen = lambda x:x/0.06052

print (dollar(10000))
print (pound(10000))
print (yen(10000))
=======
# 2-19 practice

#类
class Dog:
    def __init__(self, DogName):
        self.DogName = DogName

    def print_DogName(self):
        print(self.DogName)

#定义旺财
class Dog:
    def __init__(self, DogName):
        self.name = DogName

    def print_DogName(self):
        print(self.name)

wangcai = Dog("wangcai")
wangcai.print_DogName()

#2-23 practice

#class 定义Tony最高分
class student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_score(self):
        return max(self.score)


Tony = student('Tony', 20, [69, 88, 100])
print(Tony.get_score())

# 杯子容积反值
class bottle:
    def __init__(self, capacity):
        self.capacity = capacity

    def introduce(self):
        return self.capacity

a = bottle(600)
print(a.introduce())

# 定义食物热量
class food:
    def __init__(self,caloric):
        self.caloric = caloric
    def introduce(self):
        return self.caloric

a = food('200')
print (a.introduce())

#选股票 values
shares = { 'IBM':36.6,
    'Lenovo':23.2,
    'oldboy':21.2,
    'ocean':10.2
}

m = max(shares.values())
print(m)

# emmm...
print ('''原本，
我以为，
对其他人渣，
无心撩完就跑，
对任何事情都不说清楚，
能够懂事，
和点到为止，
只是我的一种社交风格，
只是证明我不够喜欢她，
我可以转头就忘，
也可以说放下就放下，
哪怕下一秒就不联系，
我也从不怕失去。

我以为，
真正喜欢一个人，
就是甩开双子座渣的套路，
就是毫无心机的全盘托出，
就是展现我的真心和态度，
就是毫无顾忌的向对方表达爱意，
让对方有足够的安全感，
让对方对我有足够的信任感，
我考虑的那么周全，
却没想到，
我喜欢的人，
总希望我像对待别人那样渣。''')

#2-25 学习心得

#扑克牌
class Poker:
    def __init__(self, colour, num):
        self.colour = colour
        self.num = num

    def play(self):
        print(f"打出一张{self.colour}{self.num}")

p = Poker("黑桃", "A")
p.play()

#水果
class Fruit:
    def __init__(self,kind,weight):
        self.kind = kind
        self.weight = weight
    def introduce(self):
        print(f"这是一个{self.weight}的{self.kind}")
fruit = Fruit("苹果","30g")
fruit.introduce()

#成绩单
class SchoolReport:
    def __init__(self,report):
        self.report = report
    def MaxScore(self):
        return max (self.report)
Class1 = SchoolReport([81, 76, 69, 66, 62, 87, 90, 89])
print (Class1.MaxScore())

#小狗
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_information(self):
        print(f"{self.name}是一条{self.age}岁的狗")
    def sit(self):
        print(f"{self.name}蹲下了")
    def roll_over(self):
        print(f"{self.name}正在打滚")

my_dog = Dog('Judy',2)
my_dog.get_information()
my_dog.sit()
my_dog.roll_over()

#餐厅正在营业
class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"餐馆的名字是{self.restaurant_name}")
        print(f"餐馆的主营菜系是{self.cuisine_type}")

    def open_restaurant(self):
        print("餐馆正在营业中")


rtr = restaurant("全聚德", "烤鸭")
rtr.describe_restaurant()
rtr.open_restaurant()

#漂亮的E
number =[8, 1, 1, 8, 1, 1, 8]
for i in number:
    print (i * "5")

#关于电脑
class Computer:
    def __init__(self, brand):
        self.brand = brand

    def computer_brand(self):
        print(self.brand)


class Mac(Computer):
    def __init__(self, type):
        self.brand = "Mac"
        self.type = type

    def computer_type(self):
        print(self.type)


mycomputer = Mac("MacBook Air")
mycomputer.computer_brand()
mycomputer.computer_type()

#矩形
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)


class square(rectangle):
    def __init__(self, length):
        self.length = length
        self.width = length

f1 = rectangle(4, 6)
f1.area()
f2 = square(5)
f2.area()

# 手机系统
class OS:
    def __init__(self, brand):
        self.brand = brand

    def introduce(self):
        print(self.brand)


class IOS:
    def __init__(self, version):
        self.brand = "IOS"
        self.version = version

    def introduce(self):
        print(self.brand + self.version)


PhoneA = OS('Android')
PhoneA.introduce()
PhoneB = IOS('13')
PhoneB.introduce()

#类的灵活运用
class school:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def introduce(self):
        print(f"{self.name}在{self.address}")

sch = school("衡水中学", "河北")
sch.introduce()

#上学打卡
class student:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"{self.name}打卡成功")

tony = student("Tony")
tony.print_name()

#Tony的平均分和最高分
class student:
    def __init__(self, score):
        self.score = score

    def Average(self):
        sum = 0
        for i in self.score:
            sum = sum + i
        print(f"平均分为{sum / len(self.score)}")

    def HighestScore(self):
        print(f"最高分为{max(self.score)}")


Tony = student([80, 77, 92])
Tony.Average()
Tony.HighestScore()

#储存汽车信息
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

my_car = Car('Audi', 'A6L', 2019)
print(my_car.get_descriptive_name())

# make shirt
def make_shirt(word, size):
    print(f'一件印有{word}的{size}码衣服')

make_shirt("夜曲编程", "XL")
make_shirt("I love python", "L")

# make shirt 衣服
class shirt:
    def __init__(self, word, size):
        self.word = word
        self.size = size

    def make_shirt(self):
        print(f"一件印有{self.word}的{self.size}码衣服")


cloth1 = shirt("夜曲编程", "XL")
cloth1.make_shirt()
cloth2 = shirt("I love python", "L")
cloth2.make_shirt()

#使用函数计算加减乘除
def add(num1,num2):
    result = num1 + num2
    return result

def subtract(num1,num2):
    result = num1 - num2
    return result

def multiply(num1,num2):
    result = num1 * num2
    return result

def divide(num1,num2):
    result = num1 / num2
    return result

print (add(34,32))
print(subtract(34,32))
print(multiply(34,32))
print(divide(34,32))

#城市-国家
def city_country(city,country):
    return (f"{city},{country}")

print (city_country("Beijing","China"))
print (city_country("Tokyo","Japan"))

# 用class输出城市-国家
class city:
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def run(self):
        return (f"{self.city}, {self.country}")

Beijing = city("Beijing", "China")
print(Beijing.run())
Tokyo = city("Tokyo", "Japan")
print(Tokyo.run())

#钱钱钱
def combination(n):
    OneHundred = n // 100
    Fifty = (n % 100) // 50
    Twenty = (n % 50) // 20
    Ten = (n - OneHundred * 100 - Fifty * 50 - Twenty * 20) // 10
    Five = (n % 10) // 5
    One = n % 5
    print(f"百元{OneHundred}张，五十元{Fifty}张，二十元{Twenty}张，十元{Ten}张，五元{Five}张，一元{One}张")

combination(186)
combination(487)

#计算周薪
def weekly_wage(HourlyWage, Hour, StandardHours):
    if Hour <= StandardHours:
        return HourlyWage * Hour
    else:
        return (HourlyWage * StandardHours + 1.5 * HourlyWage * (Hour - StandardHours))

print(int(weekly_wage(10, 40, 35)))
print(int(weekly_wage(20, 35, 35)))

#引入代码
import datetime
today = datetime.date.today()
year = today.year
print (year == 2021)

#引入某个具体的值
from datetime import date
today = date.today()
year = today.year
print (year == 2021)

#math模块 sqrt:开平方  fabs:绝对值
import math
print (math.sqrt(100))
print (math.fabs(-0.03))

# from ... import 方法
from math import sqrt
from math import fabs
print (sqrt(100))
print (fabs(-0.03))

# 引用math所有函数
from math import *
print (sqrt(100))
print (fabs(-0.03))

#判断三角形
a = 4
b = 1
c = 4

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("等边三角形")
    if a == b or a == c or b == c:
        print("等腰三角形")
    if a != b and a != c and b != c:
        print("普通三角形")

if not (a + b > c and a + c > b and b + c > a):
    print("不能构成三角形")

#求最大值
n = [3, 7, 5, 9, 1]
print(max(n))

#有多少同学
n = 0

while True:
    if n % 5 == 1 and n % 6 == 5 and n % 7 == 4 and n % 11 == 10:
        print (n)
        break
    n = n + 1

