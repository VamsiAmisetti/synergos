def Solve(a,b,c):
  if(b>a):
    return -1
  elif(c<a):
    if(c%a==b):
      return c
    else:
      return -1
  else:
    return c-(c%a)-(a-b)

T=int(input())
for i in range(T):
  A=list(map(int,input().split()))
  out_=Solve(A[0],A[1],A[2])
  print(out_)
