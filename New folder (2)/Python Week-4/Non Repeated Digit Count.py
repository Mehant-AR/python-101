a={}
for i in input:
   if i in a:a[i]+=1
   else:a[i]=1
print(sum([1 for i in a if a[i]==1]))
