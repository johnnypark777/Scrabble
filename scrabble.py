from tkinter import *
from functools import partial

#Window Configuration
root = Tk()
root.title("JP Scrabble")
root.resizable(False,False)

prevX,prevY = -1,-1
def buttonSelect(i,j):
    global prevX,prevY
    if (prevX != -1):
        textbox[prevY][prevX].config(highlightbackground="black",relief=FLAT)
        textbox[prevY][prevX].unbind('<Button-1>')
    prevX,prevY = i,j
    textbox[j][i].focus_set()
    textbox[j][i].config(highlightcolor="white")
    textbox[j][i].bind('<Button-1>', lambda e: 'break')
    textbox[j][i].bind("<Key>",keyChar)
    textbox[j][i].bind("1",keyOne)
    textbox[j][i].bind("2",keyTwo)
    textbox[j][i].bind("3",keyThree)

def keyChar(event):
    global prevY,prevX
    if(event.char.isalpha()):
        textbox[prevY][prevX].config(bg="beige",fg="black",activeforeground="black",text=event.char.upper(),relief=FLAT,activebackground="beige")
        if(prevX < 14):
            buttonSelect(prevX+1,prevY)
    if(event.keysym=="Up" and prevY != 0):
        buttonSelect(prevX,prevY-1)
    if(event.keysym=="Down" and prevY != 14):
        buttonSelect(prevX,prevY+1)
    if(event.keysym=="Left" and prevX != 0):
        buttonSelect(prevX-1,prevY)
    if(event.keysym=="Right" and prevX != 14):
        buttonSelect(prevX+1,prevY)
    if(event.keysym=="BackSpace"):
        if(textbox[prevY][prevX].color == 0):
            textbox[prevY][prevX].config(bg="green",text="",relief=FLAT,activebackground="green")
        if(textbox[prevY][prevX].color == 1):
            textbox[prevY][prevX].config(bg="light blue",fg="black",activeforeground="black",text="2L",relief=FLAT,activebackground="light blue")
        if(textbox[prevY][prevX].color == 2):
            textbox[prevY][prevX].config(bg="pink",fg="black",activeforeground="black",text="2W",relief=FLAT,activebackground="pink")
        if(textbox[prevY][prevX].color == 3):
            textbox[prevY][prevX].config(bg="blue",fg="white",activeforeground="white",text="3L",relief=FLAT,activebackground="blue")
        if(textbox[prevY][prevX].color == 4):
            textbox[prevY][prevX].config(bg="red",fg="white",activeforeground="white",text="3W",relief=FLAT,activebackground="red")
        if(prevX!=0):
            buttonSelect(prevX-1,prevY)

def keyOne(event):
    global prevX,prevY
    textbox[prevY][prevX].config(bg="green",text="",fg="black",activeforeground="black",relief=FLAT,activebackground="green")
    textbox[prevY][prevX].color = 0
def keyTwo(event):
    global prevX,prevY
    if(textbox[prevY][prevX].color == 2):
        textbox[prevY][prevX].config(bg="light blue",fg="black",activeforeground="black",text="2L",relief=FLAT,activebackground="light blue")
        textbox[prevY][prevX].color=1
    else:
        textbox[prevY][prevX].config(bg="pink",fg="black",activeforeground="black",text="2W",relief=FLAT,activebackground="pink")
        textbox[prevY][prevX].color=2
def keyThree(event):
    global prevX,prevY
    if(textbox[prevY][prevX].color == 4):
        textbox[prevY][prevX].config(bg="blue",fg="white",activeforeground="white",text="3L",relief=FLAT,activebackground="blue")
        textbox[prevY][prevX].color=3
    else:
        textbox[prevY][prevX].config(bg="red",fg="white",activeforeground="white",text="3W",relief=FLAT,activebackground="red")
        textbox[prevY][prevX].color=4

#15x15 Textbox
textbox = list(list())
for j in range(15):
    textbox.append([])
    for i in range(15):
        textbox[j].append(Button(root,width=1,height=1,bg="green",highlightbackground="black",
borderwidth=0,activebackground="green",command=partial(buttonSelect,i,j)))
        textbox[j][i].color = 0
        textbox[j][-1].grid(row=j,column=i)


root.mainloop()

