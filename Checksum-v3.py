import os
from termcolor import cprint, colored

hashfile = os.popen("md5sum ~/*/DFCTF/Level1.zip | awk '{ print $1 }'")
filehash = hashfile.read()
filename = "Level1.zip"
if filehash == "121db0392d2ac7f4a762d5667403e7b7\n":
    status = colored ("Good\n", 'green')
else:
    status = colored ("Corrupted\n", 'red')
print (filename)
print (filehash)
print (status)

hashfile = os.popen("md5sum ~/*/DFCTF/Level2.zip | awk '{ print $1 }'")
filehash = hashfile.read()
filename = "Level2.zip"
if filehash == "dfa7f523a4be6b9599a3eb7666027c09\n":
    status = colored ("Good\n", 'green')
else:
    status = colored ("Corrupted\n", 'red')
print (filename)
print (filehash)
print (status)

hashfile = os.popen("md5sum ~/*/DFCTF/Level3.zip | awk '{ print $1 }'")
filehash = hashfile.read()
filename = "Level3.zip"
if filehash == "a4e9df590f9d37410e59d2911ab84d5a\n":
    status = colored ("Good\n", 'green')
else:
    status = colored ("Corrupted\n", 'red')
print (filename)
print (filehash)
print (status)

hashfile = os.popen("md5sum ~/*/DFCTF/Level4.zip | awk '{ print $1 }'")
filehash = hashfile.read()
filename = "Level4.zip"
if filehash == "998130de8e10c3c1e4a900e31dddb5e4\n":
    status = colored ("Good\n", 'green')
else:
    status = colored ("Corrupted\n", 'red')
print (filename)
print (filehash)
print (status)

hashfile = os.popen("md5sum ~/*/DFCTF/Level5.zip | awk '{ print $1 }'")
filehash = hashfile.read()
filename = "Level5.zip"
if filehash == "2809abe5da9c67f9ebdeb87b226ddf20\n":
    status = colored ("Good\n", 'green')
else:
    status = colored ("Corrupted\n", 'red')
print (filename)
print (filehash)
print (status)

hashfile = os.popen("md5sum ~/*/DFCTF/DFCTF.py | awk '{ print $1 }'")
filehash = hashfile.read()
filename = "DFCTF.py"
if filehash == "a365e356640143a1a565429ece041213\n":
    status = colored ("Good\n", 'green')
else:
    status = colored ("Corrupted\n", 'red')
print (filename)
print (filehash)
print (status)
