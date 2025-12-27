import json
import os

FILENAME = "students.json"
RESULT_FILENAME = "found_students.json"

INITIAL_DATA = [
    {"prizvyshche": "Коваленко", "imya": "Олександр", "po_batkovi": "Петрович", "data_narodzhennya": {"rik": 2008, "misyats": 5, "den": 10}, "stat": "ч"},
    {"prizvyshche": "Шевченко", "imya": "Марія", "po_batkovi": "Іванівна", "data_narodzhennya": {"rik": 2008, "misyats": 5, "den": 22}, "stat": "ж"},
    {"prizvyshche": "Бондаренко", "imya": "Максим", "po_batkovi": "Олегович", "data_narodzhennya": {"rik": 2007, "misyats": 12, "den": 1}, "stat": "ч"},
    {"prizvyshche": "Ткаченко", "imya": "Анна", "po_batkovi": "Сергіївна", "data_narodzhennya": {"rik": 2008, "misyats": 1, "den": 15}, "stat": "ж"},
    {"prizvyshche": "Кравченко", "imya": "Дмитро", "po_batkovi": "Андрійович", "data_narodzhennya": {"rik": 2007, "misyats": 5, "den": 5}, "stat": "ч"},
    {"prizvyshche": "Олійник", "imya": "Софія", "po_batkovi": "Василівна", "data_narodzhennya": {"rik": 2008, "misyats": 9, "den": 1}, "stat": "ж"},
    {"prizvyshche": "Лисенко", "imya": "Артем", "po_batkovi": "Миколайович", "data_narodzhennya": {"rik": 2007, "misyats": 3, "den": 30}, "stat": "ч"},
    {"prizvyshche": "Мельник", "imya": "Вікторія", "po_batkovi": "Юріївна", "data_narodzhennya": {"rik": 2008, "misyats": 5, "den": 18}, "stat": "ж"},
    {"prizvyshche": "Бойко", "imya": "Андрій", "po_batkovi": "Володимирович", "data_narodzhennya": {"rik": 2007, "misyats": 11, "den": 11}, "stat": "ч"},
    {"prizvyshche": "Гаврилюк", "imya": "Олена", "po_batkovi": "Олександрівна", "data_narodzhennya": {"rik": 2008, "misyats": 7, "den": 20}, "stat": "ж"}
]

def load_data():
    if not os.path.exists(FILENAME):
        save_data(INITIAL_DATA)
        return INITIAL_DATA
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_data(data, filename=FILENAME):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Помилка при збереженні файлу: {e}")

def display_students(students=None):
    if students is None:
        students = load_data()
    
    if not students:
        print("\nСписок учнів порожній.")
        return

    print(f"\n{'№':<3} {'Прізвище':<15} {'Ім`я':<12} {'Дата народж.':<12} {'Стать'}")
    print("-" * 55)
    for i, s in enumerate(students, 1):
        date_str = f"{s['data_narodzhennya']['den']:02}.{s['data_narodzhennya']['misyats']:02}.{s['data_narodzhennya']['rik']}"
        print(f"{i:<3} {s['prizvyshche']:<15} {s['imya']:<12} {date_str:<12} {s['stat']}")
    print("-" * 55)

def add_student():
    students = load_data()
    print("\nДодавання нового учня")
    prizvyshche = input("Прізвище: ")
    imya = input("Ім'я: ")
    po_batkovi = input("По батькові: ")
    
    try:
        rik = int(input("Рік народження (YYYY): "))
        misyats = int(input("Місяць народження (1-12): "))
        den = int(input("День народження (1-31): "))
    except ValueError:
        print("Дата має бути числом!")
        return

    stat = input("Стать (ч/ж): ")

    new_student = {
        "prizvyshche": prizvyshche,
        "imya": imya,
        "po_batkovi": po_batkovi,
        "data_narodzhennya": {
            "rik": rik,
            "misyats": misyats,
            "den": den
        },
        "stat": stat
    }
    
    students.append(new_student)
    save_data(students)
    print("Учня успішно додано!")

def delete_student():
    students = load_data()
    display_students(students)
    target = input("\nВведіть прізвище учня для видалення: ").strip()
    
    new_list = [s for s in students if s['prizvyshche'].lower() != target.lower()]
    
    if len(new_list) < len(students):
        save_data(new_list)
        print(f"Учня з прізвищем '{target}' видалено.")
    else:
        print("Учня з таким прізвищем не знайдено.")

def search_student():
    students = load_data()
    target = input("\nВведіть прізвище для пошуку: ").lower()
    
    found = [s for s in students if target in s['prizvyshche'].lower()]
    
    if found:
        print(f"Знайдено записів: {len(found)}")
        display_students(found)
    else:
        print("Нікого не знайдено.")

def find_by_birth_month():
    students = load_data()
    
    try:
        target_month = int(input("\nВведіть номер місяця (1-12) для пошуку іменинників: "))
    except ValueError:
        print("Будь ласка, введіть число.")
        return

    found_students = []
    
    print(f"\nУчні, що народилися у {target_month}-му місяці")
    for s in students:
        if s['data_narodzhennya']['misyats'] == target_month:
            found_students.append(s)
            print(f"{s['imya']} {s['prizvyshche']}")
            
    if found_students:
        save_data(found_students, RESULT_FILENAME)
        print(f"\nЗнайдено {len(found_students)} учнів.")
        print(f"Результат збережено у файл '{RESULT_FILENAME}'")
    else:
        print("У цьому місяці іменинників немає.")

def main():
    while True:
        print("\nГоловне Меню")
        print("1. Вивести вміст JSON файлу")
        print("2. Додати учня")
        print("3. Видалити учня")
        print("4. Пошук за прізвищем")
        print("5. Знайти учнів за місяцем народження")
        print("0. Вихід")
        
        choice = input("Ваш вибір: ")
        
        if choice == '1':
            display_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            find_by_birth_month()
        elif choice == '0':
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()