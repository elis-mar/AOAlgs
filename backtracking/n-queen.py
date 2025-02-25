"""
Given n*n grid, find placements of n chess Queens, in such a way that none of the queens paths collide

Solve with backtracking recursively
"""

# position_of_queens[row] = column is the grid[row][column] = 'Q' position of the queens
def place_queens(position_of_queens: list[int], row: int, n: int) -> bool:
    if row == n:
        return True
    else:
        for column in range(n):
            legal = True
            for i in range(row): # check if legal move
                if position_of_queens[i] == column or abs(position_of_queens[i] - column) == abs(i - row):
                    legal = False
            if legal:
                position_of_queens[row] = column
                if place_queens(position_of_queens, row + 1, n):
                    return True
                position_of_queens[row] = -1
    return False

def print_solution(position_of_queens: list[int], n: int) -> None:
    grid = [['-' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        row = i
        column = position_of_queens[i]
        grid[row][column] = 'Q'

    for row in grid:
        print(' '.join(row))

def main() -> None:
    n = int(input("Enter number for n "))
    position_of_queens = [-1 for _ in range(n)]
    if place_queens(position_of_queens, 0, n):
        print_solution(position_of_queens, n)
    else: 
        print(f'No solution exists for n = {n}')

if __name__ == "__main__":
    main()
