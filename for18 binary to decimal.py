n=input("enter the binary number")
k=1
s=0
p=len(n)
for i in range(p,0,-1):
    j=int(n[i-1])
    if j==1:
        s=k+s
    k=k*2 
print(s)       