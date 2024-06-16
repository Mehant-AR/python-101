try:
    a=input()
    b=input()
    c=int(a)/int(b)
    d=int(a)%int(b)
except ZeroDivisionError:
    print("Error: Cannot divide or modulo by zero.")
except:
    print("Error: Non-numeric input provided.")
else:
    print("Division result:",c)
    print("Modulo result:",d)
