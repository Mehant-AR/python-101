a=int(input())
b=a%100
c=a%400
if(b==0):
    if(c==0):
        print(a,"is a leap year.")
    else:
        print(a,"is not a leap year.")
elif(a%4==0):
    print(a,"is a leap year.")
