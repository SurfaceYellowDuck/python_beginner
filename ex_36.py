def calculate_element(x, y):
    return x * y


def print_operaton_table(operation, columns, rows):
    res_list = []
    for i in range(1, columns + 1):
        row_list = []
        for j in range(1, rows + 1):
            row_list.append(calculate_element(i, j))
        res_list.append(row_list)
    return res_list

print(print_operaton_table(calculate_element, 6, 6))
