import streamlit as st
import random


word_list = ['python', 'streamlit', 'discord', 'hangman']


if 'word' not in st.session_state:
    st.session_state.word = random.choice(word_list)
    st.session_state.guessed = set()
    st.session_state.attempts = 6  

display_word = ''.join([letter if letter in st.session_state.guessed else '_' for letter in st.session_state.word])
st.write(f"Word: {display_word}")


guess = st.text_input("Guess a letter:")


if guess and guess.isalpha() and len(guess) == 1:
    st.session_state.guessed.add(guess)
    
    if guess not in st.session_state.word:
        st.session_state.attempts -= 1

if all(letter in st.session_state.guessed for letter in st.session_state.word):
    st.write("Congratulations, you won!")
elif st.session_state.attempts == 0:
    st.write(f"You lost! The word was {st.session_state.word}.")
else:
    st.write(f"You have {st.session_state.attempts} attempts left.")
