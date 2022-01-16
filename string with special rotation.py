#You are provided two or more strings, where each string is associated with the number (seperated by :). If sum of square of digits is even then rotate the string right by one position, and if sum of square of digits is odd then rotate the string left by two position.
#Sample Testcases :

#I/P 1 :abcde:234,pqrs:246
#O/P 1 :cdeab spqr


s=input().split(',')
for i in s:
    sr,n=i.split(":")
    l=len(sr)
    sum=0
    for j in n:
        sum +=(int(j)**2)
    if(sum%2==0):
        sm=sr[l-2:l]
        print(sm+sr[0:l-2],end=' ')
    else:
        sm=sr[0]
        print(sr[1:l-1]+sm,end=' ')