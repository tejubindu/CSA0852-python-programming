a=[]
j=int(input("enter the number of elements:"))
print("enter the elements of the list:")
for i in range(0,j):
    x=int(input())
    a.append(x)
a.sort()
m=int(input("enter m value:"))
n=int(input("enter n value:"))
sum=a[j-m]+a[n-1]
sub=a[j-m]-a[n-1]
print("mth maximum element=",a[j-m])
print("nth minimum element=",a[n-1])
print("sum=",sum)
print("difference=",sub)
