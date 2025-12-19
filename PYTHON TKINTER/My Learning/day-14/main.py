from tkinter import *

root = Tk()
root.title('List Box')
root.geometry('400x350')

l1 = Listbox(root, height = 10, 
                  width = 15, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "lucida 10 bold italic",
                  fg = "yellow")

Label(root,text='FOOD Items').pack(anchor='w')


l1.insert(0, "Dosa")
l1.insert(1, "Idli")
l1.insert(2, "Paratha")
l1.insert(3, "Samosa")
l1.insert(4, "Vada")

l1.delete(3)


l1.pack(anchor='w')
root.mainloop()