d ={
    (1,2,3): '5',
    (1,2): '2',
    'c': '3',
}
def gen(d):
    for i,j in d.items():
        yield i,j
val = gen(d)
print(next(val))
print(next(val))

# top = 'a'
# print("\n",d.keys(),"\n\n",d.values(),"\n\n",d.items(),"\n\n",d,"\n\n")
# class a():
#     pass
# b= a()
# print(a())
# list1 =[1,2,1,3,42,4,5]
# a = list(dict.fromkeys(list1))
# list1=dict(list1)
# print(list1.keys())

