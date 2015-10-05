import subprocess
from itertools import product
import sys

def send_data(string):
    process = subprocess.Popen("./graphic", stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print string
    out, err = process.communicate(string + "\n")
    if "alive" in out:
        print "Got it! %s" % (string)
        sys.exit(0)

moves = "ARL"
counter = 1
while True:
    for move in product(moves, repeat=counter):
        move = "".join(move)
        send_data(move)
    counter += 1
