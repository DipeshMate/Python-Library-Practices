from tkinter import *
root = Tk()

root.geometry('900x450')
root.title('Day-3 Prac')

'''-------------label & packs attributes-------'''
# relief(border-styling) = SUNKEN, RAISED, GROOVE, RIDGE
# font = "Helvetica 9","comicsansms","Times 15 bold italic"

test = Label(text='''Ratan Naval Tata[pronunciation?] (28 December 1937 – 9 October 2024) was an Indian industrialist and philanthropist 
             \n who was chairman of Tata Group and Tata Sons from 1991 to 2012, and interim chairman from October 2016 through 
             \nFebruary 2017.[2][3] In 2008, he received the Padma Vibhushan, the second highest civilian honour in India. 
             \nRatan had previously received the Padma Bhushan, the third highest civilian honour, in 2000.[4]\n
             ''',bg='cyan',fg='black',font="Helvetica 8 bold",padx=70,pady=40,relief=RAISED, borderwidth=6)

# anchor = "nw(north-west)" , side = top, fill=X/Y, padx, pady
test.pack(side='bottom', anchor='sw',padx=30, pady=30)

root.mainloop()