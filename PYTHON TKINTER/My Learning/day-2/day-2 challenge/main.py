from tkinter import *
from PIL import Image, ImageTk
import os

Dipesh = Tk()
Dipesh.title('Photos Album')
Dipesh.geometry('1240x2050')

frameTitle = Label(text='Photo Album')
frameTitle.pack()
'''trying single file'''


image_found = False

for root,dirs,files in os.walk("./images/"):
    for file1 in files:
        if file1.endswith(".png"):
            image_found = True
            # Concatenating directory path with the file name to get the full path
            full_file_path = os.path.join(root, file1)
            # print(f"Full file path: {full_file_path}")
            photo = PhotoImage(file=full_file_path)
            label = Label(image=photo)
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack()
             
                
        if file1.endswith('.jpg'):
            image_found = True
            checking_File_path = os.path.join(root, file1)
            # print(f"checking_File_path: {checking_File_path}")
            photo = ImageTk.PhotoImage(file=checking_File_path)
            label = Label(image=photo)
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack()
        
if not image_found:
    print("No PNG/JPG images found in the folder.")
    label = Label(text='No Images in the folder')
    label.pack()              
    
       
        
            

Dipesh.mainloop()