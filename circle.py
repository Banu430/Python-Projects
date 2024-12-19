#using tinker libraries GUI
from tkinter import*
from tkinter.ttk import*

from time import strftime
#for time formatting

root = Tk() 
#root window

root.title("Clock")
#title name

def time():
    string = strftime('%H:%M:%S %p')
    #time format
    label.config(text=string)
    #updates label with correct time
    label.after(1000, time)

label = Label(root, font=("ds-digital",80), background = "white", foreground = "cyan")
# clock formatting
label.pack(anchor = 'center')
#clock posistion
time()
# to start the clock

mainloop()
# keeps the window open and running untill user closes
