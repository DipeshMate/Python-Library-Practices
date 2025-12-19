from tkinter import *
from  PIL import Image,ImageTk
import os

def every_100(text):
    finalText = ""
    for i in range(0,len(text)):
        finalText +=text[i]
        if i%80==0 and i!=0:
            finalText += "\n"
    return finalText;        


Challenge = Tk()
Challenge.geometry('1000x800')
Challenge.title('NewsPaper Challenge- News Aap Tak')

texts=[]
photos=[]



for root,dirs,files in os.walk("/files/"):
    print('first loop')
    for file1 in range(0,3):
        print('second loop')
        with open(f"{file1+1}.txt") as f:
            text = f.read()
            texts.append(every_100(text))    
        print(texts)
for root,dirs,files in os.walk("./d-3 challenge/"):
   for file1 in files:
        if file1.endswith(".png"):
            image = PhotoImage(file=f"{file1+1}.png")
            image = image.resize((220,235),Image.A)
            photos.append(image)       
    
f0= Frame(Challenge,width=800,height=70)
headLine = Label(f0,text='The Times Of India',padx=20,pady=10,fg='black',bg='OliveDrab1',relief='groove',font='Times 25 bold italic').pack(pady=20)
date = Label(f0,text='Oct 16 2052',padx=8,pady=5,fg='black',font='lucida 13 bold italic').pack()

f1= Frame(Challenge,width=900,height=300,bg='powder blue')
# Label(f1,text = texts[0], padx=22,pady=22).pack(side=LEFT)
# Label(f1,image=photos[0]).pack()

f0.pack()        
f1.pack(anchor="w")
Challenge = mainloop()