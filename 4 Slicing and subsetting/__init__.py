"""
Slicing lists:
breeds[2:5]

Sort the index before you slice:
dogs_srt = dogs.set_index(["breed", "color"]).sort_index()
print(dogs_srt)

Slicing the outer index level:
dogs_srt.loc["Chow Chow":"Poodle"]

Slicing the inner index levels badly:
dogs_srt.loc["Tan":"Grey"]

Slicing the inner index levels correctly:
dogs_srt.loc[("Labrador", "Brown"):("Schnauzer", "Grey")]

Slicing columns thi won't get any other columns after height_cm:
dogs_srt.loc[:, "name":"height_cm"]

Slice twice rows then columns:
dogs_srt.loc[("Labrador", "Brown"):("Schnauzer", "Grey"), "name":"height_cm"]

Dog days:
dogs = dogs.set_index("date_of_birth").sort_index()
print(dogs)

Slicing by dates:
# Get dogs with date_of_birth between 2014-08-25 and 2016-09-16:
dogs.loc["2014-08-25":"2016-09-16"]
# Get dogs with date_of_birth between 2014-01-01 and 2016-12-31
dogs.loc["2014":"2016"]

Subsetting by row/column number (show rows from index 2 to 4 , show columns from index 1 to 3)
print(dogs.iloc[2:5, 1:4])







temperatures_bool = temperatures[(temperatures["date"] >= '2010-01-01' ) & (temperatures["date"] <= '2011-12-01' )]
print(temperatures_bool)
"""
