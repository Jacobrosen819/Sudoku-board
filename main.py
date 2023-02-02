import random
#row one numbers 
sudoku_board_row_1_spot_1 = 0
sudoku_board_row_1_spot_2 = 0
sudoku_board_row_1_spot_3 = 0
sudoku_board_row_1_spot_4 = 0
sudoku_board_row_1_spot_5 = 0
sudoku_board_row_1_spot_6 = 0
sudoku_board_row_1_spot_7 = 0
sudoku_board_row_1_spot_8 = 0
sudoku_board_row_1_spot_9 = 0
num_place_1= 0

#row two numbers
sudoku_board_row_2_spot_1 = 0
sudoku_board_row_2_spot_2 = 0
sudoku_board_row_2_spot_3 = 0
sudoku_board_row_2_spot_4 = 0
sudoku_board_row_2_spot_5 = 0
sudoku_board_row_2_spot_6 = 0
sudoku_board_row_2_spot_7 = 0
sudoku_board_row_2_spot_8 = 0
sudoku_board_row_2_spot_9 = 0
num_place_2= 0

#row three numbers
sudoku_board_row_3_spot_1 = 0
sudoku_board_row_3_spot_2 = 0
sudoku_board_row_3_spot_3 = 0
sudoku_board_row_3_spot_4 = 0
sudoku_board_row_3_spot_5 = 0
sudoku_board_row_3_spot_6 = 0
sudoku_board_row_3_spot_7 = 0
sudoku_board_row_3_spot_8 = 0
sudoku_board_row_3_spot_9 = 0
num_place_3= 0

first_square_break = "__________________________________"

sudoku_board_row_1_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_board_row_2_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_board_row_3_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sudoku_board_square_1_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_board_square_2_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku_board_square_3_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]

square_number= 0
sudoku_board_row_1_Numbers = []
sudoku_board_row_2_Numbers = []
sudoku_board_row_3_Numbers = []

while len(sudoku_board_row_1_Numbers)!= 9:  
  num_place_1 =  random.choice(sudoku_board_row_1_int)
  sudoku_board_row_1_Numbers.append(num_place_1)
  sudoku_board_row_1_int.remove(num_place_1)
  
  square_number += 1
  if square_number <= 3:
    sudoku_board_square_1_int.remove(num_place_1)
  elif square_number <= 6:
    sudoku_board_square_2_int.remove(num_place_1)
  else:
    sudoku_board_square_3_int.remove(num_place_1)
     
#sudoku_board_row_1_Numbers.append(random.choice(sudoku_board_row_1_int))


while len(sudoku_board_row_2_Numbers)!= 9:
  square_number += 1
  if square_number <= 12:
    num_place_2 =  random.choice(sudoku_board_square_1_int)
    sudoku_board_row_2_Numbers.append(num_place_2)
    sudoku_board_square_1_int.remove(num_place_2)
  elif square_number <= 15:
    num_place_2 =  random.choice(sudoku_board_square_2_int)
    sudoku_board_row_2_Numbers.append(num_place_2)
    sudoku_board_square_2_int.remove(num_place_2)
  else:
    num_place_2 =  random.choice(sudoku_board_square_3_int)
    sudoku_board_row_2_Numbers.append(num_place_2)
    sudoku_board_square_3_int.remove(num_place_2)

while len(sudoku_board_row_3_Numbers)!= 9:
  square_number += 1 
  if square_number <= 21:
    num_place_3 =  random.choice(sudoku_board_square_1_int)
    sudoku_board_row_3_Numbers.append(num_place_3)
    sudoku_board_square_1_int.remove(num_place_3)
  elif square_number <= 24:
    num_place_3 =  random.choice(sudoku_board_square_2_int)
    sudoku_board_row_3_Numbers.append(num_place_3)
    sudoku_board_square_2_int.remove(num_place_3) 
  else:
    num_place_3 =  random.choice(sudoku_board_square_3_int)
    sudoku_board_row_3_Numbers.append(num_place_3)
    sudoku_board_square_3_int.remove(num_place_3)

#print(sudoku_board_row_1_Numbers[0]) #test

sudoku_board_row_1_spot_1 = sudoku_board_row_1_Numbers[0]
sudoku_board_row_1_spot_2 = sudoku_board_row_1_Numbers[1]
sudoku_board_row_1_spot_3 = sudoku_board_row_1_Numbers[2]
sudoku_board_row_1_spot_4 = sudoku_board_row_1_Numbers[3]
sudoku_board_row_1_spot_5 = sudoku_board_row_1_Numbers[4]
sudoku_board_row_1_spot_6 = sudoku_board_row_1_Numbers[5]
sudoku_board_row_1_spot_7 = sudoku_board_row_1_Numbers[6]
sudoku_board_row_1_spot_8 = sudoku_board_row_1_Numbers[7]
sudoku_board_row_1_spot_9 = sudoku_board_row_1_Numbers[8]

sudoku_board_row_1 = [[sudoku_board_row_1_spot_1, sudoku_board_row_1_spot_2, sudoku_board_row_1_spot_3] , [sudoku_board_row_1_spot_4, sudoku_board_row_1_spot_5, sudoku_board_row_1_spot_6] , [sudoku_board_row_1_spot_7, sudoku_board_row_1_spot_8, sudoku_board_row_1_spot_9]]

sudoku_board_row_2_spot_1 = sudoku_board_row_2_Numbers[0]
sudoku_board_row_2_spot_2 = sudoku_board_row_2_Numbers[1]
sudoku_board_row_2_spot_3 = sudoku_board_row_2_Numbers[2]
sudoku_board_row_2_spot_4 = sudoku_board_row_2_Numbers[3]
sudoku_board_row_2_spot_5 = sudoku_board_row_2_Numbers[4]
sudoku_board_row_2_spot_6 = sudoku_board_row_2_Numbers[5]
sudoku_board_row_2_spot_7 = sudoku_board_row_2_Numbers[6]
sudoku_board_row_2_spot_8 = sudoku_board_row_2_Numbers[7]
sudoku_board_row_2_spot_9 = sudoku_board_row_2_Numbers[8]

sudoku_board_row_2 = [[sudoku_board_row_2_spot_1, sudoku_board_row_2_spot_2, sudoku_board_row_2_spot_3], [sudoku_board_row_2_spot_4, sudoku_board_row_2_spot_5, sudoku_board_row_2_spot_6], [sudoku_board_row_2_spot_7, sudoku_board_row_2_spot_8, sudoku_board_row_2_spot_9]]

sudoku_board_row_3_spot_1 = sudoku_board_row_3_Numbers[0]
sudoku_board_row_3_spot_2 = sudoku_board_row_3_Numbers[1]
sudoku_board_row_3_spot_3 = sudoku_board_row_3_Numbers[2]
sudoku_board_row_3_spot_4 = sudoku_board_row_3_Numbers[3]
sudoku_board_row_3_spot_5 = sudoku_board_row_3_Numbers[4]
sudoku_board_row_3_spot_6 = sudoku_board_row_3_Numbers[5]
sudoku_board_row_3_spot_7 = sudoku_board_row_3_Numbers[6]
sudoku_board_row_3_spot_8 = sudoku_board_row_3_Numbers[7]
sudoku_board_row_3_spot_9 = sudoku_board_row_3_Numbers[8]

sudoku_board_row_3 = [[sudoku_board_row_3_spot_1, sudoku_board_row_3_spot_2, sudoku_board_row_3_spot_3], [sudoku_board_row_3_spot_4, sudoku_board_row_3_spot_5, sudoku_board_row_3_spot_6], [sudoku_board_row_3_spot_7, sudoku_board_row_3_spot_8, sudoku_board_row_3_spot_9]]


#print(sudoku_board_row_1_Numbers) #test
print (sudoku_board_row_1)
print (sudoku_board_row_2)
print (sudoku_board_row_3)
print(first_square_break)
""""
print (sudoku_board_square_1_int)
print (sudoku_board_square_2_int)
print (sudoku_board_square_3_int)
"""
#print(sudoku_board_row_1_spot_1) #test