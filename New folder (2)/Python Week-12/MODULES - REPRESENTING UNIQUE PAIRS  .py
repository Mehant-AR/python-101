a=int(input())
b=input().split()
c=int(input())
co=0
l=[int(b) for b in b]
for i in range(0,a):
    for j in range(0,a):
        if abs(l[i]-l[j])==c and i<j:
            co+=1
print(co)
