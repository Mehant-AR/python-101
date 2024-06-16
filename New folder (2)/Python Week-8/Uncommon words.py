s1 = input().split()
s2 = input().split()
d = {}
for i in s1:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in s2:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in d:
    if d[i] == 1:
        print(i, end=" ")
