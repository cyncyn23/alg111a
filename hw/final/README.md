## Sudoku by Backtracking
平常就很愛玩Sudoku，跟朋友交流後得到的靈感。

### #1 Clarify the problem
```
先找出需要填入數字的格子，再一個一個數字填進去
判斷是否符合規則，True -> 下一個，False -> 上一步。
```

### #2 Create a matrix to place the Sudoku problems
Sudoku problems from https://sudoku.com/
```py
question = [
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
```

### #3 Create a function to display Sudoku
```py
def print_sudoku(board):
    rowCount = len(board)
    colCount = len(board[0])

    # print row
    for i in range (rowCount):
        if i % 3 == 0 and i != 0:
            print("----------------------") 
        # print column
        for j in range (colCount):
            if j % 3 == 0 and j != 0:
                print("| ", end = '')
            if j != 8:
                print("{} ".format(board[i][j]), end = '')
            else:
                print(board[i][j])
```

### #4 Solving
```py
def solve (board):
    emptySpot = findEmpty(board)
    if not emptySpot:
        return True
    else row, col = emptySpot

    for i in range (1, 10):
        # if the valus is available fill it into board
        if available(board, i, row, col):
            board[row][col] = i
            
            # after fill it into board keep solve this question
            if solve(board):
                return True
            
            board[row][col] = 0
    return False
```
#### #1 Find the blank
```py
def findEmpty(board):
    rowCount = len(board)
    colCount = len(board[0])

    for i in range (rowCount):
        for j in range (colCount):
            if board[i][j] == 0:
                return (i, j)       # i = row, j = col
    return None
``` 
#### #2 Judge the rules
```py
def available(board, ans, row, col):
    # check row
    for i in range (9):
        if board[row][i] == ans and col != i:
            return False
    
    # check column
    for i in range (9):
        if board[i][col] == ans and row != i:
            return False
        
    # check 3*3
    boxIndexR = row // 3
    boxIndexC = col // 3
    
    for i in range (boxIndexR * 3, boxIndexR * 3 + 3):
        for j in range (boxIndexC * 3, boxIndexC *3 + 3):
            if board[j][i] == ans and (j, i) != (row, col):
                return False
    return True
```
## Test Program
### Code
```py
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
```
### Result
```
PS C:\Users\user\Desktop\Github\cynthia1231\alg111a\hw\final> python sudokuTest.py
0 0 0 | 0 7 8 | 0 0 5
0 0 5 | 4 2 9 | 0 0 0
7 3 0 | 0 0 1 | 0 9 0
----------------------
0 7 0 | 0 0 0 | 0 2 0
9 0 6 | 0 0 0 | 5 0 7
1 2 0 | 0 0 5 | 9 3 6
----------------------
0 6 9 | 0 5 7 | 0 8 1
3 0 1 | 9 0 0 | 0 6 0
2 0 0 | 6 1 0 | 4 5 0
************************
6 9 2 | 3 7 8 | 1 4 5
8 1 5 | 4 2 9 | 6 7 3
----------------------
5 7 3 | 1 9 6 | 8 2 4
9 4 6 | 8 3 2 | 5 1 7
1 2 8 | 7 4 5 | 9 3 6
----------------------
4 6 9 | 2 5 7 | 3 8 1
3 5 1 | 9 8 4 | 7 6 2
2 8 7 | 6 1 3 | 4 5 9
```
## Analysis the Time Complexity 
```
假設有k個格子要解決，每個格子有n種可能性，複雜度 = O(n*k)。
```
