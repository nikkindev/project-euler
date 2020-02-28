import time
start = time.time()

count = 0
for iter in range(5,1001):
  n,d = 5,2
  for i in range(2,iter+1):
    if(i == iter):  
      n,d = n+d, n
      break
    n,d = 2*n+d, n
  if(len(str(n))>len(str(d))):  count += 1
  
print(count, time.time()-start)

#Runtime: 1s