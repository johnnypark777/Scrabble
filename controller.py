from model import Model
from view import View
import tkinter as tk

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
    def main(self):
        self.view.main()

    def on_button_click(self, caption):
        if(caption == 'Start'):
            self.view.initiate()
        elif(caption == 'Confirm'):
            self.view.turn.set(self.model.turn_pass(self.view.turn.get(),self.view.PLAYER_NUM))
            self.view.update_racks()

if __name__ == '__main__':
    scrabble = Controller()
    scrabble.main()
