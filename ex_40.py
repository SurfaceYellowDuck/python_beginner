import pandas as pd

df = pd.read_csv("sample_data/california_housing_train.csv")
query_summas = df.query('0 <= population <= 500')[['median_house_value']]
mid_house_val_1 = query_summas.median()  # не совсем понял, здесь нужно определить среднее, из существующих, или среднее арифметическое
mid_house_val_2 = query_summas.sum() / query_summas.shape[0]
print(mid_house_val_1, '\n', mid_house_val_2)
