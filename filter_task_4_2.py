def filter_task_4_2(words):
    """
    Keep words longer than 4 letters.
    Args:
        words: list of strings ["hi", "hello", "world", "cat"]
    Returns:
        list of words longer than 4 letters
    """
    return len(words)>4
words=["hi", "hello", "world", "cat"]
print(list(filter(filter_task_4_2,words)))