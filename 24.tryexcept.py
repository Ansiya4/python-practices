# def div(a,b):
#     # try:
#     #     res = a/b
#     # except:
#     #     print("divition by zero not possible")
#     #     res= None
#     if a>0:
#         print("bbbbbbbbb")
#         res= a/b
#     print("aaaaaaaaaaaaaa")
#     return res

# a=10
# b=0
# ans = div(a,b)
# print(ans)
    
# def index(a,value):
#     try:
#         a[value]
#     except:
#         print("out of index")
#         return None
#     return a[value]
# li = [1,2,3,4]
# val=5
# print(index(li,val))
    
class Accident(Exception):
    def _init_(self,msg):
        self.msg=msg
    def pri(self):
        print(self.msg)

try:
    t=str(input('Enter:'))
    Accident(t)
    if t=='crash':
        raise Accident('CRAAAAASH')
except Accident as error:
    error.pri()
else:
    A=Accident(t)
    A.pri()
