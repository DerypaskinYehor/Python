import pandas as pd

data = {
    'Category': ['Електроніка', 'Одяг', 'Електроніка', 'Одяг', 'Книги'],
    'Product': ['Ноутбук', 'Футболка', 'Смартфон', 'Джинси', 'Підручник'],
    'Cost': [15000, 200, 10000, 800, 150],
    'Price': [18500, 450, 12000, 1200, 300]
}
df = pd.DataFrame(data)

df['Profit'] = df['Price'] - df['Cost']

high_profit = df[df['Profit'] > 1000]

category_stats = df.groupby('Category')['Profit'].mean()

print("Топ товари:\n", high_profit)
print("\nСередній прибуток по категоріях:\n", category_stats) 