#!/usr/bin/python3

import sys
import os
import re
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image


class Window(Frame):
    tags = []
    meta = {}
    template = ""
    replace = []
    E1 = []
    L1 = []
    winx = 500
    winy = 400
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("JSI - JReplace Template")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Open", command=self.openFile)
        file.add_command(label="Save", command=self.saveFile)
        file.add_command(label="Exit", command=self.space_rats, accelerator="Ctrl+Q")

        #added "file" to our menu
        menu.add_cascade(label="File", underline=0, menu=file)
        # create the file object)
        edit = Menu(menu)
        self.bind_all("<Control-q>", self.space_rats)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Clear", command=self.clearWindow)

        #added "file" to our menu
        menu.add_cascade(label="View", menu=edit)
        self.showImg()
        clearButton = Button(self, text="Clear",command=self.clearWindow)
        # placing the button on my window
        clearButton.place(x=325, y=460)
        quitButton = Button(self, text="Quit", command=self.space_rats)
        # placing the button on my window
        quitButton.place(x=385, y=460)

    def drawEntry(self):
        tag_count = 0
        for tag in self.tags:
            self.L1.append( Label(self, text=tag))
            self.L1[tag_count].place(x=10, y=tag_count*28)
            self.E1.append(Entry(self, bd =5))
            self.E1[tag_count].place(x=178, y=tag_count*28)
            tag_count += 1
        self.resizeWindow()

    def showImg(self):
        load = Image.open("jsi-logo-256.png")
        render = ImageTk.PhotoImage(load)
        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=190, y=200)

    def openFile(self):
        self.filename =  filedialog.askopenfilename(initialdir = "~/",title = "Select file",filetypes = (("ini files","*.ini"),("all files","*.*")))
        self.loadTemplate()
        self.drawEntry()

    def saveFile(self):
        self.filename =  filedialog.asksaveasfilename(initialdir = "~/",title = "Select file",filetypes = (("ini files","*.ini"),("all files","*.*")))
        for t in self.E1:
            self.replace.append(t.get())
        self.replaceTags()
        with open(self.filename, "w") as f:
            f.write(self.template)

    def clearWindow(self):
        for i in range(len(self.E1)):
            self.E1[i].destroy()
            self.L1[i].destroy()
        self.E1 = []
        self.L1 = []
        self.tags = []
        self.meta = {}
        self.template = ""
        self.replace = []

    def loadTemplate(self):
        if os.path.isfile(self.filename):
            # Read tags and create set
            with open(self.filename) as file:
                self.template = file.read()
            file_tags=re.findall(re.escape('<')+"(.*)"+re.escape('>'),self.template)
            for i in file_tags:
                if ':' in i:
                    self.meta[i.split(':')[0]] = i.split(':')[1]
                    self.template = template.replace('<'+i+'>','')
                else:
                    if not i in self.tags:
                        self.tags.append(i)

    def replaceTags(self):
        tag_count = 0
        for t in self.tags:
            self.template=self.template.replace("<"+t+">", self.replace[tag_count])
            tag_count += 1
        print(self.tags)
        print(self.replace)
        print(self.template)

    #Quit button function
    def space_rats(self, event=""):
        sys.exit(0)

    def resizeWindow(self):
        self.winy=(len(self.tags)+1)*30+100
        self.configure(width=self.winy) 

root = Tk()
img = PhotoImage(file='jsi-logo-256.png')
root.tk.call('wm', 'iconphoto', root._w, img)
#size of the window
root.geometry("450x500")

app = Window(root)
root.mainloop() 
