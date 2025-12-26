import string

FILE_IN = "TF7_1.txt"
FILE_OUT = "TF7_2.txt"

def has_double_letters(word):
    clean_word = word.lower()
    
    for i in range(len(clean_word) - 1):
        if clean_word[i] == clean_word[i+1] and clean_word[i].isalpha():
            return True
    return False

def create_source_file(filename):
    lines = [
        "Сонце світить яскраво, а навколо літають бджоли.",
        "Програмування -- це цікавий процес, але потребує уваги.",
        "Ганна та Алла пішли до каси.",
        "В цьому рядку немає подвоєнь літер.", 
        "Root, tree, apple, success!"
    ]
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')
        print(f"Файл '{filename}' успішно створено.")
    except OSError as e:
        print(f"Не вдалося створити файл '{filename}': {e}")

def process_files(file_in, file_out):
    found_words = []
    
    try:
        with open(file_in, 'r', encoding='utf-8') as f_read:
            text = f_read.read()
            
            translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
            clean_text = text.translate(translator)
            
            words = clean_text.split()
            
            for word in words:
                if has_double_letters(word):
                    found_words.append(word)
        
        with open(file_out, 'w', encoding='utf-8') as f_write:
            if found_words:
                for word in found_words:
                    f_write.write(word + '\n')
            else:
                f_write.write("Слів з подвоєнням літер не знайдено.\n")
                
        print(f"Обробку завершено. Результат записано у '{file_out}'.")

    except FileNotFoundError:
        print(f"Файл '{file_in}' не знайдено. Спочатку створіть його.")
    except OSError as e:
        print(f"Виникла проблема при роботі з файлами: {e}")

def print_result_file(filename):
    print(f"\nВміст файлу {filename}")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
            print("------------------------------")
    except FileNotFoundError:
        print(f"Файл '{filename}' не існує.")
    except OSError as e:
        print(f"Не вдалося прочитати файл: {e}")

def main():
    create_source_file(FILE_IN)
    process_files(FILE_IN, FILE_OUT)
    print_result_file(FILE_OUT)

if __name__ == "__main__":
    main()