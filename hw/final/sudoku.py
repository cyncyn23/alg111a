def available(board, ans, row, col):
    # check row
    for i in range (9):
        if board[row][i] == ans and col != i:
            #print("find!")
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
            if board[i][j] == ans and (i, j) != (row, col):
                return False
    return True

def findEmpty(board):
    rowCount = len(board)
    colCount = len(board[0])

    for i in range (rowCount):
        for j in range (colCount):
            if board[i][j] == 0:
                return (i, j)       # i = row, j = col
    return None

def solve (board):
    emptySpot = findEmpty(board)
    if not emptySpot:
        return True
    else: row, col = emptySpot
    """print('row =',row)
    print('col =',col)"""

    for i in range (1, 10):
        #print('values = ',i)
        # if the valus is available fill it into board
        if available(board, i, row, col):
            board[row][col] = i
            #print(board[row][col])
            
            # after fill it into board keep solve this question
            if solve(board):
                return True
            
            board[row][col] = 0
    return False

def startSolve (board):
    if solve(board):
        return board

def printSudoku(board):
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