import streamlit as st

st.title("Tic-Tac-Toe")


if "board" not in st.session_state:
    st.session_state.board = [None] * 9
if "turn" not in st.session_state:
    st.session_state.turn = "X"

def check_win(board):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] is not None:
            return board[combo[0]]
    return None


def display_board():
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            idx = i * 3 + j
            if st.button(st.session_state.board[idx] if st.session_state.board[idx] else str(idx), key=idx):
                if st.session_state.board[idx] is None:
                    st.session_state.board[idx] = st.session_state.turn
                    st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
                    if winner := check_win(st.session_state.board):
                        st.write(f"{winner} wins!")
                        st.session_state.board = [None] * 9
                    break

    if None not in st.session_state.board:
        st.write("It's a tie!")
        st.session_state.board = [None] * 9  

display_board()
