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
Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

How many rows and columns are there?
What are the data types?
Summarize the dataframe with .info and .describe
What is the the weight of the fastest animal?
What is the overal percentage of specials?
How many animals are hoppers that are above the median speed? What percentage is this?

'''

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
