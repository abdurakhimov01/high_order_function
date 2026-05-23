def max_task_2_2(words):
    """
    Find the longest word.
    Args:
        words: list of strings ["pen", "notebook", "eraser"]
    Returns:
        longest word
    """
    return max(list(map(lambda x: len(x),words)))
print(max_task_2_2(words=["pen", "notebook", "eraser"]))
