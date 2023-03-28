'''
1. Copy the code from the lesson to create a dataframe full of student grades.
'''


#Run this python version 3 code and store the dataframe to answer additional questions in this thread:

import pandas as pd
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)





'''
    What is the python version 3 code to create a column named passing_english that indicates whether each student has a passing grade in english (70 or higher) from 
    the df dataframe?
'''
df['passing_english'] = df['english'] >= 70

'''
    What is the python version 3 code to sort the english grades in df dataframe by the passing_english column? How are duplicates handled?
'''
df.sort_values(by=['passing_english', 'english'], ascending=[False, False], inplace=True)

'''
This code sorts the df dataframe by the passing_english column first, and then by the english column in descending order. The ascending parameter is set to 
[False, False] to sort both columns in descending order. The inplace parameter is set to True to modify the df dataframe in place rather than creating a new 
sorted dataframe.

Duplicates are handled by the sort_values method according to the order of the columns in the by parameter. In this case, if there are multiple students 
with the same passing grade in English, they will be sorted by their English grades in descending order. If there are still ties, the order of the original 
df dataframe will be preserved.
'''

'''
    What is the python version 3 code to sort by english grades (failing at the top of the list) and then by student name with the df dataframe?
'''

df.sort_values(by=['passing_english', 'english', 'name'], ascending=[True, True, True], inplace=True)
'''

This code sorts the df dataframe by the passing_english column first in ascending order (so that failing grades appear at the top of the list), then by the 
english column in ascending order (so that the lowest English grades appear first within each passing/failing group), and finally by the name column in ascending 
order (so that students are sorted alphabetically within each passing/failing group). The ascending parameter is set to [True, True, True] to sort all three columns 
in ascending order. The inplace parameter is set to True to modify the df dataframe in place rather than creating a new sorted dataframe.
'''

'''
    What is the python version 3 code to sort the english grades first by passing_english, and then by the actual english grade?
'''
df.sort_values(by=['passing_english', 'english'], ascending=[False, False], inplace=True)
'''
This code sorts the df dataframe by the passing_english column first, so that passing grades appear before failing grades. Within each group of passing or failing 
grades, the english column is then sorted in descending order, so that the highest English grades appear first within each passing/failing group. The ascending 
parameter is set to [False, False] to sort both columns in descending order. The inplace parameter is set to True to modify the df dataframe in place rather than 
creating a new sorted dataframe.

'''
'''
    What is the python version 3 code to calculate each students overall grade (the overall grade is the average of the math, english, and reading grades) and add 
    it as a new column on the df dataframe? Also, include code to print the results.
'''
df['overall_grade'] = df[['math', 'english', 'reading']].mean(axis=1)
print(df)
'''
This code first calculates the mean of the math, english, and reading columns for each row using the mean() method, with axis=1 specified to calculate the mean across 
columns. It then creates a new column called overall_grade in the df dataframe to store the resulting means.

The print(df) command is used to print the updated df dataframe, which now includes a new column called overall_grade containing each student's overall grade.

'''

'''
All the datasets loaded from the pydataset library will be pandas dataframes.

2. Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
    How many rows and columns are there?
    '''
import pandas as pd
from pydataset import data

mpg = data('mpg')
mpg.shape
# Output: (234, 11)
# There are 234 rows and 11 columns.

'''
    What are the data types of each column?
'''
mpg.dtypes
# Output:
# manufacturer       object
# model              object
# displ             float64
# year                int64
# cyl                 int64
# trans              object
# drv                object
# cty                 int64
# hwy                 int64
# fl                 object
# class              object
# dtype: object


'''
    Summarize the dataframe with .info and .describe
'''
mpg.info()
mpg.describe()

'''
    Rename the cty column to city.
    Rename the hwy column to highway.
'''
mpg = mpg.rename(columns={'cty': 'city', 'hwy': 'highway'})

'''
    Do any cars have better city mileage than highway mileage?
'''
mpg[mpg.city > mpg.highway]
# Output: Empty DataFrame
# Columns: [manufacturer, model, displ, year, cyl, trans, drv, city, highway, fl, class]
# Index: []


'''
    Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
'''
mpg['mileage_difference'] = mpg.highway - mpg.city

'''
    Which car (or cars) has the highest mileage difference?
'''
mpg[mpg.mileage_difference == mpg.mileage_difference.max()]
# The car with the highest mileage difference is the 1999 Honda Insight with a mileage difference of 18.

'''
    Which compact class car has the lowest highway mileage? The best?
'''
# Lowest
mpg[mpg['class'] == 'compact'].sort_values(by='highway').head(1)


# Best
mpg[mpg['class'] == 'compact'].sort_values(by='highway', ascending=False).head(1)


'''
    Create a column named average_mileage that is the mean of the city and highway mileage.
'''
mpg['average_mileage'] = (mpg.city + mpg.highway) / 2


'''
    Which dodge car has the best average mileage? The worst?
'''
# Best
mpg[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage', ascending=False).head(1)

# Worst
mpg[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage').head(1)


'''
3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
'''
import pandas as pd
from pydataset import data

mammals = data('Mammals')


'''
    How many rows and columns are there?
'''
mammals.shape
# Output: (107, 4)
# 107 rows, 4 columns

'''
    What are the data types?
'''
mammals.dtypes
# weight (float64)
# speed (float64)
# hoppers (bool)
# specials (bool)
# dtype: (object)


'''
    Summarize the dataframe with .info and .describe
'''
mammals.info()
mammals.describe()


'''
    Write code with python version 3 using the numpy and pandas libraries and the pydataset Mammals to show the weight of the animal with the highest speed
  
'''
import numpy as np
import pandas as pd
from pydataset import data

mammals = data('Mammals')

# Get the row of the animal with the highest speed
animal_with_max_speed = mammals.loc[mammals['speed'].idxmax()]

# Get the weight of the animal with the highest speed
weight_of_max_speed_animal = animal_with_max_speed['weight']

print("The weight of the animal with the highest speed is", weight_of_max_speed_animal)

'''
    Write code with python version 3 using the numpy and pandas libraries and the pydataset Mammals to show the overal percentage of specials (bool)?
'''
import numpy as np
import pandas as pd
from pydataset import data

mammals = data('Mammals')

# Calculate the overall percentage of specials
total_specials = mammals['specials'].sum()
total_animals = len(mammals)
percentage_specials = (total_specials / total_animals) * 100

print("The overall percentage of specials is", percentage_specials)

#The overall percentage of specials is 9.34579439252336

'''
    Write code with python version 3 using the numpy and pandas libraries and the pydataset Mammals to show how many animals are hoppers (bool) that are above
    the median speed (float64)? What percentage is this?
'''
import numpy as np
import pandas as pd
from pydataset import data

mammals = data('Mammals')

# Calculate the median speed
median_speed = mammals['speed'].median()

# Get the subset of hoppers with speed above median
hoppers_above_median_speed = mammals[(mammals['hoppers']) & (mammals['speed'] > median_speed)]

# Get the count of hoppers with speed above median
count_hoppers_above_median_speed = len(hoppers_above_median_speed)

# Calculate the percentage of hoppers with speed above median
total_hoppers = mammals['hoppers'].sum()
percentage_hoppers_above_median_speed = (count_hoppers_above_median_speed / total_hoppers) * 100

print("The number of hoppers with speed above the median is", count_hoppers_above_median_speed)
print("The percentage of hoppers with speed above the median is", percentage_hoppers_above_median_speed)

# The number of hoppers with speed above the median is 7
# The percentage of hoppers with speed above the median is 63.63636363636363
