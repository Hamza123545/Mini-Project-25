import streamlit as st
import time

st.title("Countdown Timer")

minutes = st.number_input("Enter minutes:", min_value=0, max_value=60, value=0)
seconds = st.number_input("Enter seconds:", min_value=0, max_value=60, value=10)

if st.button("Start Timer"):
    total_seconds = minutes * 60 + seconds
    timer_placeholder = st.empty() 
    
    for i in range(total_seconds, -1, -1):
        mins, secs = divmod(i, 60)
        timer_placeholder.markdown(f"### ⏱️ {mins:02d}:{secs:02d}")
        time.sleep(1)
    
    timer_placeholder.markdown("### ⏱️ Time's up!")
