n=int(input("enter a value:"))
temp=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(temp==r):
    print("the value is a palindrome")
else:
    print("the value is not a palindrome")
