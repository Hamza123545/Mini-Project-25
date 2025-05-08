import streamlit as st
import random
import time

st.set_page_config(page_title="Snake Game", layout="centered")
st.title("🐍 Snake Game - Streamlit Version")


GRID_SIZE = 10
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5)]
    st.session_state.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    st.session_state.direction = "RIGHT"
    st.session_state.score = 0
    st.session_state.game_over = False

def move_snake():
    head_x, head_y = st.session_state.snake[0]

    if st.session_state.direction == "UP":
        new_head = (head_x, head_y - 1)
    elif st.session_state.direction == "DOWN":
        new_head = (head_x, head_y + 1)
    elif st.session_state.direction == "LEFT":
        new_head = (head_x - 1, head_y)
    else:  # RIGHT
        new_head = (head_x + 1, head_y)

    # Check collision
    if (new_head in st.session_state.snake or
        not (0 <= new_head[0] < GRID_SIZE and 0 <= new_head[1] < GRID_SIZE)):
        st.session_state.game_over = True
        return

    st.session_state.snake.insert(0, new_head)

    if new_head == st.session_state.food:
        st.session_state.score += 1
        st.session_state.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    else:
        st.session_state.snake.pop()

def draw_board():
    board = [["⬛" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    fx, fy = st.session_state.food
    board[fy][fx] = "🍎"
    for x, y in st.session_state.snake:
        board[y][x] = "🟩"
    return board


col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️"):
        st.session_state.direction = "LEFT"
with col2:
    if st.button("⬆️"):
        st.session_state.direction = "UP"
    if st.button("⬇️"):
        st.session_state.direction = "DOWN"
with col3:
    if st.button("➡️"):
        st.session_state.direction = "RIGHT"

if not st.session_state.game_over:
    move_snake()
    board = draw_board()
    for row in board:
        st.write("".join(row))
    st.write(f"Score: {st.session_state.score}")
    time.sleep(0.3)
    st.experimental_rerun()
else:
    st.error("Game Over!")
    if st.button("Restart"):
        for key in ["snake", "food", "direction", "score", "game_over"]:
            del st.session_state[key]
        st.experimental_rerun()
