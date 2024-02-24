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
        for index, student in enumerate(self.students,1):
            print(f'{index}. {student}')

    def __str__(self):
        return self.name_course



# Pwede kayong mag-add ng student gamit yung functions na ginawa ko, pwede rin magremove
# Lahat ng mga naka blue as listed above pwede nyo gamitin as functions kunware
# homeroom.add_students(student1), homeroom.add_students(student2) tas maa-add sila
# Pag na-add na pwede nyo na gamitin tong homeroom.average_grade() na nakalagay sa baba--
# tas ipapakita kung ano yung grade.
# Try nyo daw i-explore kung interested kayo hehe
# Para maintindihan nyo to, Manood kayo ng OOP Python ni Tech With Tim at yung kay Bro Code,,
# mahalaga kasi to para sa kivy gawa ng madaming OOP don (Object-Oriented Programming)

#update ko try ko kumuha ng user input:
print("Hello to Classes practice!")
print(f"Here are some of the things you can do!")
courses = []
exit = False
while True:

    print(f"1. Create a course")
    print(f"2. Add a student")
    print(f"3. Remove a student")
    print(f"4. Show students in a course")
    print(f"5. Calculate the average grade of students in a course")
    print(f"6. Exit")
    try:
        choice = int(input("> "))
        if choice == 1:
            name = input("What would you like to be the name of your course? ")
            max_students = int(input("What would you like to be the maximum students in the course? "))
            course = Course(name, max_students)
            courses.append(course)
            print(f"You've created a course named: {name.title()} with a maximum of {max_students} students")
        elif choice == 2:
            if not courses:
                print("No courses have been created yet :(")
                continue
            elif courses:
                print("Select the course that you want to add students to: ")
                for index, course in enumerate(courses, 1):
                    print(f"{index}. {course.name_course}")
                course_index = int(input("Type the number of the course: ")) - 1
                course = courses[course_index]
                name_student = input("What would you like to be the name of your student? ").title()
                age = int(input("What is the age of your student? "))
                grade = int(input("What is the grade of your student? "))
                student = Students(name_student, age, grade)
                course.add_student(student)
                print(f"The student has been added to course {course} ")
        elif choice == 3:
            if not courses:
                print("No courses have been created yet :(")
                continue
            elif courses:
                print("Select the course from which you want to remove a student: ")
                for index, course in enumerate(courses, 1):
                    print(f"{index}. {course.name_course}")
                course_index = int(input("Type the number of the course: ")) - 1
                course = courses[course_index]

                if not course.students:
                    print("No students enrolled in this course :(")
                    continue

                course.show_students()
                student_index = int(input("Enter the number of the student you want to remove: ")) - 1

                if 0 <= student_index < len(course.students):
                    student = course.students[student_index]
                    course.remove_student(student)
                    print(f"{student.name} has been successfully removed from the course.")
                else:
                    print("Invalid student number. Please try again.")
        elif choice == 4:
            if not courses:
                print("No courses have been created yet :(")
                continue
            print("Select a course to show the number of students:")

            for index, course in enumerate(courses, 1):
                print(f"{index}. {course.name_course}")
            course_index = int(input("Enter the number of the course: ")) - 1
            course = courses[course_index]
            if not course.students:
                print("No students yet :(")
            course.show_students()
            proceed = input("Go back? (Yes or No) ").lower()
            if proceed == "yes":
                pass
            elif proceed == "no":
                break
            else:
                print("There are only 2 options!")
        elif choice == 5:
            if not courses:
                print("No courses have been created yet :(")
                continue
            print("Select a course to show the number of students:")
            for index, course in enumerate(courses, 1):
                print(f"{index}. {course.name_course}")
            course_index = int(input("Enter the number of the course: ")) - 1
            course = courses[course_index]
            if not course.students:
                print("No students yet :(")
            else:
                average_grade = course.average_grade()
                if average_grade is not None:
                    print(f"The average grade of {course.name_course} course is {average_grade}%")
                    proceed = input("Go back? (Yes or No) ").lower()
                    if proceed == "yes":
                        pass
                    elif proceed == "no":
                        break
                    else:
                        print("There are only 2 options!")
        elif choice == 6:
            while not exit:
                confirm = input("Are you sure? (Yes or No?): ").lower()
                if confirm == "yes":
                    quit()
                elif confirm == 'no':
                    exit = True
                else:
                    print("Yes or No only!")
    except ValueError:
        print("That's not a number!")




