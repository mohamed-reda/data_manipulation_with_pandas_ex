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

is_lab = dogs["breed"] == "Labrador"
is_brown = dogs["color"] == "Brown"
dogs[is_lab & is_brown]
or:
dogs[ (dogs["breed"] == "Labrador")  &(dogs["color"] == "Brown") ]
Subsetting based on multiple conditions

is_black_or_brown = dogs["color"].isin(["Black", "Brown"])
dogs[is_black_or_brown]
Subsetting using .isin()




# Sort homelessness by 'individuals'
homelessness_fam = homelessness.sort_values("family_members", ascending=False)
print(homelessness_fam.head())

homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())


fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == 'Pacific')]
# homelessness[homelessness["individuals"] > 1000]
# See the result
print(fam_lt_1k_pac)

print(homelessness.)
"""
