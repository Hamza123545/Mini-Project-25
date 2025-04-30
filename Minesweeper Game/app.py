import streamlit as st
import random


BOARD_SIZE = 5
MINES = 5


def create_board():
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    mines = random.sample(range(BOARD_SIZE * BOARD_SIZE), MINES)
    for mine in mines:
        row, col = divmod(mine, BOARD_SIZE)
        board[row][col] = -1 

    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == -1:
                continue
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE and board[nr][nc] == -1:
                        board[r][c] += 1
    return board


def display_board():
    board = st.session_state.board
    revealed = st.session_state.revealed
    for r in range(BOARD_SIZE):
        cols = st.columns(BOARD_SIZE)
        for c in range(BOARD_SIZE):
            key = f"{r}-{c}"
            if revealed[r][c]:
                value = board[r][c]
                if value == -1:
                    cols[c].button("💣", key=key, disabled=True)
                elif value == 0:
                    cols[c].button(" ", key=key, disabled=True)
                else:
                    cols[c].button(str(value), key=key, disabled=True)
            else:
                if cols[c].button(" ", key=key):
                    revealed[r][c] = True
                    if board[r][c] == -1:
                        st.error("💥 Game Over! You hit a mine.")
                        for i in range(BOARD_SIZE):
                            for j in range(BOARD_SIZE):
                                revealed[i][j] = True


if "board" not in st.session_state:
    st.session_state.board = create_board()
    st.session_state.revealed = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

st.title("🧨 Minesweeper")
display_board()
if st.button("🔄 Restart Game"):
    del st.session_state["board"]
    del st.session_state["revealed"]
    st.rerun()
