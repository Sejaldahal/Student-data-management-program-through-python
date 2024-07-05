import re
from exceptions import NoMatchingNameError
from student_calculations import calculate_student_details
from file_handling import write_data

class Teacher:
    def __init__(self, name: str, subject: str, id: str, address: str, email: str, phone_number: str):
        self.name = name
        self.subject = subject
        self.id = id
        self.address = address
        self.email = email
        self.phone_number = phone_number

    @staticmethod
    def validate_email(email: str) -> bool:
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    @staticmethod
    def validate_phone_number(phone_number: str) -> bool:
        return phone_number.isdigit() and len(phone_number) == 10

    @staticmethod
    def accept() -> 'Teacher':
        name = input("Enter name: ")
        subject = input("Enter subject: ")
        id = input("Enter ID: ")
        address = input("Enter address: ")
        email = input("Enter email: ")
        if not Teacher.validate_email(email):
            raise ValueError("Invalid email format")
        phone_number = input("Enter phone number: ")
        if not Teacher.validate_phone_number(phone_number):
            raise ValueError("Invalid phone number")
        return Teacher(name, subject, id, address, email, phone_number)

    @staticmethod
    def display_all(teachers):
        for teacher in teachers:
            print(f"Name: {teacher.name}, Email: {teacher.email}, Phone: {teacher.phone_number}, Subject: {teacher.subject}")

    @staticmethod
    def search(teachers, name: str):
        for teacher in teachers:
            if teacher.name == name:
                return teacher
        raise NoMatchingNameError(f"No teacher found with the name {name}")

    @staticmethod
    def delete(teachers, name: str):
        return [teacher for teacher in teachers if teacher.name != name]

    @staticmethod
    def store_student_details(student):
        calculate_student_details(student)
        write_data('students.json', student.__dict__)
        print(f"Stored details for student {student.name}")

# import json

# class Teacher:
#     def __init__(self, name, subject, id, address, email, phone_number):
#         self.name = name
#         self.subject = subject
#         self.id = id
#         self.address = address
#         self.email = email
#         self.phone_number = phone_number

#     @classmethod
#     def accept(cls):
#         name = input("Enter teacher name: ")
#         subject = input("Enter subject: ")
#         id = input("Enter id: ")
#         address = input("Enter address: ")
#         email = input("Enter email: ")
#         phone_number = input("Enter phone number: ")
#         return cls(name, subject, id, address, email, phone_number)

#     @staticmethod
#     def display_all(teachers):
#         for teacher in teachers:
#             print(f"Name: {teacher.name}, Email: {teacher.email}, Phone: {teacher.phone_number}, Subject: {teacher.subject}")

#     @staticmethod
#     def search(teachers, name):
#         for teacher in teachers:
#             if teacher.name == name:
#                 return teacher
#         raise NoMatchingNameError(f"No teacher found with name {name}")

#     @staticmethod
#     def delete(teachers, name):
#         for teacher in teachers:
#             if teacher.name == name:
#                 teachers.remove(teacher)
#                 return teachers
#         raise NoMatchingNameError(f"No teacher found with name {name}")
