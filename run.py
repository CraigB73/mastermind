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
    return player_guess


   
def guess_calculate(random_secret_code, player_guess):

    secret_code_counter = Counter(random_secret_code)
    player_guess_counter = Counter(player_guess)
    
    common_values = secret_code_counter & player_guess_counter
     
    total_values = sum(common_values.values())
    
    correct_posititons = sum(1 for s,p in zip(random_secret_code, player_guess) if s == p)
    
    common_values = total_values - correct_posititons
    
    message = (f'Number of correct placements {correct_posititons}', f'Number of correct letters {common_values}' )
    (a, b) = message
    print(a, b)

random_game_code = []                
difficulty = get_difficulty_input()
code = secret_generated_code(difficulty, CODE_LIST)
if code:
    random_game_code.extend(code)
    print(code) 
get_player_guess()
print(difficulty)

print(f'randomCode:  {random_game_code}\n', f'playerGuess: {player_guess}')
guess_calculate(random_game_code, player_guess)

#  game_code = Counter(random_code)
#     player_guess = Counter(player_code)
    
#     compare_code = game_code & player_guess
    
#     total = sum(compare_code.values())

    
#     if total > 0:
#         print("TOTAL", total)