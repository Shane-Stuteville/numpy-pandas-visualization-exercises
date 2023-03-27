'''
Use pandas to create a Series named fruits from the following list:

["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

Use Series attributes and methods to explore your fruits Series.

1. Determine the number of elements in fruits.
Write code with python version 3 using the numpy and pandas libraries to determine the number of elements in the following list
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
'''
import numpy as np
import pandas as pd

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

fruits_series = pd.Series(fruits)

number_of_elements = fruits_series.count()

print("Number of elements in the list:", number_of_elements)

'''
2. Output only the index from fruits.
Write code with python version 3 using the numpy and pandas libraries to output only the index from the following list:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

'''
import pandas as pd

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", 
          "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", 
          "blueberry", "blackberry", "gooseberry", "papaya"]

fruits_df = pd.DataFrame(fruits, columns=["Fruit"])
print(fruits_df.index)

'''
3. Output only the values from fruits.
Write code with python version 3 using the numpy and pandas libraries to output only the values from the following list:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
'''
import pandas as pd

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

df = pd.DataFrame(fruits, columns=['Fruits'])

print(df['Fruits'].values)


'''
4. Confirm the data type of the values in fruits.
Write code with python version 3 using the numpy and pandas libraries to confirm the data type of the values in following list:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
'''
import numpy as np
import pandas as pd

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

fruits_array = np.array(fruits)
fruits_series = pd.Series(fruits_array)

print("The data type of the values in the list is:", fruits_series.dtype)

'''
5. Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
Write code with python version 3 using the numpy and pandas libraries to output the first five values, then the last three values, and then output 
two random values from following list:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

'''
import numpy as np
import pandas as pd

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", 
          "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", 
          "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

df = pd.DataFrame(fruits, columns=['Fruits'])

# First five values
print("First five values:")
print(df.head())

# Last three values
print("\nLast three values:")
print(df.tail(3))

# Two random values
print("\nTwo random values:")
print(df.sample(2))


''' 
6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.
Write code with python version 3 using the numpy and pandas libraries to run .describe() on the following list:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

'''
import numpy as np
import pandas as pd

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

s = pd.Series(fruits)
print(s.value_counts())

'''

7. Run the code necessary to produce only the unique string values from fruits.
Write code with python version 3 using the numpy and pandas libraries necessary to produce only the unique string values from the following list:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
'''
import numpy as np
import pandas as pd

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

# Convert the list to a pandas series
fruits_series = pd.Series(fruits)

# Get the unique values using unique() method
unique_fruits = fruits_series.unique()

# Print the unique values
print("Unique values in the fruits list:")
print(unique_fruits)

'''

8. Determine how many times each unique string value occurs in fruits.
Write code with python version 3 using the numpy and pandas libraries to determine how many times each unique string value occurs in the following list:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
'''
import numpy as np
import pandas as pd

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", 
          "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", 
          "blueberry", "blackberry", "gooseberry", "papaya"]

# Convert the list to a pandas DataFrame
fruits_df = pd.DataFrame(fruits, columns=['Fruits'])

# Group the data by 'Fruits' and count the occurences of each unique value
counts = fruits_df.groupby(['Fruits']).size().reset_index(name='Counts')

# Print the result
print(counts)


'''

9. Determine the string value that occurs most frequently in fruits.
Write code with python version 3 using the numpy and pandas libraries to determine the string value that occurs most frequently in the following list:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

'''
import numpy as np
import pandas as pd

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

# Create a pandas series from the list
fruits_series = pd.Series(fruits)

# Find the most frequent value using the mode() function
most_frequent = fruits_series.mode().iloc[0]

print("The most frequent value is: ", most_frequent)

'''

10. Determine the string value that occurs least frequently in fruits.
Write code with python version 3 using the numpy and pandas libraries to determine the string value that occurs least frequently in the following list:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", 
"kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
'''
import numpy as np
import pandas as pd

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

# Convert the list to a pandas Series
fruits_series = pd.Series(fruits)

# Get the count of each unique value
value_counts = fruits_series.value_counts()

# Get the string value that occurs least frequently
least_frequent = value_counts.idxmin()

print("The string value that occurs least frequently is:", least_frequent)
