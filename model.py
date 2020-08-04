import string
import re
class Model:
    LETTER_SCORE = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
    def __init__(self):
        '''
        '''
        self.scores = list()

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
        tile_name = tile.winfo_name()
        tile_frame = tile.winfo_parent()
        i = 0
        j = 0
        if tile_name[-1].isdigit():
            i = int(next(re.finditer(r'\d+$', tile_name)).group(0))
        if tile_frame[-1].isdigit():
            j = int(re.compile(r'(\d+)$').search(tile_frame).group(1))
        print(i,j)
        if char in letter_list:
            key = "char"
        switcher = {
            "char": 1,
            "BACKSPACE": 2,
            "UP": 3,
            "DOWN": 4,
            "LEFT": 5,
            "RIGHT": 6
        }
        name = tile_name.rstrip(string.digits)
        key = switcher.get(key)
        if key == 1:
            if j != 0:
                j -= 1
            return key,i,j
        elif key == 2:
            if i > 2:
                name += str(i-1)
            if i == 7 and j == 7:
                return key,name
            else:
                if i != 0:
                    i -= 1
                if j != 0:
                    j -= 1
                return key+1,name,i,j
    ##Unfinished methods
