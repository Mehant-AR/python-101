s=input()
l=[]
for i in s:
    if(i.isalpha()):
        l.append(i)
l.reverse()
r=''
index=0
for i in s:
    if(i.isalpha()):
        r+=l[index]
        index+=1
    else:
        r+=i
print(r)
