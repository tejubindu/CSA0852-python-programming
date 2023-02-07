a=[]
b=[]
n=int(input("Enter the  number of elements in list:"))
print("Enter the names:")
for i in range(n):
    x=input()
    b=x.lower()
    a.append(b)
print("Enter the choice of sorting:")
print("A.ascending order")
print("D.descending order")
choice=input("Enter choice (A/D):")
if choice=='A':
    a.sort()
    print("Ascending order:",a)
elif choice=='D':
    a.sort(reverse=True)
    print("Descending order",a)
else:
    print("wrong choice")
