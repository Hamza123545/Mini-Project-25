import streamlit as st

st.title("Mad Libs Game")

noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
adj = st.text_input("Enter an adjective:")

if noun and verb and adj:
    story = f"Today, I saw a {adj} {noun} that tried to {verb} on my laptop!"
    st.write("### Here's your story:")
    st.write(story)
    st.download_button("Download Story", story, file_name="mad_libs_story.txt")