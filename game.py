import random


def generate_target():
    return random.randint(1000, 9999)


def quit_game(target_number):
    return f"The correct number was {target_number}"


def invalid_input():
    return "Invalid input. Please enter a four-digit number."


def play_again():
    output_str = "Do you want to play again? (yes/no):"
    return input(output_str).strip().lower() == "yes"


def game_feedback(guess, target):
    feedback = ""
    for i in range(4):
        if guess[i] == target[i]:
            feedback += "●"  # Circle for correct digit in right spot
        elif guess[i] in target:
            feedback += "x"  # 'x' for correct digit in wrong spot
        else:
            feedback += "_"
    return feedback


def initiate_game():
    play = True

    while play:
        target_number = generate_target()
        attempts = 0
        target_str = str(target_number)
        print("Welcome to the Number Guessing Game!")
        print("Try to guess the four-digit number.")

        while True:
            player_input = input("Enter your guess or type 'quit' to exit: ")
            player_guess = player_input.strip()

            if player_guess.lower() == "quit":
                print(quit_game(target_number))
                break  # Exit the inner loop to stop the game

            if len(player_guess) != 4 or not player_guess.isdigit():
                print(invalid_input())
                continue

            attempts += 1
            if player_guess == target_str:
                print(
                    f"Congratulations!Attempts taken {attempts}"
                )
                break
            else:
                feedback = game_feedback(player_guess, target_str)
                print(f"Feedback: {feedback}")

        play = play_again()


if __name__ == "__main__":
    initiate_game()
