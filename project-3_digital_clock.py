from tkinter import *   #tkinter is a library that is used to build user interfaces in general.
from tkinter import ttk   #ttk is a sub module of tkinter
from tkinter import font
import datetime

def quit(*args):   #so we'll use this to quit the application
    root.destory()   #it will cause the main loop to exit. So when you close the window for the application thats the method that will trigger the application to close it.

def clock_time():
    #Get the time remaining until the event
    time = datetime.datetime.now()
    time = time.strftime("Today Date: %d-%m-%Y\nNow time: %H:%M:%S")
    #time = (time.strftime("%H:%M:%S"))
    txt.set(time)
    root.after(1000,clock_time)   #it is used to trigger the countdown after 1000milliseconds.

#use tkinter library for showing the clock
root = Tk()   #TK basically create the root. Everything that you put on screen, whether it is a text box, a button, or an image, is known as a widget and the must all be placed in the root.
root.attributes("-fullscreen",False)
root.configure(background="green")
root.bind("x",quit)
root.after(1000,clock_time)

fnt = font.Font(family="Helvetica", size=50, weight="bold")
txt = StringVar()   #this will hold a string value by default.
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="green")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()