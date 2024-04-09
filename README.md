# Guess.py - A Number Guessing Game

## Overview

`Guess.py` is a Python-based number guessing game. The script generates a random integer between 1 and 100 and prompts the user to guess the number. The game provides feedback on whether the user's guess is too low or too high, and continues until the correct number is guessed.

## Detailed Description

The script begins by importing the `random` module and defining a helper function `isfloat(x)`. This function attempts to convert its argument to a float. If the conversion is successful, it returns `True`; otherwise, it returns `False`.

The main part of the script starts by generating a random integer between 1 and 100. It then enters a loop where it prompts the user to guess the number. If the user's input is an integer, it compares the input to the generated number. If the guess is correct, it congratulates the user and ends the game. If the guess is too low or too high, it informs the user and prompts for another guess. If the user's input is not an integer, the script checks if it's a float using the `isfloat(x)` function.

## Installation

Python 3 is required to run this script. If you don't have Python installed, you can download it from [here](https://www.python.org/downloads/).

## Usage

To run the script, navigate to the directory containing `Guess.py` and run the following command in your terminal:

```bash
python Guess.py