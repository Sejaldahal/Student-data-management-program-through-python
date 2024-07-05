
import re
from typing import List, Dict
from exceptions import NoMatchingNameError
from student_calculations import calculate_student_details

class Student:
    def __init__(self, name: str, roll_number: str, email: str, phone_number: str, marks: Dict[str, int], address: str,**kwargs):
        self.name = name
        self.roll_number = roll_number
        self.email = email
        self.phone_number = phone_number
        self.marks = marks
        self.address = address
        self.percentage = None
        self.highest_score = None
        self.lowest_score = None
        self.pass_fail = None
        self.__dict__.update(kwargs)

    @staticmethod
    def validate_email(email: str) -> bool:
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    @staticmethod
    def validate_phone_number(phone_number: str) -> bool:
        return phone_number.isdigit() and len(phone_number) == 10

    @staticmethod
    def accept() -> 'Student':
        name = input("Enter name: ")
        roll_number = input("Enter roll number: ")
        email = input("Enter email: ")
        if not Student.validate_email(email):
            raise ValueError("Invalid email format")
        phone_number = input("Enter phone number: ")
        if not Student.validate_phone_number(phone_number):
            raise ValueError("Invalid phone number")
        marks = {}
        n_subjects = int(input("Enter number of subjects: "))
        for _ in range(n_subjects):
            subject = input("Enter subject name: ")
            mark = int(input("Enter mark: "))
            marks[subject] = mark
        address = input("Enter address: ")
        return Student(name, roll_number, email, phone_number, marks, address)

    @staticmethod
    def display_all(students):
        for student in students:
            print(f"Name: {student.name}, Email: {student.email}, Phone: {student.phone_number}, Roll Number: {student.roll_number}")

    @staticmethod
    def search(students, name: str):
        for student in students:
            if student.name == name:
                return student
        raise NoMatchingNameError(f"No student found with the name {name}")

    @staticmethod
    def delete(students, name: str):
        return [student for student in students if student.name != name]

    def display_details(self):
        calculate_student_details(self)
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Marks: {self.marks}")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"Highest Score: {self.highest_score}")
        print(f"Lowest Score: {self.lowest_score}")
        print(f"Pass/Fail: {'Pass' if self.pass_fail else 'Fail'}")

# # import json

# # class Student:
# #     def __init__(self, name, roll_number, email, phone_number, marks, address, percentage=None, **kwargs):
# #         self.name = name
# #         self.roll_number = roll_number
# #         self.email = email
# #         self.phone_number = phone_number
# #         self.marks = marks
# #         self.address = address
# #         self.percentage = percentage
# #         self.__dict__.update(kwargs)

# #     @classmethod
# #     def accept(cls):
# #         name = input("Enter student name: ")
# #         roll_number = int(input("Enter roll number: "))
# #         email = input("Enter email: ")
# #         phone_number = input("Enter phone number: ")
# #         marks = int(input("Enter marks: "))
# #         address = input("Enter address: ")
# #         return cls(name, roll_number, email, phone_number, marks, address)

# #     @staticmethod
# #     def display_all(students):
# #         for student in students:
# #             print(f"Name: {student.name}, Email: {student.email}, Phone: {student.phone_number}, Marks: {student.marks}")

# #     @staticmethod
# #     def search(students, name):
# #         for student in students:
# #             if student.name == name:
# #                 return student
# #         raise NoMatchingNameError(f"No student found with name {name}")

# #     @staticmethod
# #     def delete(students, name):
# #         for student in students:
# #             if student.name == name:
# #                 students.remove(student)
# #                 return students
# #         raise NoMatchingNameError(f"No student found with name {name}")

# #     def display_details(self):
# #         print(f"Name: {self.name}, Roll Number: {self.roll_number}, Email: {self.email}, Phone: {self.phone_number}, Marks: {self.marks}, Percentage: {self.percentage}, Address: {self.address}")

# #     def calculate_percentage(self):
# #         self.percentage = (self.marks / 100) * 100

# import json

# class Student:
#     def __init__(self, name, roll_number, email, phone_number, marks, address, percentage=None, highest_score=None, lowest_score=None, **kwargs):
#         self.name = name
#         self.roll_number = roll_number
#         self.email = email
#         self.phone_number = phone_number
#         self.marks = marks
#         self.address = address
#         self.percentage = percentage
#         self.highest_score = highest_score
#         self.lowest_score = lowest_score
#         self.__dict__.update(kwargs)

#     @classmethod
#     def accept(cls):
#         name = input("Enter student name: ")
#         roll_number = int(input("Enter roll number: "))
#         email = input("Enter email: ")
#         phone_number = input("Enter phone number: ")
#         marks = int(input("Enter marks: "))
#         address = input("Enter address: ")
#         return cls(name, roll_number, email, phone_number, marks, address)

#     @staticmethod
#     def display_all(students):
#         for student in students:
#             print(f"Name: {student.name}, Email: {student.email}, Phone: {student.phone_number}, Marks: {student.marks}")

#     @staticmethod
#     def search(students, name):
#         for student in students:
#             if student.name == name:
#                 return student
#         raise NoMatchingNameError(f"No student found with name {name}")

#     @staticmethod
#     def delete(students, name):
#         for student in students:
#             if student.name == name:
#                 students.remove(student)
#                 return students
#         raise NoMatchingNameError(f"No student found with name {name}")

#     def display_details(self):
#         print(f"Name: {self.name}, Roll Number: {self.roll_number}, Email: {self.email}, Phone: {self.phone_number}, Marks: {self.marks}, Percentage: {self.percentage}, Address: {self.address}")

#     def calculate_percentage(self):
#         self.percentage = (self.marks / 100) * 100

#     def calculate_highest_and_lowest_scores(self, scores):
#         self.highest_score = max(scores)
#         self.lowest_score = min(scores)
