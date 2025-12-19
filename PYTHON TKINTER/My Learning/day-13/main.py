from tkinter import *
import tkinter.messagebox as tkmsg

root = Tk()
root.geometry('350x300')
root.title('Radio Button')

# var = IntVar()
# var.set(1)

var = StringVar()
var.set('r1')
Label(root, text='What would you like to have sir?', font='lucis 12 bold', justify=LEFT, padx=12).pack()

# order list

# r1 = Radiobutton(root, text='Dosa',padx=12, variable=var, value='Dosa').pack(anchor='w')
# r2 = Radiobutton(root, text='Idli',padx=12, variable=var, value='Idli').pack(anchor='w')
# r3 = Radiobutton(root, text='Paratha',padx=12, variable=var, value='Paratha').pack(anchor='w')
# r4 = Radiobutton(root, text='Samosa',padx=12, variable=var, value='Samosa').pack(anchor='w')

'''--------or---------'''

foodList = ['Dosa','Idli','Paratha','Samosa']

for i, item in enumerate(foodList):
    Radiobutton(root, text=item, variable=var,padx=12,value=item).pack(anchor='w')

def order():
    tkmsg.showinfo("Order Received",f"Your Food No.{i} {var.get()} is been Ordered.")
    
Button(root, text='Order Now',command=order, padx=8).pack()

root.mainloop()