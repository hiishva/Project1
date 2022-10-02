import sys
from datetime import datetime

memloc = 0
mode = sys.stdin.readline().rstrip()

date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
while mode != "halt":
    #opens the logger file
    if mode == "create":
        memloc = sys.stdin.readline().rstrip()
        file1 = open(memloc, 'a') #opens the file in append mode
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file1.write(date_str + " [START] Logging Started\n") #adds the start logging message to file
        sys.stdout.flush()
    #Adds the password command to the log file
    elif mode == "passkey":
        memloc = sys.stdin.readline().rstrip()
        file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [PASSKEY] Passkey set as " + memloc + "\n")
        sys.stdout.flush()
    elif mode == "resultpasskey":
        memloc = sys.stdin.readline().rstrip()
        file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [RESULT] Success\n")
        sys.stdout.flush()
    elif mode == "resultsEncrypts":
        memloc = sys.stdin.readline().rstrip()
        file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [RESULT] " + memloc + "\n")
        sys.stdout.flush()
    #Adds the error command to the log file
    elif mode == "error":
        memloc = sys.stdin.readline().rstrip()
        file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [ERROR] Passkey not set \n")
        sys.stdout.flush()
    #Adds the encrypt command to the log file
    elif mode == "encrypt":
        memloc = sys.stdin.readline().rstrip()
        file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [ENCRYPT] Encrypted " + memloc + "\n")
        sys.stdout.flush()
    #Add the decrypt command to the log file
    elif mode == "decrypt":
        memloc = sys.stdin.readline().rstrip()
        file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [DECRYPT] Decrypted " + memloc + "\n")
        sys.stdout.flush()
    #Adds the history command to the log file
    elif mode == "history":
        memloc = sys.stdin.readline().rstrip()
        file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [HISTORY] History shown \n")
        sys.stdout.flush()
    mode = sys.stdin.readline().rstrip()
file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+ " [STOP] Logging Stopped\n") #writes stop logging message to the file