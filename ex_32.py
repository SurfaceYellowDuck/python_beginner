a = [1, 3, 15, 25]
a_1 = 1
a_2 = 16
ind_list = []
for i in range(len(a)):
    if a_1 <= i <= a_2:
        ind_list.append(i - 1)
print(ind_list)
