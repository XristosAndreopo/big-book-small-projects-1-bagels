import streamlit as st
import modules as m

# Streamlit UI
st.title("Bagels Game")
st.write("""
### Instructions:
1. I have thought of a number with a specific number of digits.
2. Your goal is to guess the number.
3. I'll give you clues for each guess:
   - **Pico**: One digit is correct but in the wrong position.
   - **Fermi**: One digit is correct and in the correct position.
   - **Bagels**: No digit is correct.
4. You have a limited number of guesses. Good luck!
""")

# Configuration
NUM_DIGITS = st.number_input("Number of Digits in the Secret Number:",
                             min_value=2, max_value=10, value=3)
MAX_GUESSES = st.number_input("Maximum Number of Guesses:", min_value=1,
                              max_value=20, value=10)

# State Initialization
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = m.random_number(NUM_DIGITS)
    st.session_state.remaining_guesses = MAX_GUESSES
    st.session_state.feedback = []
    st.session_state.game_over = False

# Reset Button
if st.button("Reset Game"):
    st.session_state.secret_number = m.random_number(NUM_DIGITS)
    st.session_state.remaining_guesses = MAX_GUESSES
    st.session_state.feedback = []
    st.session_state.game_over = False
    st.success("Game reset! Start guessing.")

# Display Feedback and Input
if not st.session_state.game_over:
    st.write(
        f"**You have {st.session_state.remaining_guesses} guesses remaining.**")
    player_guess = st.text_input("Enter your guess:", max_chars=NUM_DIGITS)

    if st.button("Submit Guess"):
        if len(player_guess) != NUM_DIGITS or not player_guess.isdigit():
            st.warning(f"Please enter a valid {NUM_DIGITS}-digit number.")
        else:
            # Process the guess
            feedback = m.output(player_guess, st.session_state.secret_number)
            st.session_state.feedback.append(
                f"Your guess: {player_guess} -> {feedback}")
            st.session_state.remaining_guesses -= 1

            if feedback == "Congratulations! You found the number":
                st.success(feedback)
                st.session_state.game_over = True
            elif st.session_state.remaining_guesses == 0:
                st.error(
                    f"Game over! The secret number was {st.session_state.secret_number}.")
                st.session_state.game_over = True

# Display Feedback
if st.session_state.feedback:
    st.write("### Your Guesses and Feedback:")
    for entry in st.session_state.feedback:
        st.write(entry)

# End of Game Message
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.secret_number = m.random_number(NUM_DIGITS)
        st.session_state.remaining_guesses = MAX_GUESSES
        st.session_state.feedback = []
        st.session_state.game_over = False
        st.experimental_rerun()

