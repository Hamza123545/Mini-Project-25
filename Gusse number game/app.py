import streamlit as st

st.title("Guess the Number (Computer Guesses)")

if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 100
if "guess" not in st.session_state:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2

st.write(f"Is your number {st.session_state.guess}?")

col1, col2, col3 = st.columns(3)
if col1.button("Too Low"):
    st.session_state.low = st.session_state.guess + 1
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
elif col2.button("Too High"):
    st.session_state.high = st.session_state.guess - 1
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
elif col3.button("Correct!"):
    st.success(f"Yay! I guessed it right 🎉. It was {st.session_state.guess}")
    if st.button("Play Again"):
        for key in ["low", "high", "guess"]:
            st.session_state.pop(key)
        st.experimental_rerun()