from tkinter import *

# one instance #
def oneInstance():
    import socket
    import sys
    HOST = ''
    PORT = 4680
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print("already running")
        sys.exit()
    print("server running")

def createUI(win):
    win.minsize(width=400, height=200)
    win.maxsize(width=400, height=200)
    r=0

    win.title('Secret USB Downloader')
    # Secret Usb Downloader

    Label(win, text="                  ").grid(row=r, column=0)
    r += 1

    labelInformatiom = Label(win,text="Hello, this is a program will copy all usb devises. \n email validation is required... ")
    labelInformatiom.grid(row=r, column=1, columnspan=4)
    r += 1

    Label(win, text="").grid(row=r, column=0)
    r += 1
    Label(win, text="").grid(row=r, column=0)
    r += 1

    labelEmail = Label(win, text="Enter your EMAIL: ")
    labelEmail.grid(row=r, column=1, columnspan=2)

    global entryEmail
    entryEmail = Entry(win)
    entryEmail.grid(row=r, column=3, columnspan=2)
    r += 1

    Label(win, text="").grid(row=r, column=0)
    r += 1

    btnSubmit = Button(win, text='Submit', command=submit)
    btnSubmit.grid(row=r, column=3)

entryEmail = None
userEmail = ""
def submit():
    global userEmail
    userEmail = str(entryEmail.get())
    win.destroy()


win = Tk()
createUI(win)
win.mainloop()

print("userEmail >> " + userEmail)

import threading
class copyThread(threading.Thread):
    def __init__(self):
        super(copyThread, self).__init__()
        from copy import initial
        initial()



    def run(self):
        from copy import waitUntilUsbPluggedIn
        waitUntilUsbPluggedIn()




CT = copyThread()
# CT.setDaemon(True)
CT.start()

# import os
#
# def getFolderSize(folder):
#     total_size = os.path.getsize(folder)
#     for item in os.listdir(folder):
#         itempath = os.path.join(folder, item)
#         if os.path.isfile(itempath):
#             total_size += os.path.getsize(itempath)
#         elif os.path.isdir(itempath):
#             total_size += getFolderSize(itempath)
#     return total_size

# print("start copy thread")
# import time
# time.sleep(2)
#
# while True:
#     time.sleep(1)
#     print("Size: " + str(getFolderSize(".")))
#
#

import Pypi



print("end main")
import time
time.sleep(2)