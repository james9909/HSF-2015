import re

def is_hash(hash_):
    return re.findall(r"([a-fA-F\d]{32})", hash_)

flag = ""
for hash_ in open("hashes.md5", "r"):
    if not is_hash(hash_.strip()):
        flag += re.sub('[a-f\d]', '', hash_).strip()

print flag

# At first I thought that we had to crack all the md5 hashes, when I realized that
# some hashes were not even valid. Noticing that some of the hashes had weird characters,
# with one even having flag{, I then thought to brute force the invalid hashes for a match.
# When that didn't work, I realized that the invalid characters in the hashes probably revealed the
# flag. Extracting the invalid characters from the invalid hashes gives us the flag.

# flag{h/-\sh_it_out}
