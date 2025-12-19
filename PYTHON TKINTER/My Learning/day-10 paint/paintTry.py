from tkinter import *

root=Tk()
root.geometry('480x700')
root.title('Paint Prac')

def doubleClick(event):
    print(f'Pressed double Click on {event.x} & {event.y}')

def singleClick(event):
    print(f'Pressed single Click on {event.x} & {event.y}')


w = Canvas(root, width = 400, height = 400, bd=2, cursor='circle',relief=GROOVE) 

def paint(event):
    
    # for co-ordinates:
    (x1,y1,x2,y2) = (event.x-5), (event.y-5), (event.x+5),(event.y+5)
    
    # Color
    colour = 'DeepSkyBlue2'
    
    w.create_line(x1,y1,x2,y2,fill=colour)
    

# Display Button or label
w4 = Button(root,text='Double Click and Drag to Draw').pack(padx=20,pady=25)
w5 = Button(root,text='Exit')


# binding for paint
w.bind('<B1-Motion>', paint)
w5.bind('<Button-1>', exit)

w.pack()
w5.pack(padx=20,pady=25)
root.mainloop()