Ishva Patel
Prof. Salazar
CS 4348.502
10/3/2022
README

Files that are included and their purpose:
Encryption.py
The encryption program encrypts and decrypts the text the user inputs. In addition to that, it stores the password the user selects. Sends the encoded and decoded text to the driver program.


Logger.py
The logger program opens a file that the user inputs into the command line, and then logs all the commands that take place during the program’s run. The logger file takes the command sent from the driver program and logs those commands into the file


Driver.py
The driver program opens the encryption and decryption program. When running you pass the logger file that the user wants to log the information from. The driver program also handles the input program that is put in during the run. It sends the commands that the users inputs to the logger and the encryption file and to the logger file. It takes the values sent from the encryption program and sends that to the logger program to show that the command ran successfully.


How to run the program:
To run the program, in the command line run the command python3 driver.py [input text]. Then a menu should show up in the terminal. Select the corresponding number to the command. The passkey command, the encryption command, and the decryption command will then ask the user if they want to select a word from the history or select a new word. Press the corresponding numbers, then either type of the word you would like to select and or select the value in the history to select the word. To quit the program, you should press 5, which is the quit command for the driver program. This quit command will stop the other two programs as well.