def max_task_2_3(names):
    """
    Find the name with the highest number of letters.
    Args:
        names: list of strings ["Ann", "Robert", "Charlotte", "Mike"]
    Returns:
        name with most letters
    """
    return max(names, key=len)
print(max_task_2_3(names=["Ann", "Robert", "Charlotte", "Mike"]))
