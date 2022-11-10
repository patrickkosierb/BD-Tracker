###
#   Author @ Patrick Kosierb
###
from tkinter import *
from tkinter import ttk

root = Tk()
reason = ""

def exit_app():
    global reason
    reason = input.get()
    root.destroy()

root.title("System Informaion Update")
frm = ttk.Frame(root, padding=10)
frm.grid()
Label(frm, text="Enter reason for SW or FW change.").grid(column=0, row=0)
Button(frm, text="Enter",command=exit_app).grid(column=3,row=2)
input = Entry(frm,width=25)
input.grid(column=0,row=1)
