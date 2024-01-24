import pygame
import sys

pygame.init()

SCREEN_SIZE = 550
GRID_SIZE = 9
CELL_SIZE = SCREEN_SIZE // GRID_SIZE
FONT = pygame.font.SysFont('Arial', 40)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_grid(screen, board):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)
            if board[j][i] != 0:
                text = FONT.render(str(board[j][i]), True, BLACK)
                screen.blit(text, (i * CELL_SIZE + 15, j * CELL_SIZE + 10))

def draw_selection(screen, row, col):
    pygame.draw.rect(screen, (0, 255, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

def create_editable_board(board):
    return [[board[i][j] == 0 for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]

def is_valid_board(board):
    def valid_group(group):
        return sorted(num for num in group if num != 0) == sorted(set(num for num in group if num != 0))
    for i in range(GRID_SIZE):
        if not valid_group([board[i][j] for j in range(GRID_SIZE)]) or not valid_group([board[j][i] for j in range(GRID_SIZE)]):
            return False
    for i in range(0, GRID_SIZE, 3):
        for j in range(0, GRID_SIZE, 3):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not valid_group(square):
                return False
    return True

def draw_button(screen, text, position, size):
    font = pygame.font.SysFont('Arial', 30)
    button_rect = pygame.Rect(position, size)
    pygame.draw.rect(screen, (180, 180, 180), button_rect)
    text_render = font.render(text, True, BLACK)
    screen.blit(text_render, (position[0] + 10, position[1] + 10))
    return button_rect

def reset_board(board, editable_board):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if editable_board[i][j]:
                board[i][j] = 0

def load_sudoku_challenges(file_path):
    puzzles = []
    with open(file_path, 'r') as file:
        for line in file:
            puzzle = [int(char) if char != '0' else 0 for char in line.strip()]
            puzzles.append([puzzle[i:i + GRID_SIZE] for i in range(0, len(puzzle), GRID_SIZE)])
    return puzzles

def is_complete_board(board):
    return all(board[i][j] != 0 for i in range(GRID_SIZE) for j in range(GRID_SIZE))

def is_valid_solution(board):
    return is_valid_board(board) and is_complete_board(board)

def main():
    puzzles = load_sudoku_challenges("sudoku_challenges.txt")

    screen = pygame.display.set_mode((SCREEN_SIZE + 150, SCREEN_SIZE)) 
    pygame.display.set_caption('Sudoku Game')

    selected_cell = None
    current_level = 0  
    sample_board = puzzles[current_level] 
    editable_board = create_editable_board(sample_board)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                check_button = draw_button(screen, 'Check', (SCREEN_SIZE + 10, 20), (120, 50))
                if check_button.collidepoint(pos):
                    if is_valid_solution(sample_board):
                        print("Valid Solution! Moving to next level.")
                        current_level += 1
                        if current_level < len(puzzles):
                            sample_board = puzzles[current_level]
                            editable_board = create_editable_board(sample_board)
                        else:
                            print("Congratulations! You have completed all levels.")
                            pygame.quit()
                            sys.exit()
                    else:
                        print("Invalid Solution!")

                reset_button = draw_button(screen, 'Reset', (SCREEN_SIZE + 10, 80), (120, 50))
                if reset_button.collidepoint(pos):
                    sample_board = [row[:] for row in puzzles[current_level]]
                    editable_board = create_editable_board(sample_board)

                elif pos[0] < SCREEN_SIZE:
                    col, row = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
                    selected_cell = (row, col)

            if event.type == pygame.KEYDOWN and selected_cell:
                if event.unicode.isdigit() and "1" <= event.unicode <= "9":
                    row, col = selected_cell
                    if editable_board[row][col]:
                        sample_board[row][col] = int(event.unicode)

        screen.fill(WHITE)
        draw_grid(screen, sample_board)

        check_button = draw_button(screen, 'Check', (SCREEN_SIZE + 10, 20), (120, 50))
        reset_button = draw_button(screen, 'Reset', (SCREEN_SIZE + 10, 80), (120, 50))

        level_text = FONT.render(f'Level: {current_level + 1}', True, BLACK)
        screen.blit(level_text, (SCREEN_SIZE + 10, 150))

        if selected_cell:
            draw_selection(screen, *selected_cell)

        pygame.display.flip()

main()