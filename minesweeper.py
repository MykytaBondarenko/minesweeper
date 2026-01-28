import random

grid_width = 30
grid_height = 20
grid_mines = 50

# Colors
DARK_GREY = "\x1b[38;2;96;96;96m"
GREY = "\x1b[38;2;128;128;128m"
RED = "\x1b[38;2;255;0;0m"
LIGHT_RED = "\x1b[38;2;255;153;153m"
YELLOW = "\x1b[38;2;255;255;0m"
WHITE = "\x1b[0m"

# Printing the filled in grid to the terminal (exists for debugging)
def print_full_grid():
    print()
    print(DARK_GREY + "G" * (grid_width + 2))
    for i in range(grid_height):
        line = ""
        for j in range(grid_width):
            if (full_grid[i][j] == 0):
                line += GREY + "-"
            elif (full_grid[i][j] == 9):
                line += RED + "m"
            else:
                line += WHITE + str(full_grid[i][j])
        print(DARK_GREY + "G" + line + DARK_GREY + "G")
    print(DARK_GREY + "G" * (grid_width + 2) + WHITE)

# Printing the user's visible grid to the terminal
def print_current_grid():
    global grid_mines
    space_left = False
    print()
    print("Mines left: " + str(grid_mines))
    print(DARK_GREY + "G" * (grid_width + 2))
    for i in range(grid_height):
        line = ""
        for j in range(grid_width):
            if (current_grid[i][j] == 0):
                line += " "
                space_left = True
            elif (current_grid[i][j] == 1):
                if (full_grid[i][j] == 0):
                    line += GREY + "-"
                else:
                    line += WHITE + str(full_grid[i][j])
            elif (current_grid[i][j] == 2):
                line += LIGHT_RED + "m"
            else:
                line += YELLOW + "?"
        print(DARK_GREY + "G" + line + DARK_GREY + "G")
    print(DARK_GREY + "G" * (grid_width + 2) + WHITE)
    return space_left

def try_square(i, j):
    if (i < 0 or i >= grid_height or j < 0 or j >= grid_width):
        return 2
    current_grid[i][j] += 3
    print_current_grid()
    current_grid[i][j] -= 3
    print("Would you like to Reveal or put a Mine on this square? (r/m/n)")
    input_string = input()
    if (input_string == "r"):
        return 0
    if (input_string == "m"):
        return 3
    return 1
    
def reveal_square(i, j):
    if (i < 0 or i >= grid_height or j < 0 or j >= grid_width):
        return 2
    if (full_grid[i][j] == 9):
        return 1
    if (full_grid[i][j] == 0 and current_grid[i][j] == 0):
        current_grid[i][j] = 1
        reveal_square(i - 1, j)
        reveal_square(i + 1, j)
        reveal_square(i, j - 1)
        reveal_square(i, j + 1)
        reveal_square(i - 1, j - 1)
        reveal_square(i - 1, j + 1)
        reveal_square(i + 1, j - 1)
        reveal_square(i + 1, j + 1)
    current_grid[i][j] = 1
    return 0

def mine_square(i, j):
    global grid_mines
    if (i < 0 or i >= grid_height or j < 0 or j >= grid_width):
        return 2
    if (current_grid[i][j] == 2):
        current_grid[i][j] = 0
        grid_mines += 1
    elif (grid_mines <= 0):
        print("No mines left")
    elif (current_grid[i][j] == 0):
        current_grid[i][j] = 2
        grid_mines -= 1
    return 0

'''
    Full grid:
    0-8 = Number of mines around the square
    9 = Mine

    Current grid:
    0 = Not revealed
    1 = Revealed
    2 = Marked as a mine
'''
full_grid = [] # basically filled in grid
current_grid = [] # grid used by the user

for i in range(grid_height):
    full_grid.append([])
    current_grid.append([])
    for j in range(grid_width):
        full_grid[i].append(0)
        current_grid[i].append(0)

i = 0
while i < grid_mines:
    rand_height = random.randint(0, grid_height - 1)
    rand_width = random.randint(0, grid_width - 1)
    if (full_grid[rand_height][rand_width] == 9):
        i -= 1
    else:
        full_grid[rand_height][rand_width] = 9

        # updating the number of mines around the mine (and making sure we don't go out of the array)
        if (rand_height > 0): # north
            if (full_grid[rand_height - 1][rand_width] < 9):
                full_grid[rand_height - 1][rand_width] += 1
        if (rand_height < grid_height - 1): # south
            if (full_grid[rand_height + 1][rand_width] < 9):
                full_grid[rand_height + 1][rand_width] += 1
        if (rand_width > 0): # west
            if (full_grid[rand_height][rand_width - 1] < 9):
                full_grid[rand_height][rand_width - 1] += 1
        if (rand_width < grid_width - 1): # east
            if (full_grid[rand_height][rand_width + 1] < 9):
                full_grid[rand_height][rand_width + 1] += 1
        if (rand_height > 0 and rand_width > 0): # north-west
            if (full_grid[rand_height - 1][rand_width - 1] < 9):
                full_grid[rand_height - 1][rand_width - 1] += 1
        if (rand_height > 0 and rand_width < grid_width - 1): # north-east
            if (full_grid[rand_height - 1][rand_width + 1] < 9):
                full_grid[rand_height - 1][rand_width + 1] += 1
        if (rand_height < grid_height - 1 and rand_width > 0): # south-west
            if (full_grid[rand_height + 1][rand_width - 1] < 9):
                full_grid[rand_height + 1][rand_width - 1] += 1
        if (rand_height < grid_height - 1 and rand_width < grid_width - 1): # south-east
            if (full_grid[rand_height + 1][rand_width + 1] < 9):
                full_grid[rand_height + 1][rand_width + 1] += 1
    
    i += 1

while (print_current_grid()):
    input_string = input()
    input_arr = input_string.split()

    if (len(input_arr) != 2 or not input_arr[0].isnumeric() or not input_arr[1].isnumeric()):
        print("Input not accepted, please input two coordinates, separated by space")
        continue

    i = int(input_arr[0])
    j = int(input_arr[1])
    try_result = try_square(i, j)

    if (try_result == 2):
        print("Coordinate is outside of the grid, please enter a new one")
        continue
    if (try_result == 1):
        print("Enter a new coordinate")
        continue

    action_result = 0
    if (try_result == 3):
        action_result = mine_square(i, j)
    if (try_result == 0):
        action_result = reveal_square(i, j)

    if (action_result == 2):
        print("Coordinate is outside of the grid, please enter a new one")
        continue

    if (action_result == 1):
        print_full_grid()
        print()
        print("This square had a mine, you lost :(")
        break
else:
    print("Good job, you won! :)")