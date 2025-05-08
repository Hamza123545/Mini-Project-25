import streamlit as st
import random

st.title('Guess the Number')


if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)


guess = st.number_input('Enter your guess:', min_value=1, max_value=100)

if guess:
    if guess < st.session_state.number:
        st.write('Too low!')
    elif guess > st.session_state.number:
        st.write('Too high!')
    else:
        st.write('You guessed it!')
        st.session_state.number = random.randint(1, 100)  
