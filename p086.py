import time
start = time.time()
count = 0
size = 1
while(True):
  for i in range(1,size+1):
    for j in range(i,size+1):  #Important to choose the lower bound to avoid repeated calculations
        if((((i+j)**2+size**2)**0.5).is_integer()): count += 1
  if(count > 1000000): break
  size += 1
print(size, time.time()-start)

#Ans: 1818
#Time: 1168s