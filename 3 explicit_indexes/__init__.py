"""
Setting a column as the index:
dogs_ind = dogs.set_index("name")
print(dogs_ind)

Removing an index:
dogs_ind.reset_index()

Dropping an index (drop the customized index that I did before with the name column):
dogs_ind.reset_index(drop=True)

Indexes make subsetting simpler:
dogs[dogs["name"].isin(["Bella", "Stella"])]
dogs_ind.loc[["Bella", "Stella"]]

Index values don't need to be unique:
dogs_ind2 = dogs.set_index("breed")
print(dogs_ind2)

Subsetting on duplicated index values:
dogs_ind2.loc["Labrador"]

Multi-level indexes a.k.a. hierarchical indexes:
dogs_ind3 = dogs.set_index(["breed", "color"])
print(dogs_ind3)

Subset the outer level with a list:
dogs_ind3.loc[["Labrador", "Chihuahua"]]

Subset inner levels with a list of tuples:
dogs_ind3.loc[[("Labrador", "Brown"), ("Chihuahua", "Tan")]]

Sorting by index values:
dogs_ind3.sort_index()

Controlling sort_index:
dogs_ind3.sort_index(level=["color", "breed"], ascending=[True, False])





"""
