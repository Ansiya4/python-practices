# s= "hellooooddsadf"
# print(s[0].upper())
# str = "Hello" 

# print('C://python37') # prints C://python37 as it is written    
# print("The string str : %s"%(str))
# print("The string str : %s",(str))

# b = "   Hello, my, World!    "
# print(b.split())
# print(b[:-5:-1])
# print(b[-5:-1])
# print(b[8:12])
# print(b.strip())
# print(b.replace("H","h").strip())
# print(b.strip().split("o"))
# t =('a', 'b','c')
# s="".join(t)
# print(s)
# d ={"a":1,
#     "b":2}
# sep = 'test'
# print(" ".join(d))
# print(d)
# aa = [ "a","b","c","d"]
# bb = ('x','y')

# [print(x) for x in aa]

# aa.insert(4,"e")
# print(aa)

# aa[2]='xx'
# print(aa)
# aa.extend(bb)
# print(aa)
# aa.remove('x')
# print(aa)
# aa.pop(1)
# print(aa)
# del aa[1]
# aa.clear()
# print(aa)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# print([x for x in fruits if 'p' in x])
# print(['orange' if x=='banana' else x for x in fruits])

# d ={
#     'a':1,
#     'b':2,
#     'c':3,
#     'd':4
# }
# print(d.keys())
# print(d.values())
# print(d.items())
# print(d['c'])
# for i in d:
#     print(i)
# d['d'] = 10
# print(d)
# if 'c' in d:
#     print("yes")
# x = d.get('d')
# print(x)
# d.update({'d':4})
# d.update({'d':10})
# print(d)
# for i in d:
#     print(d[i])
# for i,j in d.items():
#     print(i,j)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("year", 1222)
car['color'] = 'black'
print(x)
print(car)