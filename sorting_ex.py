"""

sorting:
dogs.sort_values("weight_kg")

dogs.sort_values("weight_kg", ascending=False)
for Sorting in descending order


dogs.sort_values(["weight_kg", "height_cm"])
Sorting by multiple variables

dogs.sort_values(["weight_kg", "height_cm"], ascending=[True, False])
Sorting by multiple variables

dogs["name"]
Subsetting columns

dogs[["breed", "height_cm"]]
=
cols_to_subset = ["breed", "height_cm"]
dogs[cols_to_subset]
Subsetting multiple columns

dogs["height_cm"] > 50
Subsetting rows and in print it gets true or false

dogs[dogs["height_cm"] > 50]
Subsetting rows and it fets the rows values that valid

dogs[dogs["breed"] == "Labrador"]
Subsetting based on text data

dogs[dogs["date_of_birth"] < "2015-01-01"]
Subsetting based on dates

















print(homelessness.)
"""
