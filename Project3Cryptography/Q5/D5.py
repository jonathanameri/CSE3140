from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import MD5

# we need to retrieve the key used to encode
# we will copy how the key was generated in R5.py:
BLOCKSIZE = 2048
h = MD5.new()
with open('R5.py', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        h.update(buf)
        buf = afile.read(BLOCKSIZE)
key = h.digest()

encrypted_file = 'e2e2.txt'
file = open(encrypted_file, 'rb')
iv = file.read(16)
ciphered_text = file.read()
file.close()
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(cipher.decrypt(ciphered_text), AES.block_size)

print(plaintext)
