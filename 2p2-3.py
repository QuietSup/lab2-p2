from tabulate import tabulate


class Student:
    """Contains info about each student, including firs&last name, record book# grades and an average grade"""
    def __init__(self, first_name, last_name, record_book, *grades):
        """Checks if info about student was entered correctly

        Checks if all the data was entered; if first&last names have str type;
        if record book# has int type; if grades aren't empty have int type and vary
        in range 0<G<=5. Contains self.avrg_grade=None attribute, which is supposed
        to be changed after counting it in Group class

        :type first_name: str
        :type last_name: str
        :param record_book: record book numbers, which must differ from each other
        :type record_book: int
        :param grades: a tuple of all the grades
        :type grades: tuple(int)
        """
        if not (first_name and last_name and record_book and grades):
            raise ValueError("empty string")
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("first and last name must be str")
        if not isinstance(record_book, int):
            raise TypeError("record book number is not int")
        for gr in grades:
            if not gr:
                raise ValueError("empty grade")
            if not isinstance(gr, int):
                raise TypeError("all grades must be int")
            if gr <= 0 or gr > 5:
                raise ValueError("each grade must be in range 0<G<=5")

        self.avrg_grade = None
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book
        self.grades = grades

    @property
    def row(self):
        """Returns a row with info about student's first&last name, record book and average grade to build a table

        :returns: the "row" with info about record book#, first&last names, average grade
        :rtype: tuple(int, str, str, int)
        """
        return self.record_book, self.first_name, self.last_name, self.avrg_grade


class Group:
    """Contains info about all the students and methods to count average grades and return a table of top5 students"""
    def __init__(self, *students):
        """Checks if info about all the students and number of them was entered correctly

        Checks if data about all the students is entered correctly and this string
        isn't empty; if their number is in range 0<N<=20; if there's no duplicate
        first&last name together and no duplicate record book#

        :param students: a tuple of all the students
        :type students: tuple(class Student)
        """
        for i in students:
            if not i:
                raise ValueError("empty string")
            if not isinstance(i, Student):
                raise TypeError("student is entered incorrectly")

        if len(students) <= 0 or len(students) > 20:
            raise ValueError("Number of students is available in range: 0<N<=20")

        not_double_name = []
        not_double_book = []
        for smb in students:
            if (smb.first_name, smb.last_name) not in not_double_name:
                not_double_name.append((smb.first_name, smb.last_name))
            else:
                raise ValueError(f'{smb.first_name} {smb.last_name} repeats')

            if smb.record_book not in not_double_book:
                not_double_book.append(smb.record_book)
            else:
                raise ValueError(f'record book #{smb.record_book} repeats')

        self.students = students

    def all_avrg_grades(self):
        """Calculates an average grade for each student"""
        for smb in self.students:
            smb.avrg_grade = sum(smb.grades) / len(smb.grades)

    @property
    def best(self) -> str:
        """Returns a table of top5 students with the biggest average grade at its top"""
        sorted_student = sorted(self.students, key=lambda e: e.avrg_grade)
        mydata = []
        for i in sorted_student[:-5:-1]:
            mydata.append(i.row)
        head = ["Record book, #", "First name", "Last name", "Avrg grade"]
        return tabulate(mydata, headers=head, tablefmt="fancy_grid")


a = Student("Arissa", "Beltran", 1, 4, 3, 2, 4, 1)
b = Student("Kelan", "Sanford", 2, 3, 4, 1, 1, 5)
c = Student("Kiara", "Keller", 3, 2, 4, 3, 5, 3)
d = Student("Aniyah", "Harris", 4, 3, 2, 1, 2, 3)
e = Student("Darlene", "Cleveland", 5, 5, 5, 4, 5, 4)
f = Student("Sianna", "Macdonald", 6, 4, 1, 1, 4, 5)
g = Student("Elis", "Legge", 7, 3, 2, 1, 5, 2)
h = Student("Jay", "Gibbons", 8, 4, 4, 1, 3, 5)
i = Student("Khadija", "Medina", 9, 3, 5, 1, 5, 4)

a = Group(a, b, c, d, e, f, g, h, i)
a.all_avrg_grades()
print(a.best)
