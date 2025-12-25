def main():
    try:
        n = int(input("Введіть кількість елементів масиву (N): "))
        
        if n <= 0:
            print("Кількість елементів має бути більше 0.")
            return

        print(f"Введіть {n} дійсних чисел:")
        arr = []
        for i in range(n):
            num = float(input(f"Елемент {i + 1}: "))
            arr.append(num)

        print("\nДодатні елементи у зворотному порядку:")
        
        found_positive = False
        
        for i in range(n - 1, -1, -1):
            if arr[i] > 0:
                print(arr[i], end=" ")
                found_positive = True
        
        if not found_positive:
            print("Додатних елементів не знайдено.")

    except ValueError:
        print("Будь ласка, вводьте коректні числа.")

if __name__ == "__main__":
    main()