# x = lambda a,b,c : a*b*c
# a = x(1,2,3)
# print(a)
# print(x(2,3,4))
l = ['a','b','c','d','e','f','g']
m = [1,2,2,1,1,1,3]
di= {i:j for i,j in zip(l,m)}
print(di)
print(di.values())
di = {i:m.count(i) for i in m}
x = [i for i in di if di.values()]
print()

# txt = "hello, my name is Peter, I am 26 years old"

# x = txt.split()

# print(x)