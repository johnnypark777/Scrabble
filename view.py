import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    PAD = 15
    PLAYER_NUM = 2
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.value_var = tk.StringVar()
        self.title('Scrabble')
        self._make_main_frame()
        self._make_labels()
        self._make_buttons()

    def main(self):
        self.mainloop()

    ##Private methods

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_buttons(self):
        outer_frm= ttk.Frame(self.main_frm)
        outer_frm.pack()
        frm = ttk.Frame(outer_frm)
        frm.pack()
        for i in range(self.PAD):
            for j in range(self.PAD):
                x_axis = chr(65+j)
                y_axis = i+1
                self._configure_button(frm,(x_axis,y_axis))
            frm = ttk.Frame(outer_frm)
            frm.pack()
        self._configure_button(frm,'Confirm')

    def _configure_button(self,frm,txt):
        btn = tk.Button(frm, text=txt,width=6,height=1,command=(
            lambda button=txt:self.controller.on_button_click(txt)
            )
        )

        if txt == 'Confirm':
            btn.pack(side='left',padx=10,pady=10)
            return

        btn.config(bg="green",width=1, height=1, highlightbackground="black",
borderwidth=0,activebackground="green")
        btn.pack(side='left')

    #Incomplete Methods
    def _make_labels(self):
        ### Change by player number
        outer_frm= ttk.Frame(self.main_frm)
        outer_frm.pack(fill='both')
        player_label = ttk.Label(outer_frm,text="Player 1:")
        player_label.pack(side='left',padx=50,pady=10)
        player_label = ttk.Label(outer_frm,text="Player 2:")
        player_label.pack(side='right',padx=50,pady=10)
        #PLAYER SCORE
        #
        #
        #
        #
        #

    #Archived methods
    #def _start_frame(self):
    #    self.strt_frm = ttk.Frame(self)
    #    self.strt_frm.pack()
    #    self._configure_button(self.strt_frm,'Start')
