from tkinter import *
from tkinter import messagebox
from functools import partial
from GameData import *

#Window Configuration
root = Tk()
root.title("JP Scrabble")
root.resizable(False,False)

prevX,prevY = -1,-1

#Function that runs when a textbox(button) is selected.
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

#Function when key is pressed after the button is selected.
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
    if(event.char is '1'):
        boardSetup(0,prevX,prevY,textbox[prevY][prevX].letter)
    if(event.char is '2'):
        if(textbox[prevY][prevX].color == 2):
            boardSetup(1,prevX,prevY,textbox[prevY][prevX].letter)
        else:
            boardSetup(2,prevX,prevY,textbox[prevY][prevX].letter)
    if(event.char is '3'):
        if(textbox[prevY][prevX].color == 4):
            boardSetup(3,prevX,prevY,textbox[prevY][prevX].letter)
        else:
            boardSetup(4,prevX,prevY,textbox[prevY][prevX].letter)

#15x15 Game board backend
def boardSetup(num,x,y,char):
    if(num == 0):
        textbox[y][x].config(bg="green",text="",relief=FLAT,activebackground="green")
        textbox[y][x].color = 0
    if(num == 1):
        textbox[y][x].config(bg="light blue",fg="black",activeforeground="black",text="2L",relief=FLAT,activebackground="light blue")
        textbox[y][x].color = 1
    if(num == 2):
        textbox[y][x].config(bg="pink",fg="black",activeforeground="black",text="2W",relief=FLAT,activebackground="pink")
        textbox[y][x].color = 2
    if(num == 3):
        textbox[y][x].config(bg="blue",fg="white",activeforeground="white",text="3L",relief=FLAT,activebackground="blue")
        textbox[y][x].color = 3
    if(num == 4):
        textbox[y][x].config(bg="red",fg="white",activeforeground="white",text="3W",relief=FLAT,activebackground="red")
        textbox[y][x].color = 4
    if(char.isalpha()):
        textbox[prevY][prevX].config(bg="beige",fg="black",activeforeground="black",text=char.upper(),relief=FLAT,activebackground="beige")
        textbox[prevY][prevX].letter = char.upper()
    else:
        textbox[prevY][prevX].letter = ''

#Letter Board
def displayCurrentLetters():
    givenLetters = Text(root, width=11, height=1, borderwidth=0,background=root.cget("background"),font=("Courier",25))
    givenLetters.tag_configure("subscript", offset=-4,font=("Courier",13))
    for i in range(len(currentLetters)):
        givenLetters.insert("insert", currentLetters[i],"", "1", "subscript")
    givenLetters.configure(state="disabled")
    givenLetters.grid(row = 16,column=0,columnspan=15)

#Saving the game data to GameData.py when closing the program.
def windowClose():
    if messagebox.askokcancel("Exit?", "Exit?"):
        boardColor = list()
        boardLetter = list()
        for i in range(len(textbox)):
            for j in range(len(textbox[i])):
                boardColor.append(textbox[i][j].color)
                boardLetter.append(textbox[i][j].letter)
                f = open("GameData.py","w")
        f.write("boardColor = "+str(boardColor)+"\n")
        f.write("boardLetter = "+str(boardLetter)+"\n")
        f.write("currentLetters = "+str(currentLetters)+"\n")
        root.destroy()

#15x15 Board Frontend
textbox = list(list())
for j in range(15):
    textbox.append([])
    for i in range(15):
        textbox[j].append(Button(root,width=1,height=1,bg="green",highlightbackground="black",
borderwidth=0,activebackground="green",command=partial(buttonSelect,i,j)))
        boardSetup(boardColor[i+15*j],i,j,boardLetter[i+15*j])
        textbox[j][-1].grid(row=j,column=i)

#Score board
ScorePlayer1 = Label(root,text="Player 1: 0",width=15,font=("Courier",11))
ScorePlayer1.grid(row = 0,column=16)
ScorePlayer2 = Label(root,text="Player 2: 0",width=15,font=("Courier",11))
ScorePlayer2.grid(row = 1,column=16)

#Letter board
displayCurrentLetters()




root.protocol("WM_DELETE_WINDOW",windowClose)
root.mainloop()

