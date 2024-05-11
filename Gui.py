import tkinter as tk
import chess
#from chessboard import display
import random
import time

board = chess.Board()
valid_fen = board.fen()
moves = list(board.legal_moves)

saved_moves = ''
move_num = 0

turn = 'w'

class ChessBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Chess Board")
        self.configure(bg='#2c3e50')
        self.geometry("1024x600")
        self.attributes('-fullscreen', True)
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
        
        self.turn_lbl = tk.Label(self, text='Turn:', width=5, height=3, bg='#2c3e50', fg='white', font=('Roboto',25))
        self.turn_lbl.place(x=635,y=0)
        
        self.turn_white_lbl = tk.Label(self, text='White', width=5, height=3, bg='#af7ac4', fg='white', font=('Roboto',25))
        self.turn_white_lbl.place(x=762,y=0)
        
        self.turn_black_lbl = tk.Label(self, text='Black', width=5, height=3, bg='#2c3e50', fg='white', font=('Roboto',25))#34495e
        self.turn_black_lbl.place(x=890,y=0)#2c3e50
        
        self.moves_lbl = tk.Label(self, text=saved_moves, width=40, height=15, bg='#98a3a3', fg='white', font=('Roboto',10), anchor='nw', wraplength=330, justify='left')
        self.moves_lbl.place(x=635,y=130)
        
        self.menu_btn = tk.Label(self, text='Main\nmenu', width=6, height=3, bg='#34495e', fg='white', font=('Roboto',17), justify='center')
        self.menu_btn.place(x=635,y=395)
        
        self.reset_btn = tk.Label(self, text='Reset\nboard', width=6, height=3, bg='#34495e', fg='white', font=('Roboto',17), justify='center')
        self.reset_btn.place(x=727,y=395)
        
        self.test_btn = tk.Label(self, text='Other\noption', width=6, height=3, bg='#34495e', fg='white', font=('Roboto',17), justify='center')
        self.test_btn.place(x=819,y=395)
        
        self.autohome_btn = tk.Label(self, text='Auto\nhome', width=6, height=3, bg='#c0392b', fg='white', font=('Roboto',17), justify='center')
        self.autohome_btn.place(x=911,y=395)
        
        self.credits_lbl = tk.Label(self, text='Made by\nDominik Wilczewski', width=50, height=3, bg='#2c3e50', fg='white', font=('Roboto',10), justify='center')
        self.credits_lbl.place(x=600,y=560)
        
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
                color = "#edd6b0" if (i + j) % 2 == 0 else "#b88762"
                self.canvas.create_rectangle(j * 75, i * 75, (j + 1) * 75, (i + 1) * 75, fill=color)

    def draw_pieces(self):
        self.canvas.delete("piece")
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece != ' ':
                    self.canvas.create_image(j * 75 + 37.5, i * 75 + 37.5, image=self.piece_images[piece], tags="piece")

    def move_piece(self, event):
        global board, valid_fen, moves, move_num, saved_moves, turn

        col = event.x // 75
        row = event.y // 75
        
        promotion = False
        
        if self.selected_piece is None:
            self.selected_piece = (row, col)
            self.piece_to_move = self.canvas.find_closest(event.x, event.y)
            target_row, target_col = self.selected_piece
            if self.board[target_row][target_col] == ' ':
                self.selected_piece = None
        
        else:     
            target_row, target_col = self.selected_piece

            move = self.algebraic_notation(target_row, target_col, row, col)
            #print(move)
            
            decrypt_move = [m for m in move]
            #print(decrypt_move)
            #print(self.board[row][col])
            #print(self.board[target_row][target_col])
            if decrypt_move[3] == '8' and self.board[target_row][target_col] in ['P']:
                move = move + 'q'
                #print('new move:',move)
                promotion = True
            if decrypt_move[3] == '1' and self.board[target_row][target_col] in ['bp']:
                move = move + 'q'
                #print('new move:',move)
                promotion = True
                
            
            moves = list(board.legal_moves) 
            moves = [move.uci() for move in moves]
            #print(moves)
            if move in moves:
                print('legal')
                    #print(moves)
                if promotion == True:
                    board.push_san(str(move))
                    valid_fen = board.fen()
                #print(valid_fen)
                #print(move)

                if self.board[target_row][target_col] != self.board[row][col] and self.board[target_row][target_col] != ' ' and move in moves:
                    
                    if self.board[target_row][target_col] != ' ' and self.board[row][col] != self.board[target_row][target_col]:  # Check if the target square is occupied
                        
                        self.canvas.delete(self.piece_to_move)  # Remove the piece from the canvas
                        
                    self.board[target_row][target_col], self.board[row][col] = self.board[row][col], self.board[target_row][target_col]
                    
                    if self.board[target_row][target_col] != self.board[row][col]:
                        self.board[target_row][target_col] = ' '
                        
                    #print(self.board[target_row][target_col], self.board[row][col])
                    
                    #print(row,col)
                    #print(target_row,target_col)
                    #print(self.selected_piece)
                    #print(self.piece_to_move)
                    #print(self.board[row][col])
                    #print(self.board[target_row][target_col])
                    if promotion == False:
                        move = self.algebraic_notation(target_row, target_col, row, col)
                        moves = list(board.legal_moves) 
                        moves = [move.uci() for move in moves]

                            #print(moves)
                        board.push_san(str(move))
                        valid_fen = board.fen()
                    else:
                        if self.board[row][col] == 'P':
                            self.board[row][col] = 'Q'
                        elif self.board[row][col] == 'bp':
                            self.board[row][col] = 'bq'
                        
                    print(valid_fen)
                    #print(move)
                    #print(self.board)
                    print(board)
                    
                    self.draw_pieces()
                    
                    saved_moves += '['+str(move)+'], '
                    self.moves_lbl.configure(text=saved_moves)

                    self.selected_piece = None
                    self.piece_to_move = None
                    promotion = False
                    
                    if turn == 'w':
                        turn = 'b'
                        self.turn_black_lbl.configure(bg='#af7ac4')   
                        self.turn_white_lbl.configure(bg='#2c3e50')
                    elif turn == 'b':
                        turn = 'w'
                        self.turn_black_lbl.configure(bg='#2c3e50')   
                        self.turn_white_lbl.configure(bg='#af7ac4')
                    
            else:
                self.selected_piece = None
                self.piece_to_move = None
                promotion = False
            print(moves)
        #print(self.board)
    
    def algebraic_notation(self, start_row, start_col, end_row, end_col):
        files = 'abcdefgh'
        ranks = '87654321'
        start_square = files[start_col] + ranks[start_row]
        end_square = files[end_col] + ranks[end_row]
        return start_square + end_square

    def menu(self, event):
        print('menu')
        
    def autohome(self, event):
        print('autohome')
        
    def reset(self, event):
        print('reset')
        
    def test(self, event):
        print('test')   
    
if __name__ == "__main__":
    app = ChessBoard()
    app.canvas.bind("<Button-1>", app.move_piece)
    app.autohome_btn.bind("<Button-1>", app.autohome)
    app.menu_btn.bind("<Button-1>", app.menu)
    app.test_btn.bind("<Button-1>", app.test)
    app.reset_btn.bind("<Button-1>", app.reset)
    app.mainloop()