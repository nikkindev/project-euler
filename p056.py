m = 0
for i in range(1,100):
  for j in range(1,100):
    ret = 0
    for s in str(i**j):
      ret += int(s)
      if(ret > m): m = ret
print(m) 