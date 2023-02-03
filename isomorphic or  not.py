def isisomorphic(string1,string2):
   if len(string1)!=len(string2):
        return False
   else:
    map1,map2={},{}
    for i in range(len(string1)):
       ch1,ch2=string1[i],string2[i]
       if ch1 not in map1:
        map1[ch1]=ch2
       if ch2 not in map2:
        map2[ch2]=ch1
       if map1[ch1]!=ch2 or map2[ch2]!=ch1:
         return False
    return True
string1=input("string1=")
string2=input("strint2=")
print(isisomorphic(string1,string2))
