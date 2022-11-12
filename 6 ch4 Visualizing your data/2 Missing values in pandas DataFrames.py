"""
Detecting missing values and print false if the values is null for each value (Check individual values):
dogs.isna()


Detecting any missing values and print just one false if the whole column has one null value (Check each column):
dogs.isna().any()


Counting missing values:
dogs.isna().sum()

Plotting missing values (how much for each column):
import matplotlib.pyplot as plt
dogs.isna().sum().plot(kind="bar")
plt.show()

Removing missing values, don't get the uncomplaining row:
dogs.dropna()

Replacing missing values
dogs.fillna(0)




















"""
