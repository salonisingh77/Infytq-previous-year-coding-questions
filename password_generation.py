
# Online Python - IDE, Editor, Compiler, Interpreter

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
            