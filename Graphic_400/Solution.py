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
for x in range(64):
    for move in product(moves, repeat=x):
        move = "".join(move)
        send_data(move)
