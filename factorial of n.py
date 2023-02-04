n=int(input("Enter a number:"))
fact=1
count=0
if(n<0):
    print("Negative number")
else:
    for i in range(1,n+1):
        fact=fact*i
        if(n%i==0):
            count+=1
    print("factorial of",n,"is:",fact)
    print("Number of factors for",n,"is:",count)
