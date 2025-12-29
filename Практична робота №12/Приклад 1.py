import numpy as np

grades = np.array([85, 90, 78, 92, 88, 76, 95, 89])

print(f"Середній бал: {np.mean(grades)}")
print(f"Медіана: {np.median(grades)}")

grades_12 = (grades / 100) * 12
print(f"Оцінки: {grades_12.round(1)}")

normalized_grades = (grades - np.min(grades)) / (np.max(grades) - np.min(grades))
print(f"Нормалізовані дані: {normalized_grades.round(2)}")
