#1
def listCourses():
  with open("course.txt", "r") as courses:
    content = courses.readlines()
    for i in range(len(content)):
      print(content[i].split(";")[1])
#2
def registeredStudent():
  with open("course.txt", "r") as courses:
    content = courses.readlines()
    for i in range(len(content)):
      f = (content[i].split(";")[3])
      if int(f) > 0:
        print(content[i].split(";")[1])
#3
def addingCourse():
  with open("course.txt", "a") as courses:
    courseCode = input("Please write the course code: ")
    courseName = input("Please write the course name: ")
    instructorName = input("Please write the instructor name: ")
    studentCount = input(
      "Please write the number of students of the course contains: ")
    a = courseCode + ";" + courseName + ";" + instructorName + ";" + studentCount + "\n"
    courses.write(a)
  print("Courses added successfully")
#4
def courseCode():
  with open("course.txt", "r") as courses:
    a = input("Please write the course code: ")
    content = courses.readlines()
    list = []
    for i in range(len(content)):
      list.append(content[i].split(";")[0])
    if a in list:
      print("This course exists")
    else:
      print("This course does not exist")
#5
def courseName():
  with open("course.txt", "r") as courses:
    name = input("Please write the course name: ")
    content = courses.readlines()
    list = []
    for i in content:
      if i not in list:
        a = i.split(";")
        list.append(a)
    for k in list:
      for l in k:
        if name in l:
         print(k[1])
#6
def studentRegister():
  with open("student.txt", "a") as students:
    name = input("Please write the student name: ")
    id = input("Please write the student id that contains 6 digits: ")
    courseCode = input("Please write the course code: ")
    students.write("\n" + id + ";" + name + ";" + courseCode)
    print("Student added successfully")

#7
def studentCourses():
  with open ("student.txt","r") as students:
    content = students.readlines()
    for i in content:
      i =i.replace("\n","")
      i = i.split(";")
      print(i[1])
      print(i[2:])
      print("\n")
#8    
def crowdedCourses():
  with open("course.txt", "r") as courses:
    content = courses.readlines()
    list = []
    for i in content:
      i =i.strip()
      m = i.split(";")
      list.append(int(m[3]))
    list.sort(reverse=True)
    list = list[:3]
    for i in content:
      i = i.strip()
      m = i.split(";")
      if int(m[3]) in list:
        print(m[1])
# #9
def mostCourseRegistrations():
  with open ("student.txt","r") as students:
    content = students.readlines()
    courses = {}
    studentsList = []

    for i in content:
      i=i.strip()
      m=i.split(";")[2]
      name = i.split(";")[1]
      courses[name]=(len(m.split(",")))
    for l in range(3):
      maxWord = max(courses, key= courses.get)
      if maxWord not in studentsList:
        studentsList.append(maxWord)
        courses.pop(maxWord)
    print(studentsList)
    

def mainMenu():

  menu = """  1-List all the courses
  2-List all the course that have at least one student registered.
  3-Add a new course.
  4-Search a course by course code.
  5-Search a course by name.
  6-Register a student to a course.
  7-List all the students their registered courses.
  8-List top 3 most crowded courses.
  9-List top 3 students with the most course registrations.
  10-Exit"""
  print(menu)
while True:
  mainMenu()
  choice = input("Choice:")
  if choice == "1":
    listCourses()
    pass
  elif choice == "2":
    registeredStudent()
  elif choice == "3":
    addingCourse()
  elif choice == "4":
    courseCode()
  elif choice == "5":
    courseName()
  elif choice == "6":
    studentRegister()
  elif choice == "7":
    studentCourses()
  elif choice == "8":
    crowdedCourses()
  elif choice == "9":
    mostCourseRegistrations()
  elif choice == "10":
    print("You have logged out of the menu.")
  else:
    print("Please try again.")
  
