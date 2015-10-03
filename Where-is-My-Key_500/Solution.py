import string

key = "VeryLongKeyYouWillNeverGuess"

enc = open("message_2.enc").read()

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

def brute(message, pos):
    global enc, key
    encrypted = encrypt(message, key)
    if enc[pos] == encrypted[pos]:
        return True
    return False

alphabet = string.printable
message = ""
for pos in range(len(enc)):
    for letter in alphabet:
        temp = message
        temp += letter
        if brute(temp, pos):
            message += letter
            break
print message

# flag{3ncrypti0n_f0r_th3_w1n}
