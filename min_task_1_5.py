def min_task_1_5(tuples):
    """
    Find the tuple with the smallest second element.
    Args:
        tuples: list of tuples [(1, 3), (2, 2), (3, 1)]
    Returns:
        tuple with smallest second element
    """
    return min(tuples, key=lambda x: x[1])
print(min_task_1_5(tuples=[(1, 3), (2, 2), (3, 1)]))