import streamlit as st
import numpy as np


def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


st.title("🧩 Sudoku Solver")

user_input = st.text_area("Enter Sudoku puzzle as 9x9 grid (use 0 for empty spaces):", 
"""5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9""")

try:
    board = [[int(x) if x != "0" else 0 for x in row.split()] for row in user_input.strip().split("\n")]
    if len(board) != 9 or any(len(row) != 9 for row in board):
        st.error("Please enter exactly 9 rows with 9 numbers each.")
    else:
        if st.button("🧠 Solve Sudoku"):
            if solve_sudoku(board):
                st.success("Solved Sudoku:")
                st.write(np.array(board))
            else:
                st.error("No solution found.")
except ValueError:
    st.error("Please make sure all inputs are numbers (0-9) separated by spaces.")
