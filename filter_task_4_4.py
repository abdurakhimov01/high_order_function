def filter_task_4_4(names):
    """
    Filter names that start with "A".
    Args:
        names: list of strings ["Alice", "Bob", "Anna", "Charlie"]
    Returns:
        list of names that start with "A"
    """
    return names[0]=="A"
a=["Alice", "Bob", "Anna", "Charlie"]
print(list(filter(filter_task_4_4,a)))