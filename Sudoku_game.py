import pygame
import sys
import numpy as np
import pandas as pd

# Initialize Pygame
pygame.init()
pygame.font.init()
original_grid = np.array([])  # Initialize an empty NumPy array

# Constants
WIDTH, HEIGHT = 540, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialize the display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

# Initialize global variables
# ... (existing code)

# Initialize global variables
current_level = 0
sudoku_grid = np.array([])  # Initialize an empty NumPy array
original_grid = np.array([])  # Add this line

# Add the rest of your script below...
# Initialize an empty NumPy array
level_font = pygame.font.Font(None, 36)  # Add this line

# Add the rest of your script below...

def load_sudoku(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        sudoku_lines = file.readlines()

    sudoku_levels = []
    for line in sudoku_lines:
        line_digits = [int(char) for char in line.strip() if char.isdigit()]
        if len(line_digits) == 81:
            sudoku_levels.append(np.array(line_digits).reshape((9, 9)))
        else:
            raise ValueError(f"Invalid number of elements in a line of the Sudoku grid: {line}")

    return np.array(sudoku_levels)



def initialize_game():
    global current_level, sudoku_levels, sudoku_grid, original_grid

    # Load Sudoku challenges
    sudoku_levels = load_sudoku('sudoku_challenges.txt')

    # Check if there are any Sudoku levels
    if not sudoku_levels:
        print("Error: No Sudoku challenges found.")
        sys.exit()

    # Additional debugging information
    print(f"Total Sudoku Levels: {len(sudoku_levels)}")

    if current_level < len(sudoku_levels):
        original_grid = np.copy(sudoku_levels[current_level])
        sudoku_grid = np.copy(original_grid)
        print(f"Sudoku Grid Shape: {sudoku_grid.shape}")
        print(f"Original Grid Shape: {original_grid.shape}")
        print(f"Original Grid:\n{original_grid}")
    else:
        print("Error: No Sudoku challenges for the current level.")
        sys.exit()




# Check if the Sudoku puzzle is solved
# Check if the Sudoku puzzle is solved
def is_solved():
    return np.array_equal(sudoku_grid, original_grid)

# Draw the Sudoku grid
def draw_grid(screen):
    for i in range(1, GRID_SIZE):
        thickness = 2 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)

# Draw the numbers on the Sudoku grid
# Draw the numbers on the Sudoku grid
# Draw the numbers on the Sudoku grid
def draw_numbers(screen, level):
    font = pygame.font.Font(None, 36)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            number = str(sudoku_grid[i, j]) if original_grid[i][j] != 0 else ""
            text = font.render(number, True, BLACK)

            # Calculate cell position
            x = j * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2
            y = i * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2

            # Draw numbers in the cells
            screen.blit(text, (x, y))

    # Draw the level number
    level_text_rendered = level_font.render(f"Level: {level + 1}", True, BLACK)
    screen.blit(level_text_rendered, (10, HEIGHT - 40))



# Draw the buttons
def draw_buttons(screen):
    font = pygame.font.Font(None, 36)

    # Check button
    pygame.draw.rect(screen, GRAY, (WIDTH - 150, HEIGHT - 50, 120, 40))
    check_text = font.render("Check", True, BLACK)
    screen.blit(check_text, (WIDTH - 140, HEIGHT - 40))

    # Exit button
    pygame.draw.rect(screen, GRAY, (WIDTH - 300, HEIGHT - 50, 120, 40))
    exit_text = font.render("Exit", True, BLACK)
    screen.blit(exit_text, (WIDTH - 280, HEIGHT - 40))

# Main game loop
# Main game loop
# ... (existing code)

# Variables for player input
selected_cell = None
input_number = None

# Main game loop
# Main game loop
# Main game loop
def main():
    global sudoku_grid, original_grid, current_level

    # Variables for player input
    selected_cell = None
    input_number = None

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                # Check if a cell is clicked
                selected_cell = (y // CELL_SIZE, x // CELL_SIZE)  # Swap x and y due to row, column indexing
            elif event.type == pygame.KEYDOWN and selected_cell is not None:
                # Check if a number key is pressed
                if pygame.K_1 <= event.key <= pygame.K_9:
                    input_number = event.key - pygame.K_0
                elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    # Allow the player to clear the cell using Backspace or Delete
                    input_number = 0

        # Handle player input
        if selected_cell is not None and input_number is not None:
            if original_grid[selected_cell] == 0:
                sudoku_grid[selected_cell] = input_number

        # Clear input variables
        selected_cell = None
        input_number = None

        screen.fill(WHITE)
        draw_grid(screen)
        draw_numbers(screen, current_level)
        draw_buttons(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    main()
