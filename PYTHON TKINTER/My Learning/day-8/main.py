'''---------Form making using checkbox-----------'''


from tkinter import *

root = Tk()
root.geometry('450x300')
root.title('Student Form')

# Form Title
title = Label(root, text='The Student Details', font='Helvetica 12 bold italic', relief=RAISED, padx=15,pady=6).grid(pady=12,column=1,padx=8)

#creating Form of student details and packing
Label(root, text='Name: ').grid(row=1,column=0)
Label(root, text='Class: ').grid(row=2,column=0)
Label(root, text='Gender: ').grid(row=3,column=0)
Label(root, text='Contact: ').grid(row=4,column=0)

# Tkinter variable for storing entries
name = StringVar()
classes = StringVar()
gender = StringVar()
contact = StringVar()
checkStudent = BooleanVar()

# use Entry() for inputs

nameValue = Entry(root,textvariable=name).grid(row=1,column=1)
classValue = Entry(root,textvariable=classes).grid(row=2,column=1)
genderValue = Entry(root,textvariable=gender).grid(row=3,column=1)
contactValue = Entry(root,textvariable=contact).grid(row=4,column=1)

# creating checkbox for student check
checkValue = Checkbutton(root,text='is Student is of our college..!!?',variable=checkStudent).grid(row=5,column=1)

def checking():
    print(f"{name.get(), classes.get(), gender.get(), contact.get(),checkStudent.get()} \n")
    with open('studentRecords.txt','a') as f: 
        f.write(f"{name.get(), classes.get(), gender.get(), contact.get(),checkStudent.get()} \n")
        
# submit button
Button(root,text='Submit', command = checking).grid(row=6,column=1)

root.mainloop()