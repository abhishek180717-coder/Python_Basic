with open("Data.txt", "r") as file:
    data = file.read()
    
print(data)    


with open('students.txt', 'w') as f:
    f.write('Rahul Sharma, 86, Bhopal\n')
    f.write('Priya Verma, 92, Indore\n')
    f.write('Amit Kumar,73,Jabalpur\n')
    
with open('student.txt','a') as f:
    f.write('Sneha Joshi,88, Bhopal\n')
    
with open('student.txt', 'r') as f:
    content = f.read()
print(content)    
        
with open('student.txt', 'r') as f:
    for line in f:
        name, marks, city = line.strip().split(',')
        print(f'{name:<15} | {marks:>5} | {city}')
        print("____________")    
    