a=input()
n=len(a)
r=0
for i,d in enumerate(a): 
     r+=int(d)**(i+1)
     if r==int(a):
        print("Yes")
    else:
          print("No")
