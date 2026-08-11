import numpy as np
import pandas as pd

# 
# #for DataFrame to CSV File convert
# # df.to_csv ('Friends.csv', index = False)     #for DataFrame to CSV File convert without index

# print(df.describe())                           #for Numerical Calculation like (count, mean, std, min, 25%, 50%, 75%, max)
# print(df.head(2))                              #for  show start 2 rows
# print(df.tail(2))                              #for show last 2 rows
 
# import pandas as pd
# Harsh = pd.read_csv ("Friends.csv")
# print(Harsh)

# print(Harsh["City"])
# Harsh.index = ['First','Second', 'Third', 'Fourth', 'Fifth']
# print(Harsh)



Ser = pd.Series(np.random.rand(20))
print(Ser)
print(type(Ser))

newdf = pd.DataFrame(np.random.rand(100, 5), index = np.arange(100))
print(newdf)
print(type(newdf))

# print(newdf.head())               #Show Start 5 Rows
# print(newdf.head)               #Show all Rows
# print(newdf.describe())           #Show Numerical Calculation
# print(newdf.dtypes)               #Datatype batata hai
# print(newdf.index)                #Index ki range batata hai
# print(newdf.columns)              #Column ki range batata hai

# newdf1 = newdf.to_numpy()         #for Convert numpy array
# print(newdf1)

# newdf1 = newdf.T                   #Transform row=column, column=row
# print(newdf1)


# newdf1 = newdf.sort_index(axis=0, ascending=False)   #Reverse indexing start with (99-0)
# print(newdf1)

# newdf1 = newdf.sort_index(axis=1, ascending=False)   #Reverse indexing start with (4-0)
# print(newdf1)

# newdf1 = newdf[0]
# print(newdf1)               #only 0 Column show
# print(type(newdf1))         #Show Datatype


# newdf2 = newdf
# newdf2[0][0] = 9876
# print(newdf)