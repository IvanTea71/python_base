students = [{"name": "ivan", "grades": [80, 90, 78]},
            {"name": "mihail", "grades": [95, 90, 97]},
            {"name": "dmiry", "grades": [60, 70, 64]},
            {"name": "vladislav", "grades": [60, 75, 70]}]


def calculate_average_grade(grades):
    return sum(grades) / len(grades)


def calculate_academic_performance(average_grades):
    if average_grades >= 75:
        return "Успешен"
    else:
        return "Отстающий"


def calculate_general_grade(students):
    total = 0

    for student in students:
        total += calculate_average_grade(student["grades"])

    print(f"Средний балл всех студетов: {total / len(students)}")


def print_info(students):
    for student in students:
        print(f"Студент: {student["name"]}"
              f"\nСредний балл: {calculate_average_grade(student["grades"])}"
              f"\nСтатус: {calculate_academic_performance(calculate_average_grade(student["grades"]))}\n")


def remove_worse_student(students):
    weakest_student = students[0]

    for student in students:
        if calculate_average_grade(student["grades"]) < calculate_average_grade(weakest_student["grades"]):
            weakest_student = student

    students.remove(weakest_student)
    calculate_general_grade(students)


def add_student(students):
    students.append({"name": "anatoly", "grades": [100, 90, 98]})
    calculate_general_grade(students)


print_info(students)
calculate_general_grade(students)
add_student(students)
remove_worse_student(students)