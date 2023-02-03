count_lower=0
count_upper=0
count_number=0
print("enter * to exit:")
for i in range(10):
    x=input("enter any character:")
    if(x=="*"):
       break
    if(x.islower()):
        count_lower+=1
    elif(x.isupper()):
        count_upper+=1
    elif(x.isnumeric()):
        count_number+=1
print("the number of lowercase character is:",count_lower)
print("the number of uppercase character is:",count_upper)
print("count of numbers is:",count_number)
