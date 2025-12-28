import matplotlib.pyplot as plt
import sys

data_storage = {
    "metadata": {
        "indicator_name": "Діти, які не відвідують початкову школу",
        "source": "Світовий банк (World Bank Open Data)",
        "period": "2010-2021"
    },
    "Ukraine": {
        "years": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
        "values": [35430, 32100, 28900, 25600, 48500, 62300, 65100, 59400, 52300, 48800, 43200, 39500],
        "color": "#1f77b4"
    },
    "USA": {
        "years": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
        "values": [1650000, 1580000, 1520000, 1460000, 1410000, 1380000, 1450000, 1510000, 1560000, 1590000, 1680000, 1610000],
        "color": "#d62728"
    }
}

print("Візуалізація даних Світового банку")
print(f"Показник: {data_storage['metadata']['indicator_name']}")
print("Доступні країни: Україна, США")
print("-" * 40)

user_input = input("Введіть назву країни для побудови діаграми (наприклад, 'Україна' або 'США'): ").strip()

selected_country_key = None

if user_input.lower() in ['україна', 'ukraine', 'ua']:
    selected_country_key = "Ukraine"
elif user_input.lower() in ['сша', 'usa', 'united states', 'us']:
    selected_country_key = "USA"
else:
    print(f"\nКраїну '{user_input}' не знайдено в підготовленому наборі даних.")
    print("Будь ласка, перезапустіть програму та оберіть Україну або США.")
    sys.exit()

country_data = data_storage[selected_country_key]
years = country_data["years"]
values = country_data["values"]
bar_color = country_data["color"]
indicator_title = data_storage["metadata"]["indicator_name"]

plt.figure(figsize=(12, 7))
bars = plt.bar(years, values, color=bar_color, width=0.7, edgecolor='black', linewidth=0.7, zorder=3, alpha=0.8)
plt.title(f"{indicator_title}\nДинаміка для країни: {selected_country_key} ({years[0]}-{years[-1]})", 
          fontsize=16, fontweight='bold', pad=20)

plt.xlabel("Рік", fontsize=12, labelpad=10)
plt.ylabel("Кількість дітей", fontsize=12, labelpad=10)
plt.xticks(years, rotation=45)
plt.ticklabel_format(style='plain', axis='y')
plt.grid(axis='y', linestyle='--', color='gray', alpha=0.5, zorder=0)

for bar in bars:
    height = bar.get_height()
    label_text = f'{height:,}' 
    plt.text(bar.get_x() + bar.get_width() / 2, height, label_text, 
             ha='center', va='bottom', fontsize=9, rotation=0, color='black')

plt.tight_layout()
plt.show()