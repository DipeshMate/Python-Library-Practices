'''----------Events and Binds in Tkinker------'''

# widget.bind(event, handler)

'''
In Tkinter, events are represented as strings with a specific format. Here's a breakdown of the format and some common examples:
Format:

--><modifier-type-detail>
Modifier: Optional, indicates special keys like Shift, Control, Alt, etc. (e.g., <Shift-Button-1>)
Type: The type of event (e.g., Button, Key, Motion)
Detail: Additional information about the event (e.g., 1 for left mouse button, Return for Enter key)
Common Examples:

-->Mouse Events:
<Button-1>: Left mouse button click
<Button-2>: Middle mouse button click
<Button-3>: Right mouse button click
<Double-Button-1>: Double-click with left mouse button
<B1-Motion>: Mouse movement with left button held down
<Enter>: Mouse enters a widget
<Leave>: Mouse leaves a widget

-->Keyboard Events:
<Key>: Any key press
<Return>: Enter key press
<Escape>: Escape key press
<Up>: Up arrow key press
<Down>: Down arrow key press
<Left>: Left arrow key press
<Right>: Right arrow key press

-->Window Events:
<Configure>: Window resized or moved
<FocusIn>: Widget gains focus
<FocusOut>: Widget loses focus
'''


from tkinter import *

root=Tk()
root.geometry('480x700')
root.title('Paint')

def doubleClick(event):
    print(f'Pressed double Click on {event.x} & {event.y}')

def singleClick(event):
    print(f'Pressed single Click on {event.x} & {event.y}')
    
w1 = Button(root,text='Press Double Click')
w2 = Button(root,text='Press Single Click')
w3 = Button(root,text='Exit')

w1.bind('<Double-Button-1>',doubleClick)
w2.bind('<Button-1>',singleClick)
w3.bind('<Button-1>', quit)

w1.pack(padx=8,pady=4)
w2.pack(padx=8,pady=4)
w3.pack(padx=8,pady=4)

root.mainloop()