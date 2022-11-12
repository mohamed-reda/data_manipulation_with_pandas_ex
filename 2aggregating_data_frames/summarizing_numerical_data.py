"""
Summarizing numerical data:
dogs["height_cm"].mean()
or
.median() , .mode()
.min() , .max()
.var() , .std()
.sum()
.quantile()

compute custom summary statistics:
dogs["height_cm"].agg()

compute .3 of the columns:
def fun(column):
    column.quantile(.3)
dogs["height_cm"].agg(fun)

Summaries on multiple columns:
dogs[["weight_kg", "height_cm"]]..agg(fun)

Multiple summaries:
dogs["weight_kg"].agg([fun, fun2])

Cumulative sum:
dogs["weight_kg"].cumsum()

Cumulative statistics:
.cummax()
.cummin()
.cumprod()

Dropping duplicate names:
vet_visits.drop_duplicates(subset="name")

Dropping duplicate pairs:
sales = vet_visits.drop_duplicates(subset=["name", "breed"])
print(sales)

Easy as 1, 2, 3:
sales["breed"].value_counts()
sales["breed"].value_counts(sort=True)

Proportions
sales["breed"].value_counts(normalize=True)
store_depts["department"].value_counts(sort="department", ascending=False)

--------------------------------------------------------------------------------------------------
Summaries by group(is the black dogs is heavier than the brown in average):
dogs[dogs["color"] == "Black"]["weight_kg"].mean()

Grouped summaries:
dogs.groupby("color")["weight_kg"].mean()

Multiple grouped summaries:
dogs.groupby("color")["weight_kg"].agg([min, max, sum])

Grouping by multiple variables
dogs.groupby(["color", "breed"])["weight_kg"].mean()

Many groups, many summaries
dogs.groupby(["color", "breed"])[["weight_kg", "height_cm"]].mean()

--------------------------------------------------------------------------------------------------
Group by to pivot table:
dogs.groupby("color")["weight_kg"].mean()
=
dogs.pivot_table(values="weight_kg", index="color")

Different statistics:
import numpy as np
dogs.pivot_table(values="weight_kg", index="color", aggfunc=np.median)

Multiple statistics:
dogs.pivot_table(values="weight_kg", index="color", aggfunc=[np.mean, np.median])

Pivot on two variables:
dogs.groupby(["color", "breed"])["weight_kg"].mean()
dogs.pivot_table(values="weight_kg", index="color", columns="breed")

Filling missing values in pivot tables:
dogs.pivot_table(values="weight_kg", index="color", columns="breed", fill_value=0)

Summing with pivot tables (it adds another column of the mean of each row):
dogs.pivot_table(values="weight_kg", index="color", columns="breed",
fill_value=0, margins=True)






# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales["store",'department'].value_counts()
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales[is_holiday]].drop_duplicates(subset=['store', 'department'])

# Print date col of holiday_dates
print(holiday_dates['date'])






"""
""""
print(sales['weekly_sales'].median())

print(sales["temperature_c"].agg(iqr))

print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr,np.median]))

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date", ascending=True)

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1["weekly_sales"].cummax()


# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
"""
