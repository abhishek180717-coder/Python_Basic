# with open("Data.txt", "r") as file:
#     data = file.read()
    
# print(data)    


# with open('students.txt', 'w') as f:
#     f.write('Rahul Sharma, 86, Bhopal\n')
#     f.write('Priya Verma, 92, Indore\n')
#     f.write('Amit Kumar,73,Jabalpur\n')
    
# with open('student.txt','a') as f:
#     f.write('Sneha Joshi,88, Bhopal\n')
    
# with open('student.txt', 'r') as f:
#     content = f.read()
# print(content)    
        
# with open('student.txt', 'r') as f:
#     for line in f:
#         name, marks, city = line.strip().split(',')
#         print(f'{name:<15} | {marks:>5} | {city}')
#         print("____________")    
    
    
#CSV File Processing:
# import csv 

# records = [
#     ['Name', 'Marks', 'city', 'Grade'],
#     ['Rahul', '85', 'Bhoapal', 'B'],
#     ['Amit', '87', 'Indore', 'A'],
#     ['Abhi', '89', 'Dhar', 'C'],
# ]   
# with open ('students.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)
    
    
# with open ('students.csv','r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row["Name"]}: {row["Marks"]} marks ({row["city"]})')
        
        
        
#CSV file Processsing Assignment:
import csv

records = [
      ['Name', 'Age', 'Marks1', 'Marks2', 'Marks3'],
      ['Rohan', '25', '77', '80', '79'],
      ['Anil', '35', '66', '95', '98'],
      ['Abhijeet', '15', '75', '90', '76'],
      ['Darshan', '45', '85', '85', '65'],
      ['Harshit', '55', '90', '75', '70'],  
]

with open('CLI.csv', 'w', newline='') as file:
    csv.writer(file).writerows(records)
    
student = input("enter student name:") 

found = False   
    
with open ('CLI.csv', 'r') as file:
    for row in csv.DictReader(file):
        if row ["Name"] == student:
            print(f"Name:{row["Name"]}, Age:{row["Age"]}, Marks1:{row["Marks1"]}, Marks2:{row["Marks2"]}, Marks3:{row["Marks3"]}")
            found = True
            break
    
if not found:        
    print("student Record not Found!")       
     