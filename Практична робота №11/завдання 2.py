import pandas as pd
import matplotlib.pyplot as plt

filename = 'comptage_velo_2012.csv'

try:
    df = pd.read_csv(filename, parse_dates=['Date'], dayfirst=True)
except FileNotFoundError:
    print(f"Файл '{filename}' не знайдено.")
    print("Перевірте, чи файл лежить у папці зі скриптом і чи правильно він називається.")
    exit()

df.set_index('Date', inplace=True)

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

df = df.select_dtypes(include=['number'])

total_cyclists = df.sum().sum()
print(f"\n1. Загальна кількість велосипедистів за рік: {int(total_cyclists)}")

print("\n2. Кількість по кожній велодоріжці:")
print(df.sum())

print("\n3. Найпопулярніший місяць для перших 3-х велодоріжок:")
monthly_data = df.resample('ME').sum() # 'ME' - кінець місяця

selected_paths = df.columns[:3]

for path in selected_paths:
    if path in monthly_data.columns:
        max_date = monthly_data[path].idxmax()
        max_val = monthly_data[path].max()
        month_name = max_date.strftime('%B')
        print(f"   - {path}: {month_name} ({int(max_val)})")

plt.figure(figsize=(10, 6))

path_to_plot = df.columns[0] 

monthly_data[path_to_plot].plot(kind='bar', color='skyblue', edgecolor='black')

plt.title(f'Завантаженість велодоріжки "{path_to_plot}" (2012)')
plt.xlabel('Місяць')
plt.ylabel('Кількість')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()