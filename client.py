from socket  import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    query = input()
    if (query == "EXIT"):
        break

    s.send(str.encode(query))

    data = s.recv(1024)
    print(bytes.decode(data))
    
s.close()
