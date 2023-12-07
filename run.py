import random

CODE_LIST = ['Z', 'X', 'C', 'V', 'B']
player_guess = []

def game_instruction():
    print()
    print("You will be given 10 tries.\n")
    print("A max of 5 letters to choose from.")
    print("Letters are located on the last row of the keyboard starting with: z, x, c, v, and b.\n")
    print('Your entries are not case sensitive.')
    print('When entering you code make sure you have no empty spaces after the comma ex:(z,x,c,v )\n')
    print('Crack the code before you run out of tries to become a "Mastermind."\n')
    print("To start the game. Enter your difficulty: Easy, Normal, or Expert\n")

def get_difficulty_input():
    """
    Gets difficulty input from player.
    Performs check to ensure player input is one of three choices.
    """
    level_values = ['easy', 'normal', 'expert']
    while True:
        player_input = str(input(f"Enter you difficulty level: "))
        try:
            if player_input.lower() in level_values:
                
                return player_input.lower()
            else:
                raise ValueError(f'Make sure to enter: easy, normal, or expert.\n')
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
            raise ValueError("Invalid difficulty level. Check that you have entered correct value")
    except ValueError as e:
        print(e)


def get_player_guess():
    """
    Gets players guess towards the hidden code.
    """
    global player_guess

    player_input = str(input("Enter your guess here: ").upper())
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
                print(f'{e} You can only enter the letters: Z, X, C, V, and B!\n')
                return get_player_guess()
            try:
                if len(player_guess) != int(number):
                    raise ValueError
            except ValueError as e:
                print(f'{e} For your code to work you need to enter a {number} letters code!')
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
   
    for a, b in zip(secret_code, player_guess):
        if a == b:
            total_matching += 1
    
        if b in secret_code:
            total_letters += 1

    if total_letters > 1:
        letter_plural = 'letters'
    else:
        letter_plural = 'letter'
    
    if secret_code != player_guess:    
        print(f'You have {total_matching} {letter_plural} in the correct position and {total_letters} correct {letter_plural} in your guess!')
    else:
        print()
        
    return total_letters, total_matching 
   
def updates_tries_left(secret_code):
    """
    Updates the number of tries remaining after each guess has been entered.
    """
    try_count = 10
    if try_count > 1:
        guess_plural = 'guesses'
    else:
        guess_plural = 'guess'
    while try_count > 0:
        player_guess = get_player_guess()
        total_letters(secret_code, player_guess)

        if player_guess == secret_code:
            try_count -= 1
            print(f'Great job you cracked the code: {", ".join(secret_code)} in {try_count} {guess_plural} 😄')
            break
        else:
            
            try_count -= 1
            print(f'{try_count} {guess_plural} left!')
            print(f'Last guess { player_guess}')
            player_guess.clear()

    else:
        print('Out of guesses 🎆 💣 🤯. Better luck next time!')
        raise RuntimeError
 

game_instruction()
difficulty = get_difficulty_input()
def main():
    global difficulty    
    secret_code = secret_generated_code(difficulty)
    if secret_code:
        print(secret_code)
        updates_tries_left(secret_code)
main()