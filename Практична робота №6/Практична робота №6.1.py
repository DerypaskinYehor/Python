import datetime

def add_student(database):
    print("\nДодавання нового студента (v2.0)")
    name = input("Введіть ПІБ: ")
    group = input("Номер групи: ")
    course = int(input("Курс: "))
    
    subjects = {}
    n = int(input("Скільки предметів додати? "))
    total_score = 0
    
    for _ in range(n):
        sub_name = input("Назва предмета: ")
        grade = int(input(f"Оцінка з {sub_name}: "))
        # Студент 2: Додано дату для кожного предмета
        date_str = datetime.date.today().strftime("%d.%m.%Y") 
        subjects[sub_name] = {
            "grade": grade,
            "date": date_str
        }
        total_score += grade
    
    avg_score = total_score / n if n > 0 else 0
    
    new_student = {
        "full_name": name,
        "group": group,
        "course": course,
        "subjects": subjects,
        "average_score": round(avg_score, 2),
        "is_active": True
    }
    
    database.append(new_student)
    print(f"Запис додано! Середній бал: {avg_score}")

def sort_students_by_grade(database):
    if not database:
        print("База даних порожня. Нічого сортувати.")
        return
    
    sorted_list = sorted(database, key=lambda x: x['average_score'], reverse=True)
    
    print("\nРейтинг студентів за успішністю")
    for i, s in enumerate(sorted_list, 1):
        print(f"{i}. {s['full_name']} | Сер. бал: {s['average_score']} | Група: {s['group']}")

def show_all(database):
    print("\nПовний список студентів:")
    for s in database:
        print(f"\nСтудент: {s['full_name']} (Курс {s['course']})")
        print(f"Група: {s['group']} | Середній бал: {s['average_score']}")
        print("Оцінки:")
        for sub, details in s['subjects'].items():
            print(f"  - {sub}: {details['grade']} (дата: {details['date']})")

if __name__ == "__main__":
    students_list = []
    while True:
        print("\nМеню:\n1. Додати студента\n2. Показати рейтинг (сортування)\n3. Вивести повний список\n4. Вийти")
        choice = input("Оберіть дію: ")
        if choice == "1":
            add_student(students_list)
        elif choice == "2":
            sort_students_by_grade(students_list)
        elif choice == "3":
            show_all(students_list)
        elif choice == "4":
            print("Програму завершено.")
            break