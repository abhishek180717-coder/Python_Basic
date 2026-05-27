#print("Hello MindCoders!")


#age = 5

#print(age)


#myNamevariable -- camel casin

#my_Name_variable -- Snake casin  
     
     

#'''name = "Abhishek"

#profession = "Data Enginner"

#experience = 2     

#print("Hello, I am" ,name,". I am a" ,profeesion, profesionally. And I have around", experience,"years of experience with it." '''
      

    #'''python data type 

     # text- str 

      #numeric- int,float, complex

      #sequence- list,tuple,range

      #mapping- dict

      #set- set,frozenset

      #binary- bytes,bytearray,memoryview

      #none- nonetype'''
      
      

# x = 5 
# print(type(x))

# x = "Hello World"
# print(x)
# print(type(x))

# x = 20
# print(x)
# print(type(x))

# x = 20.5
# print(x)
# print(type(x))

# x = 1j
# print(x)
# print(type(x))

# x = ["apple", "banana", "cherry"]
# print(x)
# print(type(x))

# x = ("apple", "banana", "cherry")
# print(x)
# print(type(x))

# x = range(6)
# print(x)
# print(type(x))

# x = {"name" : "john", "age" : 36}
# print(x)
# print(type(x))

# x = {apple", "banana", "cherry"}
# print(x)
# print(type(x))

# x = frozenset({"apple,","banana","cherry"})
# print(x)
# print(type(x))

# x = True
# print(x)
# print(type(x))

# x = bytearray(5)
# print(x)
# print(type(x))

# x = memoryview(bytes(5)
# print(x)
# print(type(x))

# x = None
# print(x)
# print(type(x))



# x = 4

# print(x < 5 and x < 10)

# print(x > 5 or x > 10)

# print(x > 3 or x > 10)

# print(not(x > 3 or x > 10))'''


# x = ["Maruti", "BMW"]

# y = ["Maruti", "BMW"]

# z = x
# print(x is y)

# print(x is z)
# print(x is not y)

# print(x is not z)


# y = ["Maruti", "BMW"]




# name = input("Please enter your name:")

# print("Hello", name)




# z = int(x) + int(y)

# print("Sum:", z)




# While True:

# print("I'm stuck inside a loop!")



# largest_number = -999999999


# number =int(input("Enter a number or type -1 to stop"))


# while number != -1:

#     if number > largest_number:

#         largest_number = number

#     number = int(input("Enter a number or type -1 to stop:"))
    

# print ("The largest number is:", largest_number)'''
    
     

# number = int(input("Enter a number:"))


# count = 1

# even = 0

# odd = 0

# while count<=number:

#     if count % 2 == 0: 

#         even += 1

#     else:

#         odd += 1

#     count += 1
    

# print("Even= ", even)

# print("Odd= ", odd)'''



# for counter in range(100):

#     print("counter:", counter)
    
    

# for counter in range(2, 8):

#    print("The value of counter is currently:", counter)
   
   

# for counter in range(2, 8, 3):

#    print("The value of counter is currently:", counter)
   
   

# power = 1

# for expo in range(16):

#     print("2 to the power of", expo, "is", power)

#     power *= 2 
    
    
    

# print("The break instruction:")

# for counter in range(1, 6):

#     if counter == 3:

#      break

#     print("Inside the loop.", counter)

# print("outside the loop.")



# print("The break instruction:")

# for counter in range(1, 6):

#     if counter == 3:
#      continue 

#     print("Inside the loop.", counter)

# print("outside the loop.")
              
    


  # var = 10 

# print(var > 0)

# print(not (var <= 0))


# var = 10

# print(var != 0)

# print(not (var == 0))


# numbers = [10, 5, 7, 2, 1]
# print(type(numbers))

# print(numbers[2])


# numbers = []

# numbers = [1, 2, 3, 4, 5]

# print(numbers)
# print(type(numbers))

# print("first element contents", numbers[0])

# print("second element contents", numbers[1])

# print("third element contents", numbers[2])

# print("fourth element contents", numbers[3])

# print("five element contents", numbers[4])


# numbers[0] = 10

# print("numbers[0] after modification:",numbers[0])
# print(numbers)


# numbers[1] = numbers[4]
# print(numbers)
# print(len(numbers))

# del numbers[2]
# print(numbers)
# print(len(numbers))


# print(numbers[-1])

# print(numbers[-2])

# print(numbers[-3])

# print(numbers[-4])



# numbers = [1, 2, 3, 4, 5]
# print(len(numbers))

# del numbers[-1]
# print(numbers)

# numbers[len(numbers)//2] = int(input("Enter a number:"))
# print(numbers)



# list = [5, 4, 3, 2, 1]
# print(list)

# list.append(6)
# print(list)


# list.insert(0, 0)
# print(list) 


# for temp in range (1, 7):

#   print(""+str(temp)*temp)


# for temp in range (1, 7):
#   print(str(temp)*temp)

# my_list = [1, 2, 3, 4, 5,  6, 7, 8, 9, 10]
# for iterator in range(len(my_list)):
#   print(my_list[iterator])

# list =[]
# for iterator in range(1, 11):
#   list.append(iterator)
# print(list)  

# list =[]
# for iterator in range(10):
#   list.append(iterator+1)
# print(list)  

# list =[10, 20, 30, 40, 50, 60, 70, 80, 90,100]
# for iterator in range(len(list)):
#   list[iterator] = list[iterator] +1
  
# print(list)



# list =[10, 20, 30, 40, 50, 60, 70, 80, 90,100]
# for iterator in range(len(list)):
#   list[iterator] += 1
  
# print(list)


# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# sum = 0
# for iterator in range(len(lst)):
#   sum += lst[iterator]

# print(sum)


# variable1 = 5
# variable2 = 10

# print("Variable1:", variable1)
# print("Variable2:", variable2)

# variable1, variable2 = variable2, variable1

# print("Variable1:", variable1)
# print("Variable2:", variable2)

# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# list[4], list[1] = list[1], list[4]

# print(list)           


# print("list(+1)")

# Github
# git add *
# git commit -m "edit name"
# git push
  
  
      