from Crypto.Cipher import AES
import sys

def usage():
    print("usage: D6 <encrypted-file>")
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