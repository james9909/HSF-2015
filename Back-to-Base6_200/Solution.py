import base64
import binascii

enc = open("release.txt", "r").readlines()
flag = ""

for x in range(len(enc)):
    enc[x] = enc[x].strip()

flag += base64.b64decode(enc[0])
flag += enc[1].decode("hex")
for num in enc[2].split(" "):
    flag += chr(int(num))

flag += binascii.unhexlify("%x" % int(enc[3], 2))
flag += "krabs_" # Base32

print flag
