
def dynamic_programming_solver(items, weights, values, CAPACITY, n_items):
    if CAPACITY <= 0 or n_items == 0 or len(weights) != n_items:
        print("error")
        exit()

    rows, cols = (n_items, CAPACITY+1)

    # create a two dimensional array for Memoization, each element is initialized to '0'
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
