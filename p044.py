import numpy as np
pent = []
for i in range(1,10000):
  pent.append(int(i*(3*i-1)*0.5))
print(len(pent))

p1,p2 = 0, 0
diff = 100000000000000
for i in pent:
  for j in pent:
    if(i == j): continue
    x = i+j
    y = abs(i-j)
    r1 = (1+np.sqrt(1+24*x))/6
    r2 = (1-np.sqrt(1+24*x))/6
    r3 = (1+np.sqrt(1+24*y))/6
    r4 = (1-np.sqrt(1+24*y))/6
    if((r1.is_integer() and r1 > 0) or (r2.is_integer() and r2 > 0)):
      if((r3.is_integer() and r3 > 0) or (r4.is_integer() and r4 > 0)):
        print(x,y)
        if(y < diff): 
          diff = y
          p1,p2 = i,j
print(p1,p2,diff)