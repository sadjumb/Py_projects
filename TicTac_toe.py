import os


class Game:
    def __init__(self):
        self.EMPTY = ' '
        self.board = self.make_board()
        self.rows = self.size_column = 3
        self.size_board = self.size_column * self.rows
        self.human, self.compute = self.pieces()
        self.print_board()

    def make_board(self):
        board = []
        for i in range(9):
            board.append(self.EMPTY)
        return board

    def print_board(self):
        print('\n\t', '-' * 23)
        for i in range(self.rows):
            print('\t', end='|')
            for j in range(self.rows):
                print('\t', self.board[self.rows * i + j], end='\t|')
            print('\n\t', '-' * 23)

    @staticmethod
    def pieces():
        X, O = 'X', 'O'
        answer = str(input("You will start first? y/n: "))
        if answer == 'y':
            return X, O
        else:
            return O, X

    def legal_movie(self):
        moves = []
        for i in range(self.size_board):
            if self.board[i] == self.EMPTY:
                moves.append(i)
        return moves

    def human_move(self):
        moves = self.legal_movie()
        print("You can move in: ", moves)
        move = int(input("Enter the position: "))
        while move not in moves:
            move = int(input("Position is wrong< enter another: "))
        return move

    def compute_move(self):
        board = self.board[::]
        best_move = [4, 0, 2, 8, 6, 1, 5, 7, 3]
        legal_move = self.legal_movie()
        print('Computer\'s move')
        for move in legal_move:
            board[move] = self.compute
            if self.winner(board=board) == self.compute:
                print(move)
                return move
            board[move] = self.EMPTY

        for move in legal_move:
            board[move] = self.human
            if self.winner(board=board) == self.human:
                print(move)
                return move
            board[move] = self.EMPTY

        for move in best_move:
            if move in legal_move:
                print(move)
                return move

    def winner(self, board=[]):
        WAYS_TO_WIN = ((0, 1, 2),
                       (0, 4, 8),
                       (0, 3, 6),
                       (1, 4, 7),
                       (2, 4, 6),
                       (2, 5, 8),
                       (3, 4, 5),
                       (6, 7, 8))
        if not board:
            board = self.board
        for i in WAYS_TO_WIN:
            if board[i[0]] == board[i[1]] == board[i[2]] == ('X' or 'O'):
                return board[i[0]]
        if self.EMPTY not in board:
            return 'Ничья'
        return None

    def run(self):
        turn = 'X'
        while not self.winner():
            if turn == self.human:
                move = self.human_move()
                self.board[move] = self.human
                turn = self.compute
            else:
                move = self.compute_move()
                self.board[move] = self.compute
                turn = self.human
            os.system("cls")
            self.print_board()
