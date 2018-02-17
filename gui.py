
import requests
from constant import WEBSITE
from constant import SERVER_UserUsing
from tkinter import *


userPassword = "";
def submit():
    print("submit")
    btnStart.config(state=DISABLED)
    btnStop.config(state=DISABLED)

    global userPassword

    url = SERVER_UserUsing
    userPassword = str(entryPassword.get())
    data = {"user": userPassword,"action":"check"}
    params = {'format': 'xml', 'platformId': 1}
    r = requests.post(url, data=data, json=None)

    if (r.status_code != 200):
        return


    print(r.text)
    labelUsageNumber.configure(text = r.text)

    try:
        val = int(r.text)

        if (val <= 0):
            labelUsageNumber.configure(text="0")
            return

        btnStart.config(state=NORMAL)

    except ValueError:
        #r.text=="USER NOT EXISTS"
        btnStart.config(state=DISABLED)
        btnStop.config(state=DISABLED)


usageLeft=0;
def start():
    print("start")
    btnStop.config(state=NORMAL)

    url = SERVER_UserUsing
    data = {"user": userPassword, "action": "use"}
    params = {'format': 'xml', 'platformId': 1}
    r = requests.post(url, data=data, json=None)

    if(r.status_code!=200):
        return


    print("left" + r.text)

    try:
        global usageLeft
        usageLeft = int(r.text)

        if(usageLeft<0):
            labelUsageNumber.configure(text="0")
            return

        labelUsageNumber.configure(text=usageLeft)
        btnStart.config(state=DISABLED)
        btnStop.config(state=NORMAL)

        CT = copyThread()
        CT.start()

    except ValueError:
        # r.text=="USER NOT EXISTS"
        btnStart.config(state=DISABLED)
        btnStop.config(state=DISABLED)


def stop():
    print("stop")
    if usageLeft>0:
        btnStart.config(state=NORMAL)

    btnStop.config(state=DISABLED)
    from copy import stopCopy
    stopCopy()

def openWebsite():
    import webbrowser
    webbrowser.open(WEBSITE)
    pass

win = Tk()

win.minsize(width=300, height=100)
# win.maxsize(width=300, height=100)

win.title('YOYO')
# Secret Usb Downloader

labelPassword = Label(win, text="Enter your password: ")
labelPassword.grid(row=0, column=0,columnspan=2)

entryPassword = Entry(win)
entryPassword.grid(row=0, column=2,columnspan=2)


labelUsage = Label(win, text="Usage Remaining: ")
labelUsage.grid(row=1, column=0,columnspan=2)

labelUsageNumber = Label(win,text="0")
labelUsageNumber.grid(row=1, column=2,columnspan=2)

labelEmpty = Label(win, text="")
labelEmpty.grid(row=2, column=0)

btnStart = Button(win, text='Start', command=start,state=DISABLED)
btnStart.grid(row=3, column=1)

btnStop = Button(win, text='Stop', command=stop,state=DISABLED)
btnStop.grid(row=3, column=2)

btnWeb = Button(win, text='WebSite', command=openWebsite,state=NORMAL)
btnWeb.grid(row=3, column=4)

btnSubmit = Button(win, text='submit', command=submitFunction,state=NORMAL)
btnSubmit.grid(row=0, column=4)


def startGui():
    print("GUI >> START")
    win.mainloop()

import threading
class copyThread(threading.Thread):
    def __init__(self):
        super(copyThread, self).__init__()
        from copy import initial
        initial()

    def run(self):
        from copy import waitUntilUsbPluggedIn
        waitUntilUsbPluggedIn()





def hide():
    global win
    win.withdraw()

def show():
    global win
    win.deiconify()