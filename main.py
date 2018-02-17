import threading,time,gui

class guiThread(threading.Thread):
    def __init__(self):
        super(guiThread, self).__init__()

    def run(self):
        gui.startGui()


class hideShowThread(threading.Thread):
    def __init__(self):
        super(hideShowThread, self).__init__()

    def run(self):
        time.sleep(5)
        self.hideGui()
        time.sleep(2)
        self.showGui()
        time.sleep(2)
        self.hideGui()


    def hideGui(self):
        gui.hide()

    def showGui(self):
        gui.show()


# hst = hideShowThread()
# hst.start()
# print("hst start")


# gt = guiThread()
# gt.start()


gui.startGui()
print("MAIN >> FINISH")
