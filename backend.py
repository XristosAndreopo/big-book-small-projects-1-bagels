import modules as m

NUM_DIGITS = 3 #Constant - Number of digits the player have to guess,
#change it if you want
MAX_GUESSES = 10 #Constant - Number of guesses the player has,
#change it if you want

winning_output = "Congratulations! You found the number"

#player will make up to MAX_GUESSES
player_tries = 0
#Main loop of game
while True:
    print("""
    When I say:    That means:
    Pico           One digit is correct but in the wrong position.
    Fermi          One digit is correct and in the right position.
    Bagels         No digit is correct.
    """)
    print(f"Guess a {NUM_DIGITS} digit number")
    # create secret number from function random_number in modules.py
    random_number_modules = m.random_number(NUM_DIGITS)
    print(random_number_modules)
    #inside loop
    while player_tries <= MAX_GUESSES:
        #input of player
        # print how many guesses can the player make
        print(f"You have {MAX_GUESSES - player_tries} out of {MAX_GUESSES} guesses")
        guess = input("Please guess what the number is:")
        #gets a string from function random_number in modules
        outcome = m.output(guess ,random_number_modules)
        print(outcome)
        if outcome == winning_output:
            #breaks out of loop
            break
        else:
            player_tries = player_tries + 1
    # play again?
    input_play_again = input("Do you want to play again? Y/N")
    if input_play_again.lower().startswith("n"):
        break

print("Thanks for playing")


