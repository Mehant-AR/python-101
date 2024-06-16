a=int(input())
b=[]
for i in range(4):
    c=int(input())
    b.append(c)
for i in range(4):
    if(b[i]%a==0):
        print("True",end=" ")
    else:
        print("False",end=" ")
