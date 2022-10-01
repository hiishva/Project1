
import sys

# memloc = 0
# mode = sys.stdin.readline().rstrip()

#Used to generate the key for encryption
def genKey (word, key):
    key = list(key)
    if len(word) == len(key): #checks if the key is the same length as the word to encrypt
        return(key) 
    else:
        for i in range(len(word) - len(key)): 
            key.append(key[i % len(key)]) #adds the extra characters needed to make the key the same length as the plaintext word
    return ("" . join(key))

#Encrypts the text using the plaintext word and the generated key
def encrypt (word, key):
    encrypted = [] 
    for i in range(len(word)): #encrypts for every letter in the plaintext using the formula (message+key) % 26
        x = (ord(string[i]) + ord(key[i])) % 26 #formula for encryption (message+key) % 26
        x += ord('A')
        encrypted.append(chr(x)) #appends the encrypt char to the ecrypted text
    return("" . join(encrypted))

#Decrypts the encrypted text using the generated key used to encrypt
def decrypt(encrypted, key):
    original = []
    for i in range(len(encrypted)): #decrypts for every letter in the encrypted text using the formula (encryptedtxt-key + 26) % 26
        x = (ord (encrypted[i]) - ord(key[i]) + 26) % 26 #formula for decryption (encryptedtxt - key + 26) % 26
        x += ord('A')
        original.append(chr(x)) #appends the decrypted char to the empty string
    return ("". join(original))


if __name__ == "__main__":
    string = input("ENTER A WORD: ") 
    string = string.upper()
    
    keyword = input("ENTER A KEY: ")
    keyword = keyword.upper()

    key = genKey(string, keyword)
    encrypted = encrypt(string, key)
    print ("ENCRYPTED: ", encrypted)
    print ("DECRYPTED: ", decrypt(encrypted, key))


