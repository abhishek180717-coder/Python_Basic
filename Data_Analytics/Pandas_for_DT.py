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



# Ser = pd.Series(np.random.rand(20))
# print(Ser)
# print(type(Ser))

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

# newdf1 = newdf[0]           #only 0 Column show
# print(newdf1)               
# print(type(newdf1))         #Show Datatype

# newdf2 = newdf[:]           #for copy
# newdf2 = newdf.copy()       #for copy

# newdf.loc[0,0] = 1432       #for change any number of rows and columns (0 row,0 column ka chnage kiya)
# print(newdf.head(2))


newdf.columns = list("ABCDE")         #For change columns name 
print(newdf)

# newdf.loc[0,'A'] = 6262                #for change number of rows and column
# print(newdf)

# newdf.loc[0,0] = 6162                  #for change number of rows and column
# print(newdf)

# Drop = newdf.drop(0, axis=1)             #for Drop 0 name columns
# print(Drop)

# Drop1 = newdf.drop(1, axis=0)             #for Drop 1 name (index or row)
# print(Drop1)

# newdf1 = newdf.loc[[1, 2], [2, 3]]        #for show only 1,2 row and 2,3 column
# print(newdf1) 

# newdf1 = newdf.loc[[1, 2, 3], :]            #for show only 1,2,3 row and all column
# print(newdf1) 


# newdf1 = newdf.loc[:, [1, 2]]               #for show all row and 1,2 column
# print(newdf1) 


# newdf_filter = newdf.loc[(newdf[0]<0.3) & (newdf[2]>0.1)]       #for filter return only (column0 < 0.3 & column2 > 0.1)
# print(newdf_filter)

# newdf1 = newdf.iloc [0, 4]                    #Return row 0 & column 4 ki value
# print(newdf1)

# newdf1 = newdf.iloc [[0, 4], [1, 2]]                    #Return row 0 & column 1,2 and row 4 & column 1,2
# print(newdf1)

# newdf_delete = newdf.drop ([0,1,2])              #for delete a row Ex(0,1,2)
# print(newdf_delete)

# newdf_delete = newdf.drop ([1,2], axis=1)        #for delete a column Ex(1,2)
# print(newdf_delete)

# newdf.drop (['A', 'D'], axis=1, inplace=True)      #for delete a column Ex(A, D)
# print(newdf)                                       #inplace = False (original ko chnage nhi karta hai ,change ko newdf me save karta hai)                                                ##inplace = False (original ko chnage nhi karta hai ,change ko newdf me save karta hai)
# print(newdf.head())                                #inplace = True (original DataFrame ko wahi par modify karta hai)


# newdf.drop ([2, 4], axis=0, inplace=True)          #for delete a row Ex(2, 4)
# print(newdf)                                       #inplace = False (original ko chnage nhi karta hai ,change ko newdf me save karta hai)                                                ##inplace = False (original ko chnage nhi karta hai ,change ko newdf me save karta hai)
# print(newdf.head())                                #inplace = True (original DataFrame ko wahi par modify karta hai)

# newdf = newdf.reset_index()                      #index name ka ek or column ban jayenga jo 0 se start hoga 
# print(newdf)
# print(newdf.head())

# newdf = newdf.reset_index(drop=True)              #index(drop=True) likhne se index ka column hat jayenga but index 0 se hi start hogi
# print(newdf)
# print(newdf.head())

# newdf = newdf['A'].isnull()                       #Return False in column A
# print(newdf)

# newdf['B'] = None                                   #Return None in all comlumn B
# print(newdf)

# newdf['B'] = None
# newdf = newdf['B'].isnull()                            #Return True in column B 
# print(newdf)

# newdf.loc[:, ['B']] = 30                           #Return 30 in all column B
# print(newdf)

# df = pd.DataFrame(  
#         {
#          "name": ["Alfred", "Batman", "Catwoman"],
#          "toy": [np.nan, "Batmobile", "Bullwhip"],
#          "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT],
#     }
# )
# df = df.dropna()                           #Delete NA value 
# print(df)



# df = pd.DataFrame(  
#         {
#          "name": ["Alfred", "Batman", "Catwoman"],
#          "toy": [np.nan, np.nan, np.nan],
#          "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT],
#     }
# )
# df = df.dropna(how = 'all', axis=1)           #for delete nan value in column
# print(df)


df = pd.DataFrame(  
        {
         "name": ["Alfred", "Batman", "Alfred"],
         "toy": [np.nan, "Batmobile", "Bullwhip"],
         "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT],
    }
)
# df = df.drop_duplicates(subset=['name'], keep='first')    #for delete duplicate name, Ex Alfred are 2 times in Dataframe 
print(df)                                                 #for (keep=first used for first value, keep=last used for last value, keep=False used for remove both value)

# print(df.shape)          #show shape (2, 3)

# df.info()                #for all information about DataFrame
# print(df)

# df['born'].value_counts(dropna = True)

# df = df.notnull()         #NaN=False ho jata hai baki True
# print(df)


# df = df.isnull()            #NaN=True ho jata hai baki False
# print(df)


import pandas as pd
data = pd.read_csv('Friends.csv')
data.iloc[0,1] = 35
print(data)