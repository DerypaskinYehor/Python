def words():
    
    word1 = input("Введіть перше слово: ")
    word2 = input("Введіть друге слово: ")

    if word1 == word2:
        print("Слова однакові.")
    else:
        print("Слова різні.")

if __name__ == "__main__":
    words()