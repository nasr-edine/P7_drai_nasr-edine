from itertools import combinations


def brute_force(n, capacity, weights, values, items):
    """Brute force method for solving knapsack problem
    :param n: number of existing items
    :param capacity: the capacity of knapsack
    :param weights: list of weights
    :param values: list of values
    :return: (cost, max_value, best_subset, list_index)
    """
    max_value = 0
    for index in range(n):
        # generating combinations from 1 to n items
        for subset in set(combinations(items, index + 1)):
            total_cost = 0
            total_profit = 0
            for i in subset:
                total_cost += weights[items.index(i)]
                total_profit += values[items.index(i)]
            if total_cost <= capacity and total_profit > max_value:
                max_value = total_profit
                best_subset = subset
    cost = 0
    for i in best_subset:
        cost += weights[items.index(i)]

    return cost, max_value, best_subset
