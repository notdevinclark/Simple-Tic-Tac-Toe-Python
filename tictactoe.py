import textwrap

empty_char = '_'
x_char = 'X'
o_char = 'O'
number_of_spaces = 9
win_count_dict = {x_char: 0, o_char: 0}
grid_string = number_of_spaces * empty_char
move_count = 0


def print_grid():
    grid = [list(row) for row in textwrap.wrap(grid_string, 3)]

    print('---------')
    for row in grid:
        row_string = ' '.join(row)
        print(f"| {row_string} |")
    print('---------')


def grid_filled():
    return True if grid_string.count(empty_char) == 0 else False


def number_of_turns(player_char):
    return grid_string.count(player_char)


def count_wins():
    top = grid_string[0:3]
    middle = grid_string[3:6]
    bottom = grid_string[6:9]
    left = grid_string[0::3]
    center = grid_string[1::3]
    right = grid_string[2::3]
    diagonal_1_to_9 = grid_string[0::4]
    diagonal_7_to_3 = grid_string[2:8:2]

    for char in list(win_count_dict):
        win_count_dict[char] = [top, middle, bottom, left, center, right,
                                diagonal_1_to_9, diagonal_7_to_3
                                ].count(char * 3)


def should_the_game_continue():
    count_wins()
    if (win_count_dict[x_char] > 0 and win_count_dict[o_char] > 0) or\
            (abs(number_of_turns(x_char) - number_of_turns(o_char)) >= 2):
                state = 'Impossible'
    elif grid_filled() and win_count_dict[x_char] == 0 and win_count_dict[o_char] == 0:
        state = 'Draw'
    elif win_count_dict[x_char] > 0:
        state = 'X wins'
    elif win_count_dict[o_char] > 0:
        state = 'O wins'
    else:
        # No End State has been triggered, the game should continue
        return True

    # An End State has been triggered, the game should NOT continue
    print(state)
    return False


def make_move(char):
    index = None

    while True:
        try:
            # Attempts to get the input and convert the string into integers
            coordinates = [int(string_input) for string_input in input().split(' ')]
        except ValueError:
            print('You should enter numbers!')
            continue

        # Validates Input is in the correct range
        if coordinates[0] < 1 or coordinates[0] > 3 or coordinates[1] < 1 or coordinates[1] > 3:
            print('Coordinates should be from 1 to 3!')
            continue

        # Converts the pass 2 integer input into the index of the grid_string
        index = (3 * (coordinates[0] - 1)) + (coordinates[1] - 1)

        if grid_string[index] != empty_char:
            print('This cell is occupied! Choose another one!')
            continue
        else:
            break

    grid_list = list(grid_string)
    grid_list[index] = char
    return ''.join(grid_list)


# Print the empty grid and start the Game
print_grid()

while should_the_game_continue():
    if move_count % 2 == 0:
        grid_string = make_move(x_char)
    else:
        grid_string = make_move(o_char)
    move_count += 1
    print_grid()

