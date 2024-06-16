#Program:
try:
    a=input()
    if int(a)>=0:
        print("You are",a,"years old.")
    else:
        print("Error: Please enter a valid age.")
except:
    print("Error: Please enter a valid age.")
