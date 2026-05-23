def max_task_2_5(people):
    """
    Find the person with the highest age.
    Args:
        people: list of dictionaries [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 45}, {"name": "Tom", "age": 28}]
    Returns:
        dictionary of person with highest age
    """
    return max(people, key=lambda x:x["age"])
print(max_task_2_5(people=[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 45}, {"name": "Tom", "age": 28}]))
