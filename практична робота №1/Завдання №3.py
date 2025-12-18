def draw_number_pattern():
    print("Числовий візерунок")
    try:
        user_input = input("Введіть ціле число: ")
        N = int(user_input)

        if 1 < N < 9:
            print(f"\nРезультат для цифри = {N}:")
            for i in range(1, N + 1):
                for j in range(N, i - 1, -1):
                    print(j, end=" ")
                
                print()
        else:
            print("Число має бути більше 1 та менше 9.")
            
    except ValueError:
        print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    draw_number_pattern()