n=input("enter the number")
p=len(n)
k=""
for i in range(p,0,-1):
    j=n[i-1]
    k=k+j
print(k)    
if int(k)==int(n):
    print("palindrome") 
else:
    print("not palindrome")       