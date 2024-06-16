#Program:
import math
try:
    n=input()
    n=float(n)
    if n < 0:
        print("Error: Cannot calculate the square root of a negative number.")
    else:
        r= math.sqrt(n)
        print("The square root of {} is {:.2f}".format(n, r))
        
except ValueError:
    print("Error: could not convert string to float")
