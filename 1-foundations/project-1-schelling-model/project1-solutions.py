def neighborhood(grid, location):

    '''
    Extracts the neighborhood of a location and uses a neighborhood extension of one

    Inputs:
        - city grid (list of lists): total grid where the neighborhood (subgrid) is extracted from
        - location (list of two int):
            the row and column index (stating at zero) of the location we extract the neighborhood for.
            examples: [0, 4] or [5, 1]
    Output:
        - neighborhood (list of lists): the neighborhood of this location at the specified extension
    '''
    i, j = location
    N = len(grid)
    subgrid = []

    # Neighborhood indices limits
    up = max(0, i - 1)
    down = min(N, i + 1)
    left = max(0, j - 1)
    right = min(N, j + 1)

    # Extracting neighborhood
    for row in grid[up: down + 1]:
        subgrid.append(row[left: right + 1])

    return subgrid

def similarity(grid, location):

    i, j = location
    my_neighborhood = neighborhood(grid, location)
    group = grid[i][j]
    numerator = 0
    denominator = 0

    # Adding units to numerator or denominator
    for street in my_neighborhood:
        for lot in street:
            if lot == group:
                numerator += 1
            if lot != '':
                denominator +=1

    return numerator / denominator

def hypothetical_similarity(grid, current_location, new_location):

    i, j = current_location
    group = grid[i][j]
    i_new, j_new = new_location

    # Creating a copy of the city grid -- that's where we work
    city_clone = clone_grid(grid)
    city_clone[i_new][j_new] = group
    city_clone[i][j] = ''

    return similarity(city_clone, new_location)

def list_available(grid, location, threshold):

    available = []

    for i, street in enumerate(grid):
        for j, lot in enumerate(street):
            if lot == '': # lot is available
                similarity = hypothetical_similarity(grid, location, [i, j])
                if similarity >= threshold:
                    available.append([i, j])

    return available

def euclidean_distance(current_location, new_location):

    dist = ((current_location[0]-new_location[0])**2 + (current_location[1]-new_location[1])**2)**(1/2)

    return dist

def move_agent(grid, location, threshold):

    similarity_score = similarity(grid, location)

    # Case 1: agent is satisfied
    if similarity_score >= threshold:
        return grid

    else:
        city_clone = clone_grid(grid)
        available = list_available(grid, location, threshold)
        i, j = location
        group = grid[i][j]

        # Case 2: no available spots
        if len(available)==0:
            return grid
        # Case 3: only one available spot
        elif len(available)==1:
            best_location = available[0]
        # Case 4: more than one available spot
        else:
            for n, new_location in enumerate(available):
                distance = euclidean_distance(location, new_location)
                # if location is the first of list, we assign it as the best
                if n == 0:
                    best_location = new_location
                    best_distance = distance
                # if not, we update best candidate only if location is closer
                else:
                    if distance < best_distance:
                        best_location = new_location
                        best_distance = distance

        new_i, new_j = best_location
        city_clone[new_i][new_j] = group
        city_clone[i][j] = ''
        return city_clone

def one_round(grid, threshold):

    N = len(grid)
    city_clone = clone_grid(grid)
    moves = 0 # move counter

    # iterating through rows
    for row_i in range(N):
        # iterating through columns
        for col_i in range(N):
            # checking that location is not empty
            if city_clone[row_i][col_i] != '':
                new_city = move_agent(city_clone, [row_i, col_i], threshold)
                # now we check if attempting to move the agent produced a
                # change in the grid. We only add +1 to the move counter if
                # the resulting grid is different to the initial one
                if new_city != city_clone:
                    moves += 1
                    # updating the old grid to compare results
                    # in the next iteration
                    city_clone = new_city

    return new_city, moves

def run_schelling(grid, threshold, max_rounds):

    moved = True
    rounds = 0 # rpunds counter
    city_clone = [row[:] for row in grid]

    while moved == True and rounds < max_rounds:

        city_clone, n_moves = one_round(city_clone, threshold)

        # if no one moved, we set moved to False and the loop will end
        if n_moves == 0:
            moved = False
        # if there were moves, we increase the round counter
        else:
            rounds += 1

    return city_clone, rounds
