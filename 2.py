from math import ceil
n, m, k = map(int, input().split())
time = ceil(n*k/m)
print(time)