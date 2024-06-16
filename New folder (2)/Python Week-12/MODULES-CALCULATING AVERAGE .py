import math
a = int(input())
n=a
b = input().split()
s = 0
p = b.index("MARKS")
while a!=0:
    c = input().split()
    s += int(c[p])/n
    a-=1
print(f"{s:.2f}")
