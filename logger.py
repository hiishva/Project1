import sys
from datetime import datetime

memloc = 0
mode = sys.stdin.readline().rstrip()

while mode != "halt":
    if mode == "create":
        memloc = sys.stdin.readline().rstrip()
        file1 = open(memloc, 'a')
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file1.write(date_str + " [START] Logging Started\n")
        sys.stdout.flush()
    elif mode == "read":
        file1.write(str(memloc) + "\n")
        print(memloc)
        sys.stdout.flush()
    elif mode == "write":
        memloc = int(sys.stdin.readline().rstrip())
    mode = sys.stdin.readline().rstrip()
