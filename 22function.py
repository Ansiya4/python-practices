# def fun(x=30, y=10):
#     print("x:",x)
#     print("y:",y)
# fun()

# output:
# x: 30
# y: 10

# def fun(x=30, y=10):
#     print("x:",x)
#     print("y:",y)
# fun(1,2)

# output:
# x: 1
# y: 2

# def fun(*values):
#     for arg in values:
#         print(arg)
# fun("hello","my","dear","rishana")

# #output
# # hello
# # my
# # dear
# # rishana

# def fun(**kwargs):
#     for key,value in kwargs.items():
#         print("%s == %s" % (key,value))
# fun(num1="hi",num2="my",num3="dear")
# # output
# # num1 == hi
# # num2 == my
# # num3 == dear

# def fun(**name):
#     for key,value in name.items():
#         print(key,value) 
# fun(num1="hi",num2="my",num3="dear")
# # output:
# # num1 hi
# # num2 my
# # num3 dear

# def fun1():
#     s="hi ansiya"
#     def fun2():
#         print(s)
#     fun2()
# fun1()
# # output
# # hi ansiya

# def cube(x):
#     return x*x*x
# cub = lambda x:x*x*x
# print(cube(4))
# print(cub(3))
# # output
# # 64
# # 27

# def swap(x,y):
#     t = x
#     x = y
#     y = t
#     print(x)
#     print(y)

# x = 2
# y = 3
# print(swap(x,y))
# swap(x,y)
# print(x)
# print(y)

# class Employee:
#     name = "roval"
#     age = 34
#     def intro(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
# obj = Employee()
# obj.intro()
# # output
# # Name: roval
# # Age: 34

# class Person:
#     def __init__(self,name):
#         self.name = name
        
#     def intro(self):
#         print(" hello,", self.name)
# obj = Person("ansiya")
# obj.intro()
# # output
# # hello, Name: ansiya

# class Maths:
#     def add(self, a, b=0):
#         return a + b
# obj = Maths()
# print(obj.add(5))
# print(obj.add(3,8))
# # output
# # 5
# # 11

# def myFun(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# args = ("Geeks", "Geeks","for")
# myFun(*args)
# kwargs = { "arg2": "for", "arg3": "Geeks","arg1": "Geeks"}
# myFun(**kwargs)
# # output:
# # arg1: Geeks
# # arg2: Geeks
# # arg3: for
# # arg1: Geeks
# # arg2: for
# # arg3: Geeks

# def myFun(*args, **kwargs):
# 	print("args: ", args)
# 	print("kwargs: ", kwargs)
# # Now we can use both *args ,**kwargs
# # to pass arguments to this function :
# myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

# # output
# # args:  ('geeks', 'for', 'geeks')
# # kwargs:  {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}