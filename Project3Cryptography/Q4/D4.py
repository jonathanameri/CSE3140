from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

encrypted_file = 'encrypted4.txt'
#we need to retrieve the key used to encode
#by looking at R4.py, this key was saved in'.key.txt'

#with open('.key.txt', mode='rb') as key_file:
#	key = key_file.read()

#since '.key.txt' does not exist, we can still use the key that's revealed
#in the R4.py program:
key = b'$\x1eA[\xb7\x0c\xfe\xd8Y^\x8c\xb7\x86\xb2\x80\xb6'

file = open(encrypted_file, 'rb')
iv = file.read(16)
ciphered_text = file.read()
file.close()
cipher = AES.new(key, AES.MODE_CBC, iv)

plaintext = unpad(cipher.decrypt(ciphered_text), AES.block_size)

print(plaintext)
