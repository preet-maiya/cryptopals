from Crypto.Cipher import AES
from helpers import str2hex, xor, pad
import random
from challenge10 import encrypt_cbc, decrypt_cbc


def encrypt_ecb(msg, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(msg)

def decrypt_ecb(msg, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(msg)

def random_bytes(min, max):
    rand = random.randint(min, max)
    rand_bytes = [chr(random.randint(32, 126)) for _ in range(rand)]
    return ''.join(rand_bytes)

def just_encrypt(msg):
    key = random_bytes(16, 16)
    padchars = (random_bytes(5, 10), random_bytes(5, 10))
    msg = padchars[0] + msg + padchars[1]
    msg = pad(msg, 16)
    choice = random.randint(0, 1)
    
    if choice:
        encrypted = encrypt_ecb(msg, key)
        mode = 'ECB'

    else:
        iv = random_bytes(16, 16)
        encrypted = encrypt_cbc(msg, key, iv)
        mode = 'CBC'

    return (mode, key, encrypted)

