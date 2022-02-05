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
