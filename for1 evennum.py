n=int(input("enter the number"))
sum=0
for i in range(1,n+1):
    if i%2==0:
        print("even number",i)
        sum=sum+i
print(sum)    