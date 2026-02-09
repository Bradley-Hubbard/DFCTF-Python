"""
Author: Bradley T Hubbard
Project: DFCTF - Final Year Developement Project - DFCTF.py
</4a756e2032332c2031393132/>

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
            exit()
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
            return()
        else:
            print ("Error wrong input")

def level1():
    print ("Level 1 - Training ")
    print ("Password = 'password'") #Level one zip file password
    userflagenter = '0'
    flag1 = "4355ae1e52814fd141ae504d2b50bf9b" #Insert Flag value in MD5 format
    flag2 = "bb1dd19b46db82539b79114e7c7e0ad9"
    flag3 = "bc9d8e8bde676d3e952a90371133fb5e"
    hint = 0
    level2password = "" # Next level's zip file password
    print ("Type  if you need help to find a flag")
    while userflagenter < '3':
        while userflagenter < '1':
            userflag1 = input("Enter flag 1: ")
            hashed_userflag1 = hashlib.md5(userflag1.encode())
            if hashed_userflag1.hexdigest() == flag1:
                userflagenter = '1'
            elif hashed_userflag1.hexdigest() == "ee2faeed038501c1deab01c7b54f2fa9": #'hint' in MD5
                print ("Import into Autopsy or mount the image onto the file system") #Insert hint here
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '1':
            userflag2 = input("Enter flag 2: ")
            hashed_userflag2 = hashlib.md5(userflag2.encode())
            if hashed_userflag2.hexdigest() == flag2:
                userflagenter = '2'
            elif hashed_userflag2.hexdigest() == "ee2faeed038501c1deab01c7b54f2fa9":
                print ("Look deeper into the image.") #Insert hint here
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '2':
            userflag3 = input("Enter flag 3: ")
            hashed_userflag3 = hashlib.md5(userflag3.encode())
            if hashed_userflag3.hexdigest() == flag3:
                userflagenter = '3'
            elif hashed_userflag3.hexdigest() == "ee2faeed038501c1deab01c7b54f2fa9":
                print ("Hail, Computer Ceasar") #Insert hint here
            else:
                print ("Wrong flag entered")
    print("Congratulations\nLevel 2 password is: ", level2password)
    print("\n\n")
    return()

menu()

