def fun():
    a = [1, 3, 15, 25]
    a_1 = int(input("Input num one"))
    a_2 = int(input("Input num two"))
    ind_list = []
    for i in range(len(a)):
        if a_1 <= a[i] <= a_2:
            ind_list.append(i)
    return ind_list
print(fun())
