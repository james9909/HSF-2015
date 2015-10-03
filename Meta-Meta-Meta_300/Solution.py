from pwn import *
import requests
import subprocess

def curl_pics():
    url = "http://54.152.5.91/img_0"
    for x in range(34, 40):
        if x < 10:
            x = "0" + str(x)
        x = str(x)
        r = requests.get(url + x + ".JPG", stream=True)
        if r.status_code == 200:
            with open("img_0" + x + ".JPG", 'wb') as f:
                for chunk in r:
                    f.write(chunk)

def parse_prompt(prompt):
    prompt = prompt.split(": ")
    url = prompt[0]
    filename = url.split("/")[-1]

    data = subprocess.check_output("exiftool -'%s' %s" % (prompt[1].strip(), filename), shell=True)
    ans = data.split(": ")[1]
    # subprocess.call("rm pic", shell=True)
    print ans
    return ans

# curl_pics()
def main():
    try:
        r = remote('54.152.5.91', 1337)
        for x in range(5):
            recv = r.recvline()
            if "flag" in recv:
                print recv
                return
            print recv
            prompt = r.recvline()
            print prompt
            r.send(parse_prompt(prompt) + "\n")

        print r.recvline()
    except:
        main()

main()
