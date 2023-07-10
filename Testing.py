class Piece:
    # This is the base class for all the pieces
    def __init__(self, color, position, symbol):
        self.color = color
        self.position = position
        self.symbol = symbol.upper() if color == 'white' else symbol.lower()
    
    # Ensures that when we print a piece, we get the symbol 
    def __str__(self):
        return self.symbol

    # This method will mirrors the white pices to create the black pieces
    def clone_and_mirror(self):
        color = "black" if self.color == "white" else "white"
        position = (7-self.position[0], self.position[1])
        symbol = self.symbol
        return type(self)(color, position, symbol)
    
# Piece specific classes
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position, 'P')
pawn = Piece("white", (1,1), 'P')
print(pawn)  # Should print 'P'
# Let's clone and mirror the black pawn and print it
pawn_clone = pawn.clone_and_mirror()
print(pawn_clone)  # Should print 'P', as the black pawn has been mirrored to a white pawn