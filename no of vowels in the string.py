s=input("Enter any string:")
b=s.lower()
count=0
for x in b:
    if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
        count+=1
print("Number of vowels in string are:",count)
