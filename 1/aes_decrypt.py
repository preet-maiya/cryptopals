from Crypto.Cipher import AES

f = open('aes_decrypt', 'r')
encoded = f.read()
encoded = ''.join(encoded.split())
encoded = encoded.decode('base64')

key = 'YELLOW SUBMARINE'
decipher = AES.new(key, AES.MODE_ECB)

msg = decipher.decrypt(encoded)

print(msg)
