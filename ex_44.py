import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(lst)
lst_dict = {"whoAmI_human": [], "whoAmI_robot": []}
for i in lst:
    if i == 'robot':
        lst_dict['whoAmI_robot'].append(True)
        lst_dict['whoAmI_human'].append(False)
    else:
        lst_dict['whoAmI_robot'].append(False)
        lst_dict['whoAmI_human'].append(True)
data_dict = pd.DataFrame(lst_dict)
print(data_dict.head(), '\n')

print(pd.get_dummies(data[["whoAmI"]].head()))
