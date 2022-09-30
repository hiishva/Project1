
import sys
from subprocess import Popen, PIPE

mem = Popen(['python3','logger.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')

for i in range(10,0,-1):
    mem.stdin.write("write\n")
    mem.stdin.write(str(i))
    mem.stdin.write("\n")
    sys.stdout.write("set to ")
    mem.stdin.write("read\n")
    mem.stdin.flush()
    print(mem.stdout.readline().rstrip())
mem.stdin.write("halt\n")
mem.stdin.flush()

mem.wait

