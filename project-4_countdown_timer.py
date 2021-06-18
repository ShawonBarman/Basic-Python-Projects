from tkinter import *   #tkinter is a library that is used to build user interfaces in general.
from tkinter import ttk   #ttk is a sub module of tkinter
from tkinter import font
import datetime

global endTime

def quit(*args):   #so we'll use this to quit the application
    root.destory()   #it will cause the main loop to exit. So when you close the window for the application thats the method that will trigger the application to close it.

def countdown_timer():
    # Get the time remaining until the event
    timeLeft = endTime - datetime.datetime.now()
    #remove the microseconds part
    timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)

    txt.set(timeLeft)
    root.after(1000,countdown_timer)   #it is used to trigger the countdown after 1000milliseconds.

#use tkinter library for showing the clock
root = Tk()   #TK basically create the root. Everything that you put on screen, whether it is a text box, a button, or an image, is known as a widget and the must all be placed in the root.
root.attributes("-fullscreen",False)
root.configure(background="black")
root.bind("x",quit)
root.after(1000,countdown_timer)

#set the end date and time for the countdown
endTime = datetime.datetime(year=2021,month=8,day=18,hour=22,minute=38,second=0)

fnt = font.Font(family="Helvetica", size=50, weight="bold")
txt = StringVar()   #this will hold a string value by default.
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="green")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()