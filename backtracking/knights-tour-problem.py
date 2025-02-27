
# Move a knight on a chessboard so that it visits every square once

def generate_board() -> list[list[bool]]: return [[False for _ in range(8)] for _ in range(8)]

def find_next_moves(board: list[list[bool]], current_position: tuple[int, int]) -> list[tuple[int, int]]:
    row = current_position[0]
    column = current_position[1]
    n = len(board)
    next_moves = []

    for r in range(1, 3):
        c = 2 if r == 1 else 1
        row_moves = (row - r, row + r)
        column_moves = (column - c, column + c)
        for row_move in row_moves:
            for column_move in column_moves:
                if row_move < 0 or row_move >= n or column_move < 0 or column_move >= n:
                    continue
                elif not board[row_move][column_move]:
                    next_moves.append((row_move, column_move))

    return next_moves 

def solved(board: list[list[bool]]) -> bool: return all(all(row) for row in board)

def solve(board: list[list[bool]], current_position: tuple[int, int]) -> bool:
    (current_row, current_column) = current_position
    board[current_row][current_column] = True

    if solved(board):
        return True

    else:
        next_moves = find_next_moves(board, current_position)
        if next_moves:
            for next_move in next_moves:
                if solve(board, next_move):
                    return True

        board[current_row][current_column] = False

    return False

def main():
    board = generate_board()
    if solve(board, (0,0)):
        print('you done did it')
    else:
        print('you not done did it')

if __name__ == '__main__':
    main()
