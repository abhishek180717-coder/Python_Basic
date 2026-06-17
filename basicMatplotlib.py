# import matplotlib.pyplot as plt
# import numpy as np
    
# #Data
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
# sales = [ 45, 55, 65, 70, 75, 80, 60, 40, 85, 90, 95, 50]    

# #Line Chart:
# plt.figure(figsize=(12,5))
# plt.plot(months, sales, marker='o', color='steelblue', linewidth=2, markersize=8)
# plt.fill_between(months, sales, alpha=0.15, color='steelblue')
# plt.title('Monthly Sales 2024(Rs.Thousand)', fontsize = 14, fontweight='bold')
# plt.xlabel('Months')
# plt.ylabel('Sales(Rs.k)')
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# # plt.show()


# cities = ['Bhopal', 'Indore', 'Gwalior', 'Jabalpur', 'Ujjain']
# students = [1200, 2800, 980, 850, 650]
# colors = ['#2196F3', '#4CAF50', '#FFC980', '#9C27B0', '#F44336']
# plt.figure(figsize=(9,5))
# bars = plt.bar(cities, students, color = colors, edgecolor = 'White', linewidth= 1.5)
# plt.title('Students Enrolled per City')
# plt.ylabel('Number of students')
# for bar, val in zip(bars, students):
#     plt.text(bar.get_x()+bar.get_width()/2,val+30,str(val),ha = 'center', fontweight ='bold')
# plt.tight_layout()    
# plt.show()


# study_hrs = np.random.uniform(2,10,50)
# marks = study_hrs * 7 + np.random.normal(0,8,50)
# marks = np.clip(marks, 30, 100)
# plt.figure(figsize=(8,5))
# plt.scatter(study_hrs, marks, c=marks, cmap ='RdYlGn', s=100, alpha=0.8)
# plt.colorbar(label='Marks')
# plt.title('Study Hours vs Exam Marks')
# plt.xlabel('Study Hours/Day')
# plt.ylabel('Exam Marks')
# plt.show()

