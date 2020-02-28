import time
start = time.time()

with open('p051primes.txt','r') as f:
  primes = [int(line.rstrip()) for line in f]

def isprime(x):
  global primes
  if (x > primes[-1]):
    if all(x%i!=0 for i in range(2,int(x**0.5)+1)):  return True
    return False
  if (x in primes): return True
  return False

fam = 8

for i in primes:
  #print(i)
  flag = 0
  if(len(str(i))-len(''.join(set(str(i)))) > 0):  #Check if there are any repeating digits
    for a in range(10-fam+1): #Finding the lowest number puts an upper cap on the least repeating number
      if(str(i).count(str(a)) > 1):
        count = 0
        for b in range(a+1,10):
          if(isprime(int(str(i).replace(str(a),str(b))))):  count += 1 #Replace recurring digit with different digits
        if(count == fam-1):
          print(i)
          flag = 1
          break
    if(flag == 1): break

print(time.time()-start)

#Runtime: 118s