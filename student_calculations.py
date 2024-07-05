# from typing import Dict, List

# def pass_fail_determination(marks: Dict[str, int]) -> bool:
#     return all(mark >= 40 for mark in marks.values())

# def highest_and_lowest_scores(marks: Dict[str, int]) -> (int, int):
#     return max(marks.values()), min(marks.values())

# def percentage(marks: Dict[str, int]) -> float:
#     total_marks = sum(marks.values())
#     return (total_marks / (len(marks) * 100)) * 100

# def rank_calculation(students: List[dict]) -> List[dict]:
#     return sorted(students, key=lambda student: sum(student['marks'].values()), reverse=True)
# from typing import Dict, List

# def pass_fail_determination(marks: Dict[str, int]) -> bool:
#     return all(mark >= 40 for mark in marks.values())

# def highest_and_lowest_scores(marks: Dict[str, int]) -> (int, int):
#     return max(marks.values()), min(marks.values())

# def percentage(marks: Dict[str, int]) -> float:
#     total_marks = sum(marks.values())
#     return (total_marks / (len(marks) * 100)) * 100

# def rank_calculation(students: List[dict]) -> List[dict]:
#     return sorted(students, key=lambda student: sum(student['marks'].values()), reverse=True)

# def calculate_student_details(student):
#     student.pass_fail = pass_fail_determination(student.marks)
#     student.highest_score, student.lowest_score = highest_and_lowest_scores(student.marks)
    # student.percentage = percentage(student.marks)

from typing import Dict, List

def pass_fail_determination(marks: Dict[str, int]) -> bool:
    return all(mark >= 40 for mark in marks.values())

def highest_and_lowest_scores(marks: Dict[str, int]) :
    return max(marks.values()), min(marks.values())

def percentage(marks: Dict[str, int]) -> float:
    total_marks = sum(marks.values())
    return (total_marks / (len(marks) * 100)) * 100

def rank_calculation(students: List[dict]) -> List[dict]:
    return sorted(students, key=lambda student: sum(student['marks'].values()), reverse=True)

def calculate_student_details(student):
    student.pass_fail = pass_fail_determination(student.marks)
    student.highest_score, student.lowest_score = highest_and_lowest_scores(student.marks)
    student.percentage = percentage(student.marks)
