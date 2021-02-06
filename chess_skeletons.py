

class ChessBoard(object):
    """
    """
    def __init__(self, size=(8, 8), board=None, pieces=None, dead_pieces=None, mode="default"):
        """
        """
        self._board = board
        self._size = size # attributes retained by the class need the self reference also
        self._pieces = pieces
        self._dead_pieces = dead_pieces

        self._generate_board_state(mode=mode) # using functions for initialization can be good practice

    def _get_size(self):
        return self._size # how to access class attributes some where else in the object

    def _generate_board_state(self, mode="default"):
        self._board = []
        for rank in range(self._size[0]):
            self._board.append([])
            for file_ in range(self._size[1]):
                if (rank + file_) % 2 == 0:
                    self._board[rank].append(Square('black'))
                else:
                    self._board[rank].append(Square('white'))

        if mode == "default":
            self._generate_default_board() # calling functions inside others can make your code more concise and clean
        elif mode == "random":
            self._generate_random_board()

    def _generate_default_board(self):
        self._pieces = {'white': [],
                        'black': []}
        self._dead_pieces = {'white': [],
                             'black': []}
        power_pieces = {0: Rook, 1: Knight, 2: Bishop, 3: Queen,
                        4: King, 5: Bishop, 6: Knight, 7: Rook}
        for rank in range(self._size[0]):
            for file_ in range(self._size[1]):
                if rank == 1:
                    color = 'white'
                    piece = Pawn(position=(rank, file_), color=color)
                elif rank == 6:
                    color = 'black'
                    piece = Pawn(position=(rank, file_), color=color)
                elif rank == 0:
                    color = 'white'
                    piece = power_pieces[file_](position=(rank, file_), color=color)
                elif rank == 7:
                    color = 'black'
                    piece = power_pieces[file_](position=(rank, file_), color=color)
                else:
                    piece = None
                if piece != None:
                    self._pieces[color].append(piece)

                self._board[rank][file_]._piece = piece

    def __repr__(self, view='white'):
        repr_string = ""
        if view == 'white':
            for rank in range(len(self._board)-1, -1, -1):
                repr_string += str(self._board[rank]) + '\n'
        elif view == 'black':
            for rank in range(len(self._board)):
                repr_string += str(self._board[rank][::-1]) + '\n'
        return repr_string

    def __str__(self):
        return self.__repr__()

    def _visualize(self, view='white'):
        return self.__repr__(view=view)



class Square(object):
    def __init__(self, color, piece=None):
        self._color = color
        self._piece = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self._piece == None:
            return self._color[0]
        return str(self._piece)


class Piece(object):    # truth be told, I don't know what (object) does because they all should inherit from object
    """
    """
    def __init__(self, position, color, player=None, ptype='Piece'): # abstract definition that can be called in child class
        """
        """
        self._position = position
        self._player = player
        self._color = color
        self._ptype = ptype

    def _move(self):    # abstract definition to be overloaded
        pass

    def _attack(self):
        pass

    def _die(self):     # abstract method, may not be needed
        pass

    def _get_moves(self):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self._ptype[0]


class Pawn(Piece):
    """
    """
    def __init__(self, position, color, player=None):
        """
        """
        super(Pawn, self).__init__(position=position, color=color, player=player,
            ptype='Pawn')    # calling parent init function


class Knight(Piece):
    """
    """
    def __init__(self, position, color, player=None):
        """
        """
        super(Knight, self).__init__(position=position, color=color, player=player,
            ptype='knight')   # this also give an instance the self._position attribute


class Bishop(Piece):
    """
    """
    def __init__(self, position, color, player=None):
        """
        """
        super(Bishop, self).__init__(position=position, color=color, player=player,
            ptype='Bishop')


class Rook(Piece):
    """
    """
    def __init__(self, position, color, player=None):
        """
        """
        super(Rook, self).__init__(position=position, color=color, player=player,
            ptype='Rook')


class Queen(Piece):
    """
    """
    def __init__(self, position, color, player=None):
        """
        """
        super(Queen, self).__init__(position=position, color=color, player=player,
            ptype='Queen')


class King(Piece):
    """
    """
    def __init__(self, position, color, player=None):
        """
        """
        super(King, self).__init__(position=position, color=color, player=player,
            ptype='King')


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
    print(chess_board0)
    piece = Pawn((0, 1), "white")
