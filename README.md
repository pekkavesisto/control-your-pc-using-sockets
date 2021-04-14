# Control your PC with commands

This is a simple python application that i made, you can control your pc using simple commands, for example: ```open chrome```

## Requirements

You will need ```Python```

Keyboard module:
```pip install keyboard```

A Computer or laptop (You can run these scripts on android using termux BUT you cant control your android)

This has been tested only on ```Windows 10```, so i don't know if it will work on older versions

## Usage

1. Download the files in this repository

2. Run the ``` server.py ```

3. Then run the ```client.py```

4. Now the client will connect to the server.

5. To test it, simply try to do ```open notepad```, this should open notepad.

## Info

The client will only connect to the server if the server is running on the same computer, BUT there is a way how you can control your computer from almost any device.

## Control your computer/laptop from another computer/laptop.

Okay, for this all you will need is:

[ngrok](https://ngrok.com/)


1. Firstly, download the ```server.py``` on the computer you want to control (Lets call this Computer 1) and then the ```client.py``` on the other computer. (Lets call this Computer 2)

2. Then download [ngrok](https://ngrok.com/) on same computer
