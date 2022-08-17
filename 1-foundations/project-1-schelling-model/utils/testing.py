import utils

def yes():
    print("yes")

def test_neighborhood(fun):

    city = utils.city('data/city1.csv')
    answer1 = None
    answer2 = None
    answer3 = None
    answer4 = None

    # Case 1: extract a small neighborhood in the center of a city
    print('Testing case 1: small neigborhood in the center of a city')

    try:
        correct1 = utils.city('data/correct-results/correct-case1-neighborhood.csv')
        answer1 = fun(city, 1, (3, 4))
        if answer1 == correct1:
            print('\tPassed')
        else:
            if answer1:
                print('Your solution:')
                utils.show_grid(answer1)
                print('\nCorrect answer:')
                utils.show_grid(correct1)
            raise ValueError('Solution did not pass test')

    except Exception as err:
        raise err

    # Case 2: corner location
    print('Testing case 2: location in a corner')

    try:
        correct2 = utils.city('data/correct-results/correct-case2-neighborhood.csv')
        answer2 = fun(city, 2, (0, 0))
        if answer2 == correct2:
            print('\tPassed')
        else:
            if answer2:
                print('Your solution:')
                utils.show_grid(answer2)
                print('\nCorrect answer:')
                utils.show_grid(correct2)
            raise ValueError('Solution did not pass test')

    except Exception as err:
        raise err

    # Case 3: neighborhood of extension = zero
    print('Testing case 3: neighborhood of extension zero')

    try:
        correct3 = utils.city('data/correct-results/correct-case3-neighborhood.csv')
        answer3 = fun(city, 0, (3, 4))
        if answer3 == correct3:
            print('\tPassed')
        else:
            if answer3:
                print('Your solution:')
                utils.show_grid(answer3)
                print('\nCorrect answer:')
                utils.show_grid(correct3)
            raise ValueError('Solution did not pass test')

    except Exception as err:
        raise err

    # Case 4: big neighborhood of extension higher than the city
    print('Testing case 4: big neighborhood of extension higher than a city')

    try:
        correct4 = utils.city('data/correct-results/correct-case4-neighborhood.csv')
        answer4 = fun(city, 10, (3, 3))
        if answer4 == correct4:
            print('\tPassed')
        else:
            if answer4:
                print('Your solution:')
                utils.show_grid(answer4)
                print('\nCorrect answer:')
                utils.show_grid(correct4)
            raise ValueError('Solution did not pass test')

    except Exception as err:
        raise err

    print('You can continue with the next task')
    return None
