import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 500)

y = np.sqrt(x) * np.sin(10 * x)

plt.figure(figsize=(10, 6))

plt.plot(x, y,
         linestyle='-',
         color='darkblue',
         linewidth=2,
         label=r'$Y(x) = \sqrt{x} \cdot \sin(10x)$')

plt.title("Графік функції Y(x)", fontsize=14)
plt.xlabel("X", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()