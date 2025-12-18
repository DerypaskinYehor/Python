N = int(input("Введіть число N: "))

if 1 < N < 9:
    for i in range(N):
        for j in range(N, i, -1):
            print(j, end=" ")
        print()
else:
    print("Число повинно задовольняти умову 1 < N < 9.")
