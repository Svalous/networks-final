import sys
import os
import random
import string
from socket import *

# Random alphanumeric string of length l
def rand_str(l):
  ret = ''
  for i in range(l):
    ret += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
  return ret

NUM_TRANSMISSIONS=10
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
  # Generate a random string
  data=rand_str(10)

  # Send it to the server
  client_socket.send(data.encode())

  # Print data for debugging
  print("sent: " + data)

  # Receive echoed data back from server
  echoed_data = client_socket.recv(4096)

  # Print out echoed data for debugging
  print("received echo: " + echoed_data.decode())
  print("")

# Close socket
client_socket.close()
