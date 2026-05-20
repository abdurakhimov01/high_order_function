def filter_task_4_2(words):
    """
    Keep words longer than 4 letters.
    Args:
        words: list of strings ["hi", "hello", "world", "cat"]
    Returns:
        list of words longer than 4 letters
    """
    words=["hi", "hello", "world", "cat"]
    o=[]
    for i in words:
        if len(i)>4:
            o.append(i)
    return o
print(filter_task_4_2(words=["hi", "hello", "world", "cat"]))