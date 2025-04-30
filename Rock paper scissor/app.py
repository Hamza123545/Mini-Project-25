import streamlit as st
import random

st.title("Rock, Paper, Scissors")

choices = ["Rock", "Paper", "Scissors"]
user_choice = st.selectbox("Choose one:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)
    st.write(f"Computer chose: **{computer_choice}**")

    if user_choice == computer_choice:
        st.info("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        st.success("You win! 🎉")
    else:
        st.error("Computer wins! 😢")
