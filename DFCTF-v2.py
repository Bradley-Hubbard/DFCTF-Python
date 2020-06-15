"""
Author: Bradley T Hubbard
Project: DFCTF - Final Year Development Project - DFCTF-v2.py
</4a756e2032332c2031393132/>

Prototype version 2

"""
import hashlib

def menu():
    print ("Digital Forensic Capture The Flag\n\n\n")
    print ("Image available from: The Share OneDrive Folder\n\n")
    print ("Please select one of the following")
    menuoption = '-0'
    while menuoption != '0':
        print ("1 = Select a level")
        print ("0 = Exit")
        menuoption = input("Enter selection: ")
        if menuoption == '1':
            level()
        elif menuoption == '0':
            print ("Goodbye")
        else:
            print ("Error wrong input")      

def level():
    level = '-0'
    print ("\nLEVEL MENU\n\n\n")
    print (" Main Menu = 0\n level\n 1 = Level 1\n 2 = Level 2\n 3 = Level 3\n 4 = Level 4\n 5 = Level 5")
    while level != '0':
        level = input("Enter level: ") 
        if level == '1':
            level1()
        elif level == '2':
            level2()
        elif level == '3':
            level3()
        elif level == '4':
            level4()
        elif level == '5':
            level5()
        elif level == '0':
            menu()
        else:
            print ("Error wrong input")

def level1():
    print ("Level 1 - Training ")
    print ("Password = 'password'")
    userflagenter = '0'
    flag1 = '8155b811eb2dba10bbf07d1d0795897c'
    flag2 = "d7de1cf9b987d83be20c6fce49332a39"
    flag3 = "98592d2e45d026ac84a26b3f60ef5211"
    hint = 0
    level2password = "rNg1o42-R8"
    print ("Type  if you need help to find a flag")
    while userflagenter < '3':
        while userflagenter < '1':
            userflag1 = input("Enter flag 1: ")
            hashed_userflag1 = hashlib.md5(userflag1.encode())
            if hashed_userflag1.hexdigest() == flag1:
                userflagenter = '1'
            elif hashed_userflag1.hexdigest() == "ee2faeed038501c1deab01c7b54f2fa9":
                print ("It sounds like morse code. Take a closer look.")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '1':
            userflag2 = input("Enter flag 2: ")
            hashed_userflag2 = hashlib.md5(userflag2.encode())
            if hashed_userflag2.hexdigest() == flag2:
                userflagenter = '2'
            elif hashed_userflag2.hexdigest() == "ee2faeed038501c1deab01c7b54f2fa9":
                print ("Look closer at the python scripts.")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '2':
            userflag3 = input("Enter flag 3: ")
            hashed_userflag3 = hashlib.md5(userflag3.encode())
            if hashed_userflag3.hexdigest() == flag3:
                userflagenter = '3'
            elif hashed_userflag3.hexdigest() == "ee2faeed038501c1deab01c7b54f2fa9":
                print ("Try the wordlist and md5hash.txt in hashcat.")
            else:
                print ("Wrong flag entered")
    print("Congratulations\nLevel 2 password is: ", level2password)
    print("\n\n")
    level()

def level2():
    print ("Level 2")
    userflagenter = '0'
    flag1 = "d400905730f2d6b1fec3fb6b967f75f0"
    flag2 = "6c9f17bfc9423a864b40f675fe13a926"
    flag3 = "3f22d41bc3a5e957009dca0da9e97121"
    hint = 0
    level3password = "nr9thYXZ-0423"
    print ("Type  if you need help to find a flag")
    while userflagenter < '3':
        while userflagenter < '1':
            userflag1 = input("Enter flag 1: ")
            hashed_userflag1 = hashlib.md5(userflag1.encode())
            if hashed_userflag1.hexdigest() == flag1:
                userflagenter = '1'
            elif hashed_userflag1.hexdigest() == "ee2faeed038501c1deab01c7b54f2fa9":
                print ("Try using the word document's name as one word.")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '1':
            userflag2 = input("Enter flag 2: ")
            hashed_userflag2 = hashlib.md5(userflag2.encode())
            if hashed_userflag2.hexdigest() == flag2:
                userflagenter = '2'
            elif hashed_userflag2.hexdigest() == "ee2faeed038501c1deab01c7b54f2fa9":
                print ("Using steghide. Just press enter")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '2':
            userflag3 = input("Enter flag 3: ")
            hashed_userflag3 = hashlib.md5(userflag3.encode())
            if hashed_userflag3.hexdigest() == flag3:
                userflagenter = '3'
            elif hashed_userflag3.hexdigest() == "ee2faeed038501c1deab01c7b54f2fa9":
                print ("Modern Ceaser Cipher")
            else:
                print ("Wrong flag entered")
    print("Congratulations\nLevel 3 password is: ", level3password)
    print("\n\n")
    level()

def level3():
    print ("Level 3")
    userflagenter = '0'
    flag1 = "23c9a8c26bce998215693baf900645e6"
    flag2 = "2b7a7c6fc7a1e14c7605ffe3313a587f"
    flag3 = "7b3d7942786a25e23f172c804fa9d391"
    hint = 0
    level4password = "J8tifn-rn+3"
    print ("Type 'hint' if you need help to find a flag")
     while userflagenter < '3':
        while userflagenter < '1':
            userflag1 = input("Enter flag 1: ")
            hashed_userflag1 = hashlib.md5(userflag1.encode())
            if hashed_userflag1.hexdigest() == flag1:
                userflagenter = '1'
            elif hashed_userflag1.hexdigest() == "ee2faeed038501c1deab01c7b54f2fa9":
                print ("Look for emails")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '1':
            userflag2 = input("Enter flag 2: ")
            hashed_userflag2 = hashlib.md5(userflag2.encode())
            if hashed_userflag2.hexdigest() == flag2:
                userflagenter = '2'
            elif hashed_userflag2.hexdigest() == "ee2faeed038501c1deab01c7b54f2fa9":
                print ("Pigpen")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '2':
            userflag3 = input("Enter flag 3: ")
            hashed_userflag3 = hashlib.md5(userflag3.encode())
            if hashed_userflag3.hexdigest() == flag3:
                userflagenter = '3'
            elif hashed_userflag3.hexdigest() == "ee2faeed038501c1deab01c7b54f2fa9":
                print ("Stegcrack + passwords.txt")
            else:
                print ("Wrong flag entered")
    print("Congratulations\nLevel 4 password is: ", level4password)
    print("\n\n")
    level()
    
menu()
