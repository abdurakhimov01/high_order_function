def map_task_3_4(numbers):
    """
    Square each number.
    Args:
        numbers: list of integers [1, 4, 5]
    Returns:
        list of squared numbers
    """
    return list(map(lambda x: x**2,numbers))
print(map_task_3_4(numbers=[1, 4, 5]))
