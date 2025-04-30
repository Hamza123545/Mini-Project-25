import streamlit as st
import random

st.title("🎶 Markov Chain Text Composer")

def generate_markov_chain(text, n=2):
    words = text.split()
    chains = {}
    for i in range(len(words) - n):
        pair = tuple(words[i:i + n])
        next_word = words[i + n]
        chains.setdefault(pair, []).append(next_word)
    return chains

def generate_text(chains, n=2, length=50):
    if not chains:
        return "Error: Empty Markov Chain. Try entering more input text."
    pair = random.choice(list(chains.keys()))
    result = list(pair)
    for _ in range(length):
        next_words = chains.get(pair)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        pair = tuple(result[-n:])
    return " ".join(result)


st.subheader("📝 Input")
text_input = st.text_area("Enter some text to train the Markov Chain:")

st.subheader("⚙️ Settings")
n = st.slider("Select n-gram size (n)", min_value=1, max_value=5, value=2)
length = st.slider("Length of generated text (number of words)", min_value=10, max_value=200, value=50)


if text_input:
    words = text_input.split()
    if len(words) <= n:
        st.warning(f"Please enter more text (at least {n + 1} words) to generate a Markov chain.")
    else:
        chains = generate_markov_chain(text_input, n)
        generated_text = generate_text(chains, n, length)
        st.subheader("🧠 Generated Text")
        st.write(generated_text)
else:
    st.info("Enter some text above to get started!")
