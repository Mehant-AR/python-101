a=int(input())
c=0
for i in range(a):
    if a==2**i:
        c+=1
if c==1:
    print("True")
else:
    print("False")
