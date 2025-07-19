import streamlit as st
import random

# Initialize session state
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.guesses = []

st.title("🎯 GUESS THE NUMBER!")

# Introductory game rules
st.write("**WELCOME TO GUESS ME!**")
st.write("I'm thinking of a number between **1 and 100**.")
st.write("📏 If your guess is more than 10 away from my number, I'll tell you you're **COLD**.")
st.write("🔥 If your guess is within 10 of my number, I'll tell you you're **WARM**.")
st.write("⬇️ If your guess is farther than your most recent guess, I'll say you're getting **COLDER**.")
st.write("⬆️ If your guess is closer than your most recent guess, I'll say you're getting **WARMER**.")
st.write("LET'S PLAY!")

# Input section
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit"):
    st.session_state.guesses.append(guess)

    if guess == st.session_state.number:
        st.success(f"🎉 CONGRATS! You guessed the number in {len(st.session_state.guesses)} tries.")
        st.balloons()
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.guesses = []
    elif len(st.session_state.guesses) == 1:
        st.info("WARM!" if abs(guess - st.session_state.number) <= 10 else "COLD!")
    else:
        prev = st.session_state.guesses[-2]
        st.info("WARMER!" if abs(guess - st.session_state.number) < abs(prev - st.session_state.number) else "COLDER!")
