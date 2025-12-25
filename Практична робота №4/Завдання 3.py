def list():
    try:
        line = input("Введіть елементи списку через пробіл: ")
        return line.split() 
    except Exception as e:
        print(f"Виникла помилка при введенні: {e}")
        return []

def print_list(lst, message="Список:"):
    print(f"{message} {lst}")

def remove_duplicates(lst):
    unique_list = []
    seen = set()
    
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
            
    return unique_list

def main():
    my_list = list()
    print_list(my_list, "Початковий список:")
    clean_list = remove_duplicates(my_list)
    print_list(clean_list, "Список без повторень:")

if __name__ == "__main__":
    main()