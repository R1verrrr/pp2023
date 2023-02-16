from random import randint

print("Hello !")

#input function
system = []

students_list = []
courses_list = []

number_of_students = int(input("Please enter the number of the students in the class: "))
def student_iput():
    
    for i in range(0, number_of_students):
        print("Student " + str(i+1) + ": ")
        student = [input("Please enter name: "), input("Please enter ID: "), input("Please enter dob:")]
        students_list.append(student)
    
def course_input():

    number_of_courses = int(input("Please enter the number of courses: "))
    
    for i in range(0, number_of_courses):
        print("Course " + str(i+1) + ": ")
        course = (input("Please enter the name of course: "), input("Please enter course ID: "))
        courses_list.append(course)


def add_to_system():

    for i in range(0, number_of_students):
        choice = int(input("Choose a course by index for student " + str(i+1)) + ": ")
        new_element = {}
        new_element["Name of student: "] = students_list[i][0]
        new_element["Student ID: "] = students_list[i][1]
        new_element["DoB: "] = students_list[i][2]
        new_element["Course participating in: "]  = courses_list[choice][0]
        new_element["Course ID: "] = courses_list[choice][1]
        #element["Mark: "] = input("Please enter the mark: ")
        system.append(new_element)



if "__name__" == "main":
    student_iput()
    print(students_list)
    course_input()
    print(courses_list)
    add_to_system()
    print(system)

