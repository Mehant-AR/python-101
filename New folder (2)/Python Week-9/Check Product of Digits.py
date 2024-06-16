def productDigits(n):
    a=n
    temp=[]
    list1=[]
    list2=[]
    rem=0
    while a!=0:
        rem=a%10
        temp.append(rem)
        a=a//10
    for i in range(len(temp)):
        if(i+1)%2==0:
            list1.append(temp[i])
        else:
            list2.append(temp[i])
    pro=1
    sum=0
    for i in list1:
        sum+=i
    for i in list2:
        pro*=i
    if pro%sum==0:
        return True
    else:
        return False
