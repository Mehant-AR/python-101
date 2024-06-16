l=[]
while(True):
    a=input()
    if a!=" ":
        l.append(a)
    else:
        break
l=dict.fromkeys(l)
for i in l:
    print(i) 
