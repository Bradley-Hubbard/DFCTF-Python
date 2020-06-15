"""
Author: Bradley T Hubbard
Project: DFCTF - Final Year Development Project - DFCTF.py
</4a756e2032332c2031393132/>

Prototype version 1

"""

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
    flag1 = "</fnn8weurn/>"
    flag2 = "</!#co91/>"
    flag3 = "</42BHTJ/>"
    hint = 0
    level2password = "rNg1o42-R8"
    print ("Type 'hint' if you need help to find a flag")
    while userflagenter < '3':
        while userflagenter < '1':
            userflag1 = input ("Enter flag 1: ")
            if userflag1 == flag1:
                userflagenter = '1'
            elif userflag1 == 'hint':
                print ("It sounds like morse code. Take a closer look.")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '1':
            userflag2 = input("Enter flag 2: ")
            if userflag2 == flag2:
                userflagenter = '2'
            elif userflag2 == 'hint':
                print ("Look closer at the python scripts.")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '2':
            userflag3 = input("Enter flag 3: ")
            if userflag3 == flag3:
                userflagenter = '3'
            elif userflag3 == 'hint':
                print ("Try the wordlist and md5hash.txt in hashcat.")
            else:
                print ("Wrong flag entered")
    print("Congratulations\nLevel 2 password is: ", level2password)
    print("\n\n")
    level()
    
def level2():
    print ("Level 2")
    userflagenter = '0'
    flag1 = "</67BE9on!/>"
    flag2 = "</r3Wr!94i5/>"
    flag3 = "</nCe0in3/>"
    hint = 0
    level3password = "nr9thYXZ-0423"
    print ("Type 'hint' if you need help to find a flag")
    while userflagenter < '3':
        while userflagenter < '1':
            userflag1 = input ("Enter flag 1: ")
            if userflag1 == flag1:
                userflagenter = '1'
            elif userflag1 == 'hint':
                print ("Try using the word document's name as one word.")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '1':
            userflag2 = input("Enter flag 2: ")
            if userflag2 == flag2:
                userflagenter = '2'
            elif userflag2 == 'hint':
                print ("Using steghide. Just press enter")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '2':
            userflag3 = input("Enter flag 3: ")
            if userflag3 == flag3:
                userflagenter = '3'
            elif userflag3 == 'hint':
                print ("Modern Ceaser Cipher")
            else:
                print ("Wrong flag entered")
    print("Congratulations\nLevel 3 password is: ", level3password)
    print("\n\n")
    level()

def level3():
    print ("Level 3")
    userflagenter = '0'
    flag1 = "</Di4oxje/>"
    flag2 = "</wmfi42jr/>"
    flag3 = "</Ir9032j&/>"
    hint = 0
    level4password = "J8tifn-rn+3"
    print ("Type 'hint' if you need help to find a flag")
    while userflagenter < '3':
        while userflagenter < '1':
            userflag1 = input ("Enter flag 1: ")
            if userflag1 == flag1:
                userflagenter = '1'
            elif userflag1 == 'hint':
                print ("Look for emails")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '1':
            userflag2 = input("Enter flag 2: ")
            if userflag2 == flag2:
                userflagenter = '2'
            elif userflag2 == 'hint':
                print ("Pigpen")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '2':
            userflag3 = input("Enter flag 3: ")
            if userflag3 == flag3:
                userflagenter = '3'
            elif userflag3 == 'hint':
                print ("Stegcrack + passwords.txt")
            else:
                print ("Wrong flag entered")
    print("Congratulations\nLevel 4 password is: ", level4password)
    print("\n\n")
    level()
    
def level4():
    print ("Level 4")
    userflagenter = '0'
    flag1 = "</DJnRoFI2TJ/>" # Add values once made
    flag2 = "</JFKsDJW104/>"
    flag3 = "</ehf9ew3r/>"
    hint = 0
    level5password = "JF95-04ti"
    print ("Type 'hint' if you need help to find a flag")
    while userflagenter < '3':
         while userflagenter < '1':
            userflag1 = input ("Enter flag 1: ")
            if userflag1 == flag1:
                userflagenter = '1'
            elif userflag1 == 'hint':
                print ("Instragram")
            else:
                print ("Wrong flag entered. Please try again.")
         while userflagenter == '1':
            userflag2 = input("Enter flag 2: ")
            if userflag2 == flag2:
                userflagenter = '2'
            elif userflag2 == 'hint':
                print ("Twitter")
            else:
                print ("Wrong flag entered. Please try again.")
         while userflagenter == '2':
            userflag3 = input("Enter flag 3: ")
            if userflag3 == flag3:
                userflagenter = '3'
            elif userflag3 == 'hint':
                print ("Reddit")
            else:
                print ("Wrong flag entered")
    print("Congratulations\nLevel 5 password is: ", level5password)
    print("\n\n")
    level()

def level5():
    print ("Level 5")
    userflagenter = '0'
    flag1 = "</9pFj2r3R/>"
    flag2 = "</fui4bfu/>"
    flag3 = "<//>"
    hint = 0
    level6password = ""# Add once made
    print ("Type 'hint' if you need help to find a flag")
    while userflagenter < '3':
        while userflagenter < '1':
            userflag1 = input ("Enter flag 1: ")
            if userflag1 == flag1:
                userflagenter = '1'
            elif userflag1 == 'hint':
                print ("Research mounting dd images in linux")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '1':
            userflag2 = input("Enter flag 2: ")
            if userflag2 == flag2:
                userflagenter = '2'
            elif userflag2 == 'hint':
                print ("Look through the files")
            else:
                print ("Wrong flag entered. Please try again.")
        while userflagenter == '2':
            userflag3 = input("Enter flag 3: ")
            if userflag3 == flag3:
                userflagenter = '3'
            elif userflag3 == 'hint':
                print ("what is kwz?")
            else:
                print ("Wrong flag entered")
    print("Congratulations\nLevel 6 password is: ", level6password)
    print("\n\n")
    level()
menu()
