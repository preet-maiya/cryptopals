from Crypto.Cipher import AES
from helpers import pad, xor, str2hex

def encrypt_cbc(msg, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)
    msg = pad(msg, 16)
    msg = str2hex(msg)
    blocks = [msg[i:i+32] for i in range(0, len(msg), 32)]
    encrypted = ''
    en = str2hex(iv)

    for block in blocks:
        ip = xor(en, block)
        en = cipher.encrypt(ip.decode('hex')).encode('hex')
        encrypted += en

    return encrypted
        
def decrypt_cbc(msg, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)
    blocks = [msg[i:i+32] for i in range(0, len(msg), 32)]
    decrypted = ''
    prev = str2hex(iv)

    for block in blocks:
        dec = cipher.decrypt(block.decode('hex')).encode('hex')
        d = xor(prev, dec)
        prev = block
        decrypted += d

    return decrypted

# msg = "Hello Bitches! Tis I, Preetham!"
# iv = '0'*16

# enc = encrypt_cbc(msg, key, iv)
# print(enc)

# dec = decrypt_cbc(enc, key, iv)
# print(dec.decode('hex'))

f = open('challenge10', 'r')
encrypted = ''.join(f.read().split())
encrypted = encrypted.decode('base64').encode('hex')

iv = chr(0) * 16
key = "YELLOW SUBMARINE"

decrypted = decrypt_cbc(encrypted, key, iv)
print(decrypted.decode('hex'))