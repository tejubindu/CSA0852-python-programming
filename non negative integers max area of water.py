def maxArea(A,len):
    area=0
    for i in range(len):
        for j in range(i+1,len):
            area=max(area,min(A[j],A[i])*(j-i))
    return area
b=[]
a=int(input("enter the number of elements:"))
print("enter the elements:")
for i in range(0,a):
      c=int(input())
      b.append(c)
print("array=",b)
print("maximum area of water=",maxArea(b,a))
