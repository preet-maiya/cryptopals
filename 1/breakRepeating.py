from hamming import hamming
import numpy as np
from collections import Counter
import operator

def decode(enc):
    hex_letters = [enc[i:i+2] for i in range(0, len(enc), 2)]
    count = dict(Counter(hex_letters))
    score = []

    for i in range(0, 256):
        s = 0
        for hexs, c in count.items():
            decoded = int(hexs, 16)^i
            if (decoded>=65 and decoded<=90) or (decoded>=97 and decoded<=122) or (decoded>=48 and decoded<=57) or decoded==10 or decoded==32:
                s += c
 
        score.append(s)

    index, value = max(enumerate(score), key=operator.itemgetter(1))
    # print(score)
    # print(index, value)
    final = ''
    for letter in hex_letters:
        conv = int(letter, 16)^index
        conv = '%02x'%conv
        final += conv

    return index, value, final

f = open('decryptThis', 'r')
encoded = f.read()
encoded = ''.join(encoded.split())
encoded = encoded.decode('base64').encode('hex')

possible = []
# print(len(encoded))
for size in range(2, 41):
    keysize = 2*size
    chunk1 = encoded[0:keysize]
    chunk2 = encoded[keysize:2*keysize]
    chunk3 = encoded[2*keysize:3*keysize]
    chunk4 = encoded[3*keysize:4*keysize]
    distance1 = hamming(chunk1, chunk2)
    distance2 = hamming(chunk3, chunk4)
    normalised = float(distance1+distance2)/float(keysize)
    possible.append((size, normalised))

possible = sorted(possible, key=lambda x: x[1])
print(possible)

###############################################################

# KEYSIZE is 29
# KEY is `Terminator X: Bring the noise`

###############################################################
for size, _ in possible[:10]:
    KEYSIZE = size
    arranged = {}
    arranged_list = []

    for i in range(KEYSIZE):
        arranged[i] = []

    count = 0

    for i in range(0, len(encoded), 2):
        byte = encoded[i] + encoded[i+1]
        arranged[count].append(byte)
        count = (count + 1) % KEYSIZE

    goupto = 100000
    final_key = ''
    for i in range(KEYSIZE):
        s = ''.join(arranged[i])
        key, _, string = decode(s)
        final_key += chr(key)
        arranged_list.append(string)
        if goupto > len(string):
            goupto = len(string)

    final = ''
    for i in range(0, goupto, 2):
        for j in range(KEYSIZE):
            final = final + (arranged_list[j][i] + arranged_list[j][i+1])

    # print(final.decode('hex'))
    print('The fucking key is {}'.format(final_key))

    # print(arranged)
