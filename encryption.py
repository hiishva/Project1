
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
    if mode == "passkey": #Setting the passkey
        passwordSet = True
        memloc = sys.stdin.readline().rstrip() 

        sys.stdout.write("result\n")
        sys.stdout.flush()
        password = memloc #stores the password to a local variable
    # Encrypts
    elif mode == "encrypt":
        encryptedtxt=""

        memloc = sys.stdin.readline().rstrip()
        word = memloc #stores the word to 
        word = word.upper()
        password = password.upper()
        key = genKey(word, password) #generated the key to encrypt
        encryptedtxt = encrypt(word, key) #encrypts the text to encrypt 

        sys.stdout.write(str(encryptedtxt) + '\n') #send the encrypted text to the driver
        sys.stdout.flush() 
    #Decrypts 
    elif mode == "decrypt":
        decryptedText =""

        memloc = sys.stdin.readline().rstrip()
        word = memloc #gets the word to decrypt
        word = word.upper() #convert the words to upper
        password = password.upper() #converts the password to upper
        key = genKey(word, password) #sets the key for the decryption

        decryptedText = decrypt(word, key) #decrypts the word

        sys.stdout.write(str(decryptedText) + '\n') # sends to driver
        sys.stdout.flush()
    #Error
    elif mode == "error": 
        sys.stdout.write("error\n") #checks the error
        sys.stdout.flush()
    mode = sys.stdin.readline().rstrip()
