import sys
from subprocess import Popen, PIPE

#PIPES TO THE LOGGER AND ENCRYPTION FILE
log = Popen(['python3', 'logger.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')
encrypts = Popen(['python3', 'encryption.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')

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
        encrypts.stdin.write("passkey\n")
        encrypts.stdin.flush()
        selectPswd = input ("Select password from history (1) or create a new one(2): \n")
        if int(selectPswd) == 1: #Select a password from history
            isPswrdSet = True
            for i in range(len(history)): 
                print(str(i + 1) + "-" + history[i]+ "\n")
            pswdChoice = input ("Select the password you'd like to use: ")
            pswd = str(history[int(pswdChoice)-1])
            encrypts.stdin.write(str(pswd) + "\n") #sends the password to the encryption
            encrypts.stdin.flush()
            log.stdin.write(str(pswd) + "\n") #sends the password to the logger
            log.stdin.flush()
            cmnd = encrypts.stdout.readline().rstrip() #gets the result that the password was set
            if cmnd == "result":
                log.stdin.write("resultpasskey\n")
                suc = "success"
                log.stdin.write(str(suc) + "\n") #writes to the logger
                cmnd = ""
                log.stdin.flush()
                pass
        else: #Choose a new password
            isPswrdSet = True
            pswd = input("Insert the password you'd like to use: ")
            history.append(str(pswd)) #adds password to the history
            encrypts.stdin.write(str(pswd) + "\n") #sends to the encryption
            encrypts.stdin.flush()
            log.stdin.write(str(pswd) +"\n") #sends to the logger
            log.stdin.flush()
            cmnd = encrypts.stdout.readline().rstrip() #gets the result from the encryption
            if cmnd == "result":
                log.stdin.write("resultpasskey\n")
                suc = "success"
                log.stdin.write(str(suc) + "\n") #sends it to logger
                cmnd = ""
                log.stdin.flush()
                pass
    #user selects encrypt
    elif int(command) == 2:
        cmnd = "encrypt"
        
        #password isn't set 
        if not isPswrdSet: #Check if the password is not set
            cmnd = "error"
            error = "error"
            encrypts.stdin.write("error\n") #sends the error message to the encryption
            encrypts.stdin.flush()
            
            log.stdin.write("error\n") #sends the error message to the logger
            log.stdin.flush()
            print("ERROR PASSWORD IS NOT SET\n")
            err = encrypts.stdout.readline().rstrip() #Recieves the error and sends to logger
            encrypts.stdin.flush()
            log.stdin.write(str(err) + "\n") #sends error to logger 
            log.stdin.flush()
            cmnd = ""
            pass

        #password is set
        else:
            encrypts.stdin.write("encrypt\n")
            encrypts.stdin.flush()
            log.stdin.write("encrypt\n")
            log.stdin.flush()
            encrypted = input("Choose from history(1) or type word(2)\n") #choose from history or from word
            if int(encrypted) == 2: #Selects a new word to encrypt
                encrpt = input("Insert the word you'd like to encrypt: ")
                history.append(encrpt) #adds the word to the history
                log.stdin.write(str(encrpt) +"\n") #sends to the logger file to log
                log.stdin.flush()
                encrypts.stdin.write(str(encrpt) +"\n") #sends to the encryption
                encrypts.stdin.flush()
                encryptedTxt = encrypts.stdout.readline().rstrip() #gets the encrypted text
                log.stdin.write("resultsEncrypts\n")
                log.stdin.write(str(encryptedTxt) + "\n")
                print("RESULTS: " + encryptedTxt + '\n') #Prints the results to the terminal 
            else: #Selects the word from the history
                for i in range(len(history)): 
                    print(str(i + 1) + "-" + history[i]+ "\n")
                encryptChoice = input ("Select the word you'd like to encrypt: ")
                encrypt = str(history[int(encryptChoice)-1])
                encrypts.stdin.write(str(encrypt) + "\n")
                encrypts.stdin.flush()
                log.stdin.write(str(encrypt) + "\n")
                log.stdin.flush()

                encryptedTxt = encrypts.stdout.readline().rstrip()
                log.stdin.write("resultsEncrypts\n")
                log.stdin.write(str(encryptedTxt) + "\n")
                print("RESULTS: " + encryptedTxt + '\n')    
    #Selects the decrypt command
    elif int(command) == 3:
        cmnd = "decrypt"
        err = "error"
        if not isPswrdSet: #Check if the password is not set
            cmnd = "error"
            error = "error"
            encrypts.stdin.write("error\n")
            encrypts.stdin.flush()
            
            log.stdin.write("error\n")
            log.stdin.flush()
            print("ERROR PASSWORD IS NOT SET\n")
            err = encrypts.stdout.readline().rstrip()
            
            log.stdin.write(str(err) + "\n") #sends error to logger
            log.stdin.flush()
            cmnd = ""
            pass
        else: #password is set
            log.stdin.write("decrypt\n")
            encrypts.stdin.write("decrypt\n")
            decrypted = input("Choose a word to be decrypted from history(1) or type a new word to be decrypted(2)\n")
            if int(decrypted) == 2: #selects to decrypt a new word
                decrypt = input("Insert the word you'd like to decrypt: ")
                history.append(decrypt) #adds word to history
                log.stdin.write(str(decrypt) + "\n") #sends to the logger file to log
                log.stdin.flush()

                encrypts.stdin.write(str(decrypt) + "\n")
                encrypts.stdin.flush()
                decryptedText = encrypts.stdout.readline().rstrip()
                log.stdin.write("resultsDecrypts\n")
                log.stdin.write(str(decryptedText) + "\n")
                print("RESULTS: " + decryptedText + '\n')
            else: #Selects from the history
                for i in range(len(history)): 
                    print(str(i + 1) + "-" + history[i]+ "\n")
                decryptChoice = input ("Select the word you'd like to decrypt: ")
                decrypt = str(history[int(decryptChoice)-1])
                log.stdin.write(str(decrypt) + "\n") #Sends the logger file decrypt command
                log.stdin.flush()
                encrypts.stdin.write(str(decrypt) + "\n") #send to the encryption file
                encrypts.stdin.flush()
                decryptedText = encrypts.stdout.readline().rstrip() #gets the decrypted text
                log.stdin.write("resultsDecrypts\n")
                log.stdin.write(str(decryptedText) + "\n") #Sends to the logger
                print("RESULTS: " + decryptedText + '\n')
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
        encrypts.stdin.write("halt\n")

log.stdin.flush()
log.wait()
encrypts.stdin.flush()
encrypts.wait()
