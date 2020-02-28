import time
from itertools import permutations
start = time.time()

def isprime(x):
  flag = 0
  for i in range(2,int(x**0.5)+1):
    if(x%i == 0):
      flag = 1
      break
  if(flag == 1): return False
  return True

flag = 0
for i in range(1000,9999):
  prime_list  = []
  count = 0
  if(isprime(i)):
    p = permutations([t for t in str(i)])
    for j in p:
      a = int(''.join(j))
      if(isprime(a)): 
        if(len(str(a)) == 4):  prime_list.append(a)
        count += 1
  #print(len(prime_list))
  prime_list = list(dict.fromkeys(prime_list))  #Get rid of repeated values
  prime_list.sort()
  
  if(1487 in prime_list): continue

  for p1 in prime_list:
    for p2 in prime_list:
      if(p1 == p2 or len(str(p1)) < 4 or len(str(p2)) < 4): continue
      if(int((p1+p2)/2) in prime_list): 
        print (p1,p2,int((p1+p2)/2), 'jawohl')
        flag += 1 

    
  if(flag == 1): break


print(time.time()-start)

#Runtime: 1.7s