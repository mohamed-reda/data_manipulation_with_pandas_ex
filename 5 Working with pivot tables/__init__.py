"""








Pivoting the dog pack get the column of height_cm, index is breed, columns is color:
dogs_height_by_breed_vs_color = dog_pack.pivot_table("height_cm", index="breed", columns="color")
print(dogs_height_by_breed_vs_color)

.loc[] + slicing is a power combo:
dogs_height_by_breed_vs_color.loc["Chow Chow":"Poodle"]

The axis argument: (the mean based on index)
dogs_height_by_breed_vs_color.mean(axis="index")


Calculating summary stats across columns: (the mean based on columns (the color))
dogs_height_by_breed_vs_color.mean(axis="columns")




















temperatures["year"] = temperatures["date"].dt.year

"""
