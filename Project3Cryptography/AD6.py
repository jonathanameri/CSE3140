from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
import sys
from Crypto.PublicKey import RSA

def usage():
    print("Usage: \n"
        "AD6 <encrypted-file-name>\n")
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
#print(session_key)
quit()

# extra code
fileParts = input.split(".")
fileName = fileParts[0]
# for loop in case file has extensions
for i in range(1, len(fileParts) - 2, 1):
    fileName = fileName + "." + fileParts[i]
fileName += ".key.encrypted"

