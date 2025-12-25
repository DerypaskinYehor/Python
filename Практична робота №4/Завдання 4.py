def input_list():
    try:
        line = input("Введіть числа через пробіл: ")
        return list(map(float, line.split()))
    except ValueError:
        print("Введіть коректні числові дані.")
        return []

def print_list(lst, message="Список:"):
    print(f"{message} {lst}")

def get_five_minimums(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[:5]

def main():
    my_list = input_list()
    
    if not my_list:
        return

    print_list(my_list, "Введений масив:")
    min_elements = get_five_minimums(my_list)
    print_list(min_elements, "5 мінімальних елементів:")

if __name__ == "__main__":
    main()