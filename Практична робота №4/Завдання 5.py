def print_set(s, message="Множина:"):
    print(f"{message} {sorted(s)}")

def modify_set_via_list(source_set, x):
    temp_list = list(source_set)
    
    if x in temp_list:
        print(f"Елемент '{x}' знайдено. Видаляємо...")
        temp_list.remove(x)
    else:
        print(f"Елемент '{x}' відсутній. Додаємо...")
        temp_list.append(x)
        
    result_set = set(temp_list)
    return result_set

def main():

    input_str = input("Введіть елементи множини А (без пробілів): ")
    set_A = set(input_str)
    print_set(set_A, "Початкова множина А:")
    x = input("Введіть символ x: ")
    
    if len(x) != 1:
        print("Потрібно ввести рівно один символ.")
        return

    set_B = modify_set_via_list(set_A, x)
    
    print_set(set_B, "Результат множини В:")

if __name__ == "__main__":
    main()