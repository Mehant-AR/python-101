a=float(input())
if(a<200):
    b=a*1.20
    if(b<=100):
        b=100
        print(format(b,".2f"))
    else:
        print(format(b,".2f"))
elif(a>=200 and a<400):
    c=a*1.50
    if(c>=400):
       print(format(c*0.15+c,".2f"))
    else:
       print(format(c,".2f")) 
elif(a>=400 and a<600):
    d=a*1.80
    print(format(d*0.15+d,".2f"))
elif(a>600):
    e=a*2.00
    print(format(e*0.15+e,".2f"))
