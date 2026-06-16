import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Ashish', 'Dhruv'],
    'Age': [22, 25, 26, 24, 20],
    'Marks': [80, 75, 60, 90, 95],
    'City': ['Indore', 'Bhopal', 'Bhopal', 'Indore', 'Ujjain'],    
}
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.head(3))
print(df.dtypes)
print(df.describe) 


#Select Columns:
print("df['Name']: \n", df['Name'])
print(df[['Name', 'Marks']]) 

#Filter Rows:
print(df[df['Marks'] >= 85])
print(df[df['City'] == 'Bhopal'])
print(df[(df['Marks'] >= 80) & (df['City']=='Indore')])

def get_grade(x):
    if x >= 90:
        return 'A'
    elif x >= 75:
        return 'B'
    else:
        return 'C'
df['Grade'] = df['Marks'].apply(get_grade)
print(df['Grade'])
print("________________")
print(df)

#GroupBy - Like Excel Pivot:
city_avg = df.groupby('City')['Marks'].mean() 
print(city_avg)

#Read real CSV file:
df2 = pd.read_csv('students.csv')
print(df2)
df2['Name'] = df2['Name'].str.strip()
df2['Marks'] = df2['Marks'].str.replace('#', '')
df2['city'] = df2['city'].str.strip('#', '')
print(df2)
#Cleaning:

df2.to_csv('clean_output.csv', index=False)

 