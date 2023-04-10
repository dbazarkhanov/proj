n = int(input())
s = input()
if 'a' not in s or 'b' not in s or 'c' not in s or 'd' not in s: print(-1)
else:
    occ = {'a': -1, 'b': -1, 'c': -1, 'd': -1}
    min_len = float('inf')
    for i, v in enumerate(s):
        occ[v] = i
        if -1 in occ.values(): continue
        length = max(occ.values()) - min(occ.values()) + 1
        if length < min_len:
            min_len = length
    print(min_len)