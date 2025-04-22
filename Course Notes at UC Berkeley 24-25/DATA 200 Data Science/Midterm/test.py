import pandas as pd

foods_df = pd.DataFrame({'Name': ["Vasanth", "Shiangyi", "Rohan", "hi"], "Age": [10, 9, 5, 4], "Height":[3.2, 2.6, 2.1, 400], "Birth Month": ["Nov", "Oct", "Dec", "Dec"]})
print(foods_df)
print(sum(foods_df["Age"]))
print(foods_df["Age"].sum())
print((foods_df["Birth Month"] == "Dec").sum())
print(foods_df.groupby("Birth Month")["Age"].agg('count'))
# print(foods_df.groupby("Birth Month").filter(lambda sf: sf["Height"].mean() < 5))


test = pd.Series([True, False, True])
print(test.sum())


panda = pd.DataFrame({"Name": ["Pete", "Sarah", "Bono", "Jasper", "May"], "height": [18, 29, 7, 4, 13], "age": [13, 4, 2, 2, 4], "Sport": ["H", "H", "S", "S", "W"]})

panda["ratio"] = panda["height"]/panda["age"]
print(panda.groupby("age")["ratio"].median())

print(panda.groupby("age").apply(lambda x: (x["height"] / x["age"]).median()))


print(panda.sort_values(by="age", ascending=False).groupby("Sport").agg({"Name":"first", "height":"first"}))