odd=['January','March','May','July','August','October','December']
even=['April','June','September','November']
a=input()
if(a=='February'):
    print("February has 28 or 29 days in it.")
if a in odd:
    print(a,"has 31 days in it.")
if a in even:
    print(a,"has 30 days in it.")
