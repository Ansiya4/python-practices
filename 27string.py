# s = ('a', 'b', 'c', 'd')
# x = "".join(s)
# print(x)

# di = {
#     'a':1,
#     'b':2,
#     'c':3,
# }

# sep="hi"
# di["hi"] = 4
# h = sep.join(di)
# print(h)
# print(di)

tup =(1,2,3,4,5,1,2,6,7,8,2,3,5,1,2,7)
li=[]
val = []
for i in tup:
    if i not in li:
        li.append(i)
        val.append(tup.count(i))
dic= {i:j for i,j in zip(li,val)}
print(list(dict.fromkeys(tup)))



