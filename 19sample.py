print("hello world")
print("\n\n")
# 1. amstrong number 
num = 153
strnum = str(num)
len_num= len(strnum)
ams=sum(int(digit)**len_num for digit in strnum)
print(ams,"\n\n\n")

#2. Prime number
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        # print("abcd")
    return True
c=0
for i in range(20):
    if prime(i):
        c +=1
    print(i,":",prime(i))
print("count:",c)

#3. 
