'''
Use the following code for the questions below:

        a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

1. How many negative numbers are there? 
Write code with python version 3 using the numpy library to list and count how many negative numbers are in this array: 
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
'''
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

negatives = a[a < 0]
count_negatives = len(negatives)

print("There are", count_negatives, "negative numbers in the array:", negatives)

'''
2. How many positive numbers are there?
Write code with python version 3 using the numpy library to list and count how many positive numbers are in this array: 
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
'''
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

positive_numbers = a[a > 0]
count = positive_numbers.size

print("The positive numbers in the array are:", positive_numbers)
print("The number of positive numbers in the array is:", count)


'''
3. How many even positive numbers are there?
Write code with python version 3 using the numpy library to list and count how many even positive numbers are in this array: 
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
'''
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# Get the positive numbers
positive_numbers = a[a > 0]

# Get the even numbers
even_numbers = positive_numbers[positive_numbers % 2 == 0]

# Count the number of even positive numbers
count = len(even_numbers)

print("The number of even positive numbers is: ", count)
print("Positive even numbers in this array are: ", even_numbers)

'''
4. If you were to add 3 to each data point, how many positive numbers would there be?
Write code with python version 3 using the numpy library to add 3 to each data point in the array, show the new array, and count the positive numbers in the new 
array: a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
'''
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# Adding 3 to each data point in the array
b = a + 3

# Showing the new array
print("The new array after adding 3 to each data point:", b)

# Counting the positive numbers in the new array
count = np.count_nonzero(b > 0)
print("The number of positive numbers in the new array:", count)

'''
5. If you squared each number, what would the new mean and standard deviation be?
Write code with python version 3 using the numpy library to square each number in the array and then calcuate new mean and standard deviation for this array:
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
'''
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# square each number in the array
squared_array = a**2

# calculate the mean of the squared array
mean = np.mean(squared_array)

# calculate the standard deviation of the squared array
std_dev = np.std(squared_array)

# display the results
print("Squared Array: ", squared_array)
print("Mean of Squared Array: ", mean)
print("Standard Deviation of Squared Array: ", std_dev)

'''
6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting 
the mean from each data point. Center the data set. See this link for more on centering.
Write code with python version 3 using the numpy library to center the array so that the new mean is 0. Show the new mean and the new array.
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
'''
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
mean = np.mean(a)
centered_array = a - mean
new_mean = np.mean(centered_array)

print("New Mean: ", new_mean)
print("New Array: ", centered_array)
print("Old Mean: ", mean)

'''
7. Calculate the z-score for each data point. Recall that the z-score is given by:
Write code with python version 3 using the numpy library to calculate the z-score for each data point for this array:
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
'''
import numpy as np

# Define the array
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# Calculate the mean and standard deviation of the array
mean = np.mean(a)
std = np.std(a)

# Calculate the z-score for each data point
z_scores = (a - mean) / std

# Print the z-scores
print("Z-Scores: ", z_scores)



