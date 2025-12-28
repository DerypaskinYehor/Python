import matplotlib.pyplot as plt
import json

json_data_string = """
{
    "students": [
        {"id": 1, "name": "Олександр", "gender": "male"},
        {"id": 2, "name": "Марія", "gender": "female"},
        {"id": 3, "name": "Іван", "gender": "male"},
        {"id": 4, "name": "Олена", "gender": "female"},
        {"id": 5, "name": "Дмитро", "gender": "male"},
        {"id": 6, "name": "Анна", "gender": "female"},
        {"id": 7, "name": "Максим", "gender": "male"},
        {"id": 8, "name": "Вікторія", "gender": "female"},
        {"id": 9, "name": "Андрій", "gender": "male"},
        {"id": 10, "name": "Софія", "gender": "female"},
        {"id": 11, "name": "Артем", "gender": "male"},
        {"id": 12, "name": "Богдан", "gender": "male"}
    ]
}
"""

data = json.loads(json_data_string)

boys_count = 0
girls_count = 0

for student in data['students']:
    if student['gender'] == 'male':
        boys_count += 1
    elif student['gender'] == 'female':
        girls_count += 1

labels = ['Хлопці', 'Дівчата']
values = [boys_count, girls_count]
colors = ['#66b3ff', '#ff9999']

plt.figure(figsize=(8, 8))

plt.pie(values, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%', 
        startangle=90, 
        explode=(0, 0),
        textprops={'fontsize': 14})

class_name = data.get('school_class', 'Клас')
plt.title(f"Гендерний склад учнів", fontsize=16, fontweight='bold')
plt.legend(title="Категорії", loc="upper right")
plt.axis('equal')
plt.show()