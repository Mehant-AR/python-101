a=int(input())
lst1=[str(x) for x in input().split(" ")]
lst2=[]
lst=[]
g=0
for i in lst1:
    if i.isdigit():
        g=int(i)
        lst.append(g)
for i in range(0,a):
    if(i==0):
        if(lst[i]>=lst[i+1]):
            lst2.append(lst[i])
    elif(i>0 and i<a-2):
        if(lst[i]>=lst[i-1] and lst[i]>=lst[i+1]):
            lst2.append(lst[i])
    elif(i==a-1):
        if(lst[i]>=lst[i-1]):
            lst2.append(lst[i])
for i in lst2:
    print(i,end=" ")
