def main():
    N = 7
    matrix = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i + j >= N - 1:
                matrix[i][j] = 13 - i - j

    print("Результат:")
    for row in matrix:
        for x in row:
            print(f"{x:2}", end=" ")
        print()

if __name__ == "__main__":

    main()
