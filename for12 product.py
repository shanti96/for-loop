n=input("enter the number")
p=0
s=len(n)+1
sum=1
for j in range(1,s):
    i=int(n[p])
    sum=sum*i
    p=p+1
print(sum)    