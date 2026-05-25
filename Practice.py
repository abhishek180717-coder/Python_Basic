#14/5/26

#1
# name = "Abhishek"
# age = 20
# course = "Python AIML"

# print("Name:", name)
# print("Age:", age)
# print("Course:", course)
  
#2
# name1 = "Abhishek"
# age1 = 20
# course1 = "Python AIML"

# print ("Student 1")
# print("Name:", name1)
# print("Age:", age1)
# print("Course:", course1)


# name2 = "Harshit"
# age2 = 22
# course2 = "AI Engineer"

# print("Student 2")
# print("Name:", name2)
# print("Age:", age2)
# print("Course:", course2)


# name3 = "Divyraj"
# age3 = 20
# course3 = "Java"

# print ("Student 3")
# print("Name:", name3)
# print("Age:", age3)
# print("Course:", course3)

#3
# a = 30
# b = 50

# a = a + b

# print ("Sum:", a)

#4
# a = 5.5
# b = 2.4

# a = a * b

# print("Multiplication:", a)

#6
# a = -40
# b = 20

# sum = a + b

# print("Sum:", sum)

#7
# a = 65
# b = 30

# difference = a - b

# print("Difference:", difference)


#10
# a = 53
# b = 5

# floor_division = a // b

# print("Floor_division:", floor_division)

#11
# a = 28
# b = 3

# remainder = a % b

# print("Remainder:", remainder)

#12
# a = 4
# b = 3

# power = a ** b

# print("Power:", power)


# 14/5/26
# #1
# print("******")
# print("*    *")
# print("*    *")
# print("*    *")
# print("*    *")
# print("******")

# #2
# print("*******")
# print("*******")
# print("*******")
# print("*******")
# print("*******")
# print("*******")

# #3
# print("######")
# print("#    #")
# print("#    #")
# print("#    #")
# print("######")

# #4
# print("#######")
# print("#######")
# print("#######")
# print("#######")
# print("#######")
# print("#######")
# print("#######")

# #5
# n = 6
# for i in range(1, n+1):
#      print((str(i) + " ")* i)
     
# #6
# print("    *    ")
# print("   * *   ")
# print("  *   *  ") 
# print(" *     * ")  
# print("***   ***")
# print("  *   *  ")
# print("  *   *  ")
# print("  *****  ")
  
  
# 16/5/26

# #1
# a = 10
# b = 20

# print("Sum =", a + b)

# #2
# a = 80 
# b = 30

# print("Difference =", a - b)

# #3
# a = 20
# b = 10

# print("Multiplication =", a * b)

# #4
# a = 50
# b = 5

# print("Division =", a / b)

# #5 
# a = 98
# b = 3

# print("Floor_division =", a // b)

# #6
# a = 100
# b = 3

# print("Remainder =", a % b)

# #7
# a = 5
# b = 2

# print("Power =", a ** b)


#24/05/26
#1
# numbers = [1, 2, 3, 4, 5]
# print(len(numbers))

# numbers.pop()

# numbers[len(numbers)//2] = int(input("Enter a number:"))

# print(numbers)


# #2
# beatles = []

# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")

# print("Current band members:", beatles)

# for member in ["Stu Sutcliffe", "Pete Best"]:
#     beatles.append(member)
# print("After adding new members:",beatles)

# del beatles[-1]
# del beatles[-1]

# print("After removing members:", beatles)

# beatles.insert(0, "Ringo Starr")

# print("Final Beatles list:")
# print(beatles)
# print("Number of members:", len (beatles))


# #3
# for i in range(1, 51):

#     if i % 3 == 0 and i % 5 == 0:
#         print("FizBuzz", end=", ")

#     elif i % 3 == 0:
#         print("Fiz", end=", ")

#     elif i % 5 == 0:
#         print("Buzz", end=", ")

#     else:
#         print(i, end=", ")

# #4
# string = "MindCoders password2 is : 1234"

# count = 0

# for ch in string:
#     if ch.isdigit():
#         count += 1

# print("Total number of Digits =", count)

# #5
# string = "U r a a n S 0 f t s k i l l 1 s 1234"

# count = 0

# for ch in string:
#     if ch.isdigit():
#         count += 1

# print("Total number of Digits =", count)

# #6
# string = "MindCoders"

# count = 0

# for ch in string:
#     if ch == 's' or ch == 'S':
#         count += 1

# print("Total count =", count)

# #7.1
# string = "UraanSoftskills"

# repeated = 0
# unique = 0

# for ch in string:
#     if string.count(ch) > 1:
#         repeated += 1
#     else:
#         unique += 1

# print("Repeated characters =", repeated)
# print("Unique characters =", unique)

# #7.2
# string = "UraanSoftskills"

# for ch in string:
#     print(ch, "=", string.count(ch))

# #7.3
# user_word = input("Enter a word: ")

# user_word = user_word.upper()

# word_without_vowels = ""

# for letter in user_word:

#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue

#     word_without_vowels += letter

# print(word_without_vowels)

#24/5/26
#1
for i in range(1, 11):
    print(i) 

#2
for i in range(1, 11):
    if i % 2 == 0:
        print(i)    
        
#3
sum = 0

for i in range(1, 16):
    sum += i

print("Sum =", sum)

#4
sum = 0

for i in range(1, 16):
    if i % 2 != 0:
        sum += i

print("Sum of odd numbers =", sum)

#5
num = 15

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
#6
numbers = [1, 2, 4, 6, 88, 125]

for i in numbers:
    print(i)
    
    
#7
number = 129475

count = 0

while number > 0:
    number = number // 10
    count += 1

print("Total digits =", count)

#8
string = "madam"

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")  
    
#9
word = input("Enter a word: ")

reverse = word[::-1]

print("Reversed word =", reverse)     

#10
num = 153

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")                

 