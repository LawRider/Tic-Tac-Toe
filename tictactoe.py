def print_field(cells):
    print("---------")
    for i in range(0, 8, 3):
        print(f"| {cells[i]} {cells[i + 1]} {cells[i + 2]} |")
    print("---------")


def analyze_field(cells):
    rows_position = [cells[i:i+3] for i in range(0, 9, 3)]
    columns_position = [cells[i::3] for i in range(0, 3)]
    diagonals_position = [cells[0::4], cells[2:7:2]]
    return rows_position + columns_position + diagonals_position


def three_in_row(field_list):
    win_list = [['X', 'X', 'X'], ['O', 'O', 'O']]
    for item in win_list:
        if item in field_list:
            if item[0][0] == 'X':
                print('X wins')
            else:
                print('O wins')
            exit()


def next_step(cells, coord):
    row, col = coord.split()
    if not (row.isdigit() or col.isdigit()):
        print("You should enter numbers!")
    elif (int(row) or int(col)) not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
    else:
        index = (int(row) - 1) + ((3 - int(col)) * 3)
        if cells[index] is not ' ':
            print("This cell is occupied! Choose another one!")
        elif cells.count == 0:
            cells[index] = 'X'
        else:
            cells[index] = ('O' if cells.count('X') > cells.count('O') else 'X')


if __name__ == '__main__':
    cells_field = list(' ' * 9)
    print_field(cells_field)
    while cells_field.count(' ') > 0:
        step_input = input("Enter the coordinates: ")
        next_step(cells_field, step_input)
        print_field(cells_field)
        three_in_row(analyze_field(cells_field))
    else:
        print('Draw')
        exit()
