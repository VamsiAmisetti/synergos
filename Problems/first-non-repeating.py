n=input()
d={}
for i in range(len(n)):
    if n[i] in d:
        d[n[i]]+=1
    else:
        d[n[i]]=1
for k in d:
    if(d[k]==1):
        print(k)
        break
