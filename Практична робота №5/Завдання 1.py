import datetime

students_db = {
    101: {
        "surname": "Коваленко", "name": "Олександр", "patronymic": "Іванович",
        "dob": (2008, 5, 12)
    },
    102: {
        "surname": "Мельник", "name": "Ірина", "patronymic": "Петрівна",
        "dob": (2008, 8, 24)
    },
    103: {
        "surname": "Ткаченко", "name": "Андрій", "patronymic": "Васильович",
        "dob": (2009, 2, 15)
    },
    104: {
        "surname": "Бойко", "name": "Оксана", "patronymic": "Сергіївна",
        "dob": (2009, 11, 30)
    },
    105: {
        "surname": "Бондар", "name": "Сергій", "patronymic": "Олександрович",
        "dob": (2008, 1, 10)
    },
    106: {
        "surname": "Кравченко", "name": "Вікторія", "patronymic": "Юріївна",
        "dob": (2009, 7, 8)
    },
    107: {
        "surname": "Олійник", "name": "Максим", "patronymic": "Володимирович",
        "dob": (2008, 9, 19)
    },
    108: {
        "surname": "Шевчук", "name": "Тетяна", "patronymic": "Ігорівна",
        "dob": (2008, 3, 22)
    },
    109: {
        "surname": "Поліщук", "name": "Дмитро", "patronymic": "Миколайович",
        "dob": (2009, 12, 5)
    },
    110: {
        "surname": "Лисенко", "name": "Олена", "patronymic": "Михайлівна",
        "dob": (2008, 6, 14)
    }
}

def print_all(db):
    if not db:
        print("Словник порожній.")
        return
    
    col_name = "Ім'я"
    
    print(f"{'ID':<5} {'Прізвище':<15} {col_name:<12} {'По батькові':<18} {'Дата народження':<15}")
    
    print("-" * 70)
    for user_id, info in db.items():
        dob_str = f"{info['dob'][2]:02d}.{info['dob'][1]:02d}.{info['dob'][0]}"
        print(f"{user_id:<5} {info['surname']:<15} {info['name']:<12} {info['patronymic']:<18} {dob_str:<15}")
    print("-" * 70)

def add_record(db):
    try:
        new_id = int(input("Введіть унікальний ID учня: "))
        if new_id in db:
            print(f"Учень з ID {new_id} вже існує.")
            return

        surname = input("Прізвище: ")
        name = input("Ім'я: ")
        patronymic = input("По батькові: ")
        
        print("Введіть дату народження:")
        year = int(input("  Рік (наприклад, 2008): "))
        month = int(input("  Місяць (1-12): "))
        day = int(input("  Число (1-31): "))

        datetime.date(year, month, day) 

        db[new_id] = {
            "surname": surname,
            "name": name,
            "patronymic": patronymic,
            "dob": (year, month, day)
        }
        print("Запис успішно додано!")

    except ValueError:
        print("Введено некоректні дані (очікувалися числа для дати/ID або неправильна дата).")
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")

def delete_record(db):
    try:
        target_id = int(input("Введіть ID учня для видалення: "))
        del db[target_id]
        print(f"Запис з ID {target_id} видалено.")
    except KeyError:
        print(f"Запису з ID {target_id} не існує.")
    except ValueError:
        print("ID має бути числом.")

def print_sorted_by_keys(db):
    print("\nСписок учнів (відсортовано за ID)")
    sorted_keys = sorted(db.keys())
    
    if not sorted_keys:
        print("Словник порожній.")
        return

    for key in sorted_keys:
        info = db[key]
        dob_str = f"{info['dob'][2]:02d}.{info['dob'][1]:02d}.{info['dob'][0]}"
        print(f"ID: {key}, {info['surname']} {info['name']}, ДН: {dob_str}")

def check_birthdays(db):
    today = datetime.date.today()
    print(f"\nСьогоднішня дата: {today.day:02d}.{today.month:02d}.{today.year}")
    
    found = False
    print("Іменинники сьогодні:")
    
    for info in db.values():
        birth_year, birth_month, birth_day = info['dob']
        
        if birth_month == today.month and birth_day == today.day:
            print(f" -> {info['name']} {info['surname']} ({birth_year} р.н.)")
            found = True
            
    if not found:
        print("На жаль, сьогодні ні в кого немає дня народження.")

def main():
    while True:
        print("\nМеню Керування Класом")
        print("1. Показати всіх учнів")
        print("2. Показати учнів (сортування за ID)")
        print("3. Додати учня")
        print("4. Видалити учня")
        print("5. Перевірити іменинників")
        print("0. Вихід")
        
        choice = input("Ваш вибір: ")
        
        if choice == "1":
            print_all(students_db)
        elif choice == "2":
            print_sorted_by_keys(students_db)
        elif choice == "3":
            add_record(students_db)
        elif choice == "4":
            delete_record(students_db)
        elif choice == "5":
            check_birthdays(students_db)
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()