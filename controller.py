from model import Model
from view import View
import tkinter as tk

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
    def main(self):
        self.view.main()

    def on_button_click(self,event):
        caption = event.widget.cget("text")
        if caption == 'Start':
            self.view.initiate()
        elif caption == 'Confirm':
            self.view.turn.set(self.model.turn_pass(self.view.turn.get(),self.view.PLAYER_NUM))
            self.view.update_racks()
        else:
            self.view.tile_selected(event.widget)

    def on_key_press(self,event):
        char = event.keysym.upper()
        key_type = self.model.key_pressed(char,self.view.letters[self.view.turn.get()-1],self.view.tile)
        key = key_type[0]
        if key_type[0] is None:
            return
        if key in (1,2,3,6,7):
            new_tile = self.view.tile.master.nametowidget(key_type[1])
            if key == 3:
                return self.view.key_pressed(key,char,new_tile,i=key_type[2],j=key_type[3])
        elif key in (4,5):
            new_tile = self.view.main_frm.nametowidget(key_type[1])
        self.view.key_pressed(key,char,new_tile)

    def gen_letters(self):
        return self.model.gen_letters()

if __name__ == '__main__':
    scrabble = Controller()
    scrabble.main()
