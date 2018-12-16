# print(1111111+3279127519045794)
# print(1/2)
# print(0XAF)
# x=3
# print(x*3)

# li=[1,2,3]
# li.append(4)
# print(li)
#
# li.extend([5,6])
# print(li)
# print(li.index(6))

# li=list(range(5))
# print(li)
# li.insert(0,"a")
# print(li)
# li.reverse()

# x=[2,5,3,1,9]
# y=x[:]
#
# z=sorted(x)
# print(z)
# from past.builtins import cmp
# print(cmp(6,5))
# s="hello"
# s[0:2]="11"

# name='123'
# # sex="yes"
# # #字符串占位符
# # print("hello %s,you are girl? %s" % (name, sex))
# # # #保留3位小数
# # from math import pi
# # print("pai is %.3f" % pi)
# l=["1","2"]
# l=[1,2,3]
# s="+"
# s1=s.join(l)
# print(s1)
#
# while True:
#     word=input("enter your name:")
#     if not word:
#         break
#     print("your name is:", word)

# print([x*x for x in range(10) if x*x%3==0])
#
# def helo():
#     'this is hello func'
#     print("hello how are you")
# print(helo.__doc__)

# def print_p(*p):
#     print(p)
# print_p("hello")
# print_p("1","2","3")

# def print_p1(title,*p):
#     print(title)
#     print(p)
# print_p1("name",1,2,3)
# print_p1("",)

# x=input("enter x:")
# y=input("enter y:")
# print(int(x)/int(y))

#异常处理
# try:
#     x=input("enter x:")
#     y=input("enter y:")
#     print(int(x)/int(y))
# except:
#     # int(y)==0
#     print("0不能作为除数")
try:
    x=input("enter x:")
    y=input("enter y:")
    print(int(x)/int(y))
except (ZeroDivisionError,TypeError,NameError)as e:
    print("0不能作为除数")
    print(e)





