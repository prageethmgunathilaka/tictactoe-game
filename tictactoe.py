class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def make_move(self, position):
        if position < 0 or position > 8:
            return False
        if self.board[position] != ' ':
            return False
        self.board[position] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        return True

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return self.board[i]
        
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return self.board[i]
        
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]
        
        if ' ' not in self.board:
            return 'Tie'
        
        return None

    def display_board(self):
        for i in range(0, 9, 3):
            print(f'{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}')
            if i < 6:
                print('---------')

def play_game():
    game = TicTacToe()
    print("Welcome to Tic-tac-toe!")
    print("Positions are numbered from 0-8, left to right, top to bottom")
    
    while True:
        game.display_board()
        try:
            position = int(input(f"Player {game.current_player}'s turn. Enter position (0-8): "))
            if not game.make_move(position):
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Please enter a number between 0 and 8")
            continue
        
        winner = game.check_winner()
        if winner:
            game.display_board()
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"Player {winner} wins!")
            break

if __name__ == "__main__":
    play_game()
