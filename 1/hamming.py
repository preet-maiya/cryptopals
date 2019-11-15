def high_bits(byte):
    count = 0

    while(byte>0):
        if byte%2:
            count += 1
        byte = byte>>1
    
    return count

def hamming(first, second):
    distance = 0
    for i in range(0, len(first), 2):
        xored = int(first[i]+first[i+1], 16) ^ int(second[i]+second[i+1], 16)
        val = high_bits(xored)
        distance += val
    return distance


# print(hamming('this is a test', 'wokka wokka!!!'))

