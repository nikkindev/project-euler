from itertools import permutations

x = list(permutations(['1','2','3','4','5','6','7']))
# Tuples should contain integers to be albe to use the .join() function later
sol = 0
for i in x:
  flag = 0
  n = int(''.join(i))
  # Check if n is prime
  for j in range(2,int(n**0.5)+1):
    if(n%j == 0):
      flag = 1
      break
  if(flag == 0 and n > sol):sol = n
print(sol)
