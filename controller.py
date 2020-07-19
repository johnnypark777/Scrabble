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
        print(f'{caption} Button Pressed')
        if(caption == 'Start'):
            self.view.initiate()

if __name__ == '__main__':
    scrabble = Controller()
    scrabble.main()
