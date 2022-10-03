
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

passwordSet = False
memloc = 0
mode = sys.stdin.readline().rstrip()

while mode != "halt":
    if mode == "passkey":
        passwordSet = True
        memloc = sys.stdin.readline().rstrip()

        sys.stdout.write("result\n")
        sys.stdout.flush()
        password = memloc
    elif mode == "encrypt":
        encryptedtxt=""

        memloc = sys.stdin.readline().rstrip()
        word = memloc
        word = word.upper()
        password = password.upper()
        key = genKey(word, password)
        encryptedtxt = encrypt(word, key)

        sys.stdout.write(str(encryptedtxt) + '\n')
        sys.stdout.flush()
    elif mode == "decrypt":
        decryptedText =""

        memloc = sys.stdin.readline().rstrip()
        word = memloc
        word = word.upper()
        password = password.upper()
        key = genKey(word, password)

        decryptedText = decrypt(word, key)

        sys.stdout.write(str(decryptedText) + '\n')
        sys.stdout.flush()

    elif mode == "error":
        sys.stdout.write("error\n")
        sys.stdout.flush()
        
    elif mode == "read":
        print(memloc)
        sys.stdout.flush()
    elif mode == "write":
        memloc = int(sys.stdin.readline().rstrip())
    mode = sys.stdin.readline().rstrip()
