n=int(input())
s=input()
flag=0
for i in s:
    if(s.count(i)==1):
        flag=1
        print(i)
        break
if(flag==0):
    print(-1)
