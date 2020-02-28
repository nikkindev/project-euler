ret = []
for i in range(11,10001):
  count = 1
  t = i
  flag = 0
  while (count<=52):
    t = t+int(str(t)[::-1])
    if(str(t)==str(t)[::-1]):
      flag = 1
      break
    count += 1
    
  if(flag == 1): continue
  if(str(i) == str(i)[::-1]): print(i)
  ret.append(i)
print(len(ret)) 