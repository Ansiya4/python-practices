a = [9,5,1,1,2,2,3,4,5,5,6,7,8,9,6,3,4,11,9]
l=[a[i] for i in range(len(a)) if a[i] not in a[:i]]
print(l)

# odd =[x for x in a if x%2 == 0]
# print(odd)
# li = [num if num%2 != 0 else 0 for num in a]
# print(li)
# print(list(dict.fromkeys(a)))
# b= ['a','b','c','d','e']
# di= {i:j for i,j in zip(b,a)}
# print(di)
z = " hello programming "
zl = z.split()
# print(zl)
# x =""
# print("".join(z.split()))

li = [ 'a','a','a', 'b','b','c','d','b']
from collections import Counter
print(dict(Counter(li)))
print({i:li.count(i) for i in li})
print([x for x in zl if x.startswith("he")])
class a:
    pass
z =a
print(z)