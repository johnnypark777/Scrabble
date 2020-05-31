from tkinter import *
from tkinter import messagebox
from random import randint
from functools import partial
import json

selectedX,selectedY = -1,-1
#Importing Saved JSON Data
letterScores = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
letterDistribution = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]
savedData = json.load(open("gameData.json","r"))
boardColor = savedData['boardColor']
boardLetter = savedData['boardLetter']
player1Tiles = savedData['player1Tiles']
player2Tiles = savedData['player2Tiles']
usedLetters = savedData['usedLetters']
scorePlayer1 = savedData['scorePlayer1']
scorePlayer2 = savedData['scorePlayer2']
player1Turn = savedData['player1Turn']
player2Turn = savedData['player2Turn']


#Window Configuration
root = Tk()
root.title("Scrabble")
root.resizable(False,False)


#Function that runs when a textbox(button) is selected.
def buttonSelect(i,j):
    global selectedX,selectedY
    if (selectedX != -1):
        textbox[selectedY][selectedX].config(highlightbackground="black",relief=FLAT)
        textbox[selectedY][selectedX].unbind('<Button-1>')
    selectedX,selectedY = i,j
    textbox[j][i].focus_set()
    textbox[j][i].config(highlightcolor="white")
    textbox[j][i].bind('<Button-1>', lambda e: 'break')
    textbox[j][i].bind("<Key>",keyChar)

#Function when key is pressed after the button is selected.
def keyChar(event):
    global selectedY,selectedX,usedLetter,player1Turn,player2Turn,player1Tiles,player2Tiles
    if(player1Turn is 1):
        if(event.char.isalpha() and event.char.upper() in player1Tiles):
            newLetter = {}
            newLetter['letter'] = event.char.upper()
            newLetter['multiplier'] = textbox[selectedY][selectedX].color
            newLetter['score'] = letterScores[ord(event.char.upper())-65]
            newLetter['xCord'] = selectedX
            newLetter['yCord'] = selectedY
            player1Tiles.remove(event.char.upper())
            usedLetters.append(newLetter)
            if(textbox[selectedY][selectedX].letter is not ''):
                player1Tiles.append(textbox[selectedY][selectedX].letter)
                usedLetters[:] = [d for d in usedLetters if d.get('letter') != textbox[selectedY][selectedX].letter]
                setTileDisplay(textbox[selectedY][selectedX].color,selectedX,selectedY,'')
            displayUpdate(selectedX,selectedY)
            setTileDisplay(-1,selectedX,selectedY,event.char)
            if(selectedX < 14):
                buttonSelect(selectedX+1,selectedY)
    if(player2Turn is 1):
        if(event.char.isalpha() and event.char.upper() in player2Tiles):
            newLetter = {}
            newLetter['letter'] = event.char.upper()
            newLetter['multiplier'] = textbox[selectedY][selectedX].color
            newLetter['score'] = letterScores[ord(event.char.upper())-65]
            newLetter['xCord'] = selectedX
            newLetter['yCord'] = selectedY
            player2Tiles.remove(event.char.upper())
            usedLetters.append(newLetter)
            if(textbox[selectedY][selectedX].letter is not ''):
                player2Tiles.append(textbox[selectedY][selectedX].letter)
                usedLetters[:] = [d for d in usedLetters if d.get('letter') != textbox[selectedY][selectedX].letter]
                setTileDisplay(textbox[selectedY][selectedX].color,selectedX,selectedY,'')
            displayUpdate(selectedX,selectedY)
            setTileDisplay(-1,selectedX,selectedY,event.char)
            if(selectedX < 14):
                buttonSelect(selectedX+1,selectedY)
    if(event.keysym=="Up" and selectedY != 0):
        buttonSelect(selectedX,selectedY-1)
    if(event.keysym=="Down" and selectedY != 14):
        buttonSelect(selectedX,selectedY+1)
    if(event.keysym=="Left" and selectedX != 0):
        buttonSelect(selectedX-1,selectedY)
    if(event.keysym=="Right" and selectedX != 14):
        buttonSelect(selectedX+1,selectedY)
    if(event.keysym=="BackSpace"):
        if(textbox[selectedY][selectedX].letter is not ''):
            #TODO
            #if any(usedLetters['xCord'] == selectedX)
            if(player1Turn is 1):
                player1Tiles.append(textbox[selectedY][selectedX].letter)
                usedLetters[:] = [d for d in usedLetters if d.get('letter') != textbox[selectedY][selectedX].letter]
                displayUpdate(selectedX,selectedY)
                setTileDisplay(textbox[selectedY][selectedX].color,selectedX,selectedY,'')
            if(player2Turn is 1):
                player2Tiles.append(textbox[selectedY][selectedX].letter)
                usedLetters[:] = [d for d in usedLetters if d.get('letter') != textbox[selectedY][selectedX].letter]
                displayUpdate(selectedX,selectedY)
                setTileDisplay(textbox[selectedY][selectedX].color,selectedX,selectedY,'')
        if(selectedX!=0):
            buttonSelect(selectedX-1,selectedY)
    if(event.char is '1'):
        setTileDisplay(0,selectedX,selectedY,textbox[selectedY][selectedX].letter)
    if(event.char is '2'):
        if(textbox[selectedY][selectedX].color == 2):
            setTileDisplay(1,selectedX,selectedY,textbox[selectedY][selectedX].letter)
        else:
            setTileDisplay(2,selectedX,selectedY,textbox[selectedY][selectedX].letter)
    if(event.char is '3'):
        if(textbox[selectedY][selectedX].color == 4):
            setTileDisplay(3,selectedX,selectedY,textbox[selectedY][selectedX].letter)
        else:
            setTileDisplay(4,selectedX,selectedY,textbox[selectedY][selectedX].letter)

#15x15 Game board backend
def setTileDisplay(num,x,y,char):
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
        textbox[selectedY][selectedX].config(bg="beige",fg="black",activeforeground="black",text=char.upper(),relief=FLAT,activebackground="beige")
        textbox[selectedY][selectedX].letter = char.upper()
    else:
        textbox[selectedY][selectedX].letter = ''

#Updating the tiles and the scores
currentPlayerTempScore = 0
def displayUpdate(selectedX,selectedY):
    global scorePlayer1,scorePlayer2,player1Turn,player2Turn,player1Tiles,player2Tiles,currentPlayerTempScore
    currentPlayerTempScore = 0
    givenLetters = Text(root, width=12, height=1, borderwidth=0,background=root.cget("background"),font=("Courier",25))
    givenLetters.tag_configure("subscript", offset=-4,font=("Courier",13))
    if(player1Turn is 1):
        for i in range(len(player1Tiles)):
            givenLetters.insert("insert", player1Tiles[i],"", letterScores[ord(player1Tiles[i])-65], "subscript")
        givenLetters.configure(state="disabled")
        givenLetters.grid(row = 18,column=0,columnspan=15)
    if(player2Turn is 1):
        for i in range(len(player2Tiles)):
            givenLetters.insert("insert", player2Tiles[i],"", letterScores[ord(player2Tiles[i])-65], "subscript")
        givenLetters.configure(state="disabled")
        givenLetters.grid(row = 18,column=0,columnspan=15)

    #Calculating current score (before passing the turn)
    multiple = 1
    for i in range(len(usedLetters)):
        if(usedLetters[i]['multiplier'] == 0):
            currentPlayerTempScore += usedLetters[i]['score']
        elif(usedLetters[i]['multiplier'] == 1):
            currentPlayerTempScore += usedLetters[i]['score']*2
        elif(usedLetters[i]['multiplier'] == 2):
            multiple *= 2
            currentPlayerTempScore += usedLetters[i]['score']
        elif(usedLetters[i]['multiplier'] == 3):
            currentPlayerTempScore += usedLetters[i]['score']*3
        elif(usedLetters[i]['multiplier'] == 4):
            multiple *= 3
            currentPlayerTempScore += usedLetters[i]['score']
    currentPlayerTempScore *= multiple
    if(len(usedLetters) is 7):
        currentPlayerTempScore += 50
    if(player1Turn is 1):
        Player1Label = Label(root,text="Player 1: "+str(currentPlayerTempScore+scorePlayer1),width=15,font=("Courier",11))
        Player1Label.grid(row = 1,column=0,columnspan=7)
    elif(player2Turn is 1):
        Player2Label = Label(root,text="Player 2: "+str(currentPlayerTempScore+scorePlayer2),width=15,font=("Courier",11))
        Player2Label.grid(row = 1,column=7,columnspan=8)

    if(len(usedLetters) is 0):#Subject to change as more conditions(valid letter,valid placing) are going to be applied to pass the turn
        confirmButton.grid_remove()
    else:
        confirmButton.grid()

def turnPassed():
    global player1Turn,player2Turn,currentPlayerTempScore,scorePlayer1,scorePlayer2
    player1Turn,player2Turn = player2Turn,player1Turn
    print(currentPlayerTempScore)
    if(player1Turn is 1):
        scorePlayer2 += currentPlayerTempScore
        currentPlayer = Label(root,text="Current Turn: Player 1",font=("Courier",11))
        while len(player2Tiles) < 7:
            player2Tiles.append(chr(randint(0,25)+65))
    else:
        scorePlayer1 += currentPlayerTempScore
        currentPlayer = Label(root,text="Current Turn: Player 2",font=("Courier",11))
        while len(player1Tiles) < 7:
            player1Tiles.append(chr(randint(0,25)+65))
    currentPlayer.grid(row = 2,column=0,columnspan=15)
    usedLetters.clear()
    currentPlayerTempScore = 0
    displayUpdate(-1,-1)

#Saving the game data to gameData.json when closing the program.
def windowClose():
    if messagebox.askokcancel("Exit?", "Exit?"):
        boardColor = list()
        boardLetter = list()
        for i in range(len(textbox)):
            for j in range(len(textbox[i])):
                boardColor.append(textbox[i][j].color)
                boardLetter.append(textbox[i][j].letter)
        savedData = {}
        savedData['boardColor']     = boardColor
        savedData['boardLetter']    = boardLetter
        savedData['usedLetters']    = usedLetters
        savedData['scorePlayer1']   = scorePlayer1
        savedData['scorePlayer2']   = scorePlayer2
        savedData['player1Tiles']   = player1Tiles
        savedData['player2Tiles']   = player2Tiles
        savedData['player1Turn']    = player1Turn
        savedData['player2Turn']    = player2Turn
        jsonLetterList = json.dump(savedData,open("gameData.json","w"),indent=2,ensure_ascii=True,sort_keys=True)
        root.destroy()

#15x15 Board Interface 
titleLabel = Label(root,text="Scrabble",width=15,font=("Courier",11))
titleLabel.grid(row = 0,column=0,columnspan=15)
confirmButton = Button(root,text="Confirm",command=partial(turnPassed))
confirmButton.grid(row = 19, column=0, columnspan=15)
Player1Label = Label(root,text="Player 1: "+str(scorePlayer1),width=15,font=("Courier",11))
Player1Label.grid(row = 1,column=0,columnspan=7)
Player2Label = Label(root,text="Player 2: "+str(scorePlayer2),width=15,font=("Courier",11))
Player2Label.grid(row = 1,column=7,columnspan=8)
if(player1Turn is 1):
    currentPlayer = Label(root,text="Current Turn: Player 1",font=("Courier",11))
    currentPlayer.grid(row = 2,column=0,columnspan=15)
else:
    currentPlayer = Label(root,text="Current Turn: Player 2",font=("Courier",11))
    currentPlayer.grid(row = 2,column=0,columnspan=15)

textbox = list(list())
for j in range(15):
    textbox.append([])
    for i in range(15):
        textbox[j].append(Button(root,width=1,height=1,bg="green",highlightbackground="black",
borderwidth=0,activebackground="green",command=partial(buttonSelect,i,j)))
        setTileDisplay(boardColor[i+15*j],i,j,boardLetter[i+15*j])
        textbox[j][-1].grid(row=j+3,column=i)

#Set Letter and Score board
if not usedLetters:
    while len(player1Tiles) < 7:
        player1Tiles.append(chr(randint(0,25)+65))
    while len(player2Tiles) < 7:
        player2Tiles.append(chr(randint(0,25)+65))
displayUpdate(selectedX,selectedY)


root.protocol("WM_DELETE_WINDOW",windowClose)
root.mainloop()

