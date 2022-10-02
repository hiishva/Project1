import sys
from datetime import datetime

memloc = 0
mode = sys.stdin.readline().rstrip()

date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
while mode != "halt":
    if mode == "create":
        memloc = sys.stdin.readline().rstrip()
        file1 = open(memloc, 'a')
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file1.write(date_str + " [START] Logging Started\n")
        sys.stdout.flush()
    elif mode == "passkey":
        memloc = sys.stdin.readline().rstrip()
        file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [PASSKEY] Passkey set as " + memloc + "\n")
        sys.stdout.flush()
    elif mode == "error":
        memloc = sys.stdin.readline().rstrip()
        file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [ERROR] Passkey not set \n")
        sys.stdout.flush()
    elif mode == "encrypt":
        memloc = sys.stdin.readline().rstrip()
        file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [ENCRYPT] Encrypted " + memloc + "\n")
        sys.stdout.flush()
    elif mode == "decrypt":
        memloc = sys.stdin.readline().rstrip()
        file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [DECRYPT] Decrypted " + memloc + "\n")
        sys.stdout.flush()
    elif mode == "history":
        memloc = sys.stdin.readline().rstrip()
        file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " [HISTORY] History shown \n")
        sys.stdout.flush()
    elif mode == "read":
        file1.write(str(memloc) + "\n")
        print(memloc)
        sys.stdout.flush()
    elif mode == "write":
        memloc = int(sys.stdin.readline().rstrip())
    mode = sys.stdin.readline().rstrip()
file1.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+ " [STOP] Logging Stopped\n")