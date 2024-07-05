# from teacher import Teacher
# from student import Student
# from file_handling import read_data, write_data
# from authentication import authenticate
# from exceptions import NoMatchingNameError, AuthenticationError

# def clear_and_write_data(filename: str, data_list):
#     write_data(filename, [data.__dict__ for data in data_list])

# def main():
#     teachers_file = 'teachers.json'
#     students_file = 'students.json'

#     teachers = [Teacher(**data) for data in read_data(teachers_file)]
#     students = [Student(**data) for data in read_data(students_file)]

#     while True:
#         print("1. Add Teacher\n2. Add Student\n3. Display All Teachers\n4. Display All Students\n5. Search Teacher\n6. Search Student\n7. Delete Teacher\n8. Delete Student\n9. Store Student Details\n10. Display Student Details\n11. Exit")
#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             try:
#                 if not teachers or authenticate(teachers):
#                     new_teacher = Teacher.accept()
#                     teachers.append(new_teacher)
#                     clear_and_write_data(teachers_file, teachers)
#             except AuthenticationError as e:
#                 print(e)

#         elif choice == 2:
#             new_student = Student.accept()
#             students.append(new_student)
#             clear_and_write_data(students_file, students)

#         elif choice == 3:
#             Teacher.display_all(teachers)

#         elif choice == 4:
#             Student.display_all(students)

#         elif choice == 5:
#             name = input("Enter teacher name to search: ")
#             try:
#                 teacher = Teacher.search(teachers, name)
#                 print(teacher.__dict__)
#             except NoMatchingNameError as e:
#                 print(e)

#         elif choice == 6:
#             name = input("Enter student name to search: ")
#             try:
#                 student = Student.search(students, name)
#                 print(student.__dict__)
#             except NoMatchingNameError as e:
#                 print(e)

#         elif choice == 7:
#             name = input("Enter teacher name to delete: ")
#             teachers = Teacher.delete(teachers, name)
#             clear_and_write_data(teachers_file, teachers)

#         elif choice == 8:
#             name = input("Enter student name to delete: ")
#             students = Student.delete(students, name)
#             clear_and_write_data(students_file, students)

#         elif choice == 9:
#             name = input("Enter student name to store details: ")
#             try:
#                 student = Student.search(students, name)
#                 student.calculate_percentage()
#                 clear_and_write_data(students_file, students)
#             except NoMatchingNameError as e:
#                 print(e)

#         elif choice == 10:
#             name = input("Enter student name to display details: ")
#             try:
#                 student = Student.search(students, name)
#                 student.display_details()
#             except NoMatchingNameError as e:
#                 print(e)

#         elif choice == 11:
#             break

# if __name__ == "__main__":
#     main()

from teacher import Teacher
from student import Student
from file_handling import read_data, write_data
from authentication import authenticate
from exceptions import NoMatchingNameError, AuthenticationError

def clear_and_write_data(filename: str, data_list):
    write_data(filename, [data.__dict__ for data in data_list])

def main():
    teachers_file = 'teachers.json'
    students_file = 'students.json'

    teachers = [Teacher(**data) for data in read_data(teachers_file)]
    students = [Student(**data) for data in read_data(students_file)]

    while True:
        print("1. Add Teacher\n2. Add Student\n3. Display All Teachers\n4. Display All Students\n5. Search Teacher\n6. Search Student\n7. Delete Teacher\n8. Delete Student\n9. Store Student Details\n10. Display Student Details\n11. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            try:
                if not teachers or authenticate(teachers):
                    new_teacher = Teacher.accept()
                    teachers.append(new_teacher)
                    clear_and_write_data(teachers_file, teachers)
            except AuthenticationError as e:
                print(e)

        elif choice == 2:
            new_student = Student.accept()
            students.append(new_student)
            clear_and_write_data(students_file, students)

        elif choice == 3:
            Teacher.display_all(teachers)

        elif choice == 4:
            Student.display_all(students)

        elif choice == 5:
            name = input("Enter teacher name to search: ")
            try:
                teacher = Teacher.search(teachers, name)
                print(teacher.__dict__)
            except NoMatchingNameError as e:
                print(e)

        elif choice == 6:
            name = input("Enter student name to search: ")
            try:
                student = Student.search(students, name)
                print(student.__dict__)
            except NoMatchingNameError as e:
                print(e)

        elif choice == 7:
            name = input("Enter teacher name to delete: ")
            teachers = Teacher.delete(teachers, name)
            clear_and_write_data(teachers_file, teachers)

        elif choice == 8:
            name = input("Enter student name to delete: ")
            students = Student.delete(students, name)
            clear_and_write_data(students_file, students)

        elif choice == 9:
            name = input("Enter student name to store details: ")
            try:
                student = Student.search(students, name)
                student.calculate_percentage()
                scores = [s.marks for s in students]  # Assuming you want to use the marks of all students
                student.calculate_highest_and_lowest_scores(scores)
                clear_and_write_data(students_file, students)
            except NoMatchingNameError as e:
                print(e)

        elif choice == 10:
            name = input("Enter student name to display details: ")
            try:
                student = Student.search(students, name)
                student.display_details()
            except NoMatchingNameError as e:
                print(e)

        elif choice == 11:
            break

if __name__ == "__main__":
    main()
