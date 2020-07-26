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
        if caption == 'Start':
            self.view.initiate()
        elif caption == 'confirm':
            self.view.turn.set(self.model.turn_pass(self.view.turn.get(),self.view.PLAYER_NUM))
            self.view.update_racks()
        else:
            name = 'outer.'+str(int(caption[1])-1)+'.'+caption
            self.view.tile_selected(self.view.main_frm.nametowidget(name))

if __name__ == '__main__':
    scrabble = Controller()
    scrabble.main()
