import pandas as pd

df = pd.read_csv("sample_data/california_housing_train.csv")
min_pop = df["population"].min() * 1.45
max_households = df.query(f"population < {min_pop}")["households"].max()
print(max_households)
