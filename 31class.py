class vehicle:
    def __init__(self,model, price):
        self.model = model
        self.price = price
    def show(self):
        print("Model:",self.model)
        print("Price:",self.price)

class car(vehicle):
    def __init__(self, model, price,company):
        super().__init__(model, price)
        self.company = company
    def show(self):
        super().show()
        print("Company:",self.company)

a = car("X12",1000,"audi")
b = car("Z11",100, "Pajero")
a.show()        
b.show()

# class Student:    
#     def __init__(self,name,id,age):    
#         self.name = name;    
#         self.id = id;    
#         self.age = age    
#     def display_details(self):    
#         print("Name:%s, ID:%d, age:%d"%(self.name,self.id))    
# s = Student("John",101,22)    
# print(s.__doc__)    
# print(s.__dict__)    
# print(s.__module__)    