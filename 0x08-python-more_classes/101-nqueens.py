#!/usr/bin/python3

import sys

def is_safe(board, row, col, n):
        #Check if there is a queen in the same row
        for i in range (col):
                if board[row][i] == 1:
                        return False

        #Chec upper diagonal on the left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 1:
                        return False

        #Check lower diagonal on the left side
        for i, j in zip(range(row, n), range(col, -1, -1)):
                if board[i][j] == 1:
                        return False

        return True

def solved_nqueens_util(board, col, n, result):
        if col == n:
                result.append([[row, col] for row in range(n) if board[row][col] == 1])
                return True

        res = False

        for i in range(n):
                if is_safe(board, i, n, col):
                        board[i][col] = 1

                        res = solved_nqueens_util(board, col + 1, n, result) or res

                        board[i][col]
        return res

def solved_nqueens(n):

        #Check the prop of the entry "n"
        if not isinstance(n, int):
                print("N must be a number")
                return 1
        if n < 4:
                print("N must be >= 4")
                return 1

        #Create the board based on n
        board = [[0] * n for _ in range(n)]
        #The possible position of queens not attacking each other
        result = []

        if not solved_nqueens_util(board, 0, n, result):
                return 1

        for sol in result:
                print(sol)

        return 0

if __name__ == "__main__":

        if len(sys.argv ) != 2:
                print("Usage: nqueens N\n")
                sys.exit(1)

        try:
                N = int(sys.argv[1])
        except ValueError:
                print("N must be a number\n")
                sys.exit(1)

        if N < 4:
                print("N must be >= 4\n")
                sys.exit(1)

        status = solved_nqueens(N)
        sys.exit(status)