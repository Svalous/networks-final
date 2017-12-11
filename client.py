import sys
import os
import random
import string
from socket import *

NUM_TRANSMISSIONS=1000
if (len(sys.argv) < 2):
  print("Usage: python3 "  + sys.argv[0] + " server_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
server_port=int(sys.argv[1])

# Create a socket for the client
client_socket=socket(AF_INET, SOCK_STREAM)

# Connect it to the server using the connect() function
client_socket.connect(("127.0.0.1", server_port))

# Do this NUM_TRANSMISSIONS number of times
for i in range(NUM_TRANSMISSIONS):
  ret = input("> ")
  client_socket.send(ret.encode())
  res = client_socket.recv(4096)
  print(res.decode())
  print("")

# Close socket
client_socket.close()
