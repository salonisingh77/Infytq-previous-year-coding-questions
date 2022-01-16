
# Given a string and it contains the digits as well as non-digits. We have to find the largest even number from available digits after removing the duplicates. If not possible, print -1.
#Sample Testcases :
#I/P 1:%#32%#%2
#O/P 1:#32
#I/P 2:%#2373#@
#O/P 2:732
s=input()
digit=[i for i in set(s) if i.isdigit()]
digit.sort()
digit.reverse()
n=int("".join(digit))
if n%2==0:
    print(n)
else:
    l=len(digit)
    for i in range(l-1,0,-1):
        if((int(digit[i]))%2==0):
            a=digit[i]
            digit.remove(a)
            digit.insert(l-1,a)
            e=int("".join(digit))
            print(e)
            break
    else:
        print(-1)

