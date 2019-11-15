def pad(msg, multiple):
    msglen = len(msg)
    padlen = multiple - (msglen%multiple)
    padding = chr(padlen) * padlen
    msg += padding
    return msg

def xor(s1, s2):
    res = ''
    s1 = s1.encode('hex')
    s2 = s2.encode('hex')
    for i in range(0, len(s1), 2):
        b1 = s1[i]+s1[i+1]
        b2 = s2[i]+s2[i+1]
        x = int(b1, 16) ^ int(b2, 16)
        x = "%02x"%x
        res += x

    return res.decode('hex')

def str2hex(s):
    res = ''
    for c in s:
        h = "%02x"%ord(c)
        res += h
    
    return res


# text = "YELLOW SUBMARINE"
# print(text, len(text))
# padded = pad(text, 20)
# print(padded, len(padded))
