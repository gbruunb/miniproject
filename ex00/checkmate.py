def checkmate(board):
    rows = board.split()
    board = [list(row) for row in rows]
    movement = {
        'P' : [[-1, -1], [1, 1]],
        'B' : [[]]
    }
    # display(board)
    print(find_char(board, "K"))

def find_char(board, char):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == char:
                return [i, j]
            
def display(board):
    for row in board:
        for col in row:
            print(col, end = " ")
        print()
    