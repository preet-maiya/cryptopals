from Crypto.Cipher import AES
from helpers import str2hex, xor, pad
import base64


def encrypt_cbc(msg, key, iv='\x00'*16, is_base64=False):
    cipher = AES.new(key, AES.MODE_ECB)

    if is_base64:
        msg = base64.b64decode(msg)

    msg = pad(msg, 16)
    blocks = [msg[i:i+16] for i in range(0, len(msg), 16)]
    encrypted = ''
    en = iv

    for block in blocks:
        ip = xor(en, block)
        en = cipher.encrypt(ip)
        encrypted += en

    return encrypted
        
def decrypt_cbc(msg, key, iv='\x00'*16, is_base64=False):
    cipher = AES.new(key, AES.MODE_ECB)

    if is_base64:
        print('Decoding base64...')
        msg = base64.b64decode(msg)

    blocks = [msg[i:i+16] for i in range(0, len(msg), 16)]
    decrypted = ''
    prev = iv

    for block in blocks:
        dec = cipher.decrypt(block)
        d = xor(prev, dec)
        prev = block
        decrypted += d

    return decrypted

if __name__ == '__main__':
    print('Decrypting challenge...')
    key = 'YELLOW SUBMARINE'
    file_path = '/home/preetham/cryptopals/2/data/challenge10'

    with open(file_path, 'r') as f:
        msg = '\n'.join(f.read().splitlines())

    decrypted_text = decrypt_cbc(msg, key, is_base64=True)
    # decrypted_text = decrypted_text.decode('hex')

    soln_path = '/home/preetham/cryptopals/2/data/challenge10_solved'

    with open(soln_path, 'w+') as f:
        f.write(decrypted_text) 
