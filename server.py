import time
import socket
import sys
import os
  
# Initialize s to socket
s = socket.socket()
  
# Initialize the host
host = "127.0.0.1"
  
# Initialize the port
port = 1234
  
# Bind the socket with port and host
s.bind(('', port))
  
print("Waiting...")
  
# listening for conections
s.listen()
  
# accepting the incoming connections
conn, addr = s.accept()
  
# take command as input
while True:
    print(addr, "connected!")
    command = input(str("Enter Command : "))
    conn.send(command.encode())
  
    # recieve the confrmation
    data = conn.recv(1024)
  
    if data:
      print("command recieved and executed sucessfully.")
