import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

"""
# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv',index_col=0)

# Print out cars
print(cars)
"""
# column
print(cars[['country']])
print(cars)
# Row
print(cars[0:1])
print(cars[0:1]['country'])
print('-------------------------')
print(cars.loc['US'])

print('-------------------------')
print('-------------------------')
print(cars.loc[['US']])

print('-------------------------')
print('-------------------------')
print(cars.loc[['US', 'RU'], ['country', 'cars_per_cap']])
print('-------------------------')
print('-------------------------')
print(cars.loc[:, ['country', 'cars_per_cap']])

print('-------------------------')
print('-------------------------')
print('-------------------------')
print('-------------------------')
print(cars.iloc[1])
print('-------------------------')
print(cars.iloc[[1, 2]])

# print(cars.loc[:, 'drives_right'])

"""
dr=cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)



car_maniac = cars[cars['cars_per_cap']>500]
# Print car_maniac
print(car_maniac)
"""
"""

get the first is head, which returns the first few rows of the DataFrame.
dogs.head()

the data types
dogs.info()

the number of rows, number of column 
dogs.shape
like:
(7,6)

dogs.describe()
it gets the count, mean, std, min,...., and max 

dogs.values
contains 2d numpy array [[],[],....]

dogs.columns
contains the columns name


dogs.index
gets the row numbers

------------------------------------------------------------------------------

"""
