a=int(input())
c=0
for i in range(2,a):
if(a%i==0):
c=1
if(c==1):
print("1")
elif(c==0): print("2”)
