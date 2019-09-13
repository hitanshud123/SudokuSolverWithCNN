import copy
import math
import imgProcessing
import os

def is_valid_input(inputb):
    if (len(inputb) != 81):
        return False
        
    for i in inputb:
        if (i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9'):
            return False
    
    return True

def manual_input():
    sudoku_code = input('Input:\n')
    while(not is_valid_input(sudoku_code)):
        print('\nInvalid input')
        sudoku_code = input('Input:\n')
    return sudoku_code

def image_input():
    img_dir = input('\nEnter image directory: ')
    while(not os.path.exists(img_dir)):
        print('\nInvalid Directory')
        img_dir = input('Enter image directory: ')    
    inputb = imgProcessing.getInput(img_dir)
    return inputb

def parse_board(inputb):
    board = []
    k = 0;
    for i in range(int(math.sqrt(len(inputb)))):
        board.append([])
        for j in range(int(math.sqrt(len(inputb)))):
            board[i].append(int(inputb[k]))
            k += 1 
    return board
        
def edit_board(board, edits):
    edits = edits.split(';')
    for edit in edits:
        edit = edit.split(',')
        board[int(edit[0])-1][int(edit[1])-1] = int(edit[2])

def print_board(board, title):
    print(title)
    for i in range(len(board)):
        if (i%3 == 0):
            print('--------------------------')
        for j in range(len(board[i])):
            if (j%3 == 0):
                print('| ', end='')
            if (board[i][j] == 0):
                print('_ ', end='')
            else:
                print(str(board[i][j])+' ',end='')
        print('| ')
    if(i == 8):
        print('--------------------------')       
            

def is_valid(board, value, pos):
    for i in range(len(board[pos[0]])):
        if (i != pos[1]) and (board[pos[0]][i] == value):
            return False

    for i in range(len(board)):
        if (i != pos[0]) and (board[i][pos[1]] == value):
            return False
    
    for i in range(pos[0]//3*3, pos[0]//3*3+3):
        for j in range(pos[1]//3*3, pos[1]//3*3+3):
            if ((i,j) != pos) and (board[i][j] == value):
                return False
    
    return True

    
def solve_board(board, iterations):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == 0):
                for k in range(1,10):
                    if(is_valid(board, k, (i,j))):
                        board[i][j] = k
                        if(solve_board(board, iterations+1)):
                            return True
                        board[i][j] = 0
                return False
    return True


def main():

    input_type = int(input('\nSelect your input type (1=manual, 2=image):'))
    while(input_type != 1 and input_type != 2):
        print('\nInvalid input')
        input_type = int(input('Select your input type (1=manual, 2=image):'))
    
    if(input_type == 1):
        inputb = manual_input()
    else:
        inputb = image_input()

    board = parse_board(inputb)
    print_board(board, '\n\nYour Input:')

    reinput = 1
    while(reinput != 3):
        reinput = int(input('\nEnter 1 to re-input, Enter 2 to edit, Enter 3 to continue:'))
        if (reinput == 1):
            input_type = int(input('\nSelect your input type (1=manual, 2=image):'))
            while(input_type != 1 and input_type != 2):
                print('\nInvalid input')
                input_type = int(input('Select your input type (1=manual, 2=image):'))
            
            if(input_type == 1):
                inputb = manual_input()
            else:
                inputb = image_input()

            board = parse_board(inputb)
            print_board(board, '\n\nYour Input:')


        if (reinput == 2):
            edits = input('\nEnter your edits:\n')
            edit_board(board, edits)
            print_board(board, '\n\nYour Input:')



    solution = copy.deepcopy(board)  
    print_board(board, '\n\nYour Input:')
    input('Hit Enter to solve')
    print('Solving...')
    solved = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(not is_valid(board, board[i][j], (i,j)) and (board[i][j] != 0)):
                solved = False
    if(solved):
        solved = solve_board(solution,1)
    if(solved == False):
        print('\nThis sudoku grid is unsolvable')
    else:
        print_board(solution, '\n\nThe Solution:')

if __name__ == '__main__':
    main()

