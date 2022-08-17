import utils

def test_neighborhood(fun):

    # Case 1: extract a small neighborhood in the center of a city

    city1 = utils.city('../data/city1.csv')
    correct1 = utils.city('../data/correct-results/correct-test1.csv')

    try:
        answer1 = fun(city1, 1, (3, 4))
    except error as e:
        print('Error')

    # to be finalized

    return None
