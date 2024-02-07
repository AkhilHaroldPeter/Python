# Hangman Game

### To play hangman, click here : https://replit.com/@akhilpeter/Project4-Hangman?v=1


## Description

Hangman is a classic word-guessing game where players try to guess a secret word by suggesting letters within a certain number of attempts. The game provides an engaging and interactive way to test your vocabulary and deduction skills.

## Rules

- A secret word is selected, and the player must guess it by suggesting letters.
- The player has a limited number of incorrect guesses (usually represented by the hangman's body parts).
- If the player guesses a correct letter, it is revealed in the secret word.
- If the player guesses an incorrect letter, a part of the hangman is drawn.
- The game ends when the player correctly guesses the entire word or runs out of attempts.

## How to Play

1. **Start the Game**: Launch the Hangman game.

2. **Select Word Category**: Choose the category of words you want to guess:
   - **Random Words**: Guess randomly selected words.
   - **Anime Names**: Guess names of anime titles.
   - **Country Names**: Guess names of countries.

3. **Secret Word**: A secret word from the selected category will be chosen randomly, and the player must guess it by suggesting letters.

4. **Guessing Letters**: Guess letters one at a time by inputting them through the keyboard.

5. **Correct Guesses**: If the guessed letter is in the secret word, it will be revealed in the word.

6. **Incorrect Guesses**: If the guessed letter is not in the secret word, a part of the hangman will be drawn.

7. **Win or Lose**: The game ends when the player either correctly guesses the entire word or runs out of attempts.


## Dependencies

This project requires the following Python packages:

- `random_words`: Used for generating random words to be guessed in the game.
- `pycountry`: Used for accessing country names for potential secret words.
- `text2art`: Used to create ASCII art for visual appeal.
- `pandas`: Used for data manipulation and analysis.
- `random`: Used for generating random numbers or selecting random words.

## Installation

To install the required packages, use the following `pip` commands:

```pip install random_words```
```pip install pycountry```
```pip install text2art```
```pip install pandas```

## Python Installation

To run this project, you need to have Python installed on your system. If you haven't installed Python yet, follow these steps:

### Windows

1. Download Python installer from the [official website](https://www.python.org/downloads/).
2. Run the installer, ensuring that the option to add Python to your PATH is selected.
3. Follow the installation steps, and Python will be installed on your system.

### macOS

1. macOS usually comes with Python pre-installed. To check if Python is installed, open the Terminal and type `python3 --version`. If Python is installed, it will display the version number.
2. If Python is not installed, you can install it using [Homebrew](https://brew.sh/). Open Terminal and run the following command:
`brew install python@3.9`

### Linux

1. Python is often installed by default on Linux systems. To check if Python is installed, open a terminal and type `python3 --version`. If Python is installed, it will display the version number.
2. If Python is not installed, you can install it using your distribution's package manager. For example, on Ubuntu, you can use `apt`:
`sudo apt update`
`sudo apt install python3`

## After you have installed python you can run the code by following the below steps:
- Clone the repository to your local machine: https://github.com/AkhilHaroldPeter/Python.git (If this is your first time doing this, please follow through the following documentation: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- Navigate to the directory containing the Hangman files.
- Install the required packages using pip.
- Run the 'Project4-Hangman.py' script.
- Execute the code and make selections from the options provided to enjoy the game experience.
#### Alternatively, you can download the repository as a zip file, unzip it, and then use it on your local machine.

## Key Concepts

- Word Selection: Implemented mechanisms to select words for the player to guess, ensuring a diverse and engaging gameplay experience.
- User Input Handling: Utilized input handling techniques to process the player's guesses and interactions with the game interface.
- String Manipulation: Employed string manipulation methods to display the hidden word, reveal correctly guessed letters, and update the game status.
- Game Logic: Implemented algorithms to determine whether the player's guesses are correct or incorrect, and to track the player's progress in guessing the word.
- Graphics Rendering: Utilized ASCII art or graphical representations to enhance the visual appeal of the game interface and provide feedback to the player.


