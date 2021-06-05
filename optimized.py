
def dynamic_programming_solver(items, weights, values, capacity, n_items):
    """Dynamic programming method for solving knapsack problem
    :param n_items: number of existing items
    :param capacity: the capacity of knapsack
    :param weights: list of weights
    :param values: list of values
    :return: (cost, max_value, best_items)
    """

    rows, cols = (n_items, capacity+1)

    # create a two dimensional array for Memoization
    M = [[0 for i in range(cols)] for j in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if weights[row] > col:
                M[row][col] = M[row - 1][col]
            else:
                x = max(M[row - 1][col], M[row - 1]
                        [col - weights[row]] + values[row])
                M[row][col] = x

    i = rows - 1
    j = cols - 1
    while M[i][j] == M[i][j - 1]:
        j -= 1

    i = rows - 1
    best_items = []
    best_items_index = []

    while j > 0:
        while i > 0 and M[i][j] == M[i - 1][j]:
            i -= 1
        j = j - weights[i]
        if j >= 0:
            best_items.append(items[i])
            best_items_index.append(i)
        i -= 1

    cost = 0
    for i in best_items_index:
        cost += weights[i]

    cost = cost / 100
    max_value = M[rows - 1][cols - 1]/10000
    return cost, max_value, best_items
