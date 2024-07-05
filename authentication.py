# from exceptions import AuthenticationError

# def authenticate(teachers):
#     name = input("Enter your name: ")
#     id = input("Enter your Id number: ")
#     for teacher in teachers:
#         if teacher.name == name and teacher.id == id:
#             return True
#     raise AuthenticationError("Invalid credentials")
from exceptions import AuthenticationError

def authenticate(teachers):
    name = input("Enter your name: ")
    id = input("Enter your Id number: ")
    for teacher in teachers:
        if teacher.name == name and teacher.id == id:
            return True
    raise AuthenticationError("Invalid credentials")
