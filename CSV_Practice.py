# #CSV file Processsing Assignment:
# import csv

# records = [
#       ['Name', 'Age', 'Marks1', 'Marks2', 'Marks3'],
#       ['Rohan', '25', '77', '80', '79'],
#       ['Anil', '35', '66', '95', '98'],
#       ['Abhijeet', '15', '75', '90', '76'],
#       ['Darshan', '45', '85', '85', '65'],
#       ['Harshit', '55', '90', '75', '70'],  
# ]

# with open('CLI.csv', 'w', newline='') as file:
#     csv.writer(file).writerows(records)
    
# student = input("enter student name:") 

# found = False   
    
# with open ('CLI.csv', 'r') as file:
#     for row in csv.DictReader(file):
#         if row ["Name"] == student:
#             print(f"Name:{row["Name"]}, Age:{row["Age"]}, Marks1:{row["Marks1"]}, Marks2:{row["Marks2"]}, Marks3:{row["Marks3"]}")
#             found = True
#             break
    
# if not found:        
#     print("student Record not Found!")   