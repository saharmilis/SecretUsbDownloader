# import win32api
#
# drives = win32api.GetLogicalDriveStrings()
# drives = drives.split('\000')[:-1]
# print drives
from lib2to3.pgen2 import driver

import platform,os

currentDirectory = os.getcwd()
numberOfCopy = 0
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
drivers = [];


def hasDrive(letter):
    return "Windows" in platform.system() and os.system("vol %s: 2>nul>nul" % (letter)) == 0

def initial():
    global drivers
    global letters
    print("initilize...")
    for letter in letters:
        if (hasDrive(letter)):
            drivers.append(letter)

def getNumberOfDrivers():
    global letters
    num = 0;
    for letter in letters:
        if (hasDrive(letter)):
            num += 1
    return num

def copy(fromDrive):
    import shutil
    global numberOfCopy
    global currentDirectory
    numberOfCopy += 1
    try:
        shutil.copytree(fromDrive+":", currentDirectory +"\\USB" + str(numberOfCopy));
    except:
        print("COPY >> ERROR while copy")
        pass

stopper = False
def waitUntilUsbPluggedIn():
    import time
    global stopper
    stopper = True

    while True:
        print("WAITING")

        if(stopper==False):
            print("stop copy drives")
            return

        time.sleep(1)
        numOfDrives = getNumberOfDrivers()
        if(numOfDrives > len(drivers)):
            temp = getNameUsbPluggedIn()
            copy(temp)
        if(getNumberOfDrivers() < len(drivers)):
            initial()

    print("DONE")

def getNameUsbPluggedIn():
    global drivers
    for letter in letters:
        if (hasDrive(letter)):
            if(letter in drivers):
                pass
            else :
                print(letter)
                return letter
    return None

def stopCopy():
    global stopper
    stopper = False


# def pressStart():
#     print("START COPYING")
#     initial()
#     waitUntilUsbPluggedIn()
#     usb = getNameUsbPluggedIn()
#     print("NEW USB >> " + usb)



