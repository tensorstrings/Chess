

class ChessBoard(object):
    """
    """
    def __init__(self, pieces=None, dead_pieces=None, size=(8, 8), mode="default"):
        """
        """
        self._pieces = pieces
        self._size = size # attributes retained by the class need the self reference also
        self._dead_pieces = dead_pieces

        self._generate_board_state(mode=mode) # using functions for initialization can be good practice

    def _get_size(self):
        return self._size # how to access class attributes some where else in the object

    def _generate_board_state(self, mode="default"):
        if mode == "default":
            self._generate_default_board() # calling functions inside others can make your code more concise and clean
        elif mode == "random":
            self._generate_random_board()

    def _generate_default_board(self):
        pass


class Piece(object):    # truth be told, I don't know what (object) does because they all should inherit from object
    """
    """
    def __init__(self, position, player, color, board): # abstract definition that can be called in child class
        """
        """
        self._position = position
        self._player = player
        self._color = color
        self._board = board

    def _move(self):    # abstract definition to be overloaded
        pass

    def _attack(self):
        pass

    def _die(self):     # abstract method, may not be needed
        pass

    def _get_moves(self):
        pass


class Pawn(Piece):
    """
    """
    def __init__(self, position):
        """
        """
        super(Pawn, self).__init__(position=position)    # calling parent init function


class Knight(Piece):
    """
    """
    def __init__(self, position):
        """
        """
        super(Knight, self).__init__(position=position)   # this also give an instance the self._position attribute


class Bishop(Piece):
    """
    """
    def __init__(self, position):
        """
        """
        super(Bishop, self).__init__(position=position)


class Rook(Piece):
    """
    """
    def __init__(self, position):
        """
        """
        super(Rook, self).__init__(position=position)


class Queen(Piece):
    """
    """
    def __init__(self, position):
        """
        """
        super(Queen, self).__init__(position=position)


class King(Piece):
    """
    """
    def __init__(self, position):
        """
        """
        super(King, self).__init__(position=position)


class Player(object):
    """Class player holds the methods for guided interactions with the board
    and pieces. This will be concrete in that the player can interact via
    the object, but abstract in that another class will inherit functionality
    but override relevant functions for agent interfacing

    attributes:

    methods:
    """
    def __init__(self): # note: every class function should use the 'self' reference
        """Class initialization method. This is called at object instantiation.
        Initial attributes are usually set here. Docstrings are usually used
        to describe functionality.
        """
        pass


class AgentPlayer(object):
    """
    """
    def __init__(self):
        """
        """
        pass


if __name__ == "__main__": # this code only runs if you run this file (python chess_skeletons.py)
    chess_board0 = ChessBoard()             # instantiates a chess board
    chess_board1 = ChessBoard((8,8))        # instantiates one just like it
    chess_board1 = ChessBoard(size=(8,8))   # instantiates one also just like it
