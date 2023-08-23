print("Welcome to Sudoku")
username = input("Please input your username: ")
password = input("Please input your 4 digit pin: ")
save_dir = "username.txt"
def save_file(save_dir, username, pasword):
    with open(save_dir, 'r') as file:
        lines = file.readlines()
        if line_number < 1 or line_number > len(lines):
            print("Invalid line number!")
            return None
        sudoku_line = lines[line_number - 1].strip()
        if len(sudoku_line) != 81:
            print("Invalid Sudoku format!")
            return None
        return sudoku_line

def read_sudoku_from_file(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if line_number < 1 or line_number > len(lines):
            print("Invalid line number!")
            return None
        sudoku_line = lines[line_number - 1].strip()
        if len(sudoku_line) != 81:
            print("Invalid Sudoku format!")
            return None
        return sudoku_line

def display_sudoku(sudoku):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(sudoku[i * 9 + j], end=" ")
        print()

def solve_sudoku(sudoku):
    def is_valid(sudoku, row, col, num):
        for i in range(9):
            if sudoku[row * 9 + i] == num or sudoku[i * 9 + col] == num:
                return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if sudoku[(start_row + i) * 9 + (start_col + j)] == num:
                    return False
        return True

    def solve(sudoku):
        for i in range(9):
            for j in range(9):
                if sudoku[i * 9 + j] == '0':
                    for num in '123456789':
                        if is_valid(sudoku, i, j, num):
                            sudoku[i * 9 + j] = num
                            if solve(sudoku):
                                return True
                            sudoku[i * 9 + j] = '0'
                    return False
        return True

    sudoku = list(sudoku)
    if solve(sudoku):
        return ''.join(sudoku)
    else:
        return None

def solve_sudoku(sudoku):
    def is_valid(sudoku, row, col, num):
        for i in range(9):
            if sudoku[row * 9 + i] == num or sudoku[i * 9 + col] == num:
                return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if sudoku[(start_row + i) * 9 + (start_col + j)] == num:
                    return False
        return True

    def solve(sudoku):
        for i in range(9):
            for j in range(9):
                if sudoku[i * 9 + j] == '0':
                    for num in '123456789':
                        if is_valid(sudoku, i, j, num):
                            sudoku[i * 9 + j] = num
                            if solve(sudoku):
                                return True
                            sudoku[i * 9 + j] = '0'
                    return False
        return True

    sudoku = list(sudoku)
    if solve(sudoku):
        return ''.join(sudoku)
    else:
        return None


# Example usage
file_path = 'C:\\Users\\Arunav\\Desktop\\Projects\\Sudoku\\Ques.txt'

line_number = int(input("Input Level: "))

sudoku = read_sudoku_from_file(file_path, line_number)
if sudoku is not None:
    print("Sudoku:")
    display_sudoku(sudoku)
def real():
    response = input("Input a command, type help for list of available commands: ")
    if response == "help":
        print("Type try to input a digit.")
        print("Type solve to get the solution.")
        print("Type check to do a validity check.")
        real()
    elif response == "try":
        row2 = int(input("Input the row number: "))
        col2 = int(input("Input the coloumn number: "))
        num2 = int(input("Input the value: "))
        if sudoku is not None:
            print("Sudoku:")
            display_sudoku(sudoku)
        real()
    elif response == "solve":
        solved_sudoku = solve_sudoku(sudoku)
        if solved_sudoku is not None:
            print("\nSolved Sudoku:")
            display_sudoku(solved_sudoku)
        else:
            print("\nUnable to solve the Sudoku.")
        real()
    elif response == "check":
        print("")
        real()
    elif response == "quit":
        exit(0)
    else:
        print("Invalid Command")
        real()
real()


#load save file
#savefile encryption
#password check
#hint for one digit
#try solving(protect and un)
#if win, edit savefile