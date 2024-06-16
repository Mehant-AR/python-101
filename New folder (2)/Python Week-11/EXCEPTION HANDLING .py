try:
    a=input()
    if(int(a)>0 and int(a)<101):
        print("Valid input.")
    else:
        print("Error: Number out of allowed range")
except:
    print("Error: invalid literal for int()")
