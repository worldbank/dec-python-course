import csv

def city(file):

    '''
    Reads a city from a predefined csv file to a list of lists
    '''

    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    return data

def show_grid(grid):

    '''
    Prints a representation of a city grid, returns nothing
    '''

    for row in grid:
        print_this = '['
        for item in row:
            if item.isnumeric():
                print_this += ' ' + item + ' '
            else:
                print_this += '   '
        print_this += ']'
        print(print_this)

def test_equality(x1, x2):

    if x1 == x2:
        return True
    else:
        return False
