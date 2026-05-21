def filter_task_4_3(numbers):
    """
    Keep numbers greater than 10.
    Args:
        numbers: list of integers [5, 11, 20, 7, 10]
    Returns:
        list of numbers greater than 10
    """
    return numbers>10
w=[5, 11, 20, 7, 10]
print(list(filter(filter_task_4_3,w)))