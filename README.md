# SudokuSolverWithCNN
This program can take images of sudoku boards as an input and output it's solution. It has an incredibly fast algorithm that uses recursion and backtracking to get the solution in miliseconds.

Manual Input:

In order to manually input the board, enter each number the board row by row in one line. For blank spaces, input a 0.

Sample input: 010020300004005060070000008006900070000100002030048000500006040000800106008000000



Image Input:

To input an image, enter to directory of the image. The image must be alligned and croped so that the image only consists of the board. You can use the sample images in the imgs directory as guidlines.



Editing:

If you or the program made a small error in inputting the board, instead of reinputtting the board, you may edit small mistakes. This can be done by entering the row and column of the mistake and the number that you wan't to change it to. The rows and columns start at 1 and end at 9. These values must be separated by a comma. You may also include more than one edit by separating them with a semicolon. Please do not include any spaces.

Example: 

row,column,change;row,col,change;row,col,change

2,3,4;8,4,9;1,9,0

