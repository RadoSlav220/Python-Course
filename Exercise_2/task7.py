# Write your code here:

def countOnMainDiagonal(board, char):
    return [board[i][i] for i in range(0, len(board))].count(char)

def countOnSecondDiagonal(board, char):
    return [board[i][len(board)-i-1] for i in range(0, len(board))].count(char)

def countOnColumn(board, columnIndex, char):
    return [board[i][columnIndex] for i in range(0, len(board))].count(char)

def countOnAllColumns(board, char):
    return [countOnColumn(board, colIndex, char) for colIndex in range(0, len(board))]

def countOnAllRows(board, char):
    return [row.count(char) for row in board]

def getReportForChar(board, char):
    return countOnAllRows(board, char) + countOnAllColumns(board, char) + [countOnMainDiagonal(board, char), countOnSecondDiagonal(board, char)]

def checkForChar(board, char):
    return len(board) in getReportForChar(board, char)
    
def determine_winner(board):
    if checkForChar(board, 'X'):
        return 'X'
    elif checkForChar(board, 'O'):
        return 'O'
    else:
        return 'Draw'

board_1 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'X']
]

board_2 = [
    ['X', 'O', 'X'],
    ['O', 'O', 'O'],
    ['O', 'X', 'X']
]

board_3 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'O']
]

board_4 = [
    ['X', 'X', 'X'],
    ['O', 'O', None],
    [None, None, None]
]

board_5 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'X'],
    ['O', 'O', 'O']
]

board_6 = [
    ['O', 'O', 'X'],
    ['O', 'X', None],
    ['X', 'X', None]
]

board_7 = [
    ['X', 'O', 'X'],
    ['X', 'O', 'O'],
    ['X', 'X', 'O']
]

board_8 = [
    ['O', 'X', 'O'],
    ['O', 'X', None],
    ['X', 'X', None]
]

board_9 = [
    ['X', 'X', 'O'],
    [None, 'X', 'O'],
    [None, None, 'O']
]


assert determine_winner(board_1) == 'X'
assert determine_winner(board_2) == 'O'
assert determine_winner(board_3) == 'Draw'
assert determine_winner(board_4) == 'X'
assert determine_winner(board_5) == 'O'
assert determine_winner(board_6) == 'X'
assert determine_winner(board_7) == 'X'
assert determine_winner(board_8) == 'X'
assert determine_winner(board_9) == 'O'

"✅ All OK! +0.75 points"