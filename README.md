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

2. Then download [ngrok](https://ngrok.com/) on Computer 2, it doesn't need to be in the same folder but it will be easier if its in the same folder.

3. Start the ```server.py``` on Computer 1. (You need to run it through cmd)

4. Open cmd in the folder where your ngrok is and type ```ngrok tcp 1234```.

5. Now open the ```client.py``` file so you can edit it.
   
   In the [row 9](https://github.com/jarkko1/control-your-pc-using-sockets/blob/ef7e21fdb861e2a3dc64bd1090cd6737a702030c/client.py#L9) change ```host = "127.0.0.1"``` to ```host = "0.tcp.ngrok.io"``` (```0.tcp.ngrok.io``` is just an example domain, you need to find yours in the cmd, it will look something like that)
   
   Now in the [row 11](https://github.com/jarkko1/control-your-pc-using-sockets/blob/ef7e21fdb861e2a3dc64bd1090cd6737a702030c/client.py#L11) change ```port = 1234``` to ```port = 14753``` (```14753``` is an example port, you need to find yours in the cmd, it will look something like that)
   
6. Now run ```client.py``` on Computer 2 (You need to run it through cmd)
