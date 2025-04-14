import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Comprimentos dos segmentos do braço
L1 = 5.0  # Primeiro segmento
L2 = 3.0  # Segundo segmento
# Função para calcular as posições do braço robótico
def calc_positions(theta1, theta2):
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)
    return (0, 0), (x1, y1), (x2, y2)
# Definição dos ângulos
theta1_vals = np.linspace(0, np.pi / 2, 100)
theta2_vals = np.linspace(0, np.pi / 2, 100)
# Configuração do gráfico
fig, ax = plt.subplots()
ax.set_xlim(-9, 9)
ax.set_ylim(-9, 9)
line, = ax.plot([], [], 'o-', lw=2)
text = ax.text(-8, 8, '', fontsize=12)
# Função de animação
def update(frame):
    theta1 = theta1_vals[frame]
    theta2 = theta2_vals[frame]
    p0, p1, p2 = calc_positions(theta1, theta2)
    line.set_data([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]])
    text.set_text(f'θ1: {np.degrees(theta1):.1f}°\nθ2: {np.degrees(theta2):.1f}°')
    return line, text
# Criar animação
ani = FuncAnimation(fig, update, frames=len(theta1_vals), interval=25, blit=True)
plt.show()