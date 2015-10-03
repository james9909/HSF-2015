enc = open("message_1.enc").read()

def encrypt(plain, key):
    enc = ""
    c = 0
    p = 0
    t = 0
    i = 0
    for p in plain:
        c = chr((ord(p) + (ord(key[i % len(key)]) ^ t) + i*i) & 0xff)
        t = ord(p)
        i += 1
        enc += c
    return enc

def brute(key, pos):
    global enc
    encrypted = encrypt("Hi! This is only test message", key)
    if enc[pos] == encrypted[pos]:
        return True
    return False

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += alphabet.upper()
key = ""
for pos in range(28): # 28 is the actual length of the key
    for letter in alphabet:
        if brute(letter, pos):
            key += letter
            break
    print key
