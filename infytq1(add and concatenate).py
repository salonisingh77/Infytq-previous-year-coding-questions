s="31642372"
print(s)
a=""
m=0
k=s.find("4")
j=s.find("7")
for i in range(len(s)):
    if(i<k or i>j):
        m+=int(s[i])
a=s[k:j+1]
l=int(a)
l=l+m
print(l)


        
    