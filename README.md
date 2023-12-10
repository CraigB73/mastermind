<div align="center"><h1>MASTERMIND!</h1></div>

## Description 

*Mastermind* is a Python terminal game that uses the command line to solve the secret code.

There are three levels of difficulty. Each level increases the length of the secret code by one letter. Starting with the easy level having only a 3 letter code to solve. Every player will have 10 tries to solve the code. See if you can solve the code before your tries run out.

<div align="center"><img src= "./assets/screenshots/mock_master.png" width=700 height=500></div>

Play Mastermind: [MasterMind](https://master-mind-748a02ac12ee.herokuapp.com/)

## Table of Content 

1. [Description](#description)
2. [Table of Content](#table-of-content)
3. [How to play](#how-to-play)
4. [Features](#features)
5. [Data Model](#data-model)
6. [Libraries](#libraries)
7. [Testing](#testing)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Credits and Acknowledgements](#credits-and-acknowledgements)

## How to play

- You have 10 tries.
- Start by entering your difficulty: 
    * Easy(3 letters) 
    * Normal(4 letters) 
    * Expert(5 letters)
- A random secret code will be created with the letters: Z, X, C, V, B
- The secret code length is determined by you difficulty level.
- Your entries are not case sensitiv so go nuts on lower or uppcase.
- When entering your code leave no empty spaces before or after the comma ex:(z,x,c,v ).
- Crack the code before you run out of tries and you're a "Mastermind".


<div align="center"><h2>******************** GOOD LUCK!! ********************</h2></div>

## Features

- How to play the game  
- You are ask to enter a difficulty level

<img src= "./assets/screenshots/header.png" width=600 height=300>


- Secret code is genterated with the letters state in the instruction once you enter you difficulty level. 
- Displays you play level 
- Ask for your first guess. 


<img src= "./assets/screenshots/diff.png" width=600 height=300>



- Displays number of letters in the correct position.
- Displays number of correct letters guessed.
- Diplays previous guess.

<img src= "./assets/screenshots/enter_guess.png" width=600 height=300>

- End of game message if player solves the sercret code.
- With option to play again.

<img src= "./assets/screenshots/code_solved.png" width=600 height=75>

- Display message player runs out of tries before secret code is solved.
- Good bye message if player choosed to not play again.


<img src= "./assets/screenshots/No.png" width=600 height=100>


- Input validation  
  - Incorrect for difficult level 
  - Incorrect input for available letters
  
<img src= "./assets/screenshots/diff_val.png" width=600 height=75>
<img src= "./assets/screenshots/guess_val.png" width=600 height=75>

## Data Model 

I use function base progamming as my model. The game creats a random secret code from a list of five letters: z,x,c,v, or b. Each code length is determinded by the player inputing their difficulty level throung the command line.

Each function calls on various methond to create the random code and print statement as the game runs.
The print method is mainly used to informs the player of their progress in solving the secret code.

## Libraries
- [text2art](https://github.com/yhangf/text2art)
  - An import to create the Mastermind ACSII coversion text logo in the terminal.
  
- [Colored](https://dslackw.gitlab.io/colored/)
  - Import use to add color to printed text for readability in the terminal.

## Testing
Testing of Mastermind was done manually by:
- Ran code through a [PEP8](https://pep8ci.herokuapp.com/) linter with no major issues.  
- Performed multiple run ups of the game entering various correct and incorrect inputs to check input validators.   
- Played the game multiple times to ensure that the attemp count updated correctly. 

## Bugs
Bugs Solved:
- Accessing the get_difficult_input() assigned to difficult thought the game.
  - Fix: create global variables = difficult
- Issues with updating the correct total number of letters of players guess input to account for letters within the sercet code not just in the players guess input.  
Was solved by creating a dictionary to keep of track of the number of times each letter occurred in the secret code.

        ``` 
        remaining_letters = {
            letter: secret_code.count(letter) for letter in secret_code
        }

        ***
        if guess in secret_code and remaining_letters[guess] > 0:
                total_letters += 1
                remaining_letters[guess] -= 1
        ```

- No bugs on deployment were detected.
  
## Deployment 
- Deployment was performed using [HEROKU](heroku.com/apps).

## Credits and Acknowledgements
- [Geeks for Geeks:]( https://www.geeksforgeeks.org/) along side [ChatGBT](https://chat.openai.com/) to solve the issue the updating the total of correct letters with each players guess.
- [W3schools](https://www.w3schools.com/python/default.asp): Used as reference to sytax usage.

