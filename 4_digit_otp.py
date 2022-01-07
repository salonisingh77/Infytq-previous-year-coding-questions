"""
You will be given a number in the form of string, extract out digits at odd places, square & merge them. First 4 digits will be the required OTP.

Input : 

First Input : String

Output : 4 digit OTP
"""
s=input()
odd=[]
for i in range(len(s)):
    if i%2!=0:
        odd.append(int(s[i]))
print(odd)        
m=""        
for v in odd:
    m+=str(v*v)
    
print(m[0:4])    
    
        