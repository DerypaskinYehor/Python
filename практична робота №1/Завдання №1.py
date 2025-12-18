a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))

if a <= 0 or b <= 0:
    print("Числа a і b повинні бути додатними!")
else:
    if a < b:
        X = a / b + 1
    elif a == b:
        X = -1
    else:
        X = (a * b - 5) / a

    print("X =", X)
