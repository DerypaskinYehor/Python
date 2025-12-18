def calculate_x():
    print("Обчислення значення X")
    print("Введіть два числа a та b.")
    
    try:
        a = float(input("Введіть число a: "))
        b = float(input("Введіть число b: "))

        if a <= 0 or b <= 0:
            print("Числа a та b повинні бути більшими за нуль!")
            return

        if a < b:
            x = a / b + 1
        elif a == b:
            x = -1
        else:
            x = (a * b - 5) / a

        print(f"Результат X = {x:.2f}")

    except ValueError:
        print("Будь ласка, введіть коректні числові значення.")

if __name__ == "__main__":

    calculate_x()
