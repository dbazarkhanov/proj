n = int(input())
a = list(map(int, input().split()))
cnt = 0
prev = 0
for i in range(0, len(a)):
    for j in range(i+2, len(a)+1):
        print(i, j, sep='/')
        if sum(a[i:j]) == 0:
            cnt += 1
        elif a[-1] < 0:
            continue
        elif j == len(a):
            cnt += 1
print(cnt)