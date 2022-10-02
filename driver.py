import sys
from subprocess import Popen, PIPE

#PIPES TO THE LOGGER AND ENCRYPTION FILE
log = Popen(['python3', 'logger.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')
#encrypt = Popen(['python3', 'encryption.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')

filename = sys.argv[1] #Command line arguements, for the file name
log.stdin.write("create\n") 
log.stdin.write(filename + "\n") #sends the file name to the logger file to be opened

#VARIABLES
cmnd = ""
pswrd= ""
isPswrdSet = False
history =[] #Stores the history of calls

while cmnd != "quit":
    #Displays the menu to the user
    print("Select one of the following options: ")
    command = input("1-password\n2-encrypt\n3-decrypt\n4-history\n5-quit\n")

    #users selects passkey
    if int(command) == 1:
        cmnd = "passkey"
        log.stdin.write("passkey\n")
        log.stdin.flush()
        selectPswd = input ("Select password from history (1) or create a new one(2): \n")
        if int(selectPswd) == 1: #Select a new password
            for i in range(len(history)): 
                print(str(i + 1) + "-" + history[i]+ "\n")
            pswdChoice = input ("Select the password you'd like to use: ")
            pswd = str(history[int(pswdChoice)-1])
            log.stdin.write(str(pswd) + "\n")
            log.stdin.flush()
        else: #Choose a password from the history
            pswd = input("Insert the password you'd like to use: ")
            history.append(str(pswd))
            isPswrdSet = True
            log.stdin.write(str(pswd) +"\n")
            log.stdin.flush()
    #user selects encrypt
    elif int(command) == 2:
        cmnd = "encrypt"
        if not isPswrdSet: #Check if the password is not set
            cmnd = "error"
            log.stdin.write("error\n")
            err = "error"
            print("ERROR PASSWORD NOT SET")
            log.stdin.write(str(err) + "\n") #Sends error to logger file
            cmnd = ""
            log.stdin.flush()
            pass
        else: #password is set 
            log.stdin.write("encrypt\n")
            encrypted = input("Choose from history(1) or type word(2)\n")
            if int(encrypted) == 2: #Selects a new word to encrypt
                encrpt = input("Insert the word you'd like to encrypt: ")
                history.append(encrpt) #adds the word to the history
                log.stdin.write(str(encrpt) +"\n") #sends to the logger file to log
                log.stdin.flush()
            else: #Selects the word from the history
                for i in range(len(history)): 
                    print(str(i + 1) + "-" + history[i]+ "\n")
                encryptChoice = input ("Select the word you'd like to encrypt: ")
                encrypt = str(history[int(encryptChoice)-1])
                log.stdin.write(str(encrypt) + "\n")
                log.stdin.flush()
    #Selects the decrypt command
    elif int(command) == 3:
        cmnd = "decrypt"
        err = "error"
        if not isPswrdSet: #checks if the error is set
            cmnd = "error"
            log.stdin.write(str(err) + "\n")
            print("ERROR PASSWORD IS NOT SET\n")
            log.stdin.write(str(err) + "\n") #sends error to logger
            cmnd = ""
            log.stdin.flush()
            pass
        else: #password is set
            log.stdin.write("decrypt\n")
            decrypted = input("Choose a word to be decrypted from history(1) or type a new word to be decrypted(2)\n")
            if int(decrypted) == 2: #selects to decrypt a new word
                decrypt = input("Insert the word you'd like to decrypt: ")
                history.append(decrypt) #adds word to history
                log.stdin.write(str(decrypt) + "\n") #sends to the logger file to log
                log.stdin.flush()
            else: #Selects from the history
                for i in range(len(history)): 
                    print(str(i + 1) + "-" + history[i]+ "\n")
                decryptChoice = input ("Select the word you'd like to decrypt: ")
                decrypt = str(history[int(decryptChoice)-1])
                log.stdin.write(str(decrypt) + "\n") #Sends the logger file decrypt command
                log.stdin.flush()
    #Shows the history 
    elif int(command) == 4:
        cmnd = "history"
        hist = "history"
        log.stdin.write(str(hist) + "\n") #sends to the logger file to log
        log.stdin.write("history\n")
        #PRINTING THE HISTORY
        print("\nHISTORY: ")
        for i in range(len(history)):
            print(str(i+1) + "-" + str(history[i]))
        print("\n")
    #Quits the program
    elif int(command) == 5:
        cmnd = "quit"
        log.stdin.write("halt\n")

log.stdin.flush()
log.wait()
