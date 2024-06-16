a=int(input())
b=int(input())
c=int(input())
if(a==b and b==c and c==a):
    print("That's","a","equilateral triangle")
elif(a!=b and a!=c and b!=c):
    print("That's","a","scalene triangle")
else:
    print("That's","a","isosceles triangle")
