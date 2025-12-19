'''--------all about textVariable, Grid, and function -------'''

from tkinter import *

just = Tk()
just.title('Grid and textVariable')
just.geometry('700x500')



userValue = Label(text='username:').grid()
passValue = Label(text='password:').grid()

#To take a input we have to define it's variable classes[BooleanVar,DoubleVar,IntVar,StringVar]
userData = StringVar()
passData = StringVar()

# Entry Widget helps you to take input
userField = Entry(just,textvariable=userData).grid(row=0,column=1)
passField = Entry(just,textvariable=passData).grid(row=1,column=1)


def getValue():
    print(f"this is a username:{userData.get()}")
    print(f'this is a password:{passData.get()}')

Button(just,text='Submit', command=getValue).grid(row=2,column=1)

just.mainloop()
