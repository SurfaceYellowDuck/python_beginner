list_ = [2, 3, 4, 5, 6, 7, 8]
max_sum = 0
for x in range(len(list_)):
    sum_ = 0
    if x == 0:
        sum_ = list_[x] + list_[-1] + list_[x + 1]
    if x == len(list_) - 1:
        sum_ = list_[x] + list_[0] + list_[x - 1]
    else:
        sum_ = list_[x] + list_[x + 1] + list_[x - 1]
    if sum_ > max_sum:
        max_sum = sum_
print(max_sum)
