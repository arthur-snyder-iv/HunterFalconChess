# Author:  Arthur Snyder
# GitHub username:  arthur-snyder-iv
# Date:  March 13, 2024
# Description:  Write a program for a two-player game of a modified version of chess.  The game will essentially follow
#               typical chess rules, but there is no need to declare 'check' or 'checkmate.'  There is also no castling,
#               en passant, or pawn promotion.  In addition, there are two additional pieces added to the game either of
#               which can be added to the game, on a player's turn, to replace a lost power piece.  The additional
#               pieces enter the board on any empty square in the players first two ranks.  One of the additional pieces
#               is called a Falcon, and it moves forward like a Bishop and backward like a Rook.  The other additional
#               piece is called a Hunter, and it moves forward like a Rook and backwards like a Bishop.  Neither may
#               move horizontally.  The game ends when on one of the player's King is captured.

class Piece:
    """Represents Parent Class for all pieces in the game"""

    def __init__(self, color):
        """
        Sets the given color as an attribute.  Also sets the power piece attribute to False, the name attribute to None
        and the symbol attributes to None.  The final three attributes can be overridden by the various child classes.
        """

        self._color = color
        self._power_piece = False
        self._name = None
        self._symbol = None

    def get_color(self):
        """Returns color of piece - either BLACK or WHITE"""

        return self._color

    @staticmethod
    def is_empty():
        """Since the square is occupied by this piece, this Returns False"""

        return False

    def is_power_piece(self):
        """Returns True if piece is a power piece or False if not"""

        return self._power_piece

    def get_piece_name(self):
        """Returns True if piece is a King or False if not"""

        return self._name

    def get_symbol(self):
        """Returns the piece's symbol"""

        return self._symbol


class Pawn(Piece):
    """
    Represents a Pawn, which is a subclass of Piece.  The Pawn typically moves forward one square at a time, but can
    move either one or two squares on its initial move.  It cannot attack while moving forward and cannot jump a
    piece.  However, it can attack the opponent's piece by moving one space forward diagonally.
    """

    def __init__(self, color):
        """
        Inherits the color attribute from its parent Piece Class.  Uses the letter 'P' as its symbol, capital for the
        WHITE pieces and lower case for the BLACK pieces
        """

        super().__init__(color)
        self._name = 'PAWN'
        if self._color == 'WHITE':
            self._symbol = 'P'
        else:
            self._symbol = 'p'

    def is_movement_acceptable(self, start_location_object, end_location_object):
        """Determines whether proposed move is consistent with the rules of chess and, if so, returns True"""

        is_move_legal = False

        # Check if move is legal if it is white's turn
        if self._color == 'WHITE':
            # A single space forward is legal
            if (end_location_object.get_row() == start_location_object.get_row() + 1 and
                    end_location_object.get_piece().is_empty() and
                    end_location_object.get_column() == start_location_object.get_column()):
                is_move_legal = True

            # Two spaces forward is okay, provided it is the first move
            if (start_location_object.get_row() == 2 and end_location_object.get_row() == 4 and
                    end_location_object.get_piece().is_empty() and
                    end_location_object.get_column() == start_location_object.get_column()):
                is_move_legal = True

            # Single space diagonal move is okay, provided that an opponent's piece can be captured
            if (end_location_object.get_row() == start_location_object.get_row() + 1 and
                    abs(end_location_object.get_column() - start_location_object.get_column()) == 1 and
                    end_location_object.get_piece().get_color() == 'BLACK'):
                is_move_legal = True

        # Check if move is legal if it is black's turn
        if self._color == 'BLACK':
            # A single space forward is legal
            if (end_location_object.get_row() == start_location_object.get_row() - 1 and
                    end_location_object.get_piece().is_empty() and
                    end_location_object.get_column() == start_location_object.get_column()):
                is_move_legal = True

            # Two spaces forward is okay, provided it is the first move
            if (start_location_object.get_row() == 7 and end_location_object.get_row() == 5 and
                    end_location_object.get_piece().is_empty() and
                    end_location_object.get_column() == start_location_object.get_column()):
                is_move_legal = True

            # Single space diagonal move is okay, provided that an opponent's piece can be captured
            if (end_location_object.get_row() == start_location_object.get_row() - 1 and
                    abs(end_location_object.get_column() - start_location_object.get_column()) == 1 and
                    end_location_object.get_piece().get_color() == 'WHITE'):
                is_move_legal = True

        return is_move_legal


class Rook(Piece):
    """
    Represents a Rook, which is a subclass of Piece.  The Rook moves forward, backward and side to side in a straight
    line, but cannot move diagonally. It can move multiple squares.  It cannot jump other pieces.
    """

    def __init__(self, color):
        """
        Inherits the color attribute from its parent Piece Class.  Uses the letter 'R' as its symbol, capital for the
        WHITE pieces and lower case for the BLACK pieces.  Also sets power piece attribute to True.
        """

        super().__init__(color)
        self._name = 'ROOK'
        self._power_piece = True
        if self._color == 'WHITE':
            self._symbol = 'R'
        else:
            self._symbol = 'r'

    def is_movement_acceptable(self, start_location, end_location):
        """Determines whether proposed move is consistent with the rules of chess and, if so, returns True"""

        is_move_legal = False

        # Determine whether move is legal
        if (end_location.get_row() == start_location.get_row() or
                end_location.get_column() == start_location.get_column()):
            is_move_legal = True

        return is_move_legal


class Knight(Piece):
    """
    Represents a Knight, which is a subclass of Piece.  The Knight moves either forward/backward two squares and one
    square to the side, or to the side two squares and forward/backward one square.  The Knight can jump other pieces.
    """

    def __init__(self, color):
        """
        Inherits the color attribute from its parent Piece Class.  Uses the letter 'N' as its symbol, capital for the
        WHITE pieces and lower case for the BLACK pieces.  Sets the power piece attribute to True
        """

        super().__init__(color)
        self._name = 'KNIGHT'
        self._power_piece = True
        if self._color == 'WHITE':
            self._symbol = 'N'
        else:
            self._symbol = 'n'

    def is_movement_acceptable(self, start_location, end_location):
        """Determines whether proposed move is consistent with the rules of chess and, if so, returns True"""

        is_move_legal = False

        # Determine whether move is legal
        if ((end_location.get_row() == start_location.get_row() + 2 and
             end_location.get_column() == start_location.get_column() + 1) or
                (end_location.get_row() == start_location.get_row() + 2 and
                 end_location.get_column() == start_location.get_column() - 1) or
                (end_location.get_row() == start_location.get_row() - 2 and
                 end_location.get_column() == start_location.get_column() + 1) or
                (end_location.get_row() == start_location.get_row() - 2 and
                 end_location.get_column() == start_location.get_column() - 1) or
                (end_location.get_row() == start_location.get_row() + 1 and
                 end_location.get_column() == start_location.get_column() + 2) or
                (end_location.get_row() == start_location.get_row() + 1 and
                 end_location.get_column() == start_location.get_column() - 2) or
                (end_location.get_row() == start_location.get_row() - 1 and
                 end_location.get_column() == start_location.get_column() + 2) or
                (end_location.get_row() == start_location.get_row() - 1 and
                 end_location.get_column() == start_location.get_column() - 2)):
            is_move_legal = True

        return is_move_legal


class Bishop(Piece):
    """
    Represents a Bishop, which is a subclass of Piece.  The Bishop moves diagonally, but not horizontally or vertically.
    It can move multiple spaces.  It cannot jump other pieces.
    """

    def __init__(self, color):
        """
        Inherits the color attribute from its parent Piece Class.  Uses the letter 'B' as its symbol, capital for the
        WHITE pieces and lower case for the BLACK pieces.  Sets the power piece attribute to True
        """

        super().__init__(color)
        self._name = 'BISHOP'
        self._power_piece = True
        if self._color == 'WHITE':
            self._symbol = 'B'
        else:
            self._symbol = 'b'

    def is_movement_acceptable(self, start_location, end_location):
        """Determines whether proposed move is consistent with the rules of chess and, if so, returns True"""

        is_move_legal = False

        # Determine whether move is legal
        if (abs(end_location.get_row() - start_location.get_row()) ==
                abs(end_location.get_column() - start_location.get_column())):
            is_move_legal = True

        return is_move_legal


class Queen(Piece):
    """
    Represents a Queen, which is a subclass of Piece.  The Queen moves in any straight line direction - diagonally,
    horizontally or vertically.  It can move multiple spaces.  It cannot jump other pieces.
    """

    def __init__(self, color):
        """
        Inherits the color attribute from its parent Piece Class.  Uses the letter 'Q' as its symbol, capital for the
        WHITE piece and lower case for the BLACK piece.  Sets the power piece attribute to True.
        """

        super().__init__(color)
        self._name = 'QUEEN'
        self._power_piece = True
        if self._color == 'WHITE':
            self._symbol = 'Q'
        else:
            self._symbol = 'q'

    def is_movement_acceptable(self, start_location, end_location):
        """Determines whether proposed move is consistent with the rules of chess and, if so, returns True"""

        is_move_legal = False

        # Determine whether move is legal
        if (end_location.get_row() == start_location.get_row() or
                end_location.get_column() == start_location.get_column() or
                (abs(end_location.get_row() - start_location.get_row()) ==
                 abs(end_location.get_column() - start_location.get_column()))):
            is_move_legal = True

        return is_move_legal


class King(Piece):
    """
    Represents a King, which is a subclass of Piece.  The King moves one square in any direction.
    """

    def __init__(self, color):
        """
        Inherits the color attribute from its parent Piece Class.  Uses the letter 'K' as its symbol, capital for the
        WHITE pieces and lower case for the BLACK pieces.
        """

        super().__init__(color)
        self._name = 'KING'
        if self._color == 'WHITE':
            self._symbol = 'K'
        else:
            self._symbol = 'k'

    def is_movement_acceptable(self, start_location, end_location):
        """Determines whether proposed move is consistent with the rules of chess and, if so, returns True"""

        is_move_legal = False

        # Determine whether move is legal
        if (abs(end_location.get_row() - start_location.get_row()) <= 1 and
                abs(end_location.get_column() - start_location.get_column()) <= 1):
            is_move_legal = True

        return is_move_legal


class Falcon(Piece):
    """
    Represents a Falcon, which is a subclass of Piece.  The Falcon moves forward diagonally in a straight line, or
    backward vertically.  It cannot move horizontally.  It can move multiple squares, but cannot jump pieces.  The
    Falcon is not in play at the start of the game, but can be added on a player's turn to replace a power piece that
    has been captured by the opponent
    """

    def __init__(self, color):
        """
        Inherits the color attribute from its parent Piece Class.  Uses the letter 'F' as its symbol, capital for the
        WHITE piece and lower case for the BLACK piece.  Sets available attribute to True.
        """

        super().__init__(color)
        self._name = 'FALCON'
        self._available = True
        if self._color == 'WHITE':
            self._symbol = 'F'
        else:
            self._symbol = 'f'

    def is_available(self):
        """Returns True if the piece is available to be placed on the board"""

        return self._available

    def set_unavailable(self):
        """Sets available attribute to False"""

        self._available = False

    def is_movement_acceptable(self, start_location, end_location):
        """Determines whether proposed move is consistent with the rules of chess and, if so, returns True"""

        is_move_legal = False

        # Check to see if move is legal - if it is White's turn
        if self._color == 'WHITE':
            if (end_location.get_row() > start_location.get_row() and
                    abs(end_location.get_row() - start_location.get_row()) ==
                    abs(end_location.get_column() - start_location.get_column())):
                is_move_legal = True
            if (end_location.get_row() < start_location.get_row() and
                    end_location.get_column() == start_location.get_column()):
                is_move_legal = True

        # Check to see if move is legal - if it is Black's turn
        if self._color == 'BLACK':
            if (end_location.get_row() < start_location.get_row() and
                    abs(end_location.get_row() - start_location.get_row()) ==
                    abs(end_location.get_column() - start_location.get_column())):
                is_move_legal = True
            if (end_location.get_row() > start_location.get_row() and
                    end_location.get_column() == start_location.get_column()):
                is_move_legal = True

        return is_move_legal


class Hunter(Piece):
    """
    Represents a Hunter, which is a subclass of Piece.  The Hunter moves forward vertically in a straight line, or
    backward diagonally.  It cannot move horizontally.  It can move multiple squares, but cannot jump pieces.  The
    Hunter is not in play at the start of the game, but can be added on a player's turn to replace a power piece that
    has been captured by the opponent
    """

    def __init__(self, color):
        """
        Inherits the color attribute from its parent Piece Class.  Uses the letter 'H' as its symbol, capital for the
        WHITE piece and lower case for the BLACK piece.  Sets available attribute to True.
        """

        super().__init__(color)
        self._name = 'HUNTER'
        self._available = True
        if self._color == 'WHITE':
            self._symbol = 'H'
        else:
            self._symbol = 'h'

    def is_available(self):
        """Returns True if the piece is available to be placed on the board"""

        return self._available

    def set_unavailable(self):
        """Sets available attribute to False"""

        self._available = False

    def is_movement_acceptable(self, start_location, end_location):
        """Determines whether proposed move is consistent with the rules of chess and, if so, returns True"""

        is_move_legal = False

        # Check to see if move is legal - if it is White's turn
        if self._color == 'WHITE':
            if (end_location.get_row() > start_location.get_row() and
                    end_location.get_column() == start_location.get_column()):
                is_move_legal = True
            if (end_location.get_row() < start_location.get_row() and
                    abs(end_location.get_row() - start_location.get_row()) ==
                    abs(end_location.get_column() - start_location.get_column())):
                is_move_legal = True

        # Check to see if move is legal - if it is Black's turn
        if self._color == 'BLACK':
            if (end_location.get_row() < start_location.get_row() and
                    end_location.get_column() == start_location.get_column()):
                is_move_legal = True
            if (end_location.get_row() > start_location.get_row() and
                    abs(end_location.get_row() - start_location.get_row()) ==
                    abs(end_location.get_column() - start_location.get_column())):
                is_move_legal = True

        return is_move_legal


class Empty:
    """Represents an empty spot object that can be placed in a square object when it contains no pieces"""

    def __int__(self):
        """This class does not have any attributes"""

    @staticmethod
    def get_symbol():
        """Returns a 'empty space' character"""

        return ' '

    @staticmethod
    def is_empty():
        """Since the square is empty, this Returns True"""

        return True

    def get_color(self):
        """Do not return a color - an empty square does not have a piece with either color"""

        return


class Square:
    """Represents each square on a chess board"""

    def __init__(self, row, column, piece_object):
        """
        Defines each square by row number and column number attributes, which cannot be changed after a square object
        is created. Also has an attribute to hold a piece_object. If the square is empty, this will be the empty object.
        Otherwise, the piece_object attribute will be the piece located in that square.  There are methods to change the
        piece_object attribute
        """

        self._row = row
        self._column = column
        self._piece_object = piece_object

    def get_row(self):
        """Returns the square's row number (an integer 1-8)"""

        return self._row

    def get_column(self):
        """Return the square's column number (in integer 1-8)"""

        return self._column

    def get_piece(self):
        """Returns None if the square is empty.  If a piece is located in the square, it returns the piece object"""

        return self._piece_object

    def set_piece(self, piece_object):
        """Changes the piece reference to the given piece object"""

        self._piece_object = piece_object


class ChessVar:
    """Represents a game of the Falcon-Hunter variant of chess"""

    def __init__(self):
        """
        Define attributes that will need to be tracked during the course of the game, create all the piece objects
        that will be used in the game, define the square objects located on the board, and establish the initial setup
        of the board, with the appropriate piece objects being located on the appropriate square objects
        """

        self._game_state = 'UNFINISHED'
        self._white_turn = True
        self._power_pieces_taken_black = 0
        self._power_pieces_taken_white = 0

        # Create all the WHITE Pieces
        self._pawn_w1 = Pawn('WHITE')
        self._pawn_w2 = Pawn('WHITE')
        self._pawn_w3 = Pawn('WHITE')
        self._pawn_w4 = Pawn('WHITE')
        self._pawn_w5 = Pawn('WHITE')
        self._pawn_w6 = Pawn('WHITE')
        self._pawn_w7 = Pawn('WHITE')
        self._pawn_w8 = Pawn('WHITE')
        self._rook_w1 = Rook('WHITE')
        self._rook_w2 = Rook('WHITE')
        self._knight_w1 = Knight('WHITE')
        self._knight_w2 = Knight('WHITE')
        self._bishop_w1 = Bishop('WHITE')
        self._bishop_w2 = Bishop('WHITE')
        self._queen_w = Queen('WHITE')
        self._king_w = King('WHITE')
        self._falcon_w = Falcon('WHITE')
        self._hunter_w = Hunter('WHITE')

        # Create all the BLACK Pieces
        self._pawn_b1 = Pawn('BLACK')
        self._pawn_b2 = Pawn('BLACK')
        self._pawn_b3 = Pawn('BLACK')
        self._pawn_b4 = Pawn('BLACK')
        self._pawn_b5 = Pawn('BLACK')
        self._pawn_b6 = Pawn('BLACK')
        self._pawn_b7 = Pawn('BLACK')
        self._pawn_b8 = Pawn('BLACK')
        self._rook_b1 = Rook('BLACK')
        self._rook_b2 = Rook('BLACK')
        self._knight_b1 = Knight('BLACK')
        self._knight_b2 = Knight('BLACK')
        self._bishop_b1 = Bishop('BLACK')
        self._bishop_b2 = Bishop('BLACK')
        self._queen_b = Queen('BLACK')
        self._king_b = King('BLACK')
        self._falcon_b = Falcon('BLACK')
        self._hunter_b = Hunter('BLACK')

        # Create object for empty square
        self._empty = Empty()

        # Create a square object for each square on the board, identifying the piece it initially contains
        self._a1 = Square(1, 1, self._rook_w1)
        self._b1 = Square(1, 2, self._knight_w1)
        self._c1 = Square(1, 3, self._bishop_w1)
        self._d1 = Square(1, 4, self._queen_w)
        self._e1 = Square(1, 5, self._king_w)
        self._f1 = Square(1, 6, self._bishop_w2)
        self._g1 = Square(1, 7, self._knight_w2)
        self._h1 = Square(1, 8, self._rook_w2)
        self._a2 = Square(2, 1, self._pawn_w1)
        self._b2 = Square(2, 2, self._pawn_w2)
        self._c2 = Square(2, 3, self._pawn_w3)
        self._d2 = Square(2, 4, self._pawn_w4)
        self._e2 = Square(2, 5, self._pawn_w5)
        self._f2 = Square(2, 6, self._pawn_w6)
        self._g2 = Square(2, 7, self._pawn_w7)
        self._h2 = Square(2, 8, self._pawn_w8)
        self._a3 = Square(3, 1, self._empty)
        self._b3 = Square(3, 2, self._empty)
        self._c3 = Square(3, 3, self._empty)
        self._d3 = Square(3, 4, self._empty)
        self._e3 = Square(3, 5, self._empty)
        self._f3 = Square(3, 6, self._empty)
        self._g3 = Square(3, 7, self._empty)
        self._h3 = Square(3, 8, self._empty)
        self._a4 = Square(4, 1, self._empty)
        self._b4 = Square(4, 2, self._empty)
        self._c4 = Square(4, 3, self._empty)
        self._d4 = Square(4, 4, self._empty)
        self._e4 = Square(4, 5, self._empty)
        self._f4 = Square(4, 6, self._empty)
        self._g4 = Square(4, 7, self._empty)
        self._h4 = Square(4, 8, self._empty)
        self._a5 = Square(5, 1, self._empty)
        self._b5 = Square(5, 2, self._empty)
        self._c5 = Square(5, 3, self._empty)
        self._d5 = Square(5, 4, self._empty)
        self._e5 = Square(5, 5, self._empty)
        self._f5 = Square(5, 6, self._empty)
        self._g5 = Square(5, 7, self._empty)
        self._h5 = Square(5, 8, self._empty)
        self._a6 = Square(6, 1, self._empty)
        self._b6 = Square(6, 2, self._empty)
        self._c6 = Square(6, 3, self._empty)
        self._d6 = Square(6, 4, self._empty)
        self._e6 = Square(6, 5, self._empty)
        self._f6 = Square(6, 6, self._empty)
        self._g6 = Square(6, 7, self._empty)
        self._h6 = Square(6, 8, self._empty)
        self._a7 = Square(7, 1, self._pawn_b1)
        self._b7 = Square(7, 2, self._pawn_b2)
        self._c7 = Square(7, 3, self._pawn_b3)
        self._d7 = Square(7, 4, self._pawn_b4)
        self._e7 = Square(7, 5, self._pawn_b5)
        self._f7 = Square(7, 6, self._pawn_b6)
        self._g7 = Square(7, 7, self._pawn_b7)
        self._h7 = Square(7, 8, self._pawn_b8)
        self._a8 = Square(8, 1, self._rook_b1)
        self._b8 = Square(8, 2, self._knight_b1)
        self._c8 = Square(8, 3, self._bishop_b1)
        self._d8 = Square(8, 4, self._queen_b)
        self._e8 = Square(8, 5, self._king_b)
        self._f8 = Square(8, 6, self._bishop_b2)
        self._g8 = Square(8, 7, self._knight_b2)
        self._h8 = Square(8, 8, self._rook_b2)

        # Arrange board into a dictionary
        self._board = {
            'a1': self._a1, 'b1': self._b1, 'c1': self._c1, 'd1': self._d1,
            'e1': self._e1, 'f1': self._f1, 'g1': self._g1, 'h1': self._h1,
            'a2': self._a2, 'b2': self._b2, 'c2': self._c2, 'd2': self._d2,
            'e2': self._e2, 'f2': self._f2, 'g2': self._g2, 'h2': self._h2,
            'a3': self._a3, 'b3': self._b3, 'c3': self._c3, 'd3': self._d3,
            'e3': self._e3, 'f3': self._f3, 'g3': self._g3, 'h3': self._h3,
            'a4': self._a4, 'b4': self._b4, 'c4': self._c4, 'd4': self._d4,
            'e4': self._e4, 'f4': self._f4, 'g4': self._g4, 'h4': self._h4,
            'a5': self._a5, 'b5': self._b5, 'c5': self._c5, 'd5': self._d5,
            'e5': self._e5, 'f5': self._f5, 'g5': self._g5, 'h5': self._h5,
            'a6': self._a6, 'b6': self._b6, 'c6': self._c6, 'd6': self._d6,
            'e6': self._e6, 'f6': self._f6, 'g6': self._g6, 'h6': self._h6,
            'a7': self._a7, 'b7': self._b7, 'c7': self._c7, 'd7': self._d7,
            'e7': self._e7, 'f7': self._f7, 'g7': self._g7, 'h7': self._h7,
            'a8': self._a8, 'b8': self._b8, 'c8': self._c8, 'd8': self._d8,
            'e8': self._e8, 'f8': self._f8, 'g8': self._g8, 'h8': self._h8,
        }

    def get_game_state(self):
        """Return the game state attribute"""

        return self._game_state

    def make_move(self, start_location, end_location):
        """
        Takes in two locations on the board and determines whether the proposed move is valid.  If not, returns False.
        Otherwise, performs the requested move, performs a capture if appropriate, and determines whether opponent's
        King is captured.
        """

        # Confirm that start and end locations are valid squares.  If not, return False
        if start_location not in self._board or end_location not in self._board:
            return False

        # Confirm that game is not over yet.  If it is, return False
        if self._game_state != 'UNFINISHED':
            return False

        # Set variables to the value of the three relevant objects - start square, end square, and piece
        start_square_object = self._board[start_location]
        end_square_object = self._board[end_location]
        piece_object = start_square_object.get_piece()

        # Confirm that start location is not emtpy.  If it is, return False
        if piece_object.is_empty() is True:
            return False

        # Confirm that start location contains player's piece.  If not, return False
        if ((self._white_turn is True and piece_object.get_color() != 'WHITE') or
                (self._white_turn is False and piece_object.get_color() != 'BLACK')):
            return False

        # Confirm that player making move does not have a piece in the end location.  If he or she does, return False
        if (end_square_object.get_piece().is_empty() is False and
                end_square_object.get_piece().get_color() == piece_object.get_color()):
            return False

        # Call is_valid_move method for the relevant piece object to confirm that move is legal.  If not, return False
        if piece_object.is_movement_acceptable(start_square_object, end_square_object) is False:
            return False

        # Determine whether requested move illegally jumps over another piece.  If so, return False
        if (piece_object.get_piece_name() != 'KNIGHT' and
                (abs(end_square_object.get_row() - start_square_object.get_row()) > 1 or
                 abs(end_square_object.get_column() - start_square_object.get_column()) > 1)):

            # Set variables that will be used to check the squares located between the start and end locations
            test_square_row = start_square_object.get_row()
            test_square_column = start_square_object.get_column()
            target_square_row = end_square_object.get_row()
            target_square_column = end_square_object.get_column()

            # Iterate through the squares between the start and end locations, checking each square to confirm its empty
            while test_square_row != target_square_row or test_square_column != target_square_column:

                # Adjust the test square coordinates so that it is one square closer to target square
                if target_square_row > test_square_row:
                    test_square_row += 1
                if target_square_row < test_square_row:
                    test_square_row -= 1
                if target_square_column > test_square_column:
                    test_square_column += 1
                if target_square_column < test_square_column:
                    test_square_column -= 1

                # Determine whether test square made it to the target square without jumping any pieces
                if test_square_row == target_square_row and test_square_column == target_square_column:
                    continue

                # Determine whether test square is empty, if not return False
                if self.is_square_empty(test_square_row, test_square_column) is False:
                    return False

        # If all of the above conditions are met, the proposed move is valid.  Continue with the proposed move.
        # Determine whether one of the opponent's pieces is in the end location.  If so, capture the opponent's piece
        if ((self._white_turn is True and end_square_object.get_piece().get_color() == 'BLACK') or
                (self._white_turn is False and end_square_object.get_piece().get_color() == 'WHITE')):

            # If the captured piece is a power piece, add one to the opponent's power pieces taken variable
            if end_square_object.get_piece().is_power_piece() is True:
                if end_square_object.get_piece().get_color() == 'BLACK':
                    self._power_pieces_taken_black += 1
                else:
                    self._power_pieces_taken_white += 1

            # If the captured piece is the King, update date game state to 'WHITE_WON' or 'BLACK_WON' as appropriate
            if end_square_object.get_piece().get_piece_name() == 'KING':
                if end_square_object.get_piece().get_color() == 'BLACK':
                    self._game_state = 'WHITE_WON'
                else:
                    self._game_state = 'BLACK_WON'

        # Update the end location square's piece reference to the player's piece
        end_square_object.set_piece(piece_object)

        # Update the start location square's piece reference to empty
        start_square_object.set_piece(self._empty)

        # Toggle the white_turn attribute
        if self._white_turn is True:
            self._white_turn = False
        else:
            self._white_turn = True

        return True

    def enter_fairy_piece(self, identity_of_piece, location):
        """
        Takes in the identity of the fairy piece to be added into play and the square on which it will enter into play.
        Confirms that the piece is appropriate and that it is appropriate to add the piece to the given square.  If so,
        the fairy piece is added into play.
        """

        # If location is not on board, return False
        if location not in self._board:
            return False

        # If appropriate power_pieces_taken variable is 0, return False
        if self._white_turn is True and self._power_pieces_taken_white == 0:
            return False

        if self._white_turn is False and self._power_pieces_taken_black == 0:
            return False

        # Confirm that game is not over yet.  If it is, return False
        if self._game_state != 'UNFINISHED':
            return False

        # Set variables to the value of the two relevant objects - piece and location
        # Set variable for White Fairy Piece
        if self._white_turn is True:
            if identity_of_piece == 'H':
                new_piece_object = self._hunter_w
            elif identity_of_piece == 'F':
                new_piece_object = self._falcon_w
            else:
                return False

        # Set Black Fairy Piece
        if self._white_turn is False:
            if identity_of_piece == 'h':
                new_piece_object = self._hunter_b
            elif identity_of_piece == 'f':
                new_piece_object = self._falcon_b
            else:
                return False

        # Set variable for new_square_object
        new_square_object = self._board[location]

        # If given piece's available attribute is False, return False
        if new_piece_object.is_available() is False:
            return False

        # If given location is not in one of the two rows in may enter, return False
        if self._white_turn is True and new_square_object.get_row() > 2:
            return False

        if self._white_turn is False and new_square_object.get_row() < 7:
            return False

        # If given location is already occupied by a piece, return False
        if self.is_square_empty(new_square_object.get_row(), new_square_object.get_column()) is False:
            return False

        # If all of the above conditions are met, the proposed fairy piece addition is valid.  Proceed with move.
        # Update location square's piece reference to the given fairy piece
        new_square_object.set_piece(new_piece_object)

        # Set Fairy Piece's available attribute to False
        new_piece_object.set_unavailable()

        # Subtract one (1) from player's power_pieces_ taken variable
        if self._white_turn is True:
            self._power_pieces_taken_white -= 1
        else:
            self._power_pieces_taken_black -= 1

        # Toggle white_turn attribute
        if self._white_turn is True:
            self._white_turn = False
        else:
            self._white_turn = True

        return True

    def display_board(self):
        """Displays the chess board"""

        print('\n     Falcon-Hunter Variant of Chess\n')
        print('     a   b   c   d   e   f   g   h')
        print('   ---------------------------------')
        print('8  |', self._board['a8'].get_piece().get_symbol(), end=" ")
        print('|', self._board['b8'].get_piece().get_symbol(), end=" ")
        print('|', self._board['c8'].get_piece().get_symbol(), end=" ")
        print('|', self._board['d8'].get_piece().get_symbol(), end=" ")
        print('|', self._board['e8'].get_piece().get_symbol(), end=" ")
        print('|', self._board['f8'].get_piece().get_symbol(), end=" ")
        print('|', self._board['g8'].get_piece().get_symbol(), end=" ")
        print('|', self._board['h8'].get_piece().get_symbol(), '|')
        print('   ---------------------------------')
        print('7  |', self._board['a7'].get_piece().get_symbol(), end=" ")
        print('|', self._board['b7'].get_piece().get_symbol(), end=" ")
        print('|', self._board['c7'].get_piece().get_symbol(), end=" ")
        print('|', self._board['d7'].get_piece().get_symbol(), end=" ")
        print('|', self._board['e7'].get_piece().get_symbol(), end=" ")
        print('|', self._board['f7'].get_piece().get_symbol(), end=" ")
        print('|', self._board['g7'].get_piece().get_symbol(), end=" ")
        print('|', self._board['h7'].get_piece().get_symbol(), '|')
        print('   ---------------------------------')
        print('6  |', self._board['a6'].get_piece().get_symbol(), end=" ")
        print('|', self._board['b6'].get_piece().get_symbol(), end=" ")
        print('|', self._board['c6'].get_piece().get_symbol(), end=" ")
        print('|', self._board['d6'].get_piece().get_symbol(), end=" ")
        print('|', self._board['e6'].get_piece().get_symbol(), end=" ")
        print('|', self._board['f6'].get_piece().get_symbol(), end=" ")
        print('|', self._board['g6'].get_piece().get_symbol(), end=" ")
        print('|', self._board['h6'].get_piece().get_symbol(), '|')
        print('   ---------------------------------')
        print('5  |', self._board['a5'].get_piece().get_symbol(), end=" ")
        print('|', self._board['b5'].get_piece().get_symbol(), end=" ")
        print('|', self._board['c5'].get_piece().get_symbol(), end=" ")
        print('|', self._board['d5'].get_piece().get_symbol(), end=" ")
        print('|', self._board['e5'].get_piece().get_symbol(), end=" ")
        print('|', self._board['f5'].get_piece().get_symbol(), end=" ")
        print('|', self._board['g5'].get_piece().get_symbol(), end=" ")
        print('|', self._board['h5'].get_piece().get_symbol(), '|')
        print('   ---------------------------------')
        print('4  |', self._board['a4'].get_piece().get_symbol(), end=" ")
        print('|', self._board['b4'].get_piece().get_symbol(), end=" ")
        print('|', self._board['c4'].get_piece().get_symbol(), end=" ")
        print('|', self._board['d4'].get_piece().get_symbol(), end=" ")
        print('|', self._board['e4'].get_piece().get_symbol(), end=" ")
        print('|', self._board['f4'].get_piece().get_symbol(), end=" ")
        print('|', self._board['g4'].get_piece().get_symbol(), end=" ")
        print('|', self._board['h4'].get_piece().get_symbol(), '|')
        print('   ---------------------------------')
        print('3  |', self._board['a3'].get_piece().get_symbol(), end=" ")
        print('|', self._board['b3'].get_piece().get_symbol(), end=" ")
        print('|', self._board['c3'].get_piece().get_symbol(), end=" ")
        print('|', self._board['d3'].get_piece().get_symbol(), end=" ")
        print('|', self._board['e3'].get_piece().get_symbol(), end=" ")
        print('|', self._board['f3'].get_piece().get_symbol(), end=" ")
        print('|', self._board['g3'].get_piece().get_symbol(), end=" ")
        print('|', self._board['h3'].get_piece().get_symbol(), '|')
        print('   ---------------------------------')
        print('2  |', self._board['a2'].get_piece().get_symbol(), end=" ")
        print('|', self._board['b2'].get_piece().get_symbol(), end=" ")
        print('|', self._board['c2'].get_piece().get_symbol(), end=" ")
        print('|', self._board['d2'].get_piece().get_symbol(), end=" ")
        print('|', self._board['e2'].get_piece().get_symbol(), end=" ")
        print('|', self._board['f2'].get_piece().get_symbol(), end=" ")
        print('|', self._board['g2'].get_piece().get_symbol(), end=" ")
        print('|', self._board['h2'].get_piece().get_symbol(), '|')
        print('   ---------------------------------')
        print('1  |', self._board['a1'].get_piece().get_symbol(), end=" ")
        print('|', self._board['b1'].get_piece().get_symbol(), end=" ")
        print('|', self._board['c1'].get_piece().get_symbol(), end=" ")
        print('|', self._board['d1'].get_piece().get_symbol(), end=" ")
        print('|', self._board['e1'].get_piece().get_symbol(), end=" ")
        print('|', self._board['f1'].get_piece().get_symbol(), end=" ")
        print('|', self._board['g1'].get_piece().get_symbol(), end=" ")
        print('|', self._board['h1'].get_piece().get_symbol(), '|')
        print('   ---------------------------------')

    def is_square_empty(self, given_row, given_column):
        """
        Takes in integers representing the row and column of a square on the board and determines whether that square
        is empty.  Returns True if the square is empty and False if a piece occupies the square
        """

        game_board = self._board
        for square in game_board.values():
            if square.get_row() == given_row and square.get_column() == given_column:
                return square.get_piece().is_empty()


def main():
    """
    Main portion of the program that will set up the board when a ChessVar() is assigned to a variable, and will
    accept commands to make moves, add fairy pieces, return game status, and display the board
    """

if __name__ == '__main__':
    main()
