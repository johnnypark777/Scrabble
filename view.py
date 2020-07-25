import tkinter as tk
from tkinter import ttk
from random import choices
from string import ascii_uppercase


class View(tk.Tk):
    PAD = 15
    PLAYER_NUM = 3
    LETTER_NUM = 7
    LETTER_SCORE = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.value_var = tk.StringVar()
        self.scores = self.PLAYER_NUM*[tk.IntVar()]
        self.letters = [choices(ascii_uppercase,k=self.LETTER_NUM) for _ in range(self.PLAYER_NUM)]
        self.turn = tk.IntVar()
        self.turn.set(1)
        self.title('Scrabble')
        self._make_main_frame()
        self._make_labels()
        self._make_buttons()
        self._make_racks()

    def main(self):
        self.mainloop()

    ##Private methods

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    ##Making Tiles of Scrabble
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
        self._configure_button(self.main_frm,'Confirm')

    ##A helper function for the _make_buttons function, used to add onclick feature to the buttons
    def _configure_button(self,frm,txt):
        btn = tk.Button(frm, text=txt,width=6,height=1,command=(
            lambda button=txt:self.controller.on_button_click(txt)
            )
        )

        if txt == 'Confirm':
            btn.pack(side='bottom',padx=10)
            return

        btn.config(bg="green",width=1, height=1, highlightbackground="black",
borderwidth=0,activebackground="green")
        btn.pack(side='left')

    ##Making various labels such as the scores and the indicator of a player turn
    def _make_labels(self):
        score_frm= ttk.Frame(self.main_frm)
        score_frm.pack()
        for i in range(self.PLAYER_NUM):
            player_label = tk.Label(score_frm,text="Player "+str(i+1)+": "+str(self.scores[i].get()))
            player_label.pack(side='left',padx=50)
        turn_frm = ttk.Frame(self.main_frm)
        turn_label = tk.Label(turn_frm,text="Current Turn: ")
        turn_label.pack(side='left')
        turn_num = tk.Label(turn_frm,textvariable=self.turn)
        turn_num.pack(side='left')
        turn_frm.pack()

    ##Displaying the rack which shows the letters that the player is given
    def _make_racks(self):
        rack_frm = tk.Frame(self.main_frm)
        for i in range(len(self.letters[self.turn.get()])):
            letter = self.letters[self.turn.get()][i]
            sub = self.LETTER_SCORE[ord(letter)-65]
            letter_text = tk.Text(rack_frm, height=1,width=2, borderwidth=1,relief="solid",bg='Beige',font=('TkDefaultFont',20))
            letter_text.tag_configure("subscript", offset=-4,font=("TkDefaultFont",8))
            letter_text.tag_configure("center", justify='center')
            letter_text.insert("1.0",letter,"",sub,"subscript")
            letter_text.tag_add("center", "1.0", "end")
            letter_text.configure(state="disabled")
            letter_text.pack(side='left')
        rack_frm.pack(side='bottom',pady=(20,10))

    #Incomplete methods
    def update_racks(self):
        ''

    #Archived methods
    #def _start_frame(self):
    #    self.strt_frm = ttk.Frame(self)
    #    self.strt_frm.pack()
    #    self._configure_button(self.strt_frm,'Start')
