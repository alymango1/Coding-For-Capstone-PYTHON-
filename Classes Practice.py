class Students():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
    def __str__(self):
        return self.name



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
            print("There are no student's enrolled here!")
            return None
        else:
            average = total_grade / num_students
            return average


    def show_students(self):
        print(f"Here are the list of students enrolled currently: {self.name_course} class")
        number = len(self.students)
        for index,student in enumerate(self.students,1):
            print(f'{index}. {student}: {student.get_grade()}')

student1 = Students("Jorge", 17, 97)
student2 = Students("Mark Jhun", 18, 95)
student3 = Students("Daniel", 18, 96)

homeroom = Course("Homeroom", 2)

# Pwede kayong mag-add ng student gamit yung functions na ginawa ko, pwede rin magremove
# Lahat ng mga naka blue as listed above pwede nyo gamitin as functions kunware
# homeroom.add_students(student1), homeroom.add_students(student2) tas maa-add sila
# Pag na-add na pwede nyo na gamitin tong homeroom.average_grade() na nakalagay sa baba--
# tas ipapakita kung ano yung grade.
# Try nyo daw i-explore kung interested kayo hehe
# Para maintindihan nyo to, Manood kayo ng OOP Python ni Tech With Tim at yung kay Bro Code,,
# mahalaga kasi to para sa kivy gawa ng madaming OOP don (Object-Oriented Programming)

homeroom.add_student(student1)
homeroom.add_student(student2)

homeroom.show_students()
average_grade = homeroom.average_grade()
if average_grade is not None:
    print(f"Average Grade is {average_grade}%")

