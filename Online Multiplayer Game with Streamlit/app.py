import streamlit as st
import numpy as np


if 'board' not in st.session_state:
    st.session_state.board = np.full((3, 3), '', dtype=str)
    st.session_state.turn = 'X'


for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            if st.button(st.session_state.board[i][j] if st.session_state.board[i][j] else f'[{i},{j}]'):
                st.session_state.board[i][j] = st.session_state.turn
                st.session_state.turn = 'O' if st.session_state.turn == 'X' else 'X'


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]
    for col in board.T:
        if col[0] == col[1] == col[2] != '':
            return col[0]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

winner = check_winner(st.session_state.board)
if winner:
    st.write(f"{winner} Wins!")
