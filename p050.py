import time
start = time.time()

p = [2,3,5,7,11]
for i in range(12,1000000):
  flag = 0
  for j in range(2,int(i**0.5)+1):
    if(i%j == 0):
      flag = 1
      break
  if(flag == 0): p.append(i)
print(len(p))

count = 0
start_index = 0

def issum(x):
  global p,count,start_index, flag
  for i in range(p.index(x)):
    d = i
    start_index = d
    s = 0
    temp_count = 0
    while(True):
      s+=p[d]
      temp_count += 1
      if(s == x): 
        if(temp_count > count): count = temp_count
        return True
      if(s > x):  break
      d += 1

  return False

ans = [0,0,0]
for i in p:
  if(issum(i)):
    if(count > ans[1]): ans = [i,count,start_index]
print(ans)

print(time.time()-start)

#Runtime: 1h20m