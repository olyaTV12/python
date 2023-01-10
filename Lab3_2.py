
from abc import ABC, abstractmethod


class Teacher(ABC):

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name}"


class Course(ABC):

    def __init__(self, name: str, course_program: list):
        self.name = name
        self.course_program = course_program

    def __str__(self):
        return f"{self.name}: {self.course_program}"


class CourseFactory:

    def __init__(self):
        self.factory = {}

    def point_teacher_to_course(self, teacher: Teacher, course: Course):
        if teacher in self.factory:
            self.factory[teacher].append(course.name)
        else:
            self.factory[teacher] = [course.name]

    def get_teacher_courses(self, teacher: Teacher):
        return f"{teacher.name}: {self.factory[teacher]}"


class LocalCourse(Course):
    pass


class OffsiteCourse(Course):
    pass
