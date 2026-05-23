def max_task_2_4(words):
    """
    Find the word with the most vowels.
    Args:
        words: list of strings ["tree", "education", "sky", "road"]
    Returns:
        word with most vowels
    """
    k="aeiouAEIOU"
    def hi(x):
        c=0
        for i in x:
            if i in k:
                c+=1
        return c
    return max(words,key=hi)
print(max_task_2_4(words=["tree", "education", "sky", "road"]))



