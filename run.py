import random

CODE_LIST = ['Z', 'X', 'C', 'V', 'B']
CODE = []
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
                
                return player_input.capitalize()
            else: 
                raise ValueError(f'Make sure to enter: easy, normal, or expert.\n')    
        except ValueError as e:
            print(e)
                    
level_choice = get_difficulty_input()
print(level_choice)  