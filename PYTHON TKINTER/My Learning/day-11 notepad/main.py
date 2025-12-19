from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root = Tk()
root.geometry('450x450')
root.title('Notepad')
root.wm_iconbitmap('note.ico')

def myFunc():
    print('Just Rolling')

def help():
    a = tmsg.askquestion("Help","I'll Help you in GUI, Press yes to get Help")
    if a=='yes':
        m = 'Thank You We Get Back to you'
    else:
        m = 'Okay See You soon'
    tmsg.showinfo('message',m)
    
def msg():
    value = tmsg.askquestion("Any Other help","Hey Do you need Any other help")
    
    if value:
        message = 'Ja na yaar Bhai dusri jagah'
    else:
        message = 'Dusri baar help maang deta hu terko kaan k niche'
    
    tmsg.showinfo("Message-Box",message)
def newFile():
    global file
    root.title('Untitled - Notepad')
    file = None
    TextArea.delete(1.0, END)# (1.0)start from- first line - zero character, (END)- to the last end
def openFile():
    global file
    file = askopenfilename(defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Docments","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
          
def about():
    tmsg.showinfo('Notepad','Notepad by Dipesh Mate.')
    
def saveAs():
    global file
    
    if file == None:
        # if file is none then  create a new file to save
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[("All Files","*.*"),("Text Docments","*.txt")])
    # if file is not selected
        if file =="":
           file = None
        else:
           # save as a new file
           f = open(file,'w')
           f.write(TextArea.get(1.0,END))
           f.close()
       
           root.title(os.path.basename(file)+" - Notepad")
    else:
        # save the file
           f = open(file,'w')
           f.write(TextArea.get(1.0,END))
           f.close()
def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))
  
xscrollbar = Scrollbar(root, orient=HORIZONTAL)
xscrollbar.pack(fill=BOTH,side=BOTTOM)

yscrollbar = Scrollbar(root)
yscrollbar.pack(fill=BOTH,side=RIGHT)

TextArea = Text(root,bg='lavender', font='lucida 12',
    xscrollcommand=xscrollbar.set,
    yscrollcommand=yscrollbar.set)
TextArea.pack(expand=True,fill=BOTH)

xscrollbar.config(command=TextArea.xview)
yscrollbar.config(command=TextArea.yview)
#         text.insert(END, 'a'*999)

# def start(self):
#         self.b_start.config(state=DISABLED)
#         self.b_stop.config(state=ACTIVE)

# def stop(self):
#         self.b_stop.config(state=DISABLED)
#         self.b_start.config(state=ACTIVE)

file = None

'''---- Creating Main Menu ---'''
        
mainmenu = Menu(root)

# file menu

filemenu1 = Menu(mainmenu,tearoff=0)
filemenu1.add_command(label='New Tab',command=newFile)
filemenu1.add_command(label='New Window',command=myFunc)
filemenu1.add_command(label='Open',command=openFile)
filemenu1.add_command(label='Save',command=myFunc)
filemenu1.add_command(label='Save as',command=saveAs)
filemenu1.add_command(label='Save all',command=myFunc)
filemenu1.add_separator()
filemenu1.add_command(label='Page Setup',command=myFunc)
filemenu1.add_command(label='Print',command=myFunc)
filemenu1.add_separator()
filemenu1.add_command(label='Close Tab',command=myFunc)
filemenu1.add_command(label='Close Window',command=exit)
filemenu1.add_command(label='Exit',command=exit)

mainmenu.add_cascade(menu=filemenu1,label='File')

# edit menu

editMenu = Menu(mainmenu,tearoff=0)

editMenu.add_command(label="Undo", command=myFunc)
editMenu.add_separator()
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)
editMenu.add_command(label="Delete", command=myFunc)
editMenu.add_separator()
editMenu.add_command(label="Search with Bing", command=myFunc)
editMenu.add_separator()
editMenu.add_command(label="Find", command=myFunc)
editMenu.add_command(label="Find next", command=myFunc)
editMenu.add_command(label="Find previous", command=myFunc)
editMenu.add_command(label="Replace", command=myFunc)
editMenu.add_command(label="Go to", command=myFunc)
editMenu.add_separator()
editMenu.add_command(label="Select all", command=myFunc)
editMenu.add_command(label="Time/Date", command=myFunc)
editMenu.add_separator()
editMenu.add_command(label="Font", command=myFunc)

mainmenu.add_cascade(menu=editMenu,label='Edit')

# view menu

viewMenu = Menu(mainmenu,tearoff=0)

viewMenu.add_command(label='Zoom',command=myFunc)
viewMenu.add_command(label='Status Bar',command=myFunc)
viewMenu.add_command(label='Word wrap',command=myFunc)

mainmenu.add_cascade(menu=viewMenu,label="View")

# help menu

helpMenu = Menu(mainmenu,tearoff=0)

helpMenu.add_command(label='About', command=about)
helpMenu.add_command(label='Rate us', command=help)
helpMenu.add_command(label='Message', command=msg)

mainmenu.add_cascade(label='Help',menu=helpMenu)

root.config(menu=mainmenu)
# root.configure(background='lavender')
root.mainloop()