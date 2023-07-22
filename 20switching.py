def findtype(a,type):
    for x in a:
        if isinstance(x, type):
            print(x)

listtype= ['ansiya', 'rizana', 'nasrudeen','abhijith', 23, 56, 2.5, 7, 88.5555]
findtype(listtype,int)

b = "malayalam"
if b == b[::-1] :
    print('palindrome')
else:
    print("not palindrome")

def pali(x):
    if x == x[::-1] :
        print('palindrome')
    else:
        print("not palindrome")
pali("0000")

def numsum(number):
    total = (number*(number+1))/2
    print("total:", total)
numsum(20)

def uniq(num):
    num2=[]
    k=0
    for i in num:
        if i not in num2:
            num2[k] = i
            k = k+1
    print(num2)
list1=[1,2,1,2,3,4,5,6,3]
uniq(list1)
print("using set",list(set(list1)))

def uniq(num):
    num2 = [i for index, i in enumerate(num) if i not in num[:index]]
    print(num2)
list1 = [1, 2, 1, 2, 3, 4, 5, 6, 3]
uniq(list1)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "e" in x[2]]
print(newlist)
# output
#['cherry']


original_list = [1, 2, 1, 2, 4, 5, 3, 6]
unique_elements = list(dict.fromkeys(original_list))
print(unique_elements)
#output
#[1, 2, 4, 5, 3, 6]

def uniq(num):
    num2 = [i for index, i in enumerate(num) if i not in num[:index]]
    print(num2)
list1 = [1, 2, 1, 2, 3, 4, 5, 6, 3]
uniq(list1)
# output
# [1, 2, 3, 4, 5, 6]

list1 = [1, 2, 1, 2, 3, 4, 5, 6, 3]
seen = set()
duplicates = []
for item in list1:
    if item in seen and item not in duplicates:
        duplicates.append(item)
    else:
        seen.add(item)

print(duplicates)
# output
#[1, 2, 3]

def lenof(a):
    len = 0
    for _ in a:
        len +=1
    return len
print(lenof([1,2,2,3,4,5]))
#output
# 6

def dup(lis1):
    b=[]
    for i in lis1:
        c=0
        for x in range(lenof(lis1)):
            if i == lis1[x]:
                c += 1
        if c>1:
            if i not in b:
                b.append(i)
    return b
print(dup([1,1,2,4,3,5,4,2,6,7,8,9]))
#output
#[1, 2, 4]


class a:
    def __init__(self):
        print("haaiiiiiiiiii")
print(a().__init__())
# output:
# haaiiiiiiiiii
# haaiiiiiiiiii
# None

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "h" in x]
print(newlist)
# output:
# ['cherry']


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
# output:
# ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# output
# ['apple', 'orange', 'cherry', 'kiwi', 'mango']

