import math
a=int(input())
b = a + 1
while b > 0 :
   m=math.sqrt(b)
   if(m==int(m)):
      print(b)
      break
   else:
      b = b + 1
