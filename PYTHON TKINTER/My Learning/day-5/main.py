'''-------same as label we use button--------'''

from tkinter import *

bs = Tk()

bs.title('Day-5 Button tut')
bs.geometry('600x600')


def color():
    print(f'this is just a color:')
f1 = Frame(bs,bg='cyan')
f1.pack(anchor='nw',padx=110,pady=250)

b1 = Button(f1,text='btn-1',padx=16,pady=8,command=color).pack(side=LEFT,padx=8)
b2 = Button(f1,text='btn-2',padx=16,pady=8,command=color).pack(side=LEFT,padx=8)
b3 = Button(f1,text='btn-3',padx=16,pady=8,command=color).pack(side=LEFT,padx=8)
b4 = Button(f1,text='btn-4',padx=16,pady=8,command=color).pack(side=LEFT,padx=8)

bs.mainloop()