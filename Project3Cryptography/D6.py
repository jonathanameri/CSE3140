from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import sys
import os
from Crypto.PublicKey import RSA

def usage():
    print("Usage: \n"
        "D6 <encrypted-file>\n")
if (len(sys.argv) < 2):
    usage()
    quit()

input = sys.argv[1]
key_file = input[:-13] + "key"

file_in = open(input, "rb")
session_key = open(key_file, "rb").read()

nonce, tag, ciphertext = \
    [file_in.read(x) for x in (16, 16, -1)]

# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)

output = input[:-10]
file_out = open(output, "wb")
file_out.write(data)
#print(data.decode("utf-8"))