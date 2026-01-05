def add_student(database):
    print("\nДодавання нового студента")
    name = input("Введіть ПІБ: ")
    group = input("Номер групи: ")
    course = int(input("Курс: "))
    email = input("Email: ")
    
    subjects = {}
    n = int(input("Скільки предметів додати? "))
    for _ in range(n):
        sub_name = input("Назва предмета: ")
        grade = int(input(f"Оцінка з {sub_name}: "))
        subjects[sub_name] = grade
    
    new_student = {
        "full_name": name,
        "group": group,
        "course": course,
        "subjects": subjects,
        "email": email,
        "is_active": True
    }
    
    database.append(new_student)
    print("Запис додано успішно!")

def show_all(database):
    print("\nСписок студентів:")
    for s in database:
        print(f"[{s['group']}] {s['full_name']} - Курс: {s['course']}")

# Початкова база даних
students_list = []

if __name__ == "__main__":
    while True:
        choice = input("\n1. Додати студента\n2. Показати всіх\n3. Вийти\nДія: ")
        if choice == "1":
            add_student(students_list)
        elif choice == "2":
            show_all(students_list)
        elif choice == "3":
            break