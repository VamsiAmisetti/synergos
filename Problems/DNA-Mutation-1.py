def compare(s1,s2):
    count=0
    for i in range(len(s1)):
        if(s1[i]!=s2[i]):
            count+=1
    if(count>1):
        return False
    else:
        return True
s1=input()
s2=input()
n=len(s1)-(len(s2)-1)
m=len(s2)
for i in range(n):
    if(compare(s2,s1[i:i+m])):
        print(i+1)
        break
