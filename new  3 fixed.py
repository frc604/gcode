from Tkinter import *
import math

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.t = StringVar()
        

        self.test = Entry(frame, width=10, textvariable=self.t)
        self.test.pack(side=LEFT)

        self.tc = StringVar()
        
        

        self.tcl = Label(frame, textvariable=self.tc, width=10)
        self.tcl.pack(side=LEFT)

        self.c = Button(frame, text="Compute", command=self.comp_t)
        self.c.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone"

    def comp_t(self):
        global tc 
        self.tc.set('%f' % math.sin(float(int(self.t.get())))) # construct string

root = Tk()

App = App(root)

root.mainloop()
