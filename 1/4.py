from collections import Counter
import operator
import sys


f = open('encoded', 'r')

enc = f.read()
enc = ''.join(enc.split('\n'))
# print(enc)

def decode(enc):
    hex_letters = [enc[i:i+2] for i in range(0, len(enc), 2)]
    count = dict(Counter(hex_letters))
    score = []
    for i in range(0, 256):
        s = 0
        for hexs, c in count.items():
            decoded = int(hexs, 16)^i
            if (decoded>=65 and decoded<=90) or (decoded>=97 and decoded<=122) or decoded==32 or decoded==10:
                s += c
 
        score.append(s)

    index, value = max(enumerate(score), key=operator.itemgetter(1))
 
    final = ''
    for letter in hex_letters:
        conv = int(letter, 16)^index
        conv = '%02x' % conv
        final += conv

    return index, value, final
    
max_score = -1
pos = 0
final_text = ''
final_key = 0
print(len(enc))
for i in range(len(enc) - 60):
    # sys.stdout.write("%10000i\r"%i)
    chunk = enc[i:i+60]
    # print(len(chunk))
    key, score, conv = decode(chunk)
    # print(len(conv))
    if score > max_score:
        max_score = score
        pos = i
        final_text = conv
        final_key = key

print(pos, final_key)
print(final_text.decode('hex'))
