from challenge11 import random_bytes, encrypt_ecb, str2hex
from helpers import pad


unknown = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg\
YnkK'
print(len(unknown))
unknown = unknown.decode('base64') 
print(len(unknown))
key = random_bytes(16, 16)
def just_encrypt(msg, key, decrease_unknown=0):
    msg = msg + unknown[decrease_unknown:]    
    # padchars = (random_bytes(5, 10), random_bytes(5, 10))
    # msg = padchars[0] + msg + padchars[1]
    msg = pad(msg, 16)
    encrypted = encrypt_ecb(msg, key)
    return encrypted

def get_unknown_string_size(oracle):
    ciphertext_length = len(oracle('', key))
    i = 1
    while True:
        data = "A" * i
        new_ciphertext_length = len(oracle(data, key))
        if ciphertext_length != new_ciphertext_length:
            return new_ciphertext_length - i
        i += 1

print(get_unknown_string_size(just_encrypt))
def detect_block_size(just_encrypt):
    print('Detecting block size...')
    repeat = 2
    repeat_char = 'a'
    rep = 0
    while(True):
        msg = repeat_char*repeat
        _, encrypted = just_encrypt(msg)
        rep = repeat/2
        first = encrypted[:repeat]
        second = encrypted[repeat:2*repeat]
        if first==second:
            print("Block size: {}".format(rep))
            break

        repeat += 2


# start_ascii = ord('A')
# possible = {}
# main_str = 'A'*15 
# decrease_unknown = 2
# for i in range(32, 126):
#     append_char = chr(i)
#     test_str = main_str + append_char
#     encrypted = just_encrypt(test_str, key, decrease_unknown=decrease_unknown)
#     possible[encrypted] = append_char

# encrypted = just_encrypt(main_str, key)

# print(possible[encrypted])