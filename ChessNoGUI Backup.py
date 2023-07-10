#Chess game in python without GUI
#Will add GUI later

# Lets start with the pieces
class Piece:
    # This is the base class for all the pieces
    def __init__(self, color, position, symbol, unmoved):
        self.color = color
        self.position = position
        self.symbol = symbol.upper() if color == 'white' else symbol.lower()
        self.moved = moved
    
    # Ensures that when we print a piece, we get the symbol 
    def __str__(self):
        return self.symbol

    # This method will mirrors the white pices to create the black pieces
    def clone_and_mirror(self):
        color = "black" if self.color == "white" else "white"
        position = (7-self.position[0], self.position[1])
        return type(self)(color, position)

# Piece specific classes
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, 'P', True)
    


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, 'R', True)
class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, 'N')
class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, 'B')
class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, 'Q')
class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, 'K', True)


# Lets start with the board

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)] # 8x8 board with no pieces
        self.set_up_board()

    # This method will set up the board
    def set_up_board(self):
        # Pawns
        for i in range(8):
            self.board[1][i] = Pawn("white", (1, i))
        # Rooks
        self.board[0][0] = Rook("white", (0, 0))
        self.board[0][7] = Rook("white", (0, 7))
        # Knights
        self.board[0][1] = Knight("white", (0, 1))
        self.board[0][6] = Knight("white", (0, 6))
        # Bishops
        self.board[0][2] = Bishop("white", (0, 2))
        self.board[0][5] = Bishop("white", (0, 5))
        # Queen
        self.board[0][3] = Queen("white", (0, 3))
        # King
        self.board[0][4] = King("white", (0, 4))


        # Mirror the white pieces to create the black pieces
        for i in range(2):
            for j in range(8):
                piece = self.board[i][j]
                if piece is not None:  # add a check here to avoid trying to clone None
                    self.board[7-i][j] = piece.clone_and_mirror()

    # This method will print the board
    def print_board(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    print("X ", end="")  # print 'X' for empty spaces
                else:
                    print(str(cell) + " ", end="")  
            print()  # this will make sure each row is printed on a new line
b = Board()
b.print_board()