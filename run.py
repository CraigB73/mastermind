import random
from art import text2art
from colored import  fg, bg, stylize

CODE_LIST = ['Z', 'X', 'C', 'V', 'B']
player_guess = []


def game_instruction():
    """
    Converts game logo to ACSII and print to console.
    Displays game instuctions.
    """
    logo = text2art("MASTERMIND!", chr_ignore= True)
    print()
    print('WELCOME to:')
    print(logo)
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
        input_message = "Enter you difficulty level: "
        player_input = str(input(stylize(input_message, fg("green"))))
        try:
            if player_input.lower() in level_values:
                
                return player_input.lower()
            else:
                value_error_msg ="Make sure to enter: easy, normal, or expert.\n"
                raise ValueError(stylize(value_error_msg, bg('red')))
        except ValueError as e:
            print(e)

    

def secret_generated_code(difficulty):
    """
    Generates random secret game code depending difficulty input by player.
    Checks the value of difficulty input inorder to create random game code.
    """
    local_code_list = CODE_LIST
    # Generates a random code with length depending on difficulty
    generated_code = [random.choice(local_code_list) for _ in range(len(local_code_list))] 
    
    try:
        if difficulty == 'easy':
            return generated_code[: len(generated_code) - 2]
        elif difficulty == 'normal':
            return generated_code[: len(generated_code) - 1]
        elif difficulty == 'expert':
            return generated_code
        else:
            value_error_msg = "Invalid difficulty level. Check that you have entered correct value"
            raise ValueError(stylize(value_error_msg, bg('red')))
    except ValueError as e:
        print(e)


def get_player_guess():
    """
    Gets players guess towards the hidden code.
    """
    global player_guess
    
    input_message = "Enter your guess here: "
    player_input = str(input(stylize(input_message, fg('yellow'))).upper())
    string_list = player_input.split(",")
    player_guess = string_list

    if guess_input_validation(string_list, difficulty):
        return player_guess

def guess_input_validation(players_guess, difficulty):
    """
    Validates player input against computers generate game code.
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
                value_error_msg = f"{e} You can only enter the letters: Z, X, C, V, and B!\n"
                print(stylize(value_error_msg, bg('red')))
                return get_player_guess()
            try:
                if len(player_guess) != int(number):
                    raise ValueError
            except ValueError as e:
                number_error = f'{e} For your code to work you need to enter a {number} letters code!'
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
    # This code was modified from ChatGBT to solve the problem with totaling the correct number of guessed letters
    remaining_occurrences = {letter: secret_code.count(letter) for letter in secret_code}

    for a, b in zip(secret_code, player_guess):
        if a == b:
            total_matching += 1
        
        if b in secret_code and remaining_occurrences[b] > 0:
            total_letters += 1
            remaining_occurrences[b] -= 1

    if total_letters > 1:
        letter_plural = 'letters'
    else:
        letter_plural = 'letter'
    
    if secret_code != player_guess:
        position_message = f"You have {total_matching} {letter_plural} in the correct position"
        totalletters_message = f"You have {total_letters} correct {letter_plural} in your guess!"    
        print(stylize(position_message, fg('green')))
        print(stylize(totalletters_message, fg('green')))
    else:
        print()
        
    return total_letters, total_matching 
   
def updates_tries_left(secret_code):
    """
    Updates the number of tries remaining after each guess has been entered.
    """
    try_count = 2
    if try_count > 1:
        guess_plural = 'guesses'
    else:
        guess_plural = 'guess'
    while try_count > 0:
        player_guess = get_player_guess()
        total_letters(secret_code, player_guess)

        if player_guess == secret_code:
            try_count -= 1
            end_message = f'😄 Great job you cracked the code: {", ".join(secret_code)} in {(10 - try_count)} {guess_plural} 😄!!!  '
            print(stylize(end_message, bg('green')))
            break
        else:
            try_count -= 1
            count_left_msg = f'{try_count} {guess_plural} left!'
            print(stylize(count_left_msg, fg("red")))
            print(f'Last guess { player_guess}')
            player_guess.clear()

    else:
        end_message = 'Out of guesses 🎆 💣 🤯. Better luck next time!'
        print(stylize(end_message, bg('red')))
 

game_instruction()
difficulty = get_difficulty_input()
def main():
    global difficulty    
    secret_code = secret_generated_code(difficulty)
    message  = f"Difficlty level: {difficulty.capitalize()}" 
    if secret_code:
        print(secret_code)
        print(stylize(message, fg('blue')))
        updates_tries_left(secret_code)
main()