'''Script to calculate unique knight forks given the knights position'''

import math

class ChessBoard():
  
  def __init__(self):
    print('Constructing board...')
    length = 8
    self.board = [0 for _ in range(length) for _ in range(length)]


  def get_legal_knight_moves(self, position):
    '''Method to return the square coordinates which are
    valid for a knight given the knight's position'''
    x, y = position
    possible_moves = [(-1, -2), (-1, 2), (1, -2), (1, 2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    possible_squares = []
    for del_x, del_y in possible_moves:
      if abs(x + del_x) < 8 and abs(y + del_y) < 8:
        possible_squares.append((x + del_x, y + del_y))
    return possible_squares

  def convert_to_standard_notation(self, position):
    x, y = position
    return f'{chr(ord("a") + x)}{y + 1}'

  def convert_to_coordinates(self, position):
    x = ord(position[0]) - ord('a')
    y = int(position[1]) - 1
    return (x, y)
  
  @staticmethod
  def square_root_of(number):
    '''Calculate square root'''
    if number < 0:
      print('I am not designed to handle negative numbers. Stay Positive, Man')
    return math.sqrt(number)

  def get_distances(self, position_of_knight='d4'):
    '''Use distance formula to get distances between two points'''
    x_knight, y_knight = self.convert_to_coordinates(position_of_knight)
    possible_squares = self.get_legal_knight_moves((x_knight, y_knight))
    x_R, y_R = (x_knight + 2, y_knight + 1)
    reference_point = self.convert_to_standard_notation((x_R, y_R))
    for x, y in possible_squares:
      distance_from_R = self.square_root_of((x - x_R) ** 2 + (y - y_R) ** 2)
      print(f'distance from {reference_point} to {self.convert_to_standard_notation((x, y))}: {distance_from_R}')


def main():
  '''Main method'''
  board = ChessBoard()
  board.get_distances('d4')

if __name__ == '__main__':
  main()
