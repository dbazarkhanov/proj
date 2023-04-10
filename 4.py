n = int(input())
a = list(map(int, input().split()))

cnt = {}
max_len = 0
invalid = {}

for i in range(2, n):
    cnt[a[i]] = cnt.get(a[i], 0) + 1
    print(i, cnt, sep='/')
    for j in range(2, i+1):
        if cnt[a[j]] != min(cnt.values()):
            invalid[i] = {cnt[a[j]]: 0}
print(invalid)