def min_task_1_2(words):
    """
    Find the shortest word.
    Args:
        words: list of strings ["apple", "banana", "kiwi", "pear"]
    Returns:
        shortest word
    """
    return min(words, key=len)
print(min_task_1_2(words=["apple", "banana", "kiwi", "pear"]))
