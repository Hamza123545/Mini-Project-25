import streamlit as st
import numpy as np


if 'board' not in st.session_state:
    st.session_state.board = np.zeros((6, 7), int)
    st.session_state.current_player = 1 


def drop_disc(col):
    
    for row in range(5, -1, -1):
        if st.session_state.board[row][col] == 0:
            st.session_state.board[row][col] = st.session_state.current_player
            break


def check_winner():
    for row in range(6):
        for col in range(7):
            if st.session_state.board[row][col] == 0:
                continue
            player = st.session_state.board[row][col]
            
            if col + 3 < 7 and all(st.session_state.board[row][col + i] == player for i in range(4)):
                return player
            if row + 3 < 6 and all(st.session_state.board[row + i][col] == player for i in range(4)):
                return player
            if row + 3 < 6 and col + 3 < 7 and all(st.session_state.board[row + i][col + i] == player for i in range(4)):
                return player
            if row - 3 >= 0 and col + 3 < 7 and all(st.session_state.board[row - i][col + i] == player for i in range(4)):
                return player
    return 0


for row in range(6):
    cols = st.columns(7)
    for col in range(7):
        with cols[col]:
            if st.button(' ' if st.session_state.board[row][col] == 0 else ('R' if st.session_state.board[row][col] == 1 else 'Y'), key=f'{row}-{col}'):
                drop_disc(col)
                st.session_state.current_player = 3 - st.session_state.current_player  # Switch player


winner = check_winner()
if winner:
    st.write(f"Player {winner} wins!")
elif np.all(st.session_state.board != 0):
    st.write("It's a tie!")
