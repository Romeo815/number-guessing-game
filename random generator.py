from random import randint



#computer generated random number
random_number = randint(1, 100)
score_tracker = 0
win_streak = 0

play_game = True

##First Stage
while play_game:
    player_guess = input(
        "Enter a random number between 1 and 100: Enter 'score' to get current score, "
        "or 'q' to quit: "
    ).strip().lower()


    #check score
    if player_guess == "score":
        print(f"Your current win streak is {win_streak}")
        continue

    #Quit game
    elif player_guess == "q":
        play_game = False
        continue

    #Check for blank input
    elif player_guess == "":
        print("enter valid input please: ")
        continue



    ##Convert input to an integer
    try:
        player_guess = int(player_guess)
    except ValueError:
        print("enter valid input please: ")
        continue

    if player_guess < 1 or player_guess > 100:
        print("Please enter a number between 1 and 100")
        continue

    score_tracker += 1

    if player_guess < random_number:
        print("your guess is too low")

    elif player_guess > random_number:
        print("your guess is too high")



    else:
        print("your guess is correct")
        print(f"Total guesses: {score_tracker}")
        win_streak += 1

        # Start a new round
        random_number = randint(1, 100)



print(f"Your score is {score_tracker}")
