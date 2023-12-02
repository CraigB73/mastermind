import random

CODE_LIST = ['Z', 'X', 'C', 'V', 'B']
PLAYER_GUESS = []

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

def random_generated_code(difficulty, code_charters):
    """
    Generates random game code depending difficulty input by player.
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

                    
difficulty = get_difficulty_input()
code = random_generated_code(difficulty, CODE_LIST)
print(difficulty, code)  