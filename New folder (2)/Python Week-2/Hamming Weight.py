a=int(input())
binary=bin(a)[2:]
c=0
for char in binary:
    if char=='1':
        c=c+1
print(c)
