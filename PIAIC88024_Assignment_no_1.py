#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[1]:


import numpy as np


# 2. Create a null vector of size 10 

# In[3]:


np.zeros(10)


# 3. Create a vector with values ranging from 10 to 49

# In[7]:


a = np.arange(10,50)
a


# 4. Find the shape of previous array in question 3

# In[6]:


a.shape


# 5. Print the type of the previous array in question 3

# In[8]:


type(a)


# 6. Print the numpy version and the configuration
# 

# In[2]:


import numpy as np
print(np.version.version, np.show_config())


# 7. Print the dimension of the array in question 3
# 

# In[15]:


print(a.ndim)


# 8. Create a boolean array with all the True values

# In[18]:


np.array([1,2,3,4,5],dtype = bool)


# 9. Create a two dimensional array
# 
# 
# 

# In[20]:


a = np.array([[1,2,3,4],[5,6,7,8]])
a


# 10. Create a three dimensional array
# 
# 

# In[25]:


a = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
a


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[27]:


a = np.array([1,2,3,4])
a[::-1]


# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[30]:


a = np.zeros(10)
a[4] = 1
a


# 13. Create a 3x3 identity matrix

# In[31]:


np.eye(3,3)


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[33]:


arr = np.array([1,2,3,4,5],dtype = float)
arr


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[37]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
arr1*arr2


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[39]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
arr = arr1==arr2
arr


# 17. Extract all odd numbers from arr with values(0-9)

# In[42]:


a = np.arange(10)
a[1::2]


# 18. Replace all odd numbers to -1 from previous array

# In[44]:


a = np.arange(10)
a[1::2] = -1
a


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[46]:


a = np.arange(10)
a[5:9] = 12
a


# 20. Create a 2d array with 1 on the border and 0 inside

# In[21]:


import numpy as np
x = np.ones((2,2))
x[:,:] = 0
x


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[48]:


arr2d = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
arr2d[1,1] = 12
arr2d


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[50]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[:,:] = 64
arr3d


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[56]:


a = np.arange(10).reshape(5,2)
a[0,:]


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[61]:


a = np.arange(10).reshape(5,2)
a[1,1]


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[65]:


a = np.arange(10).reshape(2,5)
a[0:2,2]


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[71]:


a = np.random.randint((10,10))
b= [5,6,7]
print("random numbers are ",a)
print(a.max())
print(a.min())


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# ---
# Find the common items between a and b
# 

# In[74]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.unique((a,b))


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[75]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a ==b)


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[78]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
#print(data)
print(data[names != "Will"])


# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[83]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
#print(data)
print(data[names == "Bob"])


# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[85]:


a = np.arange(1,16).reshape(5,3)*1.0
a


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[88]:


a = np.arange(1,17).reshape(2,2,4)
a


# 33. Swap axes of the array you created in Question 32

# In[91]:


np.transpose(a)


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[135]:



a = np.array([1,2,3,4,5,6,7,8,9,10])
b = np.sqrt(a)<0.5
a[b==0]


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[132]:


a = np.array(np.random.rand(12))
b = np.array(np.random.rand(12))
a+b


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[129]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[123]:


a = np.array([1,2,3,4,5]) 
b = np.array([5,6,7,8,9])
np.setdiff1d(a,b)


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[121]:


sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = np.array([[10,10,10]])
sampleArray[:,1] = newColumn
sampleArray


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[115]:


x = np.array([[1., 2., 3.], [4., 5., 6.]]) 
y = np.array([[6., 23.], [-1, 7], [8, 9]])
np.dot(x,y)


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[112]:


a = np.random.randn(20)
a.cumsum()

