#!/usr/bin/python3
import sys

class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_safe(self, board, row, col):
        for i in range(row):
            if board[i][col] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if board[i][j] == 1:
                return False

        return True

    def solve_nqueens(self):
        if self.n < 4:
            return []

        board = [[0 for _ in range(self.n)] for _ in range(self.n)]

        def backtrack(row):
            if row == self.n:
                self.solutions.append([[i, row_i] for row_i, i in enumerate(board)])
                return
            for col in range(self.n):
                if self.is_safe(board, row, col):
                    board[row][col] = 1
                    backtrack(row + 1)
                    board[row][col] = 0

        backtrack(0)

    def print_solutions(self):
        for solution in self.solutions:
            for row in solution:
                print(row)
            print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(n)
    solver.solve_nqueens()
    solver.print_solutions()
