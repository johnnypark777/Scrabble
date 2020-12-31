from tkinter import *
from tkinter import messagebox
from random import randint
from functools import partial
import json

# Why does it crash when selectedX 7, selectedY 7
selectedX, selectedY = -1, -1

# Importing Saved JSON Data
letterScores = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
savedData = json.load(open("gameData.json", "r"))
if not 'letterDistribution' in savedData:
    letterDistribution = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
else:
    letterDistribution = savedData['letterDistribution']
boardColor = savedData['boardColor']
boardLetter = savedData['boardLetter']
player1Tiles = savedData['player1Tiles']
player2Tiles = savedData['player2Tiles']
usedLetters = savedData['usedLetters']
scorePlayer1 = savedData['scorePlayer1']
scorePlayer2 = savedData['scorePlayer2']
player1Turn = savedData['player1Turn']
player2Turn = savedData['player2Turn']

# Window Configuration
root = Tk()
root.title("Scrabble")
root.resizable(False, False)


# Function that runs when a textbox(button) is selected.
def buttonSelect(i, j):
    global selectedX, selectedY
    if selectedX != -1:
        textbox[selectedY][selectedX].config(highlightbackground="black", relief=FLAT)
        textbox[selectedY][selectedX].unbind('<Button-1>')
    selectedX, selectedY = i, j
    textbox[j][i].focus_set()
    textbox[j][i].config(highlightcolor="white")
    textbox[j][i].bind('<Button-1>', lambda e: 'break')
    textbox[j][i].bind("<Key>", keyChar)


# Function when key is pressed after the button is selected.
def keyChar(event):
    global selectedY, selectedX, usedLetter, player1Turn, player2Turn, player1Tiles, player2Tiles
    if event.char.isalpha():
        newLetter = {}
        newLetter['letter'] = event.char.upper()
        newLetter['multiplier'] = textbox[selectedY][selectedX].color
        newLetter['score'] = letterScores[ord(event.char.upper()) - 65]
        newLetter['xCord'] = selectedX
        newLetter['yCord'] = selectedY
        ##Checking if you are allowed to replace this specific letter in the first place
        if (textbox[selectedY][selectedX].letter is not ''):
            if not (any(d['xCord'] is selectedX for d in usedLetters) and any(
                    d['yCord'] is selectedY for d in usedLetters)):
                return None
        ##If is player 1's turn and is on the player's word list
        if (player1Turn and event.char.upper() in player1Tiles):
            player1Tiles.remove(event.char.upper())
            if (textbox[selectedY][selectedX].letter is not ''):
                player1Tiles.append(textbox[selectedY][selectedX].letter)
        ##Else if is player 2's turn and is on the player's word list
        elif (player2Turn and event.char.upper() in player2Tiles):
            player2Tiles.remove(event.char.upper())
            if (textbox[selectedY][selectedX].letter is not ''):
                player2Tiles.append(textbox[selectedY][selectedX].letter)
        else:
            return None
        ##If a valid move was played, add the word to the 'usedLetters' array
        ############################################Explaining Ended Here##########################
        usedLetters.append(newLetter)
        ##Remove from usedLetters if the letter pre-exists in the tile
        usedLetters[:] = [d for d in usedLetters if d.get('letter') != textbox[selectedY][selectedX].letter]
        textbox[selectedY][selectedX].letter = event.char.upper()
        displayUpdate(selectedX, selectedY)
        setTileDisplay(-1, selectedX, selectedY, event.char)
        if (selectedX < 14):
            buttonSelect(selectedX + 1, selectedY)
    if (event.keysym == "Up" and selectedY != 0):
        buttonSelect(selectedX, selectedY - 1)
    if (event.keysym == "Down" and selectedY != 14):
        buttonSelect(selectedX, selectedY + 1)
    if (event.keysym == "Left" and selectedX != 0):
        buttonSelect(selectedX - 1, selectedY)
    if (event.keysym == "Right" and selectedX != 14):
        buttonSelect(selectedX + 1, selectedY)
    if (event.keysym == "BackSpace"):
        if (textbox[selectedY][selectedX].letter is not ''):
            if any(d['xCord'] is selectedX for d in usedLetters) and any(d['yCord'] is selectedY for d in usedLetters):
                if (player1Turn):
                    player1Tiles.append(textbox[selectedY][selectedX].letter)
                if (player2Turn):
                    player2Tiles.append(textbox[selectedY][selectedX].letter)
                usedLetters[:] = [d for d in usedLetters if d.get('xCord') != selectedX or d.get('yCord') != selectedY]
                textbox[selectedY][selectedX].letter = ''
                displayUpdate(selectedX, selectedY)
                setTileDisplay(textbox[selectedY][selectedX].color, selectedX, selectedY, '')
        if (selectedX != 0):
            buttonSelect(selectedX - 1, selectedY)
    if (event.char is '1'):
        setTileDisplay(0, selectedX, selectedY, textbox[selectedY][selectedX].letter)
    if (event.char is '2'):
        if (textbox[selectedY][selectedX].color == 2):
            setTileDisplay(1, selectedX, selectedY, textbox[selectedY][selectedX].letter)
        else:
            setTileDisplay(2, selectedX, selectedY, textbox[selectedY][selectedX].letter)
    if (event.char is '3'):
        if (textbox[selectedY][selectedX].color == 4):
            setTileDisplay(3, selectedX, selectedY, textbox[selectedY][selectedX].letter)
        else:
            setTileDisplay(4, selectedX, selectedY, textbox[selectedY][selectedX].letter)


# 15x15 Game board backend
def setTileDisplay(num, x, y, char):
    if (num == 0):
        textbox[y][x].config(bg="green", text="", relief=FLAT, activebackground="green")
    if (num == 1):
        textbox[y][x].config(bg="light blue", fg="black", activeforeground="black", text="2L", relief=FLAT,
                             activebackground="light blue")
    if (num == 2):
        textbox[y][x].config(bg="pink", fg="black", activeforeground="black", text="2W", relief=FLAT,
                             activebackground="pink")
    if (num == 3):
        textbox[y][x].config(bg="blue", fg="white", activeforeground="white", text="3L", relief=FLAT,
                             activebackground="blue")
    if (num == 4):
        textbox[y][x].config(bg="red", fg="white", activeforeground="white", text="3W", relief=FLAT,
                             activebackground="red")
    if (num != -1):
        textbox[y][x].color = num
    if (char.isalpha()):
        textbox[selectedY][selectedX].config(bg="beige", fg="black", activeforeground="black", text=char.upper(),
                                             relief=FLAT, activebackground="beige")
        textbox[selectedY][selectedX].letter = char.upper()
    else:
        textbox[selectedY][selectedX].letter = ''


# Updating the tiles and the scores
currentPlayerTempScore = 0


def displayUpdate(selectedX, selectedY):
    global scorePlayer1, scorePlayer2, player1Turn, player2Turn, player1Tiles, player2Tiles, currentPlayerTempScore
    currentPlayerTempScore = 0
    givenLetters = Text(root, width=12, height=1, borderwidth=0, background=root.cget("background"),
                        font=("Courier", 25))
    givenLetters.tag_configure("subscript", offset=-4, font=("Courier", 13))
    if (player1Turn is 1):
        for i in range(len(player1Tiles)):
            givenLetters.insert("insert", player1Tiles[i], "", letterScores[ord(player1Tiles[i]) - 65], "subscript")
    if (player2Turn is 1):
        for i in range(len(player2Tiles)):
            givenLetters.insert("insert", player2Tiles[i], "", letterScores[ord(player2Tiles[i]) - 65], "subscript")
    givenLetters.configure(state="disabled")
    givenLetters.grid(row=18, column=0, columnspan=15)

    confirmButton.grid_remove()
    # Calculating current score after confirming the word is valid (before passing the turn)
    if isValidWord():
        confirmButton.grid()
        multiple = 1
        xList = [x['xCord'] for x in usedLetters]
        yList = [y['yCord'] for y in usedLetters]
        xList.sort()
        yList.sort()
        pivot = list()
        xIsPivot = False
        yIsPivot = False
        if len(xList) == len(set(xList)):
            pivot = xList
            xIsPivot = True
            yIsPivot = False
        if len(yList) == len(set(yList)):
            pivot = yList
            xIsPivot = False
            yIsPivot = True
        if xIsPivot:
            multiple = 1
            nonMultiScore = 0
            if leftX(pivot[0] - 1, yList[0], 0, 0) != 0:
                currentPlayerTempScore = leftX(pivot[0] - 1, yList[0], 0, 0)
            tempX_1 = pivot[0]
            for i in range(len(pivot)):
                currentPlayerTempScore += check_Scr(pivot[i], yList[0], 1, multiple)[0]
                multiple = check_Scr(pivot[i], yList[0], 1, multiple)[1]
                if i != 0:
                    tempX_2 = pivot[i]
                    while tempX_1 + 1 != tempX_2:
                        currentPlayerTempScore += check_Scr(tempX_1 + 1, yList[0], 0, 0)[0]
                        tempX_1 += 1
                    tempX_1 = tempX_2
                if upY(pivot[i], yList[0] - 1, 0, 0) != 0:
                    tempScore = 0
                    if len(usedLetters) > 1:
                        tempScore += check_Scr(pivot[i], yList[0], 0, 0)[0]
                    tempScore += upY(pivot[i], yList[0] - 1, 0, 0)
                    if check_Scr(pivot[i], yList[0], 1, 1)[1] != 1:
                        tempScore *= check_Scr(pivot[i], yList[0], 1, 1)[1]
                    nonMultiScore += tempScore
                elif downY(pivot[i], yList[0] + 1, 0, 0) != 0:
                    tempScore = 0
                    if len(usedLetters) > 1:
                        tempScore += check_Scr(pivot[i], yList[0], 0, 0)[0]
                    tempScore += downY(pivot[i], yList[0] + 1, 0, 0)
                    if check_Scr(pivot[i], yList[0], 1, 1)[1] != 1:
                        tempScore *= check_Scr(pivot[i], yList[0], 1, 1)[1]
                    nonMultiScore += tempScore
            if rightX(max(pivot) + 1, yList[0], 0, 0) != 0:
                currentPlayerTempScore = rightX(max(pivot) + 1, yList[0], 0, 0)
            print("before multiple and nonMultiScore", currentPlayerTempScore)
            print("multiple", multiple)
            currentPlayerTempScore *= multiple
            print("before nonMultiScore", currentPlayerTempScore)
            print("nonMultiScore", nonMultiScore)
            currentPlayerTempScore += nonMultiScore
            print("final", currentPlayerTempScore)
        if yIsPivot:
            nonMultiScore = 0
            multiple = 1
            tempY_1 = pivot[0]
            if upY(xList[0], pivot[0] - 1, 0, 0) != 0:
                currentPlayerTempScore = upY(xList[0], pivot[0] - 1, 0, 0)
            for i in range(len(pivot)):
                currentPlayerTempScore += check_Scr(xList[0], pivot[i], 1, multiple)[0]
                print("Q check", currentPlayerTempScore)
                multiple = check_Scr(xList[0], pivot[i], 1, multiple)[1]
                if i != 0:
                    tempY_2 = pivot[i]
                    while tempY_1 + 1 != tempY_2:
                        currentPlayerTempScore += check_Scr(xList[0], tempY_1 + 1, 1, 1)[0]
                        tempY_1 += 1
                    tempY_1 = tempY_2
                if leftX(xList[0] - 1, pivot[i], 0, 0) != 0:
                    tempScore = 0
                    if len(usedLetters) > 1:
                        tempScore += check_Scr(xList[0], pivot[i], 1, multiple)[0]
                    tempScore += leftX(xList[0] - 1, pivot[i], 0, 0)
                    if check_Scr(xList[0], pivot[i], 1, 1)[1] != 1:
                        tempScore *= check_Scr(xList[0], pivot[i], 1, 1)[1]
                    nonMultiScore += tempScore
                elif rightX(xList[0] + 1, pivot[i], 0, 0) != 0:
                    tempScore = 0
                    if len(usedLetters) > 1:
                        tempScore += check_Scr(xList[0], pivot[i], 1, multiple)[0]
                    tempScore += rightX(xList[0] + 1, pivot[i], 0, 0)
                    if check_Scr(xList[0], pivot[i], 1, 1)[1] != 1:
                        tempScore *= check_Scr(xList[0], pivot[i], 1, 1)[1]
                    nonMultiScore += tempScore
            if downY(xList[0], max(pivot) + 1, 0, 0) != 0:
                currentPlayerTempScore += downY(xList[0], max(pivot) + 1, 0, 0)
            print("before multiple and nonMultiScore", currentPlayerTempScore)
            print("multiple", multiple)
            currentPlayerTempScore *= multiple
            currentPlayerTempScore += nonMultiScore
            print("Y final", currentPlayerTempScore)
        if (len(usedLetters) is 7):
            currentPlayerTempScore += 50
    if (player1Turn is 1):
        Player1Label = Label(root, text="Player 1: " + str(currentPlayerTempScore + scorePlayer1), width=15,
                             font=("Courier", 11))
        Player1Label.grid(row=1, column=0, columnspan=7)
    elif (player2Turn is 1):
        Player2Label = Label(root, text="Player 2: " + str(currentPlayerTempScore + scorePlayer2), width=15,
                             font=("Courier", 11))
        Player2Label.grid(row=1, column=7, columnspan=8)


def leftX(x, y, score, const):
    if x >= 0 and textbox[y][x].letter.isalpha():
        score += check_Scr(x, y, const, 0)[0]
        return leftX(x - 1, y, score, const)
    else:
        return score


def rightX(x, y, score, const):
    if x < 15 and textbox[y][x].letter.isalpha():
        score += check_Scr(x, y, const, 0)[0]
        return rightX(x + 1, y, score, const)
    else:
        return score


def upY(x, y, score, const):
    if y >= 0 and textbox[y][x].letter.isalpha():
        score += check_Scr(x, y, const, 0)[0]
        return upY(x, y - 1, score, const)
    else:
        return score


def downY(x, y, score, const):
    if y < 15 and textbox[y][x].letter.isalpha():
        score += check_Scr(x, y, const, 0)[0]
        return downY(x, y + 1, score, const)
    else:
        return score


def check_Scr(x, y, const, multiple):
    score = 0
    if (textbox[y][x].color == 0):
        score += letterScores[ord(textbox[y][x].letter) - 65]
    elif (textbox[y][x].color == 1):
        if const:
            score += letterScores[ord(textbox[y][x].letter) - 65] * 2
        else:
            score += letterScores[ord(textbox[y][x].letter) - 65]
    elif (textbox[y][x].color == 2):
        if const:
            multiple *= 2
        score += letterScores[ord(textbox[y][x].letter) - 65]
    elif (textbox[y][x].color == 3):
        if const:
            score += letterScores[ord(textbox[y][x].letter) - 65] * 3
        else:
            score += letterScores[ord(textbox[y][x].letter) - 65]
    elif (textbox[y][x].color == 4):
        if const:
            multiple *= 3
        score += letterScores[ord(textbox[y][x].letter) - 65]
    return score, multiple


def isValidWord():
    if (len(usedLetters) is not 0):
        xList = [x['xCord'] for x in usedLetters]
        minX = min(xList)
        maxX = max(xList)
        yList = [y['yCord'] for y in usedLetters]
        minY = min(yList)
        maxY = max(yList)
        if (minX != maxX and minY != maxY or not adjacentWord(minX, minY)):
            currentPlayerTempScore = 0
            return False
        elif (minX == maxX):
            sorted(usedLetters, key=lambda k: k['xCord'])
            return True
        else:
            sorted(usedLetters, key=lambda k: k['yCord'])
            return True


def adjacentWord(minX, minY):
    x = []
    for i in range(15):
        x.append([])
        for j in range(15):
            x[i].append(textbox[i][j].letter)
    floodFill(x, minY, minX)
    return all(tile is '' for row in x for tile in row)


def floodFill(board, x, y):
    if type(board[x][y]) is str and board[x][y].isalpha():
        board[x][y] = ""
        if (x > 0):
            floodFill(board, x - 1, y)
        if (x < len(board[y]) - 1):
            floodFill(board, x + 1, y)
        if (y > 0):
            floodFill(board, x, y - 1)
        if (y < len(board[x]) - 1):
            floodFill(board, x, y + 1)


def turnPassed():
    global player1Turn, player2Turn, currentPlayerTempScore, scorePlayer1, scorePlayer2
    if (player1Turn):
        scorePlayer1 += currentPlayerTempScore
        currentPlayer = Label(root, text="Current Turn: Player 2", font=("Courier", 11))
        while len(player1Tiles) < 7:
            randNum = randint(0, 25)
            while letterDistribution[randNum] is 0:
                randNum = randint(0, 25)
            letterDistribution[randNum] -= 1
            player1Tiles.append(chr(randNum + 65))
    if (player2Turn):
        scorePlayer2 += currentPlayerTempScore
        currentPlayer = Label(root, text="Current Turn: Player 1", font=("Courier", 11))
        while len(player2Tiles) < 7:
            randNum = randint(0, 25)
            while letterDistribution[randNum] is 0:
                randNum = randint(0, 25)
            letterDistribution[randNum] -= 1
            player2Tiles.append(chr(randNum + 65))
    currentPlayer.grid(row=2, column=0, columnspan=15)
    usedLetters.clear()
    currentPlayerTempScore = 0
    player1Turn, player2Turn = player2Turn, player1Turn
    displayUpdate(-1, -1)


# Saving the game data to gameData.json when closing the program.
def windowClose():
    if messagebox.askokcancel("Exit?", "Exit?"):
        boardColor = list()
        boardLetter = list()
        for i in range(len(textbox)):
            boardLetter.append([])
            for j in range(len(textbox[i])):
                boardColor.append(textbox[i][j].color)
                boardLetter[i].append(textbox[i][j].letter)
        savedData = {}
        savedData['boardColor'] = boardColor
        savedData['boardLetter'] = boardLetter
        savedData['usedLetters'] = usedLetters
        savedData['scorePlayer1'] = scorePlayer1
        savedData['scorePlayer2'] = scorePlayer2
        savedData['player1Tiles'] = player1Tiles
        savedData['player2Tiles'] = player2Tiles
        savedData['player1Turn'] = player1Turn
        savedData['player2Turn'] = player2Turn
        savedData['letterDistribution'] = letterDistribution
        jsonLetterList = json.dump(savedData, open("gameData.json", "w"), indent=2, ensure_ascii=True, sort_keys=True)
        root.destroy()


# 15x15 Board Interface
titleLabel = Label(root, text="Scrabble", width=15, font=("Courier", 11))
titleLabel.grid(row=0, column=0, columnspan=15)
confirmButton = Button(root, text="Confirm", command=partial(turnPassed))
confirmButton.grid(row=19, column=0, columnspan=15)
Player1Label = Label(root, text="Player 1: " + str(scorePlayer1), width=15, font=("Courier", 11))
Player1Label.grid(row=1, column=0, columnspan=7)
Player2Label = Label(root, text="Player 2: " + str(scorePlayer2), width=15, font=("Courier", 11))
Player2Label.grid(row=1, column=7, columnspan=8)
if (player1Turn is 1):
    currentPlayer = Label(root, text="Current Turn: Player 1", font=("Courier", 11))
    currentPlayer.grid(row=2, column=0, columnspan=15)
else:
    currentPlayer = Label(root, text="Current Turn: Player 2", font=("Courier", 11))
    currentPlayer.grid(row=2, column=0, columnspan=15)

textbox = list(list())
for j in range(15):
    textbox.append([])
    for i in range(15):
        textbox[j].append(Button(root, width=1, height=1, bg="green", highlightbackground="black",
                                 borderwidth=0, activebackground="green", command=partial(buttonSelect, i, j)))
        setTileDisplay(boardColor[i + 15 * j], i, j, boardLetter[j][i])
        textbox[j][-1].grid(row=j + 3, column=i)

# Set Letter and Score board
if not usedLetters:
    while len(player1Tiles) < 7:
        randNum = randint(0, 25)
        while letterDistribution[randNum] is 0:
            randNum = randint(0, 25)
        letterDistribution[randNum] -= 1
        player1Tiles.append(chr(randNum + 65))
    while len(player2Tiles) < 7:
        randNum = randint(0, 25)
        while letterDistribution[randNum] is 0:
            randNum = randint(0, 25)
        letterDistribution[randNum] -= 1
        player2Tiles.append(chr(randNum + 65))

displayUpdate(selectedX, selectedY)

root.protocol("WM_DELETE_WINDOW", windowClose)
root.mainloop()
