import json
import pickle


class Student:
    available_courses = ["Math", "Literature", "English"]
    student_json = "student.json"
    student_pickle = "student.pickle"

    def __init__(self, name, age, grade):
        self.__name = name
        self.__age = age
        self.__grade = grade
        self.__courses = []

    def __str__(self):
        return (f"name: {self.__name},"
                f"age: {self.__age},"
                f"grade: {self.__grade},"
                f"courses: {self.__courses}")

    def get_courses(self):
        return self.__courses

    def add_course(self, course):
        try:
            if course in Student.available_courses:
                self.__courses.append(course)
            else:
                raise ValueError(f"You should the course from the list {Student.available_courses}")
        except ValueError as e:
            print("Message: ", e)

    @classmethod
    def export_to_json(cls, students):
        data = []
        for student in students:
            record = {"name": student.__name, "age": student.__age, "grade": student.__grade,
                      "courses": student.__courses}
            data.append(record)
        with open(cls.student_json, 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def import_from_json(cls):
        with open(cls.student_json, 'r') as file:
            students = json.load(file)
        print(students)
        return students

    @classmethod
    def export_to_pickle(cls, students):
        with open(cls.student_pickle, "wb") as file:
            pickle.dump(students, file)

    @classmethod
    def import_from_pickle(cls):
        with open(cls.student_pickle, "rb") as file:
            students = pickle.load(file)
        for student in students:
            print(student)
        return students


student1 = Student("Alice", 15, "A")
student1.add_course("Math")

student2 = Student("Bob", 25, "A")
student2.add_course("English")

student3 = Student("Marie", 35, "A")
student3.add_course("English")

students = [student1, student3, student2]
Student.export_to_json(students)
Student.import_from_json()

Student.export_to_pickle(students)
Student.import_from_pickle()
