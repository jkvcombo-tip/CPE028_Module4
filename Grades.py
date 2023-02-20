class Grades:
    def __init__(self,course_code, course_units, course_grade):
        self.course_code = course_code
        self.course_units = course_units
        self.course_grade = course_grade

    def __str__(self):
        return f"{self.course_code}({self.course_units})({self.course_grade})"
        