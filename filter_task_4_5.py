def filter_task_4_5(students):
    """
    Filter students who passed (grade >= 60).
    Args:
        students: list of dictionaries [{"name": "Alice", "grade": 85}, {"name": "Bob", "grade": 55}, {"name": "Charlie", "grade": 70}]
    Returns:
        list of students who passed
    """
    return students["grade"]>=60
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 55},
    {"name": "Charlie", "grade": 70}
    ] 
print(list(filter(filter_task_4_5,students)))