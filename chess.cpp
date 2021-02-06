#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>


class ChessBoard{
  enum class Turn {white, black} turn;
  enum class Piece {king, queen, white_pawn, black_pawn, rook, bishop, knight};
  static map<Piece,int> pieceValues;
  bool show_coordinates false;
}
