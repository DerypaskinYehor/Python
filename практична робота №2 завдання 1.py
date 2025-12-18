import math
import sys

sys.stdout.reconfigure(encoding='utf-8')

def trigonometry():
    print("Завдання 1")
    try:
        user_input = input("Введіть число α: ")
        alpha = float(user_input)
        
        cos_a = math.cos(alpha)
        z = cos_a**2 + cos_a**4
        
        print(f"Результат z: {z:.4f}")
    except ValueError:
        print("Введено некоректні дані.")

def student_budget():
    print("\nЗавдання 2")
    try:
        user_input_a = input("Введіть розмір стипендії: ")
        a = float(user_input_a)
        
        user_input_b = input("Введіть витрати за перший місяць: ")
        b = float(user_input_b)

        if a < 0 or b < 0:
            print("Стипендія та витрати не можуть бути від'ємними!")
            return

        months = 10
        total_needed = 0
        current_expenses = b
        
        for _ in range(months):
            shortfall = current_expenses - a
            
            if shortfall > 0:
                total_needed += shortfall
            
            current_expenses *= 1.05
            
        if total_needed > 0:
            print(f"Загальна сума, яку треба попросити в батьків: {total_needed:.2f} грн.")
        else:
            print("Стипендії вистачає на проживання.")
        
    except ValueError:
        print("Введіть коректні числові дані.")

if __name__ == "__main__":
    trigonometry()
    student_budget()