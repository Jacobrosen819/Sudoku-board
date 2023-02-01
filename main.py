import random

sudoku_board_row_1_spot_1 = 0
sudoku_board_row_1_spot_2 = 0
sudoku_board_row_1_spot_3 = 0
sudoku_board_row_1_spot_4 = 0
sudoku_board_row_1_spot_5 = 0
sudoku_board_row_1_spot_6 = 0
sudoku_board_row_1_spot_7 = 0
sudoku_board_row_1_spot_8 = 0
sudoku_board_row_1_spot_9 = 0

sudoku_board_row_1 = [[sudoku_board_row_1_spot_1, sudoku_board_row_1_spot_2, sudoku_board_row_1_spot_3] , [sudoku_board_row_1_spot_4, sudoku_board_row_1_spot_5, sudoku_board_row_1_spot_6] , [sudoku_board_row_1_spot_7, sudoku_board_row_1_spot_8, sudoku_board_row_1_spot_9]]

sudoku_board_row_1_Numbers = []

while len(sudoku_board_row_1_Numbers)!= 9:
    sudoku_board_row_1_Numbers.append(random.randint(1,9))
  if sudoku_board_row_1_Numbers[0] == sudoku_board_row_1_Numbers[1]:
    sudoku_board_row_1_Numbers.pop(0)
  else:
    break

print(sudoku_board_row_1_Numbers[0])

sudoku_board_row_1_spot_1 = sudoku_board_row_1_Numbers[0]
sudoku_board_row_1_spot_2 = sudoku_board_row_1_Numbers[1]
sudoku_board_row_1_spot_3 = sudoku_board_row_1_Numbers[2]
sudoku_board_row_1_spot_4 = sudoku_board_row_1_Numbers[3]
sudoku_board_row_1_spot_5 = sudoku_board_row_1_Numbers[4]
sudoku_board_row_1_spot_6 = sudoku_board_row_1_Numbers[5]
sudoku_board_row_1_spot_7 = sudoku_board_row_1_Numbers[6]
sudoku_board_row_1_spot_8 = sudoku_board_row_1_Numbers[7]
sudoku_board_row_1_spot_9 = sudoku_board_row_1_Numbers[8]

print(sudoku_board_row_1_Numbers)
print (sudoku_board_row_1)