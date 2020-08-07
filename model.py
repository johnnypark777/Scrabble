import string
import random
import re
class Model:
    LETTER_FREQ = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]
    LETTER_SCORE = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
    PLAYER_NUM = 3
    LETTER_NUM = 7
    PAD = 15
    def __init__(self):
        '''
        '''
        self.scores = list()
        self.TILE_BAG = self.gen_tile_bag()

    def turn_pass(self,curr_player,player_num):
        if curr_player == player_num:
            curr_player = 1
        else:
            curr_player += 1
        return curr_player
    def calculate(self, player_scores, **options):
        self.scores = player_scores
    def key_pressed(self,char,letter_list,tile):
        key = char
        if char in letter_list:
            key = "char"
        switcher = {
            "char": 1,
            "BACKSPACE": 2,
            "UP": 3,
            "DOWN": 4,
            "LEFT": 5,
            "RIGHT": 6,
            "TAB": 7
        }
        key = switcher.get(key)
        return self.move_tile(key,tile)


    def move_tile(self,key,tile):
        i = self.move_tile_find_ij(tile)[0]
        j = self.move_tile_find_ij(tile)[1]
        if key in (1,4,6):
            if key == 4:
                i,j = j,i
            if i == 0:
                i += 1
            if i != self.PAD:
                i += 1
        elif key == 2:
            if i != 8 or j != 8:
                if i == 0:
                    i += 1
                if j == 0:
                    j += 1
                return key+1,self.move_tile_gen_name(tile,i,j,key),i-1,j-1
        return key+1 if key in (3,4,5,6) else key,self.move_tile_gen_name(tile,i,j,key)

    def move_tile_find_ij(self,tile):
        tile_name = tile.winfo_name()
        tile_frame = tile.winfo_parent()
        i = 0
        j = 0
        if tile_name[-1].isdigit():
            i = int(next(re.finditer(r'\d+$', tile_name)).group(0))
        if tile_frame[-1].isdigit():
            j = int(re.compile(r'(\d+)$').search(tile_frame).group(1))
        return i,j

    def move_tile_gen_name(self,tile,i,j,key):
        tile_name = tile.winfo_name()
        name = tile_name.rstrip(string.digits)
        frame_name = tile.winfo_parent().rstrip(string.digits)
        if key in (1,6):
            name += str(i)
        elif key in (2,5):
            if i > 2:
                name += str(i-1)
        elif key == 3:
            name = frame_name +'.' + tile_name
            if j > 2:
               name = frame_name + str(j-1) +'.' + tile_name
        elif key == 4:
            name = frame_name + str(i) +'.' + tile_name
        return name

    def gen_letters(self):
        arr = [[] for _ in range(self.PLAYER_NUM)]
        for i in range(self.PLAYER_NUM):
            for j in range(self.LETTER_NUM):
                random.shuffle(self.TILE_BAG)
                arr[i].append(chr(self.TILE_BAG.pop()+65))
        return arr

    def gen_tile_bag(self):
        bag = list()
        k = 0
        for i in self.LETTER_FREQ:
            for j in range(i):
                bag.append(k)
            k += 1
        return bag
    ##Unfinished methods

