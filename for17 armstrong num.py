n=input("enter the number")
p=len(n)
s=0
for i in range(0,p):
    j=int(n[i])**p
    s=s+j
print(s)
if s==int(n):
    print("its armstrong number")
else:
    print("not armsrong number")        