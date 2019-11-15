from collections import Counter
import operator


enc = raw_input()

hex_letters = [enc[i:i+2] for i in range(0, len(enc), 2)]
count = dict(Counter(hex_letters))
score = []
for i in range(0, 256):
    s = 0
    for hexs, c in count.items():
        decoded = int(hexs, 16)^i
        if (decoded>=65 and decoded<=90) or (decoded>=97 and decoded<=122) or decoded==32:
            s += c

    score.append(s)

index, value = max(enumerate(score), key=operator.itemgetter(1))

final = ''
for letter in hex_letters:
    conv = int(letter, 16)^index
    conv = '%02x' % conv
    final += conv


print(final.decode('hex'))
    
