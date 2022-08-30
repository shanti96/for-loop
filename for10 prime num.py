n=int(input("enter a number"))
for i in range(2,n+1):
    flag=True
    for j in range(2,i+1):
        if i%j==0 and i!=j:
            flag=False
            break
    if flag==True:
        print(i)         