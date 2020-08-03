class Model:
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
    def key_pressed(self,char,letter_list):
        key = char
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
        return switcher.get(key)



