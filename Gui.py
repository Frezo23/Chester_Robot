import tkinter as tk
import chess
#from chessboard import display
import random

board = chess.Board()
valid_fen = board.fen()
moves = list(board.legal_moves)

class ChessBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Chess Board")
        self.configure(bg='#d5d5d5')
        self.geometry("1024x600")
        self.canvas = tk.Canvas(self, width=600, height=600, bg='#8f8f8f', highlightthickness=0)
        self.canvas.pack(anchor='w')
        self.selected_piece = None
        self.piece_to_move = None
        self.piece_images = self.load_piece_images()
        self.board = [
            ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.draw_board()
        self.draw_pieces()

    def load_piece_images(self):
        piece_images = {}
        for piece in ['P', 'R', 'N', 'B', 'Q', 'K', 'bp', 'br', 'bn', 'bb', 'bq', 'bk']:
            piece_image = tk.PhotoImage(file=f"{piece}.png")
            piece_image = piece_image.subsample(2)  # Change these numbers as needed for proper resizing
            piece_images[piece] = piece_image
        return piece_images

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                color = "#ebecd0" if (i + j) % 2 == 0 else "#779556"
                self.canvas.create_rectangle(j * 75, i * 75, (j + 1) * 75, (i + 1) * 75, fill=color)

    def draw_pieces(self):
        self.canvas.delete("piece")
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece != ' ':
                    self.canvas.create_image(j * 75 + 37.5, i * 75 + 37.5, image=self.piece_images[piece], tags="piece")

    def move_piece(self, event):
        global board, valid_fen, moves

        col = event.x // 75
        row = event.y // 75
        if self.selected_piece is None:
            self.selected_piece = (row, col)
            self.piece_to_move = self.canvas.find_closest(event.x, event.y)
            target_row, target_col = self.selected_piece
            if self.board[target_row][target_col] == ' ':
                self.selected_piece = None
        
        else:     
            target_row, target_col = self.selected_piece

            move = self.algebraic_notation(target_row, target_col, row, col)
            moves = list(board.legal_moves) 
            moves = [move.uci() for move in moves]
            print(moves)
            if move in moves:
                print('legal')
                #valid_fen = board.fen()
                    #print(moves)
                #board.push_san(str(move))
                #print(valid_fen)
                #print(move)

                if self.board[target_row][target_col] != self.board[row][col] and self.board[target_row][target_col] != ' ' and move in moves:
                    
                    if self.board[target_row][target_col] != ' ' and self.board[row][col] != self.board[target_row][target_col]:  # Check if the target square is occupied
                        
                        self.canvas.delete(self.piece_to_move)  # Remove the piece from the canvas
                        
                    self.board[target_row][target_col], self.board[row][col] = self.board[row][col], self.board[target_row][target_col]
                    
                    if self.board[target_row][target_col] != self.board[row][col]:
                        self.board[target_row][target_col] = ' '
                        
                    #print(self.board[target_row][target_col], self.board[row][col])
                    
                    self.draw_pieces()
                    
                    print(self.selected_piece)
                    print(self.piece_to_move)

                    move = self.algebraic_notation(target_row, target_col, row, col)
                    moves = list(board.legal_moves) 
                    moves = [move.uci() for move in moves]

                        #print(moves)
                    board.push_san(str(move))
                    valid_fen = board.fen()
                    print(valid_fen)
                    print(move)
                    print(self.board)
                    print(board)

                    self.selected_piece = None
                    self.piece_to_move = None
                    if (row == 0 or row == 7) and self.board[row][col] in ['P', 'bp']:  # Check if pawn reaches last row
                        self.board[row][col] = 'Q' if self.board[row][col] == 'P' else 'bq'  # Promote pawn to queen

            else:
                self.selected_piece = None
                self.piece_to_move = None
            
        #print(self.board)
    
    def algebraic_notation(self, start_row, start_col, end_row, end_col):
        files = 'abcdefgh'
        ranks = '87654321'
        start_square = files[start_col] + ranks[start_row]
        end_square = files[end_col] + ranks[end_row]
        return start_square + end_square
    
if __name__ == "__main__":
    app = ChessBoard()
    app.canvas.bind("<Button-1>", app.move_piece)
    app.mainloop()