from pwn import *


signatures = {}
f = open("signatures.txt", "r")
for line in f.readlines():
    line = line.split(",")
    if "|" in line[0]:
        names = line[0].split("|")
        for name in names:
            signatures[name] = line[1]
    else:
        signatures[line[0]] = line[1]

def get_signature(ascii_signature):
    global signatures
    ascii_signature = ascii_signature.strip()
    return signatures[ascii_signature]

def main():
    r = remote("54.152.35.110", 1337)
    print r.recvline()

    for x in range(30):
        response = r.recvline()
        if "flag" in response:
            print response
            return
        print response
        ascii_signature = r.recvline()
        print ascii_signature
        signature = get_signature(ascii_signature)
        print signature
        r.send(signature + "\n")

main()

# The problem tells us about magic, which is referring to 'magic numbers' aka file signatures.
# The problem also tells us about a man named Gary, and we can assume that he's referring to Gary Kessler, who
# has a library of file signatures. If we download the file with all the data, which is also on his site,
# we can use it to send the correct file signatures to the server
# You can download it for yourself at http://www.garykessler.net/software/index.html#filesigs

# flag{believe_it_or_not_im_not_a_begger_im_actually_a_MAGIC_MAN}
