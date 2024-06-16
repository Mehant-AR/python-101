n = int(input())
d = {}
for i in range(n):
    s = input().split()
    d[s[0]] = list(map(int, s[1:]))
d1 = {k: sum(v) for k, v in d.items()}
sorted_d = dict(sorted(d1.items(), key=lambda x: x[1]))
for k, v in sorted_d.items():
    print(k, v)
