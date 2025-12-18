import math
from student_module import student_budget

def calculate():
    print("Завдання 1")
    try:
        user_input = input("Введіть число α: ")
        alpha = float(user_input)
        
        cos_a = math.cos(alpha)
        z = cos_a**2 + cos_a**4
        
        print(f"Результат z: {z:.4f}")
    except ValueError:
        print("Введено некоректні дані.")

if __name__ == "__main__":
    calculate()
    student_budget()