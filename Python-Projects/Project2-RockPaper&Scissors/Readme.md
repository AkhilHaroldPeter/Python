# Rock, Paper, Scissors Game

### To play RockPaperScissors, please click here : https://replit.com/@akhilpeter/Project2-RockPaperandScissors?v=1


## Description

Rock, Paper, Scissors is a classic hand game usually played between two people. The game has three possible outcomes: a tie, or a win for either player. Each player simultaneously forms one of three shapes with an outstretched hand. The possible shapes are:

- Rock: represented by a closed fist.
- Paper: represented by an open hand.
- Scissors: represented by a fist with the index and middle fingers extended, forming a V.

The winner is determined based on the chosen shapes according to the following rules:

- Rock crushes Scissors (Rock wins against Scissors).
- Scissors cuts Paper (Scissors win against Paper).
- Paper covers Rock (Paper wins against Rock).
- If both players choose the same shape, the game is a tie.

## Rules for the Python Project

1. **Player Input**: The player will choose one of the three options: Rock, Paper, or Scissors. This can be done either by typing the choice or by selecting from a menu.

2. **Computer Input**: The computer will randomly select one of the three options: Rock, Paper, or Scissors.

3. **Comparison**: The choices made by the player and the computer will be compared to determine the winner based on the rules mentioned above.

4. **Display Result**: The result of the game (win, lose, or tie) will be displayed to the player.

5. **Repeat or Quit**: After displaying the result, the player should have the option to play again or quit the game.

By implementing these rules, players can enjoy the classic Rock, Paper, Scissors game in a Python project, providing an interactive and entertaining experience.




## Dependencies

This project relies on the following Python packages:

- `text2art`:It is a tool utilized for transforming text into ASCII art. If the package is not already installed, you can install it by executing the following command: `pip install text2art`
- `random`: random module is in the python standard library. Used to give random choice from a given list of options.


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

## Usage
This project serves as a demonstration of proficiency in using the random module and if statements in Python. Additionally, it utilizes an external package called text2art to convert input text into ASCII art.
