
import sys

#FUNCTIONS FOR ENCRYPTING AND DECRYPTING THE WORDS
#Sets the key based on the length of the word
def genKey(encrypt, password):
    password = list(password)
    if len(encrypt) == len(password):
        return password
    else:
        for i in range(len(encrypt) - len(password)):
            password.append(password[i% len(password)])
    return ("".join(password))

#Encrypts the word using the key generated 
def encrypt(encrypt, password):
    encrypted = []
    for i in range(len(encrypt)):
        x = (ord(encrypt[i]) + ord(password[i])) % 26 # encrypts using the formula (message + key ) % 26
        x += ord('A')
        encrypted.append(chr(x))
    return("".join(encrypted)) #Returns the encrypted 

#Decrypts the word using the key generated
def decrypt(decrypt, password):
    original = []
    for i in range(len(decrypt)):
        x = (ord (decrypt[i]) - ord(password[i]) + 26) % 26 #decrypts using the formula (encyption - key + 26) % 26
        x += ord('A')
        original.append(chr(x))
    return ("".join(original)) #Return the decrypted 

file2 = open("test2.txt", 'w') #opens the file in append mode
file2.write("File2 opened\n")
sys.stdout.flush()

passwordSet = False
memloc = 0
mode = sys.stdin.readline().rstrip()

file2.write("after mode\n")
sys.stdout.flush()

while mode != "halt":
    file2.write("after halt\n")
    sys.stdout.flush()
    if mode == "passkey":
        file2.write("after passkey\n")
        sys.stdout.flush()
        passwordSet = True
        memloc = sys.stdin.readline().rstrip()

        sys.stdout.write("result\n")
        sys.stdout.flush()
        password = memloc
        file2.write(memloc)
        sys.stdout.flush()
    elif mode == "encrypt":
        encryptedtxt=""
        file2.write("after encrypt\n")
        sys.stdout.flush()

        memloc = sys.stdin.readline().rstrip()
        file2.write(memloc +"\n")
        sys.stdout.flush()
        word = memloc
        word = word.upper()
        password = password.upper()
        file2.write(memloc +"\n")
        sys.stdout.flush()
        key = genKey(word, password)
        file2.write(str(key) + '\n')
        sys.stdout.flush()
        encryptedtxt = encrypt(word, key)
        file2.write(encryptedtxt + '\n')
        sys.stdout.flush()

        sys.stdout.write(str(encryptedtxt) + '\n')
        sys.stdout.flush()
    elif mode == "decrypt":
        decryptedText =""
        file2.write("after decrypt")
        sys.stdout.flush()

        memloc = sys.stdin.readline().rstrip()
        file2.write(memloc +"\n")
        sys.stdout.flush()
        word = memloc
        word = word.upper()
        password = password.upper()
        file2.write(memloc +"\n")
        sys.stdout.flush()
        key = genKey(word, password)
        file2.write(str(key) + '\n')
        sys.stdout.flush()
        file2.write(str(key) + '\n')
        sys.stdout.flush()

        decryptedText = decrypt(word, key)
        file2.write(encryptedtxt + '\n')
        sys.stdout.flush()

        sys.stdout.write(str(decryptedText) + '\n')
        sys.stdout.flush()

    elif mode == "error":
        file2.write("after error\n")
        sys.stdout.flush()
        #memloc = sys.stdin.readline().rstrip()
        #file2.write(memloc)
        #sys.stdout.flush()
        sys.stdout.write("error\n")
        sys.stdout.flush()
        
    elif mode == "read":
        print(memloc)
        sys.stdout.flush()
    elif mode == "write":
        memloc = int(sys.stdin.readline().rstrip())
    mode = sys.stdin.readline().rstrip()
file2.write("End\n")
