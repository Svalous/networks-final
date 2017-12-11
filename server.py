from socket import *
import sys
NUM_TRANSMISSIONS=10
if (len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " server_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
server_port=int(sys.argv[1])

# Create a socket for the server
server_socket=socket(AF_INET, SOCK_STREAM)

# Bind it to a specific server port supplied on the command line
server_socket.bind(("127.0.0.1", server_port))

# Put server's socket in LISTEN mode
server_socket.listen()

# Call accept method to wait for a connection
(comm_socket, client_addr) = server_socket.accept()

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # receive data over the socket returned by the accept() method
  recv = comm_socket.recv(4096)
  print("received data " + recv.decode() + "; echoed it ")

  # Echo it back to the client
  comm_socket.send(recv)

# Close all sockets that were created
comm_socket.close()
server_socket.close()
