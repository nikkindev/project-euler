import time
start = time.time()

primes = []

def primefact(x): #Can be optimised by using recursion
  fact = []
  for i in range(2,x):
    if(x%i == 0 and isprime(i)):  fact.append(i)
  return(list(dict.fromkeys(fact)))

def isprime(x):
  global primes
  if(x in primes): return True
  for i in range(2,int(x**0.5)+1):
    if(x%i==0): return False
  primes.append(x)
  return True

flag = 0
for i in range(1,1000000):
  pf = primefact(i)
  if(len(pf) == 4): 
    flag += 1
    if(flag == 4):
      print(i+1-flag)
      break
    continue
  flag = 0
print(time.time()-start)

#Runtime: 18m