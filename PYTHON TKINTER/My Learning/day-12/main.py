from tkinter import *
import tkinter.messagebox as tkMsg

root = Tk()
root.geometry('450x400')
root.title('Slider Tutorial')

Label(text='Rate Us by Scale How is our service',font='times 10 bold italic',padx=10,pady=6).pack()

s1 = Scale(root, from_= 0, to = 100, orient=HORIZONTAL, tickinterval=50)
s1.set(50)

def display():
    tkMsg.showinfo('Thank You',f"Thank You for Your {s1.get()} Ratings")
b1 = Button(root, text='Submit',pady=8,command=display)

s1.pack()
b1.pack()



root.mainloop()