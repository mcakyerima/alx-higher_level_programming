#!/usr/bin/python3
""" Solve the N Queens puzzle. """
import sys

def initialize_board(n):
    """ Initialize the chessboard. """
    return [[0 for _ in range(n)] for _ in range(n)]

def print_solution(matrix):
    """ Print a valid solution. """
    for row in matrix:
        print([row[i] for i in range(1, len(row))])

def is_safe(board, row, col, pos_diagonal, neg_diagonal):
    """ Check if it's safe to place a queen at a given position. """
    if col in board[row] or row + col in pos_diagonal or row - col in neg_diagonal:
        return False
    return True

def solve_n_queens(n):
    """ Solve the N Queens puzzle. """
    matrix = [[i, 0] for i in range(n)]
    board = initialize_board(n)
    col = set()
    pos_diagonal = set()
    neg_diagonal = set()

    def backtrack(row):
        if row == n:
            print_solution(matrix)
            return

        for col_index in range(n):
            if is_safe(board, row, col_index, pos_diagonal, neg_diagonal):
                board[row][col_index] = 1
                col.add(col_index)
                pos_diagonal.add(row + col_index)
                neg_diagonal.add(row - col_index)
                matrix[row][1] = col_index
                backtrack(row + 1)
                board[row][col_index] = 0
                col.remove(col_index)
                pos_diagonal.remove(row + col_index)
                neg_diagonal.remove(row - col_index)

    backtrack(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    num = sys.argv[1]

    try:
        num_int = int(num)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if num_int < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(num_int)

