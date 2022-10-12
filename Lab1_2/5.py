MAX_STUDENTS = 20

class Student:
    def __init__(self, name, surname, record_book, *grades):
        if not all(isinstance(i, str) for i in [name, surname]):
            raise TypeError('Only type str allowed for names and record book.')
        if not isinstance(record_book, int):
            raise TypeError('Only type int allowed for record book number.')
        if not all(isinstance(i, int | float) for i in grades):
            raise TypeError('Only types int and float allowed for grades.')

        self.__name = name
        self.__surname = surname
        self.__record_book = record_book
        self.__grades = grades

    def __str__(self):
        return f'\nStudent  : {self.__name} {self.__surname}\
                 \nRecord № : {self.__record_book}\
                 \nScores   : {", ".join([str(i) for i in self.__grades])}\
                 \nAverage  : {self.average}\
                 \n-----------'

    # Helper functions for sorted().
    def __lt__(self, other) -> bool:
        return self.average < other.average

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def average(self):
        return sum(list(self.__grades)) / len(self.__grades)


class Group:
    def __init__(self, *students):
        self.__students = []
        for s in students:
            self.add(s)

    def add(self, student):
        if len(self.__students) == MAX_STUDENTS:
            raise AssertionError('Max size of group is 20 students.')
        if not isinstance(student, Student):
            raise TypeError('Only type Student allowed for students.')
        if (student.name + student.surname) in [i.name + i.surname for i in self.__students]:
            raise ValueError('Student is already in the group.')

        self.__students.append(student)

    def best_five(self):
        if len(self.__students) <= 5:
            return self.__students
        return sorted(self.__students, reverse=True)[:5]



stud1 = Student('olya',    'jojo',      101, 4, 5, 3, 3, 5)
stud2 = Student('picko',   'mirkovich', 102, 2, 3, 3, 2, 4)
stud3 = Student('oleh',    'voda',      103, 1, 2, 5, 3, 2)
stud4 = Student('michael', 'gigo',      104, 3, 4, 5, 4, 4)
stud5 = Student('picko',   'lutii',     105, 4, 2, 3, 5, 4)
stud6 = Student('vicka',   'pes',       106, 1, 5, 3, 3, 4)

group1 = Group(stud1, stud2, stud3, stud4, stud5, stud6)

print('\n\tTop 5 students:', "".join(str(i) for i in group1.best_five()))