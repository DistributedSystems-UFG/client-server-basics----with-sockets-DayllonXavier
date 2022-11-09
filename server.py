from socket  import *
from constCS import *

MAXVALUE = int(1e6)

primes = []
markPrimes = [0] * (MAXVALUE+1)

def computePrimes():
  markPrimes[0] = markPrimes[1] = 1
  for i in range(2, MAXVALUE+1):
    if (markPrimes[i]):
      continue
    for j in range(i+i, MAXVALUE+1, i):
      markPrimes[j] = 1
    primes.append(i)

def checkIfIsItAPrime(number):
  if (number < 2 or number > MAXVALUE):
    return "Out of range!"
  return 1 - markPrimes[number]

def getPosOfANumber(number):
  if (number < 2 or number > MAXVALUE):
    return "Out of range!"
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
  if (number >= primes[-1]):
    return "Out of range!"
  if (number < 2):
    return 2
  pos = getPosOfANumber(number)-1
  if (primes[pos] == number):
    pos += 1
  if (pos > len(primes)):
    return "We don't calculate a greater prime!"
  return primes[pos]

def getPreviousPrime(number):
  if (number < 2 or number > MAXVALUE):
    return "Out of range!"
  if (number == 2):
    return "The number 2 is the first prime!"
  pos = getPosOfANumber(number)-2
  return primes[pos]

def getAPrime(position):
  if (position < 1 or position > len(primes)):
    return "Out of range!"
  return primes[position-1]

print("Starting the server...")

computePrimes()
print("The prime numbers were searched up to the value {}.\n{} primes were found!".format(MAXVALUE, len(primes)))

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)     
print("Server started.")

(conn, addr) = s.accept()
while True:
  error = False
  data = conn.recv(1024)
  if not data: break
  data = bytes.decode(data)
  print("{} sent query: \'{}\'".format(addr, data))
  
  data = data.split()
  data[0] = data[0].upper()

  if (len(data) != 2):
    error = True
  try:
    data[1] = int(data[1])
  except:
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
    else:
      dataToSend = "The operation is not available."

  conn.send(str.encode(dataToSend))
conn.close()