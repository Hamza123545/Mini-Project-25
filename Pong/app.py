import streamlit as st
import time
import random

st.title("Pong Game")


if "score" not in st.session_state:
    st.session_state.score = [0, 0]


st.write(f"Player 1: {st.session_state.score[0]} | Player 2: {st.session_state.score[1]}")


if st.button("Start Game"):
    ball_x = 50
    ball_y = 50
    ball_dx = random.choice([-1, 1])
    ball_dy = random.choice([-1, 1])

    while True:
        ball_x += ball_dx
        ball_y += ball_dy
        
        if ball_x <= 0 or ball_x >= 100:
            ball_dx = -ball_dx
        if ball_y <= 0 or ball_y >= 100:
            ball_dy = -ball_dy

        st.write(f"Ball position: ({ball_x}, {ball_y})")

     
        time.sleep(0.1)
