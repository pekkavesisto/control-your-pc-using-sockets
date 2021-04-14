import time
import socket
import sys
import os
import keyboard

s = socket.socket()
  
host = "127.0.0.1"
  
port = 1234

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
    
    # This will open cmd (Command Prompt)
    if command == "open cmd":
        # you can give batch file as input here
        os.system('start cmd.exe')
        print("Opening...")
        
    # This will open chrome
    if command == "open chrome":
        # you can give batch file as input here
        os.system('start chrome.exe')
        print("Opening...")

    # This will open notepad
    if command == "open notepad":
        # you can give batch file as input here
        os.system('start notepad.exe')
        print("Opening...")

    # Simply, this will open www.youtube.com 
    if command == "open youtube":
        # you can give batch file as input here
        os.system('start www.youtube.com')
        print("Opening...")
        
    # You can google stuff using this command, i created this the easiest way so googling with spaces wont work, you can change it if you want, i might change it too.
    if command == "google":
        # you can give batch file as input here
        os.system('start www.google.com/search?q=' + google)
        print("Googling...")
        
    # By using this command you can write stuff. A bit buggy but works
    if command == "write":
        # you can give batch file as input here
        keyboard.write(write)
        print("Writing...")
        
    # You can save a file using this command, idk what this is for but i added it :)
    if command == "save":
        # you can give batch file as input here
        keyboard.send("ctrl+s")
        print("Saving...")
        
    # This will turn your pc off
    if command == "shutdown":
        # you can give batch file as input here
        os.system('shutdown /s')
        print("Shutting down...")
