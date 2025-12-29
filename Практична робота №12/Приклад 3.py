import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y1, label='Sin(x)', color='blue', linestyle='--')
plt.plot(x, y2, label='Cos(x)', color='red', linewidth=2)

plt.title('Тригонометричні функції')
plt.xlabel('Час (t)')
plt.ylabel('Амплітуда')
plt.legend()
plt.grid(True)
plt.show()