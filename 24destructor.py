class A:
    def __init__(self,name=None,age=None):
        self.name = name
        self.age = age
        print("creation")
    def __del__(self):
        print("deletion")
    
new = A()
new.name = "ansiya"
new.age=11
print(new.name,new.age)

# del new
# print(new)

# class Employee:
  
#     # Initializing
#     def __init__(self):
#         print('Employee created')
  
#     # Calling destructor
#     def __del__(self):
#         print("Destructor called")
  
# def Create_obj():
#     print('Making Object...')
#     obj = Employee()
#     print('function end...')
#     return obj
  
# print('Calling Create_obj() function...')
# obj = Create_obj()
# print('Program End...')