# # A Simple Python program to demonstrate working
# # of yield

# # A generator function that yields 1 for the first time,
# # 2 second time and 3 third time


# def simpleGeneratorFun():
# 	yield 1
# 	yield 2
# 	yield 3

# v=simpleGeneratorFun()
# print(next(v))
# print(next(v))
# print(next(v))
# # output
# # 1
# # 2
# # 3

# def simpleGeneratorFun():
# 	yield 1
# 	yield 2
# 	yield 3

# v=simpleGeneratorFun()
# for i in v:
# 	print(i)
# # output
# # 1
# # 2
# # 3

# def simpleGeneratorFun():
# 	yield 1
# 	yield 2
# 	yield 3

# v=simpleGeneratorFun()
# while True:
# 	try:
# 		print(next(v))
# 	except StopIteration:
# 		break
# # output
# # 1
# # 2
# # 3

# function to print even numbers
def simpleGeneratorFun(l):
    for i in range(l):
	    if i%2==0:
		    yield i
v=simpleGeneratorFun(10)
while True:
	try:
		print(next(v))
	except StopIteration:
		break
# output
# 0
# 2
# 4
# 6
# 8

# # Function to print sum of n Natural numbers
# def simpleGeneratorFun():
#     for i in range(10):
#         sum = i * (i+1)/2
#         yield int(sum)
# v=simpleGeneratorFun()
# while True:
# 	try:
# 		print(next(v))
# 	except StopIteration:
# 		break
# # output
# # 1
# # 3
# # 6
# # 10
# # 15
# # 21
# # 28
# # 36
# # 45

# #generator expression
# generator = (i for i in range(10) if i % 2 == 0)
# for i in generator:
#     print(i)

# generator = [i for i in range(10) if i % 2 == 0]
# print(generator)


# def fib(l):
# 	a = 0
# 	b = 1
# 	for i in range(l):
# 		num = a
# 		a = a+b
# 		b = num
# 		yield num

# limit = fib(10)
# print(next(limit))
# print(next(limit))
# print(next(limit))
# print(next(limit))
# print(next(limit))
# print(next(limit))

# for i in fib(limit):
# 	print(i)
