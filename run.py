import random
from collections import Counter
CODE_LIST = ['Z', 'X', 'C', 'V', 'B']

print()
print("You will be given 10 tries.\n")
print("A max of 5 letters to choose from.")
print("Letters are located on the last row of the keyboard starting with: z, x, c, v, and b.\n")
print('Your entries are not case sensitive.')
print('When entering you code make sure you have no empty spaces after the comma ex:(y,y, , )\n')
print('Crack the code before you run out of tries to become a "Mastermind."\n\n')
print("To start the game. Enter your difficulty: Easy, Normal, or Expert\n")

def get_difficulty_input():
    """
    Gets difficulty input from player.
    Performs check to ensure player input is one of three choices.
    """
    level_values = ['easy', 'normal', 'expert']
    while True:
        player_input = str(input(f"Enter you difficulty level: \n"))
        try:
            if player_input.lower() in level_values:

                return player_input.lower()
            else:
                raise ValueError(f'Make sure to enter: easy, normal, or expert.\n')
        except ValueError as e:
            print(e)

def secret_generated_code(difficulty, code_charters):
    """
    Generates random secret game code depending difficulty input by player.
    Checks the value of difficulty input inorder to create random game code.
    """

    generated_code = [random.choice(code_charters) for _ in range(len(code_charters))] # Generates a random code from

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

player_guess = []
def get_player_guess():
    """
    Gets players guess towards the hidden code.
    """
    global player_guess
    player_input = str(input("Enter your guess here: ").upper())
    string_list = player_input.split(",")
    player_guess.extend(string_list)
    
    if guess_input_validation(string_list, difficulty, CODE_LIST):
        return player_guess

def guess_input_validation(players_guess, difficulty, code_charaters):
    """
    Validates player input against computers generate game code.
    Validates player has entered only the lettes available to the game.
    Validates that the list length is equal to chosen diffculty.
    """
    Message = {
        "easy": 3,
        "normal": 4,
        "expert": 5
    }

    guess = players_guess

    for msg in Message: # Loops over the Message dictionary 
        if difficulty == msg:
            number = Message[msg]
            try:
                for char in guess:
                    if char not in code_charaters:
                        raise TypeError
            except TypeError as e:
                print(f'{e} You can only enter the letters: Z, X, C, V, and B!\n')
                return False, get_player_guess()
            try:
                if len(guess) != int(number):
                    raise ValueError
            except ValueError as e:
                print(f'{e} For your code to work you need to enter {number} code letters!')
                return False, get_player_guess()
            return True
        
def player_guess_check(random_secret_code, player_guess):
    """
    Checks player's guess against the computer secret code.
    Updates the number of correct letters in the correct postion.
    Updates the number oc correct letters of the player's guess.
    """
    secret_code_counter = Counter(random_secret_code)
    player_guess_counter = Counter(player_guess)

    common_values = secret_code_counter & player_guess_counter
    # total_values = sum(common_values.values())


    zip_iterator = zip(random_secret_code, player_guess)
    # Gets total of compared values in an object of tuples if they are of equal value.
    correct_posititons = sum(1 for secret, guess in zip_iterator if secret == guess)

    #Gets the minimum values between sec_code_counter and player_guess_counter values.
    correct_values = sum(min(secret_code_counter[values], player_guess_counter[values]) for values in common_values)

    #Subtracts
    # common_values = total_values - correct_posititons

    message = (f'Number of correct placements {correct_posititons}\n', f'Number of correct letters {correct_values}' )
    (a, b) = message
    print(a, b)



# Define a variable to store the previous feedback
previous_totals = None

def check_guess_gamecode(player_code):
    global previous_totals

    # Calculate the feedback for the current player guess
    feedback = player_guess_check(random_game_code, player_code)

    # If there is previous feedback, print it
    if previous_totals is not None:
        print("PREVIOUS FEEDBACK:", previous_totals)

    # Print the current feedback
    print("CURRENT FEEDBACK:", feedback)

    # Update the previous_feedback for the next iteration
    previous_totals= feedback

random_game_code = []
difficulty = get_difficulty_input()
code = secret_generated_code(difficulty, CODE_LIST)
if code:
    random_game_code.extend(code)
    print(code)
get_player_guess()
check_guess_gamecode(player_guess)
print(f'randomCode:  {random_game_code}\n', f'playerGuess: {player_guess}')
