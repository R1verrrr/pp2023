import numpy

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
        choice = int(input("Choose a course by index for student " + str(i+1) + ": "))
        new_element = {}
        new_element["Name of student: "] = students_list[i][0]
        new_element["Student ID: "] = students_list[i][1]
        new_element["DoB: "] = students_list[i][2]
        new_element["Course participating in: "]  = courses_list[choice][0]
        new_element["Course ID: "] = courses_list[choice][1]
        new_element["Mark: "] = ""
        system.append(new_element)

def enter_mark():

    while True:
        index = input("Choose a student by his/her index that you want to enter mark: ")
        if int(index) >= number_of_students or int(index) < 0:
            print("Invalid index!")

        else: 
            index = int(index)
            mark = input("Pls enter the mark: ")
            system[index]["Mark: "] = mark

def disply_all():
    for i in range(0, number_of_students):
        print("Name: " + str(system[i][0]))

student_iput()
print(students_list)
course_input()
print(courses_list)
add_to_system()
enter_mark()
disply_all()

