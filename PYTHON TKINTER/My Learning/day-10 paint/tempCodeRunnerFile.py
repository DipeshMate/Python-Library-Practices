from tkinter import *

root=Tk()
root.geometry('380x280')
root.title('Paint Prac')

def doubleClick(event):
    print(f'Pressed double Click on {event.x} & {event.y}')

def singleClick(event):
    print(f'Pressed single Click on {event.x} & {event.y}')


w = Canvas(root, width = 400, height = 250) 


def paint(event):
    
    # for co-ordinates:
    (x1,y1,x2,y2) = {{event.x1-3}, {event.y1-3}, {event.x2+3},{event.y2+3}}
    