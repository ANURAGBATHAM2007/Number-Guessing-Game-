
import streamlit as st
import random

# Initialize session state for random number and guesses
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.no_of_guesses = 0
    st.session_state.message = ""

st.title("🎯 Number Guessing Game")

st.write("I have chosen a number between **1 and 100**. Can you guess it?")

# Input for user's guess
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Button to submit guess
if st.button("Guess"):
    st.session_state.no_of_guesses += 1
    if guess > st.session_state.random_number:
        st.session_state.message = "🔽 Lower number please!"
    elif guess < st.session_state.random_number:
        st.session_state.message = "🔼 Higher number please!"
    else:
        st.session_state.message = f"🎉 Congrats!! You guessed it in {st.session_state.no_of_guesses} tries."
    
st.write(st.session_state.message)

# Restart game button
if st.button("Restart Game"):
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.no_of_guesses = 0
    st.session_state.message = ""
    st.success("Game restarted! Guess a new number 🎲")
