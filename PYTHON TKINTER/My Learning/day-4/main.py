'''--------frame--------'''

from tkinter import *


kashish = Tk()
kashish.title('Day-4 All about Frame')
kashish.geometry('500x450')

f1 = Frame(kashish, bg='cyan', borderwidth=6,relief=RAISED)
f1.pack(side=LEFT,fill='y',pady=52)

label = Label(f1,text='Hello this is Frame',bg='orange',fg='black',font="Helvetica 8 bold",padx=20,pady=15,relief=RAISED, borderwidth=6)
label.pack(padx=40,pady=20)

f2= Frame(kashish,bg='orange',borderwidth=6)
f2.pack(side=TOP,fill='x')

l=Label(f2,text='this is Frame 2',bg='blue', fg='black',font='times 15 bold italic').pack()

kashish.mainloop()