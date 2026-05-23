def min_task_1_3(words):
    """
    Find the string with the smallest number of vowels.
    Args:
        words: list of strings ["book", "sky", "quiet", "data"]
    Returns:
        string with fewest vowels
    """
    k="aeiouAEIOU"
    def hi(x):
        c=0
        for i in x:
            if i in k:
                c+=1
        return c
    return min(words, key=hi)
print(min_task_1_3(words=["book", "sky", "quiet", "data"]))
