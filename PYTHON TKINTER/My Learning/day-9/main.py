'''---------------introdue new widget: - Canvas----------------'''

from tkinter import *

root = Tk()

canvas_height= 400
canvas_width = 600
root.title('canvas widget Intro')
root.geometry(f'{canvas_width}x{canvas_height}')

# introduce new Canvas widget

canva_widget =  Canvas(root,height=canvas_height,width=canvas_width,bg='yellow',highlightcolor='green',cursor='arrow')


line_1 = canva_widget.create_line(0,40,80,0,fill='red')
line_2 = canva_widget.create_line(0,0,80,40,fill='blue')

arc = canva_widget.create_arc(180, 150, 80,
                   210, start=0,
                   extent=220,
                   fill="red")

oval = canva_widget.create_oval(80, 30, 140,
                     150,
                     fill="blue")

canva_widget.pack()
root.mainloop()