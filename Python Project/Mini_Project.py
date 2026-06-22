# BMI Calculator (Height in Meter or Feet):-

weight = float(input("Enter your weight (kg): "))

print("\nChoose height unit:")
print("1. Meter")
print("2. Feet")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    height = float(input("Enter height in meters: "))
elif choice == "2":
    height_ft = float(input("Enter height in feet: "))
    height = height_ft * 0.3048  # Convert feet to meters
else:
    print("Invalid choice!")
    exit()

bmi = weight / (height ** 2)

print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
    
    
    
    
    




# #Name Card Program:-

# first_name = input("Enter First Name: ")
# last_name = input("Enter Last Name: ")
# age = input("Enter Age: ")
# city = input("Enter City: ")
# skill = input("Enter Favourite Skill: ")

# name = first_name + " " + last_name

# print("\n" + "-" * 50)
# print(f"| {'NAME':<10}: {name:<33}|")
# print(f"| {'AGE':<10}: {age + ' years':<33}|")
# print(f"| {'CITY':<10}: {city:<33}|")
# print(f"| {'SKILL':<10}: {skill:<33}|")
# print("-" * 50)