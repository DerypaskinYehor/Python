import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import os

def model_linear(x, a, b):
    return a * x + b

def model_quadratic(x, a, b, c):
    return a * x**2 + b * x + c

def model_exponential(x, a, b, c):
    return a * np.exp(b * x) + c

def generate_data(n_points=50, noise_level=0.5):
    try:
        x = np.linspace(-10, 10, n_points)
        y_exact = 0.5 * x**2 + 2 * x + 5
        noise = np.random.normal(0, noise_level, size=len(x))
        y_data = y_exact + noise
        return x, y_data
    except Exception as e:
        print(f"[Помилка генерації даних]: {e}")
        return None, None

def save_results(x, y_true, y_pred, params, mse, filename="results"):
    try:
        df = pd.DataFrame({
            'X': x,
            'Y_Experiment': y_true,
            'Y_Approximation': y_pred,
            'Error': y_true - y_pred
        })
        csv_name = f"{filename}.csv"
        df.to_csv(csv_name, index=False)
        print(f"-> Дані збережено у файл: {csv_name}")

        txt_name = f"{filename}_report.txt"
        with open(txt_name, "w", encoding="utf-8") as f:
            f.write("Звіт про апроксимацію\n")
            f.write(f"Знайдені параметри: {params}\n")
            f.write(f"Середньоквадратична помилка (MSE): {mse:.5f}\n")
        print(f"-> Звіт збережено у файл: {txt_name}")
        
    except IOError as e:
        print(f"[Помилка запису файлу]: {e}")


def process_approximation():
    print("\nЕтап 1: Підготовка даних")
    try:
        n_str = input("Введіть кількість точок (за замовчуванням 50): ")
        n = int(n_str) if n_str else 50
        if n <= 0: raise ValueError("Кількість точок має бути > 0")
        
        noise_str = input("Введіть рівень шуму (за замовчуванням 2.0): ")
        noise = float(noise_str) if noise_str else 2.0
    except ValueError as e:
        print(f"[Помилка вводу]: {e}. Використовуються стандартні значення.")
        n, noise = 50, 2.0

    x_data, y_data = generate_data(n, noise)
    if x_data is None: return

    print("\nЕтап 2: Вибір моделі та розрахунок (SciPy)")
    print("1. Лінійна (ax + b)")
    print("2. Квадратична (ax^2 + bx + c)")
    print("3. Експоненційна (a * exp(bx) + c)")
    
    choice = input("Ваш вибір (1-3): ")
    
    model_func = None
    if choice == '1': model_func = model_linear
    elif choice == '2': model_func = model_quadratic
    elif choice == '3': model_func = model_exponential
    else:
        print("Невірний вибір. Використовується квадратична модель.")
        model_func = model_quadratic

    try:
        popt, pcov = curve_fit(model_func, x_data, y_data)
        y_fit = model_func(x_data, *popt)
        mse = np.mean((y_data - y_fit)**2)
        
        print(f"\nРезультат успішний!")
        print(f"Знайдені коефіцієнти: {popt}")
        print(f"MSE: {mse:.4f}")

    except RuntimeError:
        print("[Помилка SciPy]: Не вдалося знайти оптимальні параметри.")
        return
    except Exception as e:
        print(f"[Критична помилка]: {e}")
        return

    print("\nЕтап 3: Візуалізація та збереження")
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(x_data, y_data, label='Експериментальні дані', color='red', s=10)
        plt.plot(x_data, y_fit, label='Апроксимація (SciPy)', color='blue', linewidth=2)
        plt.title(f'Результат апроксимації (MSE={mse:.2f})')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        
        img_name = "approximation_plot.png"
        plt.savefig(img_name)
        print(f"-> Графік збережено як {img_name}")
        plt.show()
        
        save_results(x_data, y_data, y_fit, popt, mse)
        
    except Exception as e:
        print(f"[Помилка візуалізації]: {e}")

def main():
    while True:
        print("\nСистема апроксимації даних (SciPy)")
        print("1. Запустити аналіз даних")
        print("2. Вихід")
        
        cmd = input("Оберіть дію: ")
        
        if cmd == '1':
            process_approximation()
        elif cmd == '2':
            print("Роботу завершено.")
            break
        else:
            print("Невідома команда, спробуйте ще раз.")

if __name__ == "__main__":
    main()