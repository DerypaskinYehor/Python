import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'Категорія': ['А', 'А', 'А', 'Б', 'Б', 'В', 'В', 'В', 'В'],
    'Ціна': [100, 120, 110, 200, 210, 50, 60, 55, 58]
})

plt.figure(figsize=(8, 5))
sns.boxplot(x='Категорія', y='Ціна', data=df, palette='Set2')
sns.stripplot(x='Категорія', y='Ціна', data=df, color='black', alpha=0.5) # Показати точки

plt.title('Розподіл цін по категоріях')
plt.show()