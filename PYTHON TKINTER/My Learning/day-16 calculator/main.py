from tkinter import *

def click(event):
    numVal = event.widget.cget('text')   # .!frame.!button
    print(numVal)
    scrValue.set(scrValue.get() + numVal)
    screen.update() # it will update the value
    
root= Tk()
root.geometry('350x450')
root.title("Dipesh's Calculator")
root.configure(background='DeepSkyBlue2')
root.wm_iconbitmap('calculator.ico')

scrValue = StringVar()
scrValue.set("")

screen = Entry(root,textvariable=scrValue,font='lucida 20 bold')
screen.pack(ipadx=20,padx=8,pady=8) #ipadx = internal padding

btn_Frame = Frame(root, bg='green')

btnVal = Button(btn_Frame,text='9',padx=22,pady=18)
btnVal.pack(side=LEFT,padx=8)
btnVal.bind("<Button-1>", click)
btnVal = Button(btn_Frame,text='8',padx=22,pady=18)
btnVal.pack(side=LEFT,padx=8)
btnVal.bind("<Button-1>", click)
btnVal = Button(btn_Frame,text='7',padx=22,pady=18)
btnVal.pack(side=LEFT,padx=8)
btnVal.bind("<Button-1>", click)

btn_Frame.pack()

root.mainloop()