a=[]
odd=0
even=0
n=int(input("enter the number of elements in list:"))
print("enter the elements:")
for i in range(0,n):
    x=int(input())
    a.append(x)
for j in a:    
    if j%2==0:
        even=even+j**2
    else:
        odd=odd+j**2
print('[',odd,',',even,']')
    
