import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Print version
print("\nPandas version is " + pd.__version__)

# ----------------------------------------------------------------
# DataFrame creation
# ----------------------------------------------------------------

# Create an empty pandas DataFrame
df = pd.DataFrame(data=[None],
                  index=[None],
                  columns=[None])
# Marvel data
marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968]
]

# Create a marvel_df pandas DataFrame with the given marvel data
marvel_df = pd.DataFrame(data=marvel_data)

# Add column names to the marvel_df
col_names = ['Name', 'Sex', 'First appearance']
marvel_df.columns = col_names
# print(marvel_df)

# Add index names to the marvel_df (use the character name as index)
marvel_df.index = marvel_df['Name']
# print(marvel_df)

# Drop the name column as it's now the index
marvel_df = marvel_df.drop(['Name'], axis=1)
# print(marvel_df)

# Drop 'Namor' and 'Hank Pym' rows
marvel_df = marvel_df.drop(['Namor', 'Hank Pym'], axis=0)
# print(marvel_df)

# ----------------------------------------------------------------
# DataFrame selection, slicing and indexation
# ----------------------------------------------------------------

# Show the first 5 elements on marvel_df
temp = marvel_df.iloc[:5]
# print(temp)

# Show the last 5 elements on marvel_df
temp = marvel_df.iloc[-5:]
# print(temp)

# Show just the sex of the first 5 elements on marvel_df
temp = marvel_df.iloc[:5]['Sex'].to_frame()
# print(temp)

# Show the first_appearance of all middle elements on marvel_df
temp = marvel_df.iloc[1:-1]['First appearance'].to_frame()
# print(temp)

# Show the first and last elements on marvel_df
temp = marvel_df.iloc[[1, -1]]
# print(temp)

# ----------------------------------------------------------------
# DataFrame manipulation and operations
# ----------------------------------------------------------------

# Modify the first_appearance of 'Vision' to year 1964
marvel_df.loc['Vision', 'First appearance'] = 1964
# print(marvel_df)

# Add a new column to marvel_df called 'years_since' with the years since first_appearance
marvel_df['Years since'] = 2021 - marvel_df['First appearance']
# print(marvel_df)

# ----------------------------------------------------------------
# DataFrame boolean arrays (also called masks)
# ----------------------------------------------------------------

# Given the marvel_df pandas DataFrame, make a mask showing the female characters
mask = marvel_df['Sex'] == 'female'
# print(mask)

# Given the marvel_df pandas DataFrame, get the male characters
mask = marvel_df['Sex'] == 'male'
# print(marvel_df[mask])

# Given the marvel_df pandas DataFrame, get the characters with first_appearance after 1970
mask = marvel_df['First appearance'] > 1970
# print(marvel_df[mask])

# Given the marvel_df pandas DataFrame, get the female characters with first_appearance after 1970
mask = (marvel_df['Sex'] == 'female') & (marvel_df['First appearance'] > 1970)
# print(marvel_df[mask])

# ----------------------------------------------------------------
# DataFrame summary statistics
# ----------------------------------------------------------------

# Show basic statistics of marvel_df
temp = marvel_df.describe()
# print(temp)

# Given the marvel_df pandas DataFrame, show the mean value of first_appearance
temp = marvel_df['First appearance'].mean()
# print(temp)

# Given the marvel_df pandas DataFrame, show the min value of first_appearance
temp = marvel_df['First appearance'].min()
# print(temp)

# Given the marvel_df pandas DataFrame, get the characters with the min value of first_appearance
mask = marvel_df['First appearance'] == marvel_df['First appearance'].min()
# print(marvel_df[mask])

# ----------------------------------------------------------------
# DataFrame basic plottings
# ----------------------------------------------------------------

# Reset index names of marvel_df
marvel_df = marvel_df.reset_index()
# print(marvel_df)

# Plot the values of first_appearance
# plt.figure(1)
# plt.plot(marvel_df.index, marvel_df['First appearance'])
# plt.show()

# Plot a histogram (plot.hist) with values of first_appearance
# plt.figure(1)
# plt.hist(marvel_df['First appearance'])
# plt.show()

# ----------------------------------------------------------------
# Series creation
# ----------------------------------------------------------------

# Create an empty pandas Series
X = pd.Series(dtype=object)

# Given the X python list convert it to an Y pandas Series
X = ['A', 'B', 'C']
Y = pd.Series(X)
# print(X, type(X))
# print(Y, type(Y))

# Given the X pandas Series, name it 'My letters'
X = pd.Series(['A', 'B', 'C'])
X.name = 'My letters'
# print(X)

# Given the X pandas Series, show its values
X = pd.Series(['A', 'B', 'C'])
# print(X.values)

# ----------------------------------------------------------------
# Series indexation
# ----------------------------------------------------------------

# Assign index names to the given X pandas Series
X = pd.Series(['A', 'B', 'C'])
index_names = ['first', 'second', 'third']
X.index = index_names
# print(X)

# Given the X pandas Series, show its first element
X = pd.Series(['A', 'B', 'C'], index=['first', 'second', 'third'])
# temp = X[0] # by position
# temp = X.iloc[0] # by position
temp = X['first']  # by index
# print(temp)

# Given the X pandas Series, show its last element
X = pd.Series(['A', 'B', 'C'], index=['first', 'second', 'third'])
# temp = X[-1] # by position
# temp = X.iloc[-1] # by position
temp = X['third']  # by index
# print(temp)

# Given the X pandas Series, show all middle elements
X = pd.Series(['A', 'B', 'C', 'D', 'E'], index=[
              'first', 'second', 'third', 'forth', 'fifth'])
temp = X.iloc[1:-1]  # by position
# print(temp)

# Given the X pandas Series, show the elements in reverse position
X = pd.Series(['A', 'B', 'C', 'D', 'E'], index=[
              'first', 'second', 'third', 'forth', 'fifth'])
temp = X.iloc[::-1]
# print(temp)

# Given the X pandas Series, show the first and last elements
X = pd.Series(['A', 'B', 'C', 'D', 'E'],
              index=['first', 'second', 'third', 'forth', 'fifth'])
# temp = X[['first', 'fifth']]
# temp = X.iloc[[0, -1]]
temp = X[[0, -1]]
# print(temp)

# ----------------------------------------------------------------
# Series maniupulation
# ----------------------------------------------------------------

# Convert the given integer pandas Series to float
X = pd.Series([1, 2, 3, 4, 5],
              index=['first', 'second', 'third', 'forth', 'fifth'])
X = pd.Series(X, dtype=np.float16)
# print(X)

# Reverse the given pandas Series (first element becomes last)
X = pd.Series([1, 2, 3, 4, 5],
              index=['first', 'second', 'third', 'forth', 'fifth'])
X = pd.Series(X[::-1])
# print(X)

# Order (sort) the given pandas Series
X = pd.Series([4, 2, 5, 1, 3],
              index=['forth', 'second', 'fifth', 'first', 'third'])
X = X.sort_values()
# print(X)

# Given the X pandas Series, set the fifth element equal to 10
X = pd.Series([1, 2, 3, 4, 5],
              index=['A', 'B', 'C', 'D', 'E'])
X[4] = 10
# print(X)

# Given the X pandas Series, change all the middle elements to 0
X = pd.Series([1, 2, 3, 4, 5],
              index=['A', 'B', 'C', 'D', 'E'])
X[1:-1] = 0
# print(X)

# Given the X pandas Series, add 5 to every element
X = pd.Series([1, 2, 3, 4, 5],
              index=['A', 'B', 'C', 'D', 'E'])
X += 5
# print(X)

# ----------------------------------------------------------------
# Series boolean arrays (also called masks)
# ----------------------------------------------------------------

# Given the X pandas Series, make a mask showing negative elements
X = pd.Series([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
mask = X < 0
# print(mask)

# Given the X pandas Series, get the negative elements
X = pd.Series([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
mask = X < 0
# print(X[mask])

# Given the X pandas Series, get numbers higher than 5
X = pd.Series([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
mask = X > 5
# print(X[mask])

# Given the X pandas Series, get numbers higher than the elements mean
X = pd.Series([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
mask = X > X.mean()
# print(X[mask])

# Given the X pandas Series, get numbers equal to 2 or 10
X = pd.Series([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
mask = (X == 2) | (X == 10)
# print(X[mask])

# ----------------------------------------------------------------
# Logic functions
# ----------------------------------------------------------------

# Given the X pandas Series, return True if none of its elements is zero
X = pd.Series([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
# print(X.all())

# Given the X pandas Series, return True if any of its elements is zero
X = pd.Series([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
# print(X.any())

# ----------------------------------------------------------------
# Summary statistics
# ----------------------------------------------------------------

# Given the X pandas Series, show the sum of its elements
X = pd.Series([3, 5, 6, 7, 2, 3, 4, 9, 4])
# print(X.sum())

# Given the X pandas Series, show the mean value of its elements
X = pd.Series([3, 5, 6, 7, 2, 3, 4, 9, 4])
# print(X.mean())

# Given the X pandas Series, show the max value of its elements
X = pd.Series([3, 5, 6, 7, 2, 3, 4, 9, 4])
# print(X.max())
