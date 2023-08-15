a = [1,2,3,4,5]

s ={1,2,3}

t = (1,2,3)

di={
    'a':1,
    'b':2,
    'c':3
    }
l1 = ["one", "two", "three", "four"]
l2 = [1,7,1,2,3,4,2,1,4,5,6,1]
print(set(l2))

t1 = (1,2,3,4)
dic ={'one': 1, 'two': 2, 'three': 3, 'four': 4}
d = {str(key):value for key, value in zip(l1,t1)}
print(d)
ad = list(dict.fromkeys(l2))
print(ad)
s = " hello world "
s1 = [x for x in s] 
string = "one two three four"
y = [x for x in string.split()]
print(y)
print(string.split())

