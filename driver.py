
import sys
from subprocess import Popen, PIPE


log = Popen(['python3', 'logger.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')
#encrypt = Popen(['python3', 'encryption.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')
filename = sys.argv[1]
log.stdin.write("create\n")
log.stdin.write(filename + "\n")


for i in range(10,0,-1):
    log.stdin.write("write\n")
    log.stdin.write(str(i))
    log.stdin.write("\n")
    sys.stdout.write("Set to ")
    log.stdin.write("read\n")
    log.stdin.flush()
    print(log.stdout.readline().rstrip())

log.stdin.write("halt\n")
log.stdin.flush()

log.wait()












