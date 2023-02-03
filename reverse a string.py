def reverse(s):
    str=" "
    for i in s:
        str=i+str
    return str
s=input("enter any string:")
print("original string:",s)
print("reverse a string:",reverse(s))
