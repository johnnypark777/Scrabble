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
        textbox[prevY][prevX].config(highlightbackground="black")
    prevX,prevY = i,j
    textbox[j][i].config(highlightbackground="white")

def key(event):
    print("pressed")

#15x15 Textbox
textbox = list(list())
for j in range(15):
    textbox.append([])
    for i in range(15):
        textbox[j].append(Button(root,width=1,height=1,bg="green",highlightbackground="black",
borderwidth=0,activebackground="green",command=partial(buttonSelect,i,j)))
        textbox[j][-1].bind("<Key>",key)
        textbox[j][-1].grid(row=j,column=i)


root.mainloop()

