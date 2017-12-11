from socket import *
import random
import sys
from os.path import isfile, join, dirname, abspath 
from os import listdir
sys.path.append(dirname(abspath(__file__)) + '/lib')
from generator import *
NUM_TRANSMISSIONS=1000
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

# Globals to keep track of state
state = 0
answer = None

# Globals for answers
yes = ["yes", "y"]
no = ["no", "n"]

# Files and generators for randomly generated text
text_path = dirname(abspath(__file__)) + "/txt/"
files = [f for f in listdir(text_path) if isfile(join(text_path, f))] 
gens = [Generator(text_path + f) for f in files]
for g in gens:
  g.makeChain()

# getQuestion function
def getQuestion(val1, val2):
  global answer
  question = ""
  if random.randint(0,1) == 0:
    question = gens[val1].makeSentence(25)
    answer = val1
  else:
    question = gens[val2].makeSentence(25)
    answer = val2
  return question


# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # receive data over the socket returned by the accept() method
  recv = comm_socket.recv(4096)
  # Initial state, setup
  if state == 0:
    ret = "Would you like to play a game?"
    comm_socket.send(ret.encode())
    state = 1
    pass
  # Question state
  elif state == 1:
    if recv.decode().lower() in yes:
      pass
    elif recv.decode().lower() in no:
      ret = "Boo."
      comm_socket.send(ret.encode())
      state = 3
      pass
    else:
      ret = "Come again?"
      comm_socket.send(ret.encode())
      state = 0
      pass
    if state == 1:
      ret = "Alright!  Is this from {0} or {1}?\nSend 0 for {0} and 1 for {1}\n".format(files[0], files[1])
      question = getQuestion(0, 1)
      ret += str(question)
      comm_socket.send(ret.encode())
      state = 2
      pass
    pass
  # Answer state
  elif state == 2:
    ret = "Let's see here...\n"
    if int(recv.decode()) == answer:
        ret += "That was right!"
        pass
    else:
        ret += "Nope, wrong!  The answer was {}".format(str(answer))
        pass
    comm_socket.send(ret.encode())  
    state = 0
    pass
  # Quit state
  elif state == 3:
    break
  else:
    print("State error, aborting")
    break

# Close all sockets that were created
comm_socket.close()
server_socket.close()
