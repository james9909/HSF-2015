from pwn import *
import requests
from PIL import Image
from PIL.ExifTags import TAGS

def curl_pics():
    url = "http://54.152.5.91/img_0"
    for x in range(0, 40):
        if x < 10:
            x = "0" + str(x)
        x = str(x)
        r = requests.get(url + x + ".JPG", stream=True)
        if r.status_code == 200:
            with open("img_0" + x + ".JPG", 'wb') as f:
                for chunk in r:
                    f.write(chunk)

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
	decoded = TAGS.get(tag, tag)
	ret[decoded] = value
    return ret

def parse_prompt(prompt):
    prompt = prompt.split(": ")
    url = prompt[0]
    filename = url.split("/")[-1]

    f = open(filename, "rb")
    ans = get_exif(f)[prompt[1].strip()]

    print ans
    return str(ans)

# curl_pics()
def main():
    r = remote('54.152.5.91', 1337)

    # Need to submit 35 times
    for x in range(36):
        recv = r.recvline()
        if "flag" in recv:
            print recv
            return
        print recv
        prompt = r.recvline()
        print prompt
        r.send(parse_prompt(prompt) + "\n")

    print r.recvline()

main()

# Need to use the PIL module or the tags/values will not be right

# flag{so_meta_dud3}
