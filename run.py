import random
from art import text2art
from colored import fg, bg, stylize

CODE_LIST = ['Z', 'X', 'C', 'V', 'B']
player_guess = []


def game_instruction():
    """
    Converts game logo to ACSII and print to console.
    Displays game instuctions.
    """
    print()
    logo = text2art("MASTERMIND!", chr_ignore=True)
    print('WELCOME to:')
    print(stylize(logo, fg('cyan_1')))
    game_text = open("instruction.txt", "r")
    game_text
    print(game_text.read())
    game_text.close()


def get_difficulty_input():
    """
    Gets difficulty input from player.
    Performs check to ensure player input is one of three choices.
    """
    level_values = ['easy', 'normal', 'expert']

    while True:
        input_message = "Enter you difficulty level: \n"
        player_input = str(input(stylize(input_message, fg("green"))))

        try:
            if player_input.lower() in level_values:
                message = f"Difficlty level: {player_input.capitalize()}"
                print(stylize(message, fg('blue')))

                return player_input.lower()
            else:
                value_error_msg = (
                    "Make sure to enter: easy, normal, or expert."
                )
                raise ValueError(stylize(value_error_msg, bg('yellow')))

        except ValueError as e:
            print(e)


def secret_generated_code(difficulty):
    """
    Generates random secret game code depending difficulty input by player.
    Checks the value of difficulty input inorder to create random game code.
    """
    local_code_list = CODE_LIST
    # Generates a random code with length depending on difficulty input
    generated_code = [
        random.choice(local_code_list) for _ in range(len(local_code_list))
    ]

    try:
        if difficulty == 'easy':
            return generated_code[: len(generated_code) - 2]
        elif difficulty == 'normal':
            return generated_code[: len(generated_code) - 1]
        elif difficulty == 'expert':
            return generated_code
        else:
            value_error_msg = (
                "Invalid difficulty level."
            )
            raise ValueError(stylize(value_error_msg, bg('red')))

    except ValueError as e:
        print(e)


def get_player_guess():
    """
    Gets and returns player secret code guess.
    """
    global player_guess

    input_message = "Enter your guess here: \n".upper()
    player_input = str(input(stylize(input_message, fg('yellow'))).upper())
    string_list = player_input.split(",")
    player_guess = string_list

    if guess_input_validation(string_list, difficulty):
        return player_guess


def guess_input_validation(players_guess, difficulty):
    """
    Validates player input against computers generate secret code.
    Validates player has entered only the lettes available to the game.
    Validates that the list length is equal to chosen diffculty level.
    """
    Message = {
        "easy": 3,
        "normal": 4,
        "expert": 5
    }

    local_code_list = CODE_LIST
    player_guess = players_guess
    for msg in Message:
        if difficulty == msg:
            number = Message[msg]

            try:
                for char in player_guess:
                    if char not in local_code_list:
                        raise TypeError
            except TypeError as e:
                value_error_msg = (
                    f"\n{e} You can only enter the letters: Z, X, C, V, and B!"
                )
                print(stylize(value_error_msg, bg('red')))
                return get_player_guess()
            try:
                if len(player_guess) != int(number):
                    raise ValueError
            except ValueError as e:
                number_error = (
                    f'{e} You code needs to be {number} letters code!'
                )
                print(stylize(number_error, bg("red")))
                return get_player_guess()

            return True


def total_letters(secret_code, player_guess):
    """
    Checks player's guess against secret code
    using imported Counter() module.
    Updates the number of letters in the correct index.
    Updates the number oc correct letters of the player's guess.
    """

    total_letters = 0
    total_matching = 0
    # remaining_letters was modified
    # with help from ChatGBT and geeksforgeeks.org to solve the bug
    # in updating the total_letters values correctly.
    remaining_letters = {
        letter: secret_code.count(letter) for letter in secret_code
    }

    for secret, guess in zip(secret_code, player_guess):
        if secret == guess:
            total_matching += 1

        if guess in secret_code and remaining_letters[guess] > 0:
            total_letters += 1
            remaining_letters[guess] -= 1

    if total_letters > 1:
        letter_plural = 'letters'
    else:
        letter_plural = 'letter'

    if secret_code != player_guess:
        position_message = (
            f"{total_matching} {letter_plural} in the correct position"
        )
        total_message = (
            f"Total of {total_letters} correct {letter_plural}!\n"
        )
        print()
        print(stylize(position_message, fg('light_goldenrod_2c')))
        print(stylize(total_message, fg('light_cyan')))
    else:
        print()

    return total_letters, total_matching


def updates_tries_left(secret_code):
    """
    Updates the number of tries after each guess has been entered.
    Prints games messages.
    """
    try_count = 10
    guess_plural = 'guesses'
    display_secret_code = ", ".join(secret_code)
    while try_count > 0:
        player_guess = get_player_guess()
        total_letters(secret_code, player_guess)
        
        if player_guess == secret_code:
            try_count = 10 - (try_count - 1)
            congrats_msg = text2art("Congratulation!", chr_ignore=True)
            win_message = f'You solved the code: {display_secret_code} 😄!!!'
            print(stylize(congrats_msg, fg('magenta')))
            print(stylize(win_message, bg('green')))
            break

        else:
            try_count -= 1
            count_left_msg = f'{try_count} {guess_plural} left!\n'
            previous_guess = f'\nPrevious guess:  {", ".join(player_guess)}'
            print(stylize(count_left_msg, fg("dark_sea_green_1")))
            print(stylize(previous_guess, bg('light_blue')))
            player_guess.clear()

    else:
        end_message = (
            f'🤯 💣 Out of guesses 💣 🤯!! Better luck next time!'
        )
        print(f"\nSecret Code: {stylize(display_secret_code, fg('red'))}")
        print(stylize(end_message, bg('red')))
        print('Try again?')


def play_again():
    """
    Gets input value if user wants to contiune to play the game.
    """
    global difficulty 
     
    play_input = input('Play again? Y/N: \n').upper()

    if play_input == "Y":
        difficulty = get_difficulty_input()
        return True
    else:
        end_message = f' 😀 Thank you for playing. GOOD BYE! 👋'
        print(stylize(end_message, bg('dark_blue')))
        return False


def main():
    """
    Runs mastermind game functions.
    """
    global difficulty

    while True:
        secret_code = secret_generated_code(difficulty)
        if secret_code:
            updates_tries_left(secret_code)
            if not play_again():
                break


game_instruction()
difficulty = get_difficulty_input() # Used as a global variable.


main()