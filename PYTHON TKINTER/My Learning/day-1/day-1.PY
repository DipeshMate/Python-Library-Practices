'''WxPython, Kivy, PyQT, PyGTK, Pyjs and GTK+ are the most popular python libraries/frameworks
which are used to create the python GUI programs.'''

#import tkinter as tk
from tkinter import *

# create Root
root = Tk()

'''GUI LOGIC HERE'''

# window methods

root.title('Just a Demo')
root.geometry('600x600')
root.minsize('200','200')

text = Label(text='just a demo')
text.pack()

root.mainloop() #to run GUI window

