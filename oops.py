# class ThisIsMyFirstClass:
#     name = "Adtya"
#     age = 30
    
#     def getName(self):
#         print(self.name)
        

# firstobject = ThisIsMyFirstClass()
# print(firstobject)

# firstobject.getName()
# print(firstobject.name)

class Student:
    def __init__(self, name, age, gender, grade):
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = grade
        
    def printDetails(self):
        print("Name:", self.name)   
        print("Age:", self.age)
        print("Gender:", self.gender) 
        print("Grade:", self.grade)
    
mayur = Student("Mayur Sharma", 25, "Male", "12th")
print(mayur)

# mayur.name = "Mayur Sharma"
# mayur.age = 25
# mayur.gender = "Male"
# mayur.grade = "12th"

mayur.printDetails()
# print(mayur.name)
# print(mayur.age)
# print(mayur.gender)
# print(mayur.grade)