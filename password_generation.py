
#Problem: Take input from user in the given format (consist of name and code), find max digit from Code which is less or equal to the length of String and put that place Char in final String if there is no any digit found which not satisfy the condition that simply put ‘X’.
#Sample Input:
#Abhishek:34848,Mayur:4739,Friends:2949,Yeah:9889
#Sample Output:
#kueX

input_str=input().split(",")
out=""
for i in input_str:
    s,n=i.split(":")
    l=len(s)
    max=0
    for j in n:
        if(int(j)<=l and int(j)>=max):
            max=int(j)
    if(max>0):
        out+=s[int(max)-1]
    else:
        out+="X"
print(out)        
            
