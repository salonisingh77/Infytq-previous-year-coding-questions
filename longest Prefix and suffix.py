#Given a string s, find length of the longest prefix which is also suffix. The prefix and suffix should not overlap.
#Sample Testcases :
#I/P 1:codeecode
#O/P 1:4 (code is only prefix-suffix & has length 4)
#I/P 2:wwwwww
#O/P 2:3 (www is only prefix-suffix & has length 3)
s=input()
mid=len(s)//2
l=len(s)
for i in range(mid,0,-1):
    prefix=s[0:i]
    suffix=s[l-i:l]
    if(prefix==suffix):
        print(len(prefix))
        break