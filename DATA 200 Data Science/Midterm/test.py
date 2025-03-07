import pandas as pd

foods_df = pd.DataFrame({'Name': ["Vasanth", "Shiangyi", "Rohan", "hi"], "Age": [10, 9, 5, 4], "Height":[3.2, 2.6, 2.1, 400], "Birth Month": ["Nov", "Oct", "Dec", "Dec"]})

print(foods_df.groupby("Birth Month").filter(lambda sf: sf["Height"].mean() < 5))