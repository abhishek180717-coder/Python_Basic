# class ThisIsMyFirstClass:
#     name = "Adtya"
#     age = 30
    
#     def getName(self):
#         print(self.name)
        

# firstobject = ThisIsMyFirstClass()
# print(firstobject)

# firstobject.getName()
# print(firstobject.name)

# class Student:
#     def __init__(self, name, age, gender, grade):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.grade = grade
           
#     def printDetails(self):
#         print("Name:", self.name)   
#         print("Age:", self.age)
#         print("Gender:", self.gender) 
#         print("Grade:", self.grade)
    
# mayur = Student("Mayur Sharma", 25, "Male", "12th")
# print(mayur)

# mayur.name = "Mayur Sharma"
# mayur.age = 25
# mayur.gender = "Male"
# mayur.grade = "12th"

#mayur.printDetails()
# print(mayur.name)
# print(mayur.age)
# print(mayur.gender)
# print(mayur.grade)

# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.counter += 1
        
# example_object_1 = ExampleClass()     
# example_object_2 = ExampleClass(2) 
# example_object_3 = ExampleClass(4)    

# print(example_object_1.__dict__, example_object_1.counter)
# print(example_object_2.__dict__, example_object_2.counter)
# print(example_object_3.__dict__, example_object_3.counter)


# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         ExampleClass.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2
        
# example_object = ExampleClass(1)
# print(example_object.a)  
# print(example_object.b) 


# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         ExampleClass.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
            
# example_object = ExampleClass(2)

# try:
#     print("a = ",example_object.a)
# except AttributeError:
#     try:
#         print("b =",example_object.b) 
#     except AttributeError:
#         print("The error has occured! Sliently passing it!")               

   
# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         ExampleClass.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
            
# example_object = ExampleClass(2)     

# if hasattr(example_object,'a'):
#     print("a =", example_object.a)
    
# if hasattr(example_object, 'b'):
#     print("b =", example_object.b)    
         
         

# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         ExampleClass.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
            
# example_object = ExampleClass(2)     

# if hasattr(example_object,'a'):
#     print("a =", example_object.a)
    
# if hasattr(example_object, 'b'):
#     print("b =", example_object.b) 
      
            
# print(hasattr(ExampleClass, 'b'))
# print(hasattr(ExampleClass, 'a'))  


# class ExampleClass:
#     a = 1
#     counter = 0
#     def __init__(self, val = 1):
#         ExampleClass.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
            
# example_object = ExampleClass(2)     

# if hasattr(example_object,'a'):
#     print("a =", example_object.a)
    
# if hasattr(example_object, 'b'):
#     print("b =", example_object.b) 
    
# print(hasattr(ExampleClass, 'b'))
# print(hasattr(ExampleClass, 'a'))               

# class Python:
#     population = 1
#     victims = 0
#     def __init__(self):
#         self.length_ft = 3
#         self.__venomous = False
        
# myObj = Python()
# print("myObj.population:", myObj.population)
# print("myObj.victims:", myObj.victims)
# print("muObj.length_ft:", myObj.length_ft)
# print("myObj.venomous:", myObj._Python__venomous)
#print("myObj.__venomous:", myObj.__venomous)
#print("myObj.venomous:", myObj.venomous)

#Name Mangling in Methods
class Classy:
    def visible(self):
        print("visible")
        
    def __hidden(self):
        print("hidden")
        
obj = Classy()
obj.visible()
try:
    obj,__hidden()
except:
    print("Failed")
obj._Classy__hidden()                