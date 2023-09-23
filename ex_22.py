m, n = map(int, input("Enter two numbers separated by space \n").split())
list_1 = [int(input()) for _ in range(m)]
list_2 = [int(input()) for _ in range(n)]
res = sorted(set(list_1 + list_2))
print(res)
