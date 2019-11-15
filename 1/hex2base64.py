hexString = raw_input()

converted = hexString.decode('hex').encode('base64')
print(converted)

