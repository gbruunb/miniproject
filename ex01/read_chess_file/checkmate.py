def checkmate(org_board):
    try:
        rows = org_board.split()
        board = [list(row) for row in rows]

        if len(find_char(board, "K")) > 1 or len(find_char(board, "K")) < 1:
            print("K must have only one")
            return

        length_board = count_board(board)
        if length_board == 0:
            print("Invalid board")
            return

        movement = {
            "P": [[-1, -1, 1], [-1, 1, 1]],
            "B": [
                [-1, -1, length_board * 2],
                [1, 1, length_board * 2],
                [-1, 1, length_board * 2],
                [1, -1, length_board * 2],
            ],
            "R": [
                [-1, 0, length_board * 2],
                [1, 0, length_board * 2],
                [0, -1, length_board * 2],
                [0, 1, length_board * 2],
            ],
            "Q": [
                [-1, -1, length_board * 2],
                [1, 1, length_board * 2],
                [-1, 1, length_board * 2],
                [1, -1, length_board * 2],
                [-1, 0, length_board * 2],
                [1, 0, length_board * 2],
                [0, -1, length_board * 2],
                [0, 1, length_board * 2],
            ],
        }

        for i in range(length_board):
            for j in range(length_board):
                if board[i][j] in movement.keys():
                    mark_movements(board, movement, board[i][j], [i, j])

        if len(find_char(board, "X")) > 0:
            print("Success")
        else:
            print("Fail")


        # show king movability
        king_board = find_king_movements(org_board)
        if king_board:
            final_board = find_king_movability(board, king_board)
            display(final_board)
    except:
        return


def count_board(board):
    if len(board) == 0:
        return 0

    i = 0
    while i < len(board):
        if len(board[i]) == 0 or len(board[i]) != len(board):
            return 0
        i += 1

    return len(board)


def mark_movements(board, movement, piece, pos):
    directions = movement[piece]
    for direction in directions:
        for step in range(1, direction[2] + 1):
            new_x = pos[0] + direction[0] * step
            new_y = pos[1] + direction[1] * step

            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                if board[new_x][new_y] == ".":
                    board[new_x][new_y] = "*"
                elif board[new_x][new_y] in movement.keys():
                    break
                elif board[new_x][new_y] == "K":
                    board[new_x][new_y] = "X"
                    break
            else:
                break


def find_char(board, char):
    index_founded = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == char:
                index_founded.append([i, j])
    return index_founded


def display(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()


# added function
def find_king_movements(board):
    rows = board.split()
    board = [list(row) for row in rows]

    king_movements = [
        [-1, -1, 1],
        [-1, 0, 1],
        [-1, 1, 1],
        [0, -1, 1],
        [0, 1, 1],
        [1, -1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]

    king_pos = find_char(board, "K")

    if len(king_pos) != 1:
        print("K must have only one")
        return
    
    king_x, king_y = king_pos[0]

    mark_movements(board, {'K': king_movements}, 'K', [king_x, king_y])

    return board

def find_king_movability(main_board, king_board):
    new_board = [row[:] for row in main_board]  # Deep copy of the main board

    # integrate main_board and king_board to display king movability and show king cannot move
    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            if king_board[i][j] == '*':
                if new_board[i][j] == '.':
                    new_board[i][j] = 'o'  # Mark possible king move
            elif king_board[i][j] == 'K':
                new_board[i][j] = 'K'  # Keep the king position


    return new_board