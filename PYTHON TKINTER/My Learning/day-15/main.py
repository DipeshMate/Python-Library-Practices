from tkinter import *

root = Tk()
root.title('ScrollBar tut')
''' for connecting with scrollbar in window 
1. in widget like ListBox(yscrollcommand = scrollbar.set)
2. scrollbar.config(command = widget.yview) 

'''

root.geometry('400x350')

scroll = Scrollbar(root,bg='DeepSkyBlue2')
scroll.pack(fill=Y,side=RIGHT)
l1 = Listbox(root, height = 10, 
                  width = 15, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "lucida 10 bold italic",
                  fg = "yellow",
                  yscrollcommand=scroll.set)

Label(root,text='Food Items',bg='DeepSkyBlue2',padx=22
    ).pack(side=TOP)

for i in range(0,152):
    l1.insert(END,f"item {i}")

# to connect with scroolbar



scroll.config(command=l1.yview)
l1.pack(fill=BOTH)

root.mainloop()