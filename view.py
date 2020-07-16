import tkinter as tk
from tkinter import ttk
from pynput.keyboard import Key,Controller

class View(tk.Tk):
    PAD = 15
    def __init__(self,controller):
        super().__init__()
        #self.controller = controller
        self.value_var = tk.StringVar()
        self.title('Scrabble')
        self._make_main_frame()
        self._make_buttons()

    def main(self):
        keyboard = Controller()
        self.mainloop()


    ##Private Methods
    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_buttons(self):
        outer_frm= ttk.Frame(self.main_frm)
        outer_frm.pack()

        frm = ttk.Frame(outer_frm)
        frm.pack()
        btns_row = 0
        for i in range(self.PAD*self.PAD):
            if btns_row == self.PAD:
                frm = ttk.Frame(outer_frm)
                frm.pack()
                btns_row = 0
            btn = ttk.Button(frm, text=i)
            btn.pack(side='left')
            btns_row += 1
