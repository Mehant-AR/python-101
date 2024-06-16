#Program:
try:
    a=input()
    b=input()
    c=float(a)/float(b)
except ZeroDivisionError:
    print("Error: Cannot divide or modulo by zero.")
except:
    print("Error: Non-numeric input provided.")
else:
    print(c)
