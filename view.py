import tkinter as tk
from tkinter import ttk
from random import choices
from string import ascii_uppercase
import json


class View(tk.Tk):
    PAD = 15
    LETTER_SCORE = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
    PLAYER_NUM = 3
    LETTER_NUM = 7
    def __init__(self,controller):
        super().__init__()
        self.selected = False
        self.controller = controller
        self.value_var = tk.StringVar()
        self.scores = self.PLAYER_NUM*[tk.IntVar()]
        self.turn = tk.IntVar()
        self.turn.set(1)
        self._load_file()
        self.title('Scrabble')
        self._make_main_frame()
        self._make_labels()
        self._make_buttons()
        self._make_letters()
        self._make_racks()

    def main(self):
        self.mainloop()

    #Update afther the turn is passed
    def update_racks(self):
        for widget in self.rack_frm.winfo_children():
            widget.destroy()
        self._generate_text(self.rack_frm)

    def tile_selected(self,tile):
        if self.selected:
            self.tile.config(highlightbackground="black")
        self.selected = True
        self.tile = tile
        tile.config(highlightcolor="white")
        tile.focus_set()
        tile.bind("<Key>",self.controller.on_key_press)

    def key_pressed(self,key,char,new_tile,**options):
        if key == 1:
            self.tile.config(
                bg="beige",fg="black",activeforeground="black",activebackground="beige",text=char
            )
        elif key in (2,3):
            #Erasing the Letter
            if key == 2:
                self._set_tile_color(self.tile,'★')
            else:
                self._set_tile_color(self.tile,str(self.board_color[options["j"]][options["i"]]))
        self.tile_selected(new_tile)

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
                x_axis = chr(97+j)
                y_axis = i+1
                if j == 7 and i == 7:
                    self._configure_button(frm,'★')
                else:
                    self._configure_button(frm,str(self.board_color[j][i]))
            frm = ttk.Frame(outer_frm)
            frm.pack()
        self._configure_button(self.main_frm,'Confirm')

    ##A helper function for the _make_buttons function, used to add onclick feature to the buttons
    def _configure_button(self,frm,txt):
        btn = tk.Button(frm,text=txt,width=6,height=1)
        btn.bind("<1>",self.controller.on_button_click)
        if txt == 'Confirm':
            btn.pack(side='bottom',padx=10)
            return
        else:
            if txt == '★':
                self.tile_selected(btn)
            self._set_tile_color(btn,txt)
        btn.pack(side='left')

    def _set_tile_color(self, btn, txt):
        switcher = {
            '0': ('','green'),
            '1': ('2L','light blue'),
            '2': ('2W','pink'),
            '3': ('3L','blue'),
            '4': ('3W','dark red'),
            '★': ('★', 'pink')
        }
        btn.config(text=switcher.get(txt)[0])
        color = switcher.get(txt)[1]
        if txt == '3' or txt == '4':
            txt = "white"
        else:
            txt = "black"
        btn.config(bg=color,fg=txt,activeforeground=txt,activebackground=color,width=1,highlightbackground="black",borderwidth=0)


    ##Making various labels such as the scores and the indicator of a player turn
    def _make_labels(self):
        score_frm= ttk.Frame(self.main_frm)
        score_frm.pack()
        for i in range(self.PLAYER_NUM):
            player_label = tk.Label(score_frm,text="Player "+str(i+1)+": "+str(self.scores[i].get()))
            player_label.pack(side='left',padx=50)
        turn_frm = ttk.Frame(self.main_frm)
        turn_label = tk.Label(turn_frm,text="Current Turn: ")
        turn_num = tk.Label(turn_frm,textvariable=self.turn)
        turn_label.pack(side='left')
        turn_num.pack(side='left')
        turn_frm.pack()

    ##Displaying the rack which shows the letters that the player is given
    def _make_racks(self):
        self.rack_frm = tk.Frame(self.main_frm)
        self._generate_text(self.rack_frm)
        self.rack_frm.pack(side='bottom',pady=(20,10))

    def _generate_text(self,frm):
        for i in range(len(self.letters[self.turn.get()-1])):
            letter = self.letters[self.turn.get()-1][i]
            sub = self.LETTER_SCORE[ord(letter)-65]
            letter_text = tk.Text(frm, height=1,width=2, borderwidth=1,relief="solid",bg='Beige',font=('TkDefaultFont',20))
            letter_text.tag_configure("subscript", offset=-4,font=("TkDefaultFont",8))
            letter_text.tag_configure("center", justify='center')
            letter_text.insert("1.0",letter,"",sub,"subscript")
            letter_text.tag_add("center", "1.0", "end")
            letter_text.configure(state="disabled")
            letter_text.pack(side='left')

    def _make_letters(self):
        self.letters = [choices(ascii_uppercase,k=self.LETTER_NUM) for _ in range(self.PLAYER_NUM)]
        #self.letters.append(self.controller.gen_letters)
    ##Loads the saved file
    def _load_file(self):
        savedData = json.load(open("game_data.json","r"))
        self.board_color = savedData["board_color"]
    #Incomplete methods
    #Archived methods
    #def _start_frame(self):
    #    self.strt_frm = ttk.Frame(self)
    #    self.strt_frm.pack()
    #    self._configure_button(self.strt_frm,'Start')
