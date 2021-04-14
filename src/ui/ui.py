from tkinter import *

class UI:

    def __init__(self, root):
        self._root = root
    
    def start(self):
        label = Label(master = self._root, text = "Zibuzabu")
        button = Button(master = self._root, text = "Painke :D")
        entry = Entry(master= self._root)
        checkbutton = Checkbutton(master = self._root, text = "tsekkaas dää :DD")
        radiobutton = Radiobutton(master = self._root, text = "ei tää oo mikään radio xDD")
        label.pack()
        button.pack()
        entry.pack()
        checkbutton.pack()
        radiobutton.pack()
        

root = Tk()
root.title("testing")
ui = UI(root)
ui.start()
root.mainloop()