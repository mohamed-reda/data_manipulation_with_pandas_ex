"""
Histograms
import matplotlib.pyplot as plt
dog_pack["height_cm"].hist()
plt.show()


Bar plots get by group so ypu won't repeat breed, get just the mean of weight_kg:
avg_weight_by_breed = dog_pack.groupby("breed")["weight_kg"].mean()
print(avg_weight_by_breed)

Bar plots:
avg_weight_by_breed.plot(kind="bar", title="Mean Weight by Dog Breed")
plt.show()

Line plots:
sully.head()
sully.plot(x="date", y="weight_kg", kind="line")
plt.show()

Rotating axis labels ( Rotating x titles):
sully.plot(x="date", y="weight_kg", kind="line", rot=45)
plt.show()

Scatter plots:
dog_pack.plot(x="height_cm", y="weight_kg", kind="scatter")
plt.show()

Layering plots show 2 different colors of hist:
dog_pack[dog_pack["sex"]=="F"]["height_cm"].hist()
dog_pack[dog_pack["sex"]=="M"]["height_cm"].hist()
plt.show()

Add a legend to explain what is the color of each hist:
dog_pack[dog_pack["sex"]=="F"]["height_cm"].hist()
dog_pack[dog_pack["sex"]=="M"]["height_cm"].hist()
plt.legend(["F", "M"])
plt.show()

Transparency
dog_pack[dog_pack["sex"]=="F"]["height_cm"].hist(alpha=0.7)
dog_pack[dog_pack["sex"]=="M"]["height_cm"].hist(alpha=0.7)
plt.legend(["F", "M"])
plt.show()
















"""
