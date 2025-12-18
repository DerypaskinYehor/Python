def five_letters():
    
    text = input("Введіть слово або речення: ")
    
    if len(text) >= 5:
        result = text[-5:]
        print(f"Останні 5 символів: '{result}'")
    else:
        print(f"Введений рядок занадто короткий (всього {len(text)} симв.). Потрібно мінімум 5.")

if __name__ == "__main__":
    five_letters()