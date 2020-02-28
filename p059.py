import time
start = time.time()

def xor():
  with open('p059cipher.txt') as f:
    for line in f:  a = line.split(',')

  alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for u in alphabets:
    for v in alphabets:
      for w in alphabets:
        fullkey = (u+v+w)*485
        message = ''
        for i in range(len(a)): message = message + chr(ord(fullkey[i])^int(a[i]))
        if('Euler' in message): 
          print('Key:',u+v+w, 'Sum: ', sum(map(ord, message)),'\n',message)
          return True

xor()
print(time.time()-start)

#Runtime: 11s