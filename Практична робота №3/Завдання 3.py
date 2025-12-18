import string

def words_with_r():
    
    sentence = input("Введіть речення: ")
    
    words = sentence.split()
    
    count = 0
    punctuation_chars = ".,!?:;()-\"'"
    
    print("\nЗнайдені слова:")
    
    for word in words:
        clean_word = word.strip(punctuation_chars)
        
        if len(clean_word) > 0 and clean_word.lower().endswith('р'):
            print(f"- {clean_word}")
            count += 1
            
    print(f"Кількість слів, що закінчуються на 'р': {count}")

if __name__ == "__main__":
    words_with_r()