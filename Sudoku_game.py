import pygame
import sys
import numpy as np
import pandas as pd

pygame.init()
pygame.font.init()
original_grid = np.array([]) 

WIDTH, HEIGHT = 540, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")
current_level = 0
sudoku_grid = np.array([]) 
original_grid = np.array([]) 

level_font = pygame.font.Font(None, 36)

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

    sudoku_levels = load_sudoku('sudoku_challenges.txt')

    if sudoku_levels.size == 0:
        print("Error: No Sudoku challenges found.")
        sys.exit()

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

def is_solved():
    return np.array_equal(sudoku_grid, original_grid)

def draw_grid(screen):
    for i in range(1, GRID_SIZE):
        thickness = 2 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)

# Draw the numbers on the Sudoku grid
def draw_numbers(screen, level):
    font = pygame.font.Font(None, 36)

    if sudoku_grid.size > 0 and original_grid.size > 0:
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                number = str(sudoku_grid[i, j]) if original_grid[i][j] != 0 else ""
                print("number", number)
                text = font.render(number, True, BLACK)
                x = j * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2
                y = i * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2
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


# Variables for player input


# Main game loop
def main():
    global selected_cell, input_number     
    selected_cell = None
    input_number = None
    initialize_game()  
    screen.fill(WHITE)
    draw_grid(screen)
    draw_numbers(screen, current_level)
    draw_buttons(screen)
    pygame.display.flip() 
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                selected_cell = (y // CELL_SIZE, x // CELL_SIZE)
                  # Debugging print
            elif event.type == pygame.KEYDOWN:
                if selected_cell is not None:
                    if event.key == 8 or event.key == 27:
                        input_number = 0
                    elif 49 <= event.key <= 57:
                        input_number = event.key - 48
                # Update the sudoku grid based on input
                if selected_cell is not None and input_number is not None:
                    row, col = selected_cell
                    print(row)
                    print(col)
                    if original_grid[row, col] == 0:
                        sudoku_grid[row, col] = input_number
                        print(sudoku_grid[row, col],input_number)                        
                        selected_cell = None
                        input_number = None
                        screen.fill(WHITE)
                        draw_grid(screen)
                        draw_numbers(screen, current_level)
                        draw_buttons(screen)
                        pygame.display.flip()

            


        # Reset input variables
   

        

    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    main()
