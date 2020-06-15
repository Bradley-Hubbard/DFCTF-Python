"""
Author: Bradley T Hubbard
Project: DFCTF - Final Year Development Project - Checksum.py
</4a756e2032332c2031393132/>

Notes:
- Most be ran in python 3
- Add file hashes for each file
- Download and store outside of DFCTF to provide a bad hash value
"""

import glob
import hashlib
import os
from termcolor import colored, cprint


directory = os.getcwd()

for files in glob.glob(os.path.join(directory, '*.*')):
    expected = ""
    with open(files, 'rb') as getmd5:
        data = getmd5.read()
        gethash = hashlib.md5(data).hexdigest()
        #gethash values need inputting for the levels once made
        if gethash == "a365e356640143a1a565429ece041213": #DFCTF.py
            expected = "a365e356640143a1a565429ece041213"
            status = colored ('Good', 'green')
        elif gethash == "6cac79ef785135dfde02d7eda0a6b948": #Level 1
            expected = "6cac79ef785135dfde02d7eda0a6b948"
            status = colored ('Good', 'green')
        elif gethash == "": #Level 2
            expected = ""
            status = colored ('Good', 'green')
        elif gethash == "": #Level 3
            expected = ""
            status = colored ('Good', 'green')
        elif gethash == "998130de8e10c3c1e4a900e31dddb5e4": #Level 4
            expected = "998130de8e10c3c1e4a900e31dddb5e4"
            status = colored ('Good', 'green')
        elif gethash == "": #Level 5
            expected = ""
            status = colored ('Good', 'green')
        else:
            status = colored ('Bad', 'red')
            
    print ("file name: ", files)
    print ("Expected Hash Value: ", expected)
    print ("Computed hash value: ", gethash)
    print ("Status: ", status) 
    print ("\n")
