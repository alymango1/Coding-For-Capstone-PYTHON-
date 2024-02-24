class Students():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade  # Simply return the grade attribute


class Course():
    def __init__(self, name, max_students):
        self.name_course = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
            print("The following course has reached its maximum capacity")

    def remove_student(self, student):
        try:
            self.students.remove(student)
        except Exception:
            print("The student is not enrolled here!")

    def average_grade(self):
        total_grade = sum(student.get_grade() for student in self.students)
        num_students = len(self.students)
        if num_students == 0:
            print("There are no students enrolled here!")
            return None  # Return None if no students are enrolled
        else:
            average = total_grade / num_students
            return average

    def show_students(self):
        print(f"Here are the list of students enrolled currently: {self.name_course} class")
        for index, student in enumerate(self.students, 1):
            print(f'{index}. {student.name}: {student.get_grade()}')  # Print student name and grade


student1 = Students("Jorge", 17, 97)
student2 = Students("Mark Jhun", 18, 95)
student3 = Students("Daniel", 18, 96)

homeroom = Course("Homeroom", 2)

homeroom.add_student(student1)
homeroom.add_student(student2)

homeroom.show_students()  # Print list of students with their grades
average_grade = homeroom.average_grade()
if average_grade is not None:
    print("Average grade:", average_grade)
