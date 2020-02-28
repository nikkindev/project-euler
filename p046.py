import time
start = time.time()

def isprime(x):
  flag = 0
  for i in range(2,int(x**0.5)+1):
    if(x%i == 0):
      flag = 1
      break
  if(flag == 1): return False
  return True



i = 29
while(True):
  if(isprime(i)): 
    i = i+2
    continue
  flag = 0
  for j in range(2,i):
    if(isprime(j)):
      if((((i-j)/2)**0.5).is_integer()):
        flag = 1
        break
  if(flag == 0): 
    print(i)
    break
  i = i+2

print(time.time()-start)

#Runtime: 3s