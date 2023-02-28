import random

play_again = 'yes'
max_valid_guess = 5
best_score = max_valid_guess+1

while play_again == 'yes': 
    num = random.randint(1,10)

    is_right_guess = False
    num_valid_guesses = max_valid_guess

    guess = -1
    steps_to_guess = 0
    while (num != guess) and (num_valid_guesses>0):
        guess = int(input("guess the number between 1-10: "))
        steps_to_guess += 1
        if guess<num:
            print("please guess a bigger number: ")
        elif guess>num:
            print("please guess smaller number: ")
        num_valid_guesses -= 1

    if num==guess:
        print(f"You guess after {steps_to_guess} steps!!")
        if steps_to_guess < best_score:
            print("You have the best score!!")
            best_score = steps_to_guess
    else:
        print("try again...")
                    
    play_again = input("do you want to play again? (yes/no): ")
    # todo: check if input is yes/no
