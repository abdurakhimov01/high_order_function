def map_task_3_5(people):
    """
    Extract names from a list of dictionaries.
    Args:
        people: list of dictionaries [{"name": "Alice"}, {"name": "Bob"}, {"name": "Carol"}]
    Returns:
        list of names
    """
    return list(map(lambda x: x["name"],people))
print(map_task_3_5(people=[{"name": "Alice"}, {"name": "Bob"}, {"name": "Carol"}]))

