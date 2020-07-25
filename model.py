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

