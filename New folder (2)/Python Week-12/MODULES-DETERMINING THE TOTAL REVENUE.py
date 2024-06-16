a=int(input())
b=input().split()
c=int(input())
s=0
for i in range(c):
    l1=[]
    l1=input().split()
    if l1[0] in b:
        s+=int(l1[1])
        b.remove(l1[0])
print(s)
