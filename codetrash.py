#as a player I want to see a welcom message at the start

class PyPacPoe():
    def __init__(self):
        self.current_player = 'X'
        self.nu_of_turns = 0
        self.is_winner = False
        self.is_tie = False                                                                                                                                 
        self.current_board = {
            'a1': None, 'a2': None, 'a3': None,
            'b1': None, 'b2': None, 'b3': None,
            'c1': None, 'c2': None, 'c3': None,
        }
    #display a welcome message
    def dispay_welcome_message(self):
        print('''
        ---------------------------------
            Let's play PyPacPoe!
        ---------------------------------
        ''')

    #display the game board
    def display_board(self):
        print(f'''
        A  B   C
    1  |{self.current_board['a1']}  | {self.current_board['b1']} | {self.current_board['c1']} |
    2  |{self.current_board['a2']}  | {self.current_board['b2']} | {self.current_board['c2']} |
    3  |{self.current_board['a3']}  | {self.current_board['b3']} | {self.current_board['c3']} |
        ''')    

    def display_turn(self):
        print(f"It's Player {self.current_player}'s Move (example B2):")

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
    
    def get_player_move(self):
        player_move = input("Enter your move (example B2): ").lower()
        while not player_move in self.current_board:
            player_move = input("That is not a valid move. Enter your move (example B2): ").lower()
            print(self.current_board)        
        while self.current_board[player_move] != None:
            player_move = input("This space is taken. Enter your move (example B2): ").lower()
        self.current_board[player_move] = self.current_player
        print(self.current_board)
        self.nu_of_turns += 1

    def check_for_winner(self):
        if self.current_board['a1'] == self.current_board['a2'] == self.current_board['a3']== self.current_board['a1'] != None:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['b1'] == self.current_board['b2'] == self.current_board['b3'] == self.current_board['b1'] != None:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['c1'] == self.current_board['c2'] == self.current_board['c3'] == self.current_board['c1'] != None:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['a1'] == self.current_board['b1'] == self.current_board['c1'] == self.current_board['a1'] != None:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['a2'] == self.current_board['b2'] == self.current_board['c2'] == self.current_board['a2'] != None:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['a3'] == self.current_board['b3'] == self.current_board['c3'] == self.current_board['a3'] != None:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['a1'] == self.current_board['b2'] == self.current_board['c3'] == self.current_board['a1'] != None:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['a3'] == self.current_board['b2'] == self.current_board['c1'] == self.current_board['a3'] != None:
            self.is_winner = True
            self.display_winner()
        else: 
            self.nu_of_turns == 9 and not self.is_winner
            self.is_tie = True
            self.display_tie()
        return
    def display_winner(self):
        print(f"Player {self.current_player} wins!")   

    def display_tie(self):
        print("It's a tie!")

def play(self):
    while not self.is_winner:
        self.display_board()
        self.display_turn()
        self.display_board()
        self.get_player_move()
        self.check_for_winner()
        self.switch_player()

def init_game(self):
    self.display_welcome_message()
    self.play() 


new_game = PyPacPoe(play); 
new_game.init_game()

# new_game.dispay_welcome_message()
# new_game.display_board()
# new_game.display_turn()
# new_game.get_player_move()
# new_game.display_board()
# new_game.check_for_winner()
# new_game.switch_player()
# new_game.display_turn()
# new_game.get_player_move()
# new_game.display_board()
# new_game.check_for_winner()


    
       