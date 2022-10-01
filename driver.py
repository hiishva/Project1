import sys
from subprocess import Popen, PIPE


log = Popen(['python3', 'logger.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')
#encrypt = Popen(['python3', 'encryption.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')
filename = sys.argv[1]
log.stdin.write("create\n")
log.stdin.write(filename + "\n")
cmnd = ""
pswrd= ""
isPswrdSet = False
history =[]
while cmnd != "quit":
    print("Select one of the following options: ")
    command = input("1-password\n2-encrypt\n3-decrypt\n4-history\n5-quit\n")

    if int(command) == 1:
        cmnd = "passkey"
        log.stdin.write("passkey\n")
        log.stdin.flush()
        selectPswd = input ("Select password from history (1) or create a new one(2): \n")
        if int(selectPswd) == 1:
            for i in range(len(history)): 
                print(str(i + 1) + "-" + history[i]+ "\n")
            pswdChoice = input ("Select the password you'd like to use: ")
            pswd = str(history[int(pswdChoice)-1])
            log.stdin.write(str(pswd) + "\n")
            log.stdin.flush()
        else:
            pswd = input("Insert the password you'd like to use: ")
            history.append(str(pswd))
            isPswrdSet = True
            log.stdin.write(str(pswd) +"\n")
            log.stdin.flush()
    elif int(command) == 2:
        cmnd = "encrypt"
        if not isPswrdSet:
            cmnd = "error"
            log.stdin.write("error\n")
            err = "error"
            print("ERROR PASSWORD NOT SET")
            log.stdin.write(str(err) + "\n")
            cmnd = ""
            log.stdin.flush()
            print("cmnd: " + cmnd)
            pass
        else:
            log.stdin.write("encrypt\n")
            encrypted = input("Choose from history(1) or type word(2)\n")
            if int(encrypted) == 2:
                encrpt = input("Insert the word you'd like to encrypt: ")
                history.append(encrpt)
                log.stdin.write(str(encrpt) +"\n")
                log.stdin.flush()
            else:
                for i in range(len(history)): 
                    print(str(i + 1) + "-" + history[i]+ "\n")
                encryptChoice = input ("Select the word you'd like to encrypt: ")
                encrypt = str(history[int(encryptChoice)-1])
                log.stdin.write(str(encrypt) + "\n")
                log.stdin.flush()
    elif int(command) == 3:
        cmnd = "decrypt"
        err = "error"
        if not isPswrdSet:
            cmnd = "error"
            log.stdin.write(str(err) + "\n")
            print("ERROR PASSWORD IS NOT SET\n")
            log.stdin.write(str(err) + "\n")
            cmnd = ""
            log.stdin.flush()
            pass
        else:
            log.stdin.write("decrypt\n")
            decrypted = input("Choose a word to be decrypted from history(1) or type a new word to be decrypted(2)\n")
            if int(decrypted) == 2:
                decrypt = input("Insert the word you'd like to decrypt: ")
                history.append(decrypt)
                log.stdin.write(str(decrypt) + "\n")
                log.stdin.flush()
            else:
                for i in range(len(history)): 
                    print(str(i + 1) + "-" + history[i]+ "\n")
                decryptChoice = input ("Select the word you'd like to decrypt: ")
                decrypt = str(history[int(decryptChoice)-1])
                log.stdin.write(str(decrypt) + "\n")
                log.stdin.flush()
    elif int(command) == 4:
        cmnd = "history"
        hist = "history"
        log.stdin.write(str(hist) + "\n")
        log.stdin.write("history\n")
        print("\nHISTORY: ")
        for i in range(len(history)):
            print(str(i+1) + "-" + str(history[i]))
        print("\n")
    elif int(command) == 5:
        cmnd = "quit"
        log.stdin.write("halt\n")

log.stdin.flush()
log.wait()
