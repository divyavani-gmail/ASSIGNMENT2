# -*- coding: utf-8 -*-
"""Copy of Divya_pandas_pymongo_assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a8lvarhwXvd8Z2SJffSjl0o56PBg2NhS

**Consider the following Python dictionary data and Create a DataFrame using the dictionary:**

data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'],
        'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4],
        'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

**1. Create a DataFrame birds from this dictionary**
"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
print(df)

"""**2. Display a summary of the basic information about birds DataFrame and its data. I want information like mean variance,std-dev,min,max and percentiles**"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)             
print(df.describe())

"""*  describe() is used to view some basic statistical details like percentile, mean, std etc. of a data frame or a series of numeric values.

**3. Print the first 2 rows of the birds dataframe **
"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)    
#using head(n)method  
print(df.head(2))
# using iloc[ ] method
print(df.iloc[0:2])
# uing index of the rows method
print(df.iloc[[0,1]])
print(df[1:3])

"""*using head(n):
head() method returns top n rows of the dataframe where n is an integer value and it specifies the number of rows to be displayed. The default value of n is 5 therefore, head function without arguments gives the first five rows of the dataframe as an output.

* using iloc():
iloc() method is used to slice a dataframe by using the starting index and ending index of the sliced dataframe.

*
And this method can also be used by directly stating the indices of the rows we want in the iloc method. Say to get row with indices m and n.

**4. Print all the rows with only 'birds' and 'age' columns from the dataframe**
"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)
print(df[['birds','age']])

"""**5. select [2, 3, 7] rows and in columns ['birds', 'age', 'visits']**"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)             
print(df[['birds','age','visits']].iloc[[2,3,7]])

"""**6. select the rows where the number of visits is less than 4**"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)  
print("Number of visits is less than 4")
print(df[df['visits'] < 4])

"""**7. select the rows with columns ['birds', 'visits'] where the age is missing i.e NaN**"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)   
result = df[df['age'].isnull()]
print(result[['birds','visits']])

"""*isnull() function this function return dataframe of Boolean values which are True for NaN values.

**8. Select the rows where the birds is a Cranes and the age is less than 4**
"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)   
print(df[(df['birds'] == 'Cranes') & (df['age'] < 4)])

"""**9. Select the rows the age is between 2 and 4(inclusive)**"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)   
print(df[(df['age'] >= 2) & (df['age'] <= 4 )])

"""**10. Find the total number of visits of the bird Cranes**"""

import pandas as pd
import numpy as np
data = {' ': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data) 
print(df[(df['birds'] == 'Cranes') & (df['visits'] > 0)].sum())  
print(df[(df['birds'] == 'Cranes') & (df['visits'].notnull())].sum())

"""* notnull() function this function return dataframe of Boolean values which are False for NaN values.

sum() function is used to get the sum of the values for the requested axis.

**11. Calculate the mean age for each different birds in dataframe.**
"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)  
birds = df.groupby('birds')
for bird,bird_df in birds:
  print(bird,bird_df['age'].mean())

"""mean() funtion returns the mean of the values for the requested axis. If you want to compute an accumulated value, you may compute it from values located along axis 0 or axis 1. Here if you specify axis=1 you will be removing columns. If you specify axis=0 you will be removing rows from dataset

**12. Append a new row to dataframe with your choice of values for each column. Then delete that row to return the original DataFrame.**
"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)
print('Main Dataframe\n\n',df,'\n')
temp_df = {'birds':'spoonbills','age':4,'visits':2,'priority':'yes'}   
df = df.append(temp_df,ignore_index = True)
print('After appending a new row to dataframe\n\n',df,'\n')
print('After deleteing of the row\n\n',df.drop([df.index[10]]))

# using loc method
# df.loc[len(df.index)] = ['spoonbills',4,2,'yes']
# print(df)
# print(df.drop([df.index[10]]))

"""append() function is used to append rows of other dataframe to the end of the given dataframe, returning a new dataframe object. Columns not in the original dataframes are added as new columns and the new cells are populated with NaN value.

 drop() function is used to drop specified labels from rows or columns.

**13. Find the number of each type of birds in dataframe (Counts)**
"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)   
print(df['birds'].value_counts())

"""* value_counts() function returns object containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default.

**14. Sort dataframe (birds) first by the values in the 'age' in decending order, then by the value in the 'visits' column in ascending order.**
"""

l

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data) 
print('The values in the age column in decending order:\n\n',df.sort_values(by=['age'],ascending=False),'\n')  
print('The values in the visits column in ascending order:\n\n',df.sort_values('visits'))

"""* sort_values() function sorts a data frame in Ascending or Descending order of passed Column. It’s different than the sorted Python function since it cannot sort a data frame and particular column cannot be selected.

Here by is used to Single or List of column names to sort Data Frame by.and ,ascending=False its gives the decending order.
ascending=True its gives the ascending order.

**15. Replace the priority column values with'yes' should be 1 and 'no' should be 0**
"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)  
# using map
print(df['priority'].map({'yes':1,'no':0}))
# using replace
df['priority'] = df['priority'].replace({'yes':1,'no':0}) 
print(df)

"""* replace() function is used to replace a string, regex, list, dictionary, series, number etc. from a dataframe.

**16. In the 'birds' column, change the 'plovers' entries to 'trumpeters'.**
"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)
# using replace
df['birds'] = df['birds'].replace({'plovers':'trumpeters'})
print(df,'\n')   
# using map
print(df['birds'].map({'plovers':'trumpeters'}).fillna(df['birds']),'\n')
# using lambda
print(df.birds.map(lambda x: 'trumpeters' if x == 'plovers' else x) )

"""replace() function used to replace a string, regex, list, dictionary, series, number etc. from a dataframe.

17. What is the average age of Cranes given priority is yes.
"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data) 
print(df[(df['birds'] == 'Cranes') & (df['priority'] == 'yes')]['age'].mean(axis = 0))

"""mean() funtion returns the mean of the values for the requested axis.
If you want to compute an accumulated value, you may compute it from values located along axis 0 or axis 1.
Here if you specify axis=1 you will be removing columns. If you specify axis=0 you will be removing rows from dataset

18. What is the average age of each bird given that their no. of visits is 2 and priority is yes.
"""

import pandas as pd
import numpy as np 
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)  
print(df[(df['visits'] == 2 ) & (df['priority'] == 'yes')]['age'].mean(axis = 0))

"""19. Replace the Nan values in Age column by taking median values of all the age of birds"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data) 
median_value = df['age'].median(skipna =True)
# print(df['age'].mdian(skipna = True))
print(median_value)
df['age'] = df['age'].replace({np.nan:median_value})
print(df['age'])

"""median() function return the median of the values for the requested axis.median() function is applied on a pandas dataframe object, then the method returns a pandas series object which contains the median of the values over the specified axis.

20.How many unique birds are present in data?
"""

import pandas as pd
import numpy as np
data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills'], 'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
df = pd.DataFrame(data)   
print('Number of unique birds values:',df.birds.nunique())

"""unique() function is used to get the unique values of column.
nunique()function is used to get the number of unique values in column. 
"""