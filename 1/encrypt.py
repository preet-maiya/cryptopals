plain = raw_input()
len_plain = len(plain)

key = "ICE"
padding = (3 - (len_plain%3))%3
padding_char = 'p'
padding = [padding_char] * padding
padding = ''.join(padding)
plain += padding
print(padding)
key = [ord(letter) for letter in key]

cipher = ''

for i in range(0, len(plain), 3):
    chunk = [ord(letter) for letter in plain[i:i+3]]
    for i in range(3):
        enc = chunk[i] ^ key[i]
        enc = "%02x"%enc
        cipher += enc

print(cipher)
