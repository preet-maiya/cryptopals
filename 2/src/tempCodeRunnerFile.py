def encrypt_cbc(msg, key, iv='0'*16):
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
        
def decrypt_cbc(msg, key, iv='0'*16):
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