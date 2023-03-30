'''
Exercises I

3. Write code with python version 3 to create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url 
connection string formatted like this:

from env import host, user, password

url = f'mysql+pymysql://{user}:{password}@{host}/employees'
'''
def get_db_url(username, hostname, password, database):
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
    return url

'''
4. Write code with python version 3 to obtain a connection to the employees database with a url and using username: 
'''

import mysql.connector

# Define the URL to connect to the database
url = {
  'user': '
  'database': 'employees',
  'raise_on_warnings': True
}

# Connect to the database
cnx = mysql.connector.connect(**url)

# Check if the connection was successful
if cnx.is_connected():
    print('Connected to the employees database')
else:
    print('Connection failed')

# Close the connection when finished
cnx.close()



import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user=,
                              database='employees')

# Check if the connection was successful
if cnx.is_connected():
    print('Connected to the employees database')
else:
    print('Connection failed')

# Close the connection when finished
cnx.close()


'''
5. Once you have successfully run a query:

a. Intentionally make a typo in the database url. What kind of error message do you see?
'''
import mysql.connector

# Define the URL to connect to the database
url = {
  'use': 
  'database': 'employees',
  'raise_on_warnings': True
}

# Connect to the database
cnx = mysql.connector.connect(**url)

# Check if the connection was successful
if cnx.is_connected():
    print('Connected to the employees database')
else:
    print('Connection failed')

# Close the connection when finished
cnx.close()
'''
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Input In [7], in <cell line: 14>()
      4 url = {
      5   'use': 
   (...)
     10   'raise_on_warnings': True
     11 }
     13 # Connect to the database
---> 14 cnx = mysql.connector.connect(**url)
     16 # Check if the connection was successful
     17 if cnx.is_connected():

File /opt/homebrew/anaconda3/lib/python3.9/site-packages/mysql/connector/pooling.py:293, in connect(*args, **kwargs)
    290         raise ImportError(ERROR_NO_CEXT)
    292 if CMySQLConnection and not use_pure:
--> 293     return CMySQLConnection(*args, **kwargs)
    294 return MySQLConnection(*args, **kwargs)

File /opt/homebrew/anaconda3/lib/python3.9/site-packages/mysql/connector/connection_cext.py:118, in CMySQLConnection.__init__(self, **kwargs)
    115 super().__init__()
    117 if kwargs:
--> 118     self.connect(**kwargs)

File /opt/homebrew/anaconda3/lib/python3.9/site-packages/mysql/connector/abstracts.py:1175, in MySQLConnectionAbstract.connect(self, **kwargs)
   1168 """Connect to the MySQL server
   1169 
   1170 This method sets up the connection to the MySQL server. If no
   1171 arguments are given, it will use the already configured or default
   1172 values.
   1173 """
   1174 if kwargs:
-> 1175     self.config(**kwargs)
   1177 self.disconnect()
   1178 self._open_connection()

File /opt/homebrew/anaconda3/lib/python3.9/site-packages/mysql/connector/abstracts.py:626, in MySQLConnectionAbstract.config(self, **kwargs)
    624     DEFAULT_CONFIGURATION[key]
    625 except KeyError:
--> 626     raise AttributeError(f"Unsupported argument '{key}'") from None
    627 # SSL Configuration
    628 if key.startswith("ssl_"):

AttributeError: Unsupported argument 'use'

b. Intentionally make an error in your SQL query. What does the error message look like?
'''
import mysql.connector

# Define the URL to connect to the database
url = {
  'user': ',
  'raise_on_warnings': True
}

# Connect to the database
cnx = mysql.conector.connect(**url)

# Check if the connection was successful
if cnx.is_connected():
    print('Connected to the employees database')
else:
    print('Connection failed')

# Close the connection when finished
cnx.close()
'''

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Input In [8], in <cell line: 14>()
      4 url
      
     16 # Check if the connection was successful
     17 if cnx.is_connected():

AttributeError: module 'mysql' has no attribute 'conector'


6. Write code with python version 3 to obtain a connection to the employees database with a url and . The read the employees.employees and employees.titles tables 
into two separate DataFrames and then print those dataframes.
'''
import mysql.connector
import pandas as pd

# Define the URL to connect to the database
url = {
  'user': '
  'database': ,
  'raise_on_warnings': True
}

# Connect to the database
cnx = mysql.connector.connect(**url)

# Read employees table into a DataFrame
employees_df = pd.read_sql('SELECT * FROM employees', con=cnx)

# Read titles table into a DataFrame
titles_df = pd.read_sql('SELECT * FROM titles', con=cnx)

# Close the connection when finished
cnx.close()

# Print the DataFrames
print(employees_df.head())
print(titles_df.head())



'''
7. Write code with python version 3 to obtain a connection to the employees database with a url and using username: . 
The read the employees.employees and employees.titles tables into two separate DataFrames and then
print how many rows and columns are in each DataFrame.

Number of rows and columns in employees_df: (300024, 6)
Number of rows and columns in titles_df: (443308, 4)
'''
import mysql.connector
import pandas as pd

# Define the URL to connect to the database
url = {
  'user': '
  'raise_on_warnings': True
}

# Connect to the database
cnx = mysql.connector.connect(**url)

# Read employees table into a DataFrame
employees_df = pd.read_sql('SELECT * FROM employees', con=cnx)

# Read titles table into a DataFrame
titles_df = pd.read_sql('SELECT * FROM titles', con=cnx)

# Close the connection when finished
cnx.close()

# Print the number of rows and columns in each DataFrame
print("Number of rows and columns in employees_df:", employees_df.shape)
print("Number of rows and columns in titles_df:", titles_df.shape)

'''
8. Write code with python version 3 to obtain a connection to the employees database with a url and using 
 Then read the employees.employees and employees.titles tables into two separate DataFrames and then
print the summary statistics for each DataFrame.

Number of rows and columns in employees_df: (300024, 6)
Number of rows and columns in titles_df: (443308, 4)
'''

import mysql.connector
import pandas as pd

# Define the URL to connect to the database
url = {
  'user': '
  'raise_on_warnings': True
}

# Connect to the database
cnx = mysql.connector.connect(**url)

# Read employees table into a DataFrame
employees_df = pd.read_sql('SELECT * FROM employees', con=cnx)

# Read titles table into a DataFrame
titles_df = pd.read_sql('SELECT * FROM titles', con=cnx)

# Close the connection when finished
cnx.close()

# Print the number of rows and columns in each DataFrame
print("Number of rows and columns in employees_df:", employees_df.shape)
print("Number of rows and columns in titles_df:", titles_df.shape)



'''
9. Write code with python version 3 to obtain a connection to the employees database with a url and importing user, password, host, port, and database values from the 
env.py file. Then read the employees.titles table into a DataFrames and then print how many unique "titles" are in the DataFrame.

Number of unique titles in titles_df: 7
'''
import mysql.connector
import pandas as pd
from env import user, password, host, port, database

# Define the URL to connect to the database
url = {
  'user': user,
  'password': password,
  'host': host,
  'port': port,
  'database': database,
  'raise_on_warnings': True
}

# Connect to the database
cnx = mysql.connector.connect(**url)

# Read titles table into a DataFrame
titles_df = pd.read_sql('SELECT * FROM titles', con=cnx)

# Close the connection when finished
cnx.close()

# Print the number of unique titles in the DataFrame
print("Number of unique titles in titles_df:", len(titles_df['title'].unique()))



'''
10. Write code with python version 3 to obtain a connection to the employees database with a url and importing user, password, host, port, and database values from the 
env.py file. Then read the employees.titles table into a DataFrames and then print the oldest date in the to_date column.

Oldest date in the to_date column: 1985-03-01
'''
import mysql.connector
import pandas as pd
from env import user, password, host, port, database

# Define the URL to connect to the database
url = {
  'user': user,
  'password': password,
  'host': host,
  'port': port,
  'database': database,
  'raise_on_warnings': True
}

# Connect to the database
cnx = mysql.connector.connect(**url)

# Read titles table into a DataFrame
titles_df = pd.read_sql('SELECT * FROM titles', con=cnx)

# Close the connection when finished
cnx.close()

# Print the oldest date in the to_date column
print("Oldest date in the to_date column:", titles_df['to_date'].min())


'''
11. Write code with python version 3 to obtain a connection to the employees database with a url and importing user, password, host, port, and database values from the 
env.py file. Then read the employees.titles table into a DataFrames and then print the most recent date in the to_date column?

Most recent date in the to_date column: 9999-01-01
'''

import mysql.connector
import pandas as pd
from env import user, password, host, port, database

# Define the URL to connect to the database
url = {
  'user': user,
  'password': password,
  'host': host,
  'port': port,
  'database': database,
  'raise_on_warnings': True
}

# Connect to the database
cnx = mysql.connector.connect(**url)

# Read titles table into a DataFrame
titles_df = pd.read_sql('SELECT * FROM titles', con=cnx)

# Close the connection when finished
cnx.close()

# Print the most recent date in the to_date column
print("Most recent date in the to_date column:", titles_df['to_date'].max())


'''
Exercises II

1. Copy the users and roles DataFrames from the examples above.

# Create the users DataFrame.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


# Create the roles DataFrame

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

'''



'''
2. What is the result of using a right join on the users and roles DataFrames?
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

Performing a right join on the users and roles DataFrames will result in a new DataFrame that contains all the rows from the roles DataFrame 
and the matching rows from the users DataFrame, based on the id column. Rows from the roles DataFrame that do not have a matching id in the 
users DataFrame will still appear in the resulting DataFrame, with missing values in the columns that correspond to the users DataFrame.


'''


'''
3. What is the result of using an outer join on the DataFrames?

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

Performing an outer join on the users and roles DataFrames will result in a new DataFrame that contains all the rows from both DataFrames, matching 
rows based on the id columns, and filling in missing values with NaN.

'''

'''
4.What happens if you drop the foreign keys from the users and roles DataFrames and try to merge them?

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

Dropping the foreign keys from the users and roles DataFrames should not have any effect on merging them, since the foreign keys only provide a constraint 
between the two DataFrames and do not affect the merging process itself.

'''

'''
5. Write code with python version 3 to load the mpg dataset from PyDataset.
'''
from pydataset import data

mpg = data('mpg')
print(mpg.head())

'''
6. Write code with python version 3 to output and read the documentation for the mpg dataset.
'''
from pydataset import data

mpg = data('mpg')

# Output the documentation
print(data('mpg', show_doc=True))

# Read the documentation
print(mpg.DESCR)





'''
7. Write code with python version 3 to show how many rows and columns are in the mpg dataset?
The mpg dataset has 234 rows and 11 columns.
'''
import pandas as pd
from pydataset import data

mpg = data('mpg')
num_rows, num_cols = mpg.shape
print(f"The mpg dataset has {num_rows} rows and {num_cols} columns.")


'''
8. Write code with python version 3 to show column names for the mpg dataset.
'''
from pydataset import data

mpg = data('mpg')

print(mpg.columns)


'''
9. Write code with python version 3 to show the summary statistics for the mpg dataset.
'''
from pydataset import data

mpg = data('mpg')

print(mpg.describe())

'''
10. Write code with python version 3 to show how many different manufacturers there are in the mpg dataset.
    15 different manufacturers
'''
from pydataset import data

mpg = data('mpg')

print(len(mpg['manufacturer'].unique()))

'''
11. Write code with python version 3 to show how many different models there are in the mpg dataset.
    38 different models
'''
print(mpg['model'].nunique())



'''
12. Write code with python version 3 to create a column named mileage_difference and should contain the difference between highway and city mileage 
for each car in the mpg dataset. Show the mileage_difference column.
'''

import pandas as pd
from pydataset import data

# Load the mpg dataset
mpg = data('mpg')

# Create mileage_difference column
mpg['mileage_difference'] = mpg['hwy'] - mpg['cty']

# Display mileage_difference column
print(mpg['mileage_difference'])

'''
13. Write code with python version 3 to create a column named average_mileage that is the mean of the city and highway mileage in the mpg dataset. 
Show the average_mileage column.
'''
import pandas as pd
from pydataset import data

# Load the mpg dataset
mpg = data('mpg')

# Create the average_mileage column
mpg['average_mileage'] = (mpg['cty'] + mpg['hwy']) / 2

# Show the average_mileage column
print(mpg['average_mileage'])


'''
14. Write code with python version 3 to create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has 
an automatic transmission. Show the is_automatic column.
'''
from pydataset import data

mpg = data('mpg')

# Define a function to check if the transmission is automatic
def is_auto(transmission):
    if transmission.startswith("auto"):
        return True
    else:
        return False

# Apply the function to the trans column to create the is_automatic column
mpg['is_automatic'] = mpg['trans'].apply(is_auto)

# Show the is_automatic column
print(mpg['is_automatic'])



'''
15. Write code with python version 3 using the mpg dataset to find out which manufacturer has the best miles per gallon on average. Show the results.

The manufacturer with the best miles per gallon on average is honda

'''
from pydataset import data

# Load the mpg dataset
mpg = data('mpg')

# Calculate the average miles per gallon for each manufacturer
avg_mpg_by_manufacturer = mpg.groupby('manufacturer').mean()[['cty', 'hwy']].mean(axis=1)

# Find the manufacturer with the highest average miles per gallon
best_mpg_manufacturer = avg_mpg_by_manufacturer.idxmax()

# Show the results
print(f'The manufacturer with the best miles per gallon on average is {best_mpg_manufacturer}')



'''
16. Write code with python version 3 using the mpg dataset to find out whether automatic or manual cars have better miles per gallon. Show the results.

Manual cars have better miles per gallon on average.
'''
import pandas as pd
from pydataset import data

mpg = data('mpg')

# Create a boolean column for automatic transmissions
mpg['is_automatic'] = mpg['trans'].apply(lambda x: x.startswith('auto'))

# Create subsets for automatic and manual cars
auto_mpg = mpg[mpg['is_automatic'] == True]
manual_mpg = mpg[mpg['is_automatic'] == False]

# Calculate the mean miles per gallon for each subset
auto_mpg_mean = auto_mpg[['cty', 'hwy']].mean().mean()
manual_mpg_mean = manual_mpg[['cty', 'hwy']].mean().mean()

# Print the results
if auto_mpg_mean > manual_mpg_mean:
    print('Automatic cars have better miles per gallon on average.')
else:
    print('Manual cars have better miles per gallon on average.')


'''
Exercises III

1. Use your get_db_url function to help you explore the data from the chipotle database.


2. Write code with python version 3 to obtain a connection to the chipotle database with a url and importing user, password, host, port, and database values from the 
env.py file. Calculate and show the total price for each order using orders.quantity and orders.item_price.


'''
import pandas as pd
import pymysql
from env import user, password, host, port, database

# Connect to the database
conn = pymysql.connect(
    host=host,
    user=user,
    password=password,
    port=port,
    db=database
)

# Query the orders table
orders_query = """
    SELECT order_id, quantity, item_price
    FROM orders
"""
orders = pd.read_sql(orders_query, conn)

# Convert item_price to a float
orders['item_price'] = orders['item_price'].apply(lambda x: float(x[1:]))

# Calculate the total price for each order
orders['total_price'] = orders['quantity'] * orders['item_price']

# Show the total price for each order
print(orders.groupby('order_id')['total_price'].sum())


'''
3. Write code with python version 3 using pandas and numpy and not using psycog2 to obtain a connection to the mysql chipotle database with a url and importing user, 
password, host, port, and database values from the env.py file. Keep the myslq connection open find and show the 3 most popular items in chipotle.orders.item_name.

'Chicken Bowl','726'
'Chicken Burrito','553'
'Chips and Guacamole','479'

'''

import pandas as pd
from sqlalchemy import create_engine
from env import user, password, host, port, database

# Establish a connection to the database using SQLAlchemy
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

# Define a SQL query to get the top 3 most popular items
query = """
SELECT item_name, COUNT(*) AS count
FROM orders
GROUP BY item_name
ORDER BY count DESC
LIMIT 3;
"""

# Execute the query and load the results into a pandas DataFrame
df = pd.read_sql(query, engine)

# Print the results
print(df)


'''
4. Write code with python version 3 to obtain a connection to the chipotle database importing user, password, 
host, port, and database values from the env.py file. Find and show which item has produced the most revenue using chipotle.orders.item_name, chipotle.orders.quantity, 
and chipotle.orders.item_price.

'Chips and Fresh Tomato Salsa','130','0'

'''

# main.py
import psycopg2
from env import db_credentials

def connect_to_db(credentials):
    connection = psycopg2.connect(
        user=credentials['user'],
        password=credentials['password'],
        host=credentials['host'],
        port=credentials['port'],
        database=credentials['database']
    )
    return connection

def get_most_revenue_item(connection):
    cursor = connection.cursor()
    query = '''
        SELECT item_name, SUM(quantity) AS total_quantity, SUM(item_price * quantity) AS total_revenue
        FROM chipotle.orders
        GROUP BY item_name
        ORDER BY total_revenue DESC
        LIMIT 1;
    '''
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    return result

if __name__ == '__main__':
    conn = connect_to_db(db_credentials)
    item_name, total_quantity, total_revenue = get_most_revenue_item(conn)
    conn.close()

    print(f"The item with the most revenue is '{item_name}' with {total_quantity} items sold and ${total_revenue:.2f} total revenue.")




'''
5. Write code with python version 3 to obtain a connection to the chipotle database importing user, password, 
host, port, and database values from the env.py file and then use mysql to join the employees and titles DataFrames together.
'''

emp_titles = pd.merge(employees, titles, on='emp_no')

# main.py
import pandas as pd
import mysql.connector
import env

# Import required variables from env.py
user = env.user
password = env.password
host = env.host
port = env.port
database = env.database

# Create a connection using the imported values
connection = mysql.connector.connect(
    user=user,
    password=password,
    host=host,
    port=port,
    database=database
)

# Query to read data from the employees table
employees_query = "SELECT * FROM employees"

# Query to read data from the titles table
titles_query = "SELECT * FROM titles"

# Read data from the database using pandas
employees_df = pd.read_sql_query(employees_query, connection)
titles_df = pd.read_sql_query(titles_query, connection)

# Close the connection
connection.close()

# Perform the join using pandas
result_df = employees_df.merge(titles_df, on='emp_no')

# Display the result
print(result_df)




'''
6. For each title, find the hire date of the employee that was hired most recently with that title.
'''
max_hire dates = emp_titles.groupby('title').hire_date.max() 
max_hire dates = pd.merge(emp_titles, max_hire_dates, on=['title', 'hire_date']).sort_values


'''
7. Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL code to 
pull the necessary data and python/pandas code to perform the manipulations.)
'''
emp_titles.head()
emp_dept.head()
pd.merge(emp_titles, emp_dept, on='emp_no')
pd.crosstab(emp_title_dept.title, emp_titles.dept_name)

