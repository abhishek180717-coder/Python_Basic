# import numpy as np

# #Creating Array
# arr1d = np.array([1, 2, 3, 4, 5])
# arr2d = np.array([[85,90,78],[72,88,95],[91,76,83]])

# print(arr2d.shape)
# print(arr2d.dtype) 
# print(arr2d.ndim)

# #Zeros
# zeros = np.zeros((3, 4))  #Give all 0 in 3 * 4
# print(zeros)

# #Ones
# ones = np.ones((2,5))   #Give all 1 in 2 * 5
# print(ones)

# #Arange
# rng = np.arange(0, 50, 5)   #Give array of range from 0 to 50 with different of 5
# print(rng)

# #Linspace
# lin = np.linspace(0, 1, 11)    #Give 11 sequence of 0 to 11
# print(lin)

# #Random
# random = np.random.randint(40, 100,(5, 3))   #Give random number from 40 to 100 in 5 * 3
# print(random)


#Vectorized 
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr * 2)
print(arr + 5)
print(arr ** 2) 


Marks_2d = np.array(([85,90,78],[72,88,95],[91,76,83]))
print(np.mean(Marks_2d))
print(np.mean(Marks_2d, axis = 1))
print(np.mean(Marks_2d, axis = 0))
print(np.max(Marks_2d))
print(np.std(Marks_2d))  


#Boolean Indexing (Data Filtering)
arr = np.array([55,82,43,91,67,78,35,88])
print(arr[arr>70]) 



