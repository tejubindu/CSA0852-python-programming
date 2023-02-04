a=[]
n=int(input("Enter number of rows:"))
print("Enter the elements ::>")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    a.append(row)
print(a)
print("Display array in matrix form:")
for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
b=[]
n=int(input("Enter number of rows:"))
print("Enter the elements ::>")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    b.append(row)
print(b)
print("Display array in matrix form:")
for i in range(n):
    for j in range(n):
        print(b[i][j],end=" ")
    print()
result=[[0,0,0],[0,0,0],[0,0,0]]
print("The resultant addition matrix:")
for i in range(n):
    for j in range(len(a[0])):
        result[i][j]=a[i][j]+b[i][j]
        print(result[i][j],end=" ")
    print()
