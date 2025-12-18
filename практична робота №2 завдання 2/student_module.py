def student_budget():
    print("\nЗавдання 2 (з окремого модуля)")
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