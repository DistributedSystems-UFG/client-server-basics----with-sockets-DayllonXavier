from socket  import *
from constCS import * #-

MAXVALUE = int(1e6)

primes = []
markPrimes = [0] * MAXVALUE

def computePrimes():
  markPrimes[0] = markPrimes[1] = 1
  for i in range(2, MAXVALUE):
    if (markPrimes[i]):
      continue
    for j in range(i+i, MAXVALUE, i):
      markPrimes[j] = 1
    primes.append(i)

def checkIfIsItAPrime(number):
  if (number < 2 or number > MAXVALUE):
    return "Out of the range!"
  return 1 - markPrimes[number]

def getPosOfANumber(number):
  if (number < 2 or number > MAXVALUE):
    return "Out of the range!"
  l = 1
  r = len(primes)
  while(l < r):
    mid = (l + r) >> 1
    if (number == primes[mid-1]):
      return mid
    elif (number > primes[mid-1]):
      l = mid+1
    else:
      r = mid
  return r

def getNextPrime(number):
  if (number < 2 or number >= primes[-1]):
    return "Out of the range!"
  pos = getPosOfANumber(number)-1
  if (primes[pos] == number):
    pos += 1
  if (pos > len(primes)):
    return "We don't have computed a bigger prime!"
  return primes[pos]

def getPreviousPrime(number):
  if (number < 2 or number > MAXVALUE):
    return "Out of the range!"
  if (number == 2):
    return "The number 2 is the first prime!"
  pos = getPosOfANumber(number)-1
  pos -= 1
  return primes[pos]

def getAPrime(position):
  if (position < 1 or position > len(primes)):
    return "Out of the range!"
  return primes[position-1]

print("Starting the server...")
computePrimes()
servicesCommands = ['CHECK', 'POS', 'NEXT', 'PREV', 'PRIME']

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT)) 
s.listen(1)          
print("Server started.")
print("Looked for primes until {}. Founded {} primes!".format(MAXVALUE, len(primes)))

(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  error = False
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  data = bytes.decode(data)
  print(data)
  
  data = data.split()
  if (len(data) != 2):
    error = True
  if (data[0] not in servicesCommands):
    error = True
  try:
    data[1] = int(data[1])
  except:2
    error = True
  
  if (error):
    dataToSend = "Something is wrong..."
  else:
    if (data[0] == 'CHECK'):
      dataToSend = str(checkIfIsItAPrime(data[1]))
    elif (data[0] == 'POS'):
      dataToSend = str(getPosOfANumber(data[1]))
    elif (data[0] == 'NEXT'):
      dataToSend = str(getNextPrime(data[1]))
    elif (data[0] == 'PREV'):
      dataToSend = str(getPreviousPrime(data[1]))
    elif (data[0] == 'PRIME'):
      dataToSend = str(getAPrime(data[1]))

  conn.send(str.encode(dataToSend)) # return sent data plus an "*"
conn.close()               # close the connection

"""
FORMATS

CHECK {number} -> Return 1 if number is a prime number and 0 otherwise.
POS {number} -> Return the position of number in the list of primes (starting on 1). If number is not a prime, the number used will be the smallest prime bigger than number (the next prime).
NEXT {number} -> Return the smallest prime bigger than number.
PREV {number} -> Return the biggest prime smaller than number.
PRIME {position} -> Return the prime in the position {position} on the list of primes.
"""