from tkinter import *
from tkinter import messagebox
from functools import partial
from GameData import *

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
        boardSetup(-1,prevX,prevY,event.char)
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
        boardSetup(textbox[prevY][prevX].color,prevX,prevY,'')
        if(prevX!=0):
            buttonSelect(prevX-1,prevY)

def boardSetup(num,x,y,char):
    if(num == 0):
        textbox[y][x].config(bg="green",text="",relief=FLAT,activebackground="green")
    if(num == 1):
        textbox[y][x].config(bg="light blue",fg="black",activeforeground="black",text="2L",relief=FLAT,activebackground="light blue")
    if(num == 2):
        textbox[y][x].config(bg="pink",fg="black",activeforeground="black",text="2W",relief=FLAT,activebackground="pink")
    if(num == 3):
        textbox[y][x].config(bg="blue",fg="white",activeforeground="white",text="3L",relief=FLAT,activebackground="blue")
    if(num == 4):
        textbox[y][x].config(bg="red",fg="white",activeforeground="white",text="3W",relief=FLAT,activebackground="red")
    if(char.isalpha()):
        textbox[prevY][prevX].config(bg="beige",fg="black",activeforeground="black",text=char.upper(),relief=FLAT,activebackground="beige")
        textbox[prevY][prevX].letter = char.upper()
    else:
        textbox[prevY][prevX].letter = ''

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

def windowClose():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        boardColor = list()
        boardLetter = list()
        for i in range(len(textbox)):
            for j in range(len(textbox[i])):
                boardColor.append(textbox[i][j].color)
                boardLetter.append(textbox[i][j].letter)
                f = open("GameData.py","w")
                f.write("boardColor = "+str(boardColor)+"\n")
                f.write("boardLetter = "+str(boardLetter)+"\n")
        root.destroy()
#15x15 Textbox
textbox = list(list())
for j in range(15):
    textbox.append([])
    for i in range(15):
        textbox[j].append(Button(root,width=1,height=1,bg="green",highlightbackground="black",
borderwidth=0,activebackground="green",command=partial(buttonSelect,i,j)))
        textbox[j][i].color = boardColor[i+15*j]
        textbox[j][i].letter = ''
        boardSetup(boardColor[i+15*j],i,j,boardLetter[i+15*j])
        textbox[j][-1].grid(row=j,column=i)



root.protocol("WM_DELETE_WINDOW",windowClose)
root.mainloop()

