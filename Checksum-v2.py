import os
from termcolor import cprint, colored

hashfile = os.popen("md5sum ~/Documents/DFCTF/Level1.zip")
filehash = hashfile.read()
if filehash == "121db0392d2ac7f4a762d5667403e7b7  /home/bradley/Documents/DFCTF/Level1.zip\n":
    status = colored ("Good\n", 'green')
else:
    status = colored ("Corrupted\n", 'red')
print (filehash)
print (status)

hashfile = os.popen("md5sum ~/Documents/DFCTF/Level2.zip")
filehash = hashfile.read()
if filehash == "dfa7f523a4be6b9599a3eb7666027c09  /home/bradley/Documents/DFCTF/Level2.zip\n":
    status = colored ("Good\n", 'green')
else:
    status = colored ("Corrupted\n", 'red')
print (filehash)
print (status)

hashfile = os.popen("md5sum ~/Documents/DFCTF/Level3.zip")
filehash = hashfile.read()
if filehash == "1670f2b6e57f620bdacb9f872b976192  /home/bradley/Documents/DFCTF/Level3.zip\n":
    status = colored ("Good\n", 'green')
else:
    status = colored ("Corrupted\n", 'red')
print (filehash)
print (status)

hashfile = os.popen("md5sum ~/Documents/DFCTF/Level4.zip")
filehash = hashfile.read()
if filehash == "998130de8e10c3c1e4a900e31dddb5e4  /home/bradley/Documents/DFCTF/Level4.zip\n":
    status = colored ("Good\n", 'green')
else:
    status = colored ("Corrupted\n", 'red')
print (filehash)
print (status)

hashfile = os.popen("md5sum ~/Documents/DFCTF/Level5.zip")
filehash = hashfile.read()
if filehash == "f1f23ed9d4147aaff77fb3c347f9bb82  /home/bradley/Documents/DFCTF/Level5.zip\n":
    status = colored ("Good\n", 'green')
else:
    status = colored ("Corrupted\n", 'red')
print (filehash)
print (status)

hashfile = os.popen("md5sum ~/Documents/DFCTF/DFCTF.py")
filehash = hashfile.read()
if filehash == "f079539b1e976630eece50c39f04f75c  /home/bradley/Documents/DFCTF/DFCTF.py\n":
    status = colored ("Good\n", 'green')
else:
    status = colored ("Corrupted\n", 'red')
print (filehash)
print (status)
