# 16. Write a program to print the factorial of 
# a number accepted by the user.
n=int(input("enter the number"))
i=1
for j in range(n,0,-1):
    i=i*j
    print(i)