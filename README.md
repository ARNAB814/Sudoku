# Sudoku Game in Pygame

## Description
This project is an interactive Sudoku game developed using Pygame. The game features a graphical user interface where players can solve Sudoku puzzles, check their solutions, and progress through multiple levels. Each level is loaded from a text file, offering a variety of puzzles.

## Features
- Graphical User Interface using Pygame.
- Sudoku puzzle solver with mouse and keyboard inputs.
- 'Check' button to validate the current solution.
- 'Reset' button to clear all inputs and start the puzzle over.
- Level progression: Completing a puzzle advances to the next level.
- Puzzles are loaded from a text file, allowing for easy extension of the game with new levels.

## Requirements
- Python 3.x
- Pygame library

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install Pygame:
   ```
   pip install pygame
   ```
3. Clone or download this repository.

## Running the Game
1. Navigate to the game directory.
2. Run the game script:
   ```
   python sudoku_game.py
   ```
3. The game window should open, displaying the first puzzle.

## How to Play
- Click on a cell to select it and then type a number (1-9) to fill in the cell.
- Use the 'Check' button to validate your solution. If correct, the game will move to the next level.
- Use the 'Reset' button to clear all your inputs in the current puzzle.
- Complete all levels to finish the game.

## Sudoku Challenges File
- The puzzles are loaded from `sudoku_challenges.txt`.
- Each line in the file represents a Sudoku puzzle.
- Puzzles are formatted as a single line of 81 digits, where 0 represents an empty cell.
- Dataset imported from Kaggle (https://www.kaggle.com/datasets/bryanpark/sudoku)
