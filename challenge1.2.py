def fac(n):
  if n==0:
    return 1
  else:
    return n*fac(n-1)
    
n=int(input("Enter a Number"))
r=fac(n)
print(r)
