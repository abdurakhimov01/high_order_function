def filter_task_4_1(numbers):
    """
    Filter out even numbers.
    Args:
        numbers: list of integers [1, 2, 3, 4, 5]
    Returns:
        list of odd numbers
    """
    a=[]
    for i in numbers:
        if i%2==1:
            a.append(i)
    return a
print(filter_task_4_1(numbers=[1,2,3,4,5]))
