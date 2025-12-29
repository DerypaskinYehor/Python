import pandas as pd

students_db = {
    101: { "surname": "Коваленко", "name": "Олександр", "patronymic": "Іванович", "dob": (2008, 5, 12) },
    102: { "surname": "Мельник", "name": "Ірина", "patronymic": "Петрівна", "dob": (2008, 8, 24) },
    103: { "surname": "Ткаченко", "name": "Андрій", "patronymic": "Васильович", "dob": (2009, 2, 15) },
    104: { "surname": "Бойко", "name": "Оксана", "patronymic": "Сергіївна", "dob": (2009, 11, 30) },
    105: { "surname": "Бондар", "name": "Сергій", "patronymic": "Олександрович", "dob": (2008, 1, 10) },
    106: { "surname": "Кравченко", "name": "Вікторія", "patronymic": "Юріївна", "dob": (2009, 7, 8) },
    107: { "surname": "Олійник", "name": "Максим", "patronymic": "Володимирович", "dob": (2008, 9, 19) },
    108: { "surname": "Шевчук", "name": "Тетяна", "patronymic": "Ігорівна", "dob": (2008, 3, 22) },
    109: { "surname": "Поліщук", "name": "Дмитро", "patronymic": "Миколайович", "dob": (2009, 12, 5) },
    110: { "surname": "Лисенко", "name": "Олена", "patronymic": "Михайлівна", "dob": (2008, 6, 14) }
}

school_supplies = [
    {"category": "Гаджети", "product": "Ноутбук для навчання", "price": 18500, "quantity": 1},
    {"category": "Канцтовари", "product": "Набір зошитів (48 арк)", "price": 450, "quantity": 2},
    {"category": "Аксесуари", "product": "Ортопедичний рюкзак", "price": 2500, "quantity": 1},
    {"category": "Гаджети", "product": "Планшет графічний", "price": 12000, "quantity": 1},
    {"category": "Література", "product": "Атлас та контурні карти", "price": 300, "quantity": 1},
    {"category": "Спорт", "product": "Спортивний костюм", "price": 1800, "quantity": 1},
    {"category": "Канцтовари", "product": "Набір маркерів", "price": 600, "quantity": 1},
    {"category": "Гаджети", "product": "Електронна книга", "price": 5000, "quantity": 1},
    {"category": "Канцтовари", "product": "Набір для креслення", "price": 850, "quantity": 1},
    {"category": "Гаджети", "product": "Ноутбук", "price": 28000, "quantity": 1}
]

for i, student_id in enumerate(students_db):
    students_db[student_id].update(school_supplies[i])

df = pd.DataFrame.from_dict(students_db, orient='index')
df.index.name = 'ID'
df.reset_index(inplace=True)

print("1. Перші 3 рядки")
print(df[['surname', 'category', 'product', 'price']].head(3))

print("\n2. Типи даних")
print(df.dtypes)

print("\n3. Розмірність (рядки, стовпці)")
print(df.shape)

print("\n4. Описова статистика")
print(df[['price', 'quantity']].describe())

df['total_cost'] = df['price'] * df['quantity']
print("\n5. Витрати")
print(df[['surname', 'product', 'price', 'quantity', 'total_cost']].head())

expensive_items = df[df['price'] > 10000]
print("\n6. Дорогі покупки (> 10 000 грн)")
print(expensive_items[['surname', 'product', 'price']])

sorted_df = df.sort_values(by='total_cost', ascending=False)
print("\n7. Топ-3 найбільших витрат")
print(sorted_df[['surname', 'product', 'total_cost']].head(3))

print("\n8. Середня вартість покупки по категоріях")
print(df.groupby('category')['total_cost'].mean())

max_sales = df.groupby('category')['total_cost'].max()
unique_products = df['product'].nunique()
print("\n9. Додатково")
print(f"Кількість унікальних назв товарів: {unique_products}")
print("Максимальна покупка в кожній категорії:")
print(max_sales)