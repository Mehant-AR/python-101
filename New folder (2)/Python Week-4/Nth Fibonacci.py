a=int(input())
b=0
c=1
if(a==1):
     print("0")
elif(a==2):
       print("1")
else:
        for i in range (3,a+1):
              d=b+c
               b=c
               c=d
         print(d)
