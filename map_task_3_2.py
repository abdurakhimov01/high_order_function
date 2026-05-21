def map_task_3_2(words):
    """
    Convert all words to uppercase.
    Args:
        words: list of strings ["cat", "dog", "fish"]
    Returns:
        list of uppercase words
    """
    return [i.upper() for i in words]
print(map_task_3_2(words=["cat", "dog", "fish"]))
