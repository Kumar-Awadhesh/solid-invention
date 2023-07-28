from tkinter import *
from tkcalendar import *

root=Tk()
root.geometry("400x350")

cal=Calendar(root, selectmode="day", year=2023, month=7, day=28)
cal.pack(pady=10)

def my_date():
    date.config(text="Selected Date:"" "+cal.get_date())

Button(root, text="Get Date", command=my_date).pack(pady=10)

date=Label(root, text="")
date.pack(pady=10)

root,mainloop()