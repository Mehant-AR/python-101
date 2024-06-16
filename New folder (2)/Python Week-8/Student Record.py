n=int(input())
d={}
for i in range(n):
    na=input().split()
    d[na[0]]=[int(na[1]),int(na[2]),int(na[3])]
    l=int(na[3])

h=0
for i in d:
    if h< sum(d[i]):
        h=sum(d[i])
        j=i
        h1=sum(d[i])
print(j)
h=0


for i in d:
    if(h<d[i][1]):
        h=d[i][1]
        j=i
for i in d:
    if(h==d[i][1]):
        print(i,end=" ")
l1=[]
k=[]
print()
for i in d:
    if(l>d[i][2]):
        l=d[i][2]
        j=i
for i in d:
    if(l==d[i][2]):
        l1.append(i)
for i in range(-1,-len(l1)-1,-1):
    print(l1[i],end=" ")
print()

for i in d:
    if h1> sum(d[i]):
        h1=sum(d[i])
        j=i
print(j)
