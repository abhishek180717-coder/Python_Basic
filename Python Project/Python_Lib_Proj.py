#Mini Project for Python and Libraries:-

#Student Performance Analysis:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Step1: Create Dataset:-
students = {
    "Name": ["Aman","Riya","Rahul","Neha","Karan","Priya","Amit","Pooja","Rohit","Sneha",
             "Vikas","Anjali","Sahil","Nisha","Deepak","Simran","Arjun","Meena","Yash","Komal",
             "Tarun","Kajal","Manish","Payal","Abhishek"],

    "Age": [20,21,22,20,21,20,22,21,20,21,
            22,20,21,20,22,21,20,21,22,20,
            21,20,22,21,20],

    "City": ["Indore","Bhopal","Indore","Ujjain","Bhopal","Indore","Ujjain","Indore","Bhopal","Ujjain",
             "Indore","Bhopal","Ujjain","Indore","Bhopal","Ujjain","Indore","Bhopal","Ujjain","Indore",
             "Bhopal","Indore","Ujjain","Bhopal","Indore"],

    "Math": [78,88,67,90,55,76,89,66,72,80,74,91,65,84,77,69,85,73,81,60,58,92,79,68,87],
    "Science": [80,85,70,88,60,79,84,69,75,82,71,89,67,81,76,72,83,74,78,62,61,90,80,70,86],
    "English": [75,82,68,91,58,77,86,64,73,79,72,88,66,83,75,71,84,76,80,61,59,91,78,69,85],
    "Computer": [90,94,72,96,65,85,93,71,78,87,79,95,70,88,82,74,91,77,89,68,64,97,84,73,92],
    "StudyHours": [4,6,3,7,2,5,6,3,4,5,4,7,3,5,4,3,6,4,5,2,2,7,5,3,6]
}

df = pd.DataFrame(students)

#Save CSV:-
df.to_csv("students.csv", index=False)

print("CSV Created Successfully")


#Step2: Load CSV:-
df = pd.read_csv("students.csv")

#Handle Missing Values:-
df.fillna(df.mean(numeric_only=True), inplace=True)

#Step3: Calculate Total, Average:-
subjects = ["Math","Science","English","Computer"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)

#Grade Function:-
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)

#Rank:-
df["Rank"] = df["Total"].rank(method="min", ascending=False).astype(int)


#Step4: Summary Statistics:-
print("\nClass Average:", round(df["Average"].mean(),2))

topper = df.loc[df["Total"].idxmax()]
print("\nTopper:", topper["Name"])

failure_rate = (df["Grade"]=="F").mean()*100
print("Failure Rate:", round(failure_rate,2),"%")

print("\nCity Wise Average")
print(df.groupby("City")["Average"].mean())


#Step5: Charts:-
# 1. Bar Chart:-
city_avg = df.groupby("City")["Average"].mean()

plt.figure(figsize=(6,4))
city_avg.plot(kind="bar")
plt.title("City Average Marks")
plt.ylabel("Average")
plt.show()

# 2. Pie Chart:-
plt.figure(figsize=(6,6))
df["Grade"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.ylabel("")
plt.show()

# 3. Scatter Plot:-
plt.figure(figsize=(6,4))
plt.scatter(df["StudyHours"], df["Average"])
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.title("Study Hours vs Average Marks")
plt.show()

# 4. Line Chart:-
df_sorted = df.sort_values("Rank")

plt.figure(figsize=(7,4))
plt.plot(df_sorted["Rank"], df_sorted["Average"], marker="o")
plt.xlabel("Rank")
plt.ylabel("Average")
plt.title("Rank vs Average")
plt.grid(True)
plt.show()

# 5. Heatmap:-
plt.figure(figsize=(6,5))
sns.heatmap(df[subjects].corr(), annot=True, cmap="coolwarm")
plt.title("Subject Correlation")
plt.show()


# Step 6: Save Files:-
df.to_csv("cleaned_students.csv", index=False)

summary = pd.DataFrame({
    "Class Average":[df["Average"].mean()],
    "Topper":[topper["Name"]],
    "Failure Rate":[failure_rate]
})

summary.to_csv("summary_report.csv", index=False)

print("\nProject Completed Successfully!")
print("Files Saved:")
print("1. students.csv")
print("2. cleaned_students.csv")
print("3. summary_report.csv")