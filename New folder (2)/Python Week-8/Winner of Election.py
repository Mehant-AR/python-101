n=int(input())
d={}
for i in range(n):
    s=input()
    if s not in d:
        d[s]=1
    else:
        d[s]+=1
h=0
for i in d:
    if h<d[i]:
        h=d[i]
        j=i
print(j)
