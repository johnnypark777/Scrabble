from tkinter import *

root = Tk()

def myClick():
    myLabel3 = Label(root, text="clicked")
    myLabel3.grid(row=3,column=0)

#Creating a Label Widget
#[
myLabel1 = Label(root, text="Hello World")
#Alternative way
#myLabel1 = Label(root, text="Hello World").grid(row=0, column=0)
#]

myLabel2 = Label(root, text="Test label please ignore")

#Note: No parantheses on the command function
myButton1 = Button(root, text="Test button please ignore",command=myClick,bg="blue")

#Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myButton1.grid(row=2,column=0)



root.mainloop()

