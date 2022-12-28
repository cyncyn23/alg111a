from sudoku import printSudoku
from sudoku import startSolve

sudoku = [
    [0,0,0,0,7,8,0,0,5],
    [0,0,5,4,2,9,0,0,0],
    [7,3,0,0,0,1,0,9,0],
    [0,7,0,0,0,0,0,2,0],
    [9,0,6,0,0,0,5,0,7],
    [1,2,0,0,0,5,9,3,6],
    [0,6,9,0,5,7,0,8,1],
    [3,0,1,9,0,0,0,6,0],
    [2,0,0,6,1,0,4,5,0]
]

printSudoku(sudoku)
solvedSudoku = startSolve(sudoku)
print("************************") 
printSudoku(solvedSudoku)