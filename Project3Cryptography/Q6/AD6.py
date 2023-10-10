from Crypto.Cipher import PKCS1_OAEP
import sys
from Crypto.PublicKey import RSA

def usage():
    print("usage: AD6 <encrypted-key-name>")
if (len(sys.argv) < 2):
    usage()
    quit()

input = sys.argv[1] # should be in "name.extension.encrypted" format

input_file = open(input, "rb")
encrypted_key = input_file.read()
input_file.close()

private_key = RSA.import_key(open("private.pem").read())

cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(encrypted_key)

output = open(input[:-10], "wb")
output.write(session_key)
output.close()
quit()