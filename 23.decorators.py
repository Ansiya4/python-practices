# def modifyMul(Nice):
#     def add(A, b):
#         res = Nice(A + b)
#         return res
#     return add

# @modifyMul
# def mul(x):
#     return 2 * x
# print(mul(6,4))


# def modmul(nice):
#     def mul(a,b):
#         res =nice(a+b,5)
#         return res
#     return mul

# @modmul
# def mul(a,b):
#     return a*b
# print(mul(10,20))

# def modifydiv(func):
#     def div(a,b):
#         if b == 0:
#             return a+b
#         else:
#             return func(a,b)
#     return div

# @modifydiv
# def div(a,b):
#     print(a)
#     print(b)
#     return a/b
# print(div(9,0))

# def modify_add(func):
#     def add(*args):
#         res=0
#         for arg in args:
#             res = res+arg
#         return func(res)
#     return add

# @modify_add
# def add(a):
#     return 100+a

# print(add(40,30,50,1000))

# def modifyadd(func):
#     def add(*args):
#         res=0
#         for i in args:
#             res=res+i
#         res=func(res)
#         return res
#     return add

# @modifyadd
# def add(a):
#     return 100+a
# print(add(10,20,30,40,50))
# print(add(100,1000))

import time
def measure_time(original_function):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = original_function(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        return result
    return wrapper_function

@measure_time
def count_down(number):
    for i in range(number, 0, -1):
        print(i)
        time.sleep(2)
count_down(5)
