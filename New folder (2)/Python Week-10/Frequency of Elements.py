lst5=[int(x) for x in input().split(" ")]
lst=sorted(list(set(lst5)))
c=0
for i in lst:
    c=0
    for j in lst5:
        if(i==j):
            c=c+1
    print("%d %d"%(i,c))
