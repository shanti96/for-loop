n=int(input("enter the number"))
p=2
for i in range(p,n):
    if n%i==0:
        print("its not prime number")
        break
else:
    print("its prime number")    
    