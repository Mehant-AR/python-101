#Program:
t=int(input())
for i in range(0,t):
    n=int(input())
    l=[]
    for j in range(0,n):
        a=int(input())
        l.append(a)
    p=int(input())
    for k in range(0,n):
        c=0
        for m in range(i+1,n):
            if l[m]-l[k]==p:
                c=1
                print('1')
                break
        if c==1:
            break
    if c==0:
        print('0')
