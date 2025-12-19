from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry('600x1400')
test = Label(text='Hello World')
test.pack()

# for png images

photo = PhotoImage(file='iii.png')
checkPhoto = Label(image=photo)
checkPhoto.pack()

# for jpg images

jpgimage = Image.open("33.jpg")
checkJpgImage = ImageTk.PhotoImage(jpgimage)
adding2Label = Label(image=checkJpgImage)
adding2Label.pack()


root.mainloop()