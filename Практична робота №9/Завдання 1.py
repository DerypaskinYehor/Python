import csv

input_filename = 'ukraine_gdp.csv'
output_filename = 'gdp_analysis_results.csv'

def process_gdp_data():
    try:
        with open(input_filename, mode='r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            
            print(f"Вміст файлу {input_filename}")
            print(f"{header[0]:<10} | {header[1]}")
            print("-" * 25)

            gdp_data = []

            for row in reader:
                print(f"{row[0]:<10} | {row[1]}")
                
                try:
                    year = int(row[0])
                    value = float(row[1])
                    gdp_data.append((year, value))
                except ValueError:
                    continue

            print("-" * 25)

            if not gdp_data:
                print("Дані для аналізу відсутні.")
                return
            min_gdp = min(gdp_data, key=lambda x: x[1])
            max_gdp = max(gdp_data, key=lambda x: x[1])

            print(f"\nРезультати аналізу:")
            print(f"Найнижчий ВВП: {min_gdp[1]} USD у {min_gdp[0]} році")
            print(f"Найвищий ВВП: {max_gdp[1]} USD у {max_gdp[0]} році")
            save_results(output_filename, min_gdp, max_gdp)

    except FileNotFoundError:
        print(f"\nФайл '{input_filename}' не знайдено.")
        print("Будь ласка, переконайтеся, що файл знаходиться у тій же папці, що і програма.")
    except Exception as e:
        print(f"\nВиникла непередбачувана помилка: {e}")

def save_results(filename, min_val, max_val):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Indicator', 'Year', 'Value (USD)'])
            writer.writerow(['Min GDP', min_val[0], min_val[1]])
            writer.writerow(['Max GDP', max_val[0], max_val[1]])
            
        print(f"\nРезультати успішно збережено у файл '{filename}'.")
        
    except IOError:
        print(f"Не вдалося записати дані у файл '{filename}'.")

if __name__ == "__main__":
    process_gdp_data()