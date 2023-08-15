print("hello world\n")
# print("\n\n")
# 1. amstrong number 
# def gen(num):
#     num = 153
#     yield (num if sum(int(a)**len(str(num)) for a in str(num)) == num else False for a in str(num))

# print(next(gen(153)))
def gen(num):
    yield sum(int(a)**len(str(num)) for a in str(num)) == num
num = 150
print(next(gen(num))) 

# ams=sum(int(a)**len_num for a in strnum)
# print(ams,"\n\n\n")
# 2. Prime number
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
c=0
for i in range(20):
    if prime(i):
        c +=1
    print(i,":",prime(i))
print("count:",c)
#3. 
