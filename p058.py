import time
start = time.time()

def isprime(x):
  if all(x%i != 0 for i in range(2,int(x**0.5)+1)): return True
  return False


s,i = 2,2
primecount = 0
while(True):
  l = 2*(i-1)+1
  n = 4*l-2
  if(isprime(int(s+(l-1)/2))):  primecount += 1
  if(isprime(int(s+3*(l-1)/2))):  primecount += 1
  if(isprime(int(s+5*(l-1)/2))):  primecount += 1
  s = s+n-1
  if(primecount/(((i-1)*4)+1) < 0.1): break
  i = i+1

print(l, time.time()-start)

#Runtime: 32s