from tkinter import *
from tkinter import messagebox
from functools import partial
from GameData import *

#Window Configuration
root = Tk()
root.title("JP Scrabble")
root.resizable(False,False)

prevX,prevY = -1,-1
letterScores = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]

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
    global prevY,prevX,usedLetters
    if(event.char.isalpha() and event.char.upper() in currentLetters):
        currentLetters.remove(event.char.upper())
        usedLetters.append(event.char.upper())
        if(textbox[prevY][prevX].letter is not ''):
            currentLetters.append(textbox[prevY][prevX].letter)
            usedLetters.remove(textbox[prevY][prevX].letter)
            boardSetup(textbox[prevY][prevX].color,prevX,prevY,'')
        displayCurrentLetters()
        displayCurrentScores(prevX,prevY)
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
        if(textbox[prevY][prevX].letter is not ''):
            currentLetters.append(textbox[prevY][prevX].letter)
            usedLetters.remove(textbox[prevY][prevX].letter)
            displayCurrentLetters()
            displayCurrentScores(prevX,prevY)
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

#Letter Board Updating Function
def displayCurrentLetters():
    givenLetters = Text(root, width=11, height=1, borderwidth=0,background=root.cget("background"),font=("Courier",25))
    givenLetters.tag_configure("subscript", offset=-4,font=("Courier",13))
    for i in range(len(currentLetters)):
        givenLetters.insert("insert", currentLetters[i],"", letterScores[ord(currentLetters[i])-65], "subscript")
    givenLetters.configure(state="disabled")
    givenLetters.grid(row = 17,column=0,columnspan=15)

#Score board Updating Function
def displayCurrentScores(prevX,prevY):
    global ScorePlayer1,ScorePlayer2,player1Turn,player2Turn
    if(player1Turn is 1):
        ScorePlayer1 = 0
        for i in range(len(usedLetters)):
            ScorePlayer1 += letterScores[ord(usedLetters[i])-65]
    elif(player2Turn is 1):
        ScorePlayer2 = 0
        for i in range(len(usedLetters)):
            ScorePlayer2 += letterScores[ord(usedLetters[i])-65]
    Player1Label = Label(root,text="Player 1: "+str(ScorePlayer1),width=15,font=("Courier",11))
    Player1Label.grid(row = 1,column=0,columnspan=7)
    Player2Label = Label(root,text="Player 2: "+str(ScorePlayer2),width=15,font=("Courier",11))
    Player2Label.grid(row = 1,column=7,columnspan=8)


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
        f.write("usedLetters = "+str(usedLetters)+"\n")
        f.write("ScorePlayer1 = "+str(ScorePlayer1)+"\n")
        f.write("ScorePlayer2 = "+str(ScorePlayer2)+"\n")
        f.write("player1Turn = "+str(player1Turn)+"\n")
        f.write("player2Turn = "+str(player2Turn)+"\n")
        root.destroy()

#15x15 Board Interface 
titleLabel = Label(root,text="Scrabble",width=15,font=("Courier",11))
titleLabel.grid(row = 0,column=0,columnspan=15)
textbox = list(list())
for j in range(15):
    textbox.append([])
    for i in range(15):
        textbox[j].append(Button(root,width=1,height=1,bg="green",highlightbackground="black",
borderwidth=0,activebackground="green",command=partial(buttonSelect,i,j)))
        boardSetup(boardColor[i+15*j],i,j,boardLetter[i+15*j])
        textbox[j][-1].grid(row=j+2,column=i)


#Letter board
displayCurrentLetters()
displayCurrentScores(-1,-1)



root.protocol("WM_DELETE_WINDOW",windowClose)
root.mainloop()

