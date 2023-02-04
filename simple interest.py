p=int(input("Enter the principal amount:"))
t=int(input("Enter the no of years:"))
if(p<=0 or t<=0):
    print("Invalid input")
    exit()
c=input("Is customer senior citizen(y/n):")
if(c=='y'):
    r=12
else:
    r=10
SI=(p*t*r)/100
print("Interest=",SI)
