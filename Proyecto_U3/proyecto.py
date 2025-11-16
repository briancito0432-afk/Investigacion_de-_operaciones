import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. Definición del Problema ---

def f(x1, x2):
    """ La función objetivo (tiempo de respuesta global). """
    return x1**2 + 3*x2**2 + 2*x1*x2

def grad_f(x1, x2):
    """ El gradiente de la función objetivo. """
    return np.array([2*x1 + 2*x2, 2*x1 + 6*x2])

def project(x1, x2):
    """ Proyecta un punto (x1, x2) de vuelta a la línea de restricción x1 + x2 = 1. """
    delta = (1.0 - (x1 + x2)) / 2.0
    return np.array([x1 + delta, x2 + delta])

# --- 2. Implementación del Algoritmo ---

learning_rate = 0.1
n_iterations = 50
start_point = np.array([0.5, 0.5])

trajectory = [start_point]
response_times = [f(start_point[0], start_point[1])]

current_point = start_point
for i in range(n_iterations):
    grad = grad_f(current_point[0], current_point[1])
    unconstrained_point = current_point - learning_rate * grad
    current_point = project(unconstrained_point[0], unconstrained_point[1])
    
    trajectory.append(current_point)
    response_times.append(f(current_point[0], current_point[1]))

trajectory = np.array(trajectory)

# --- 3. Configuración de la Animación (Matplotlib) ---

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)
ax_inset = fig.add_axes([0.65, 0.65, 0.2, 0.2])

x_range = np.linspace(-1, 2, 100)
y_range = np.linspace(-1, 2, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = f(X, Y)

cp = ax.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.7)
fig.colorbar(cp, ax=ax, label='Tiempo de Respuesta Global (f)')
ax.contour(X, Y, Z, levels=20, colors='black', linewidths=0.5, alpha=0.5)

line_x = np.array([-1, 2])
line_y = 1.0 - line_x
ax.plot(line_x, line_y, 'r--', linewidth=2, label='Restricción ($x_1 + x_2 = 1$)')

ax.plot(1, 0, 'r*', markersize=15, label='Mínimo Global (1.0, 0.0)')

line_trajectory, = ax.plot([], [], 'o-', c='white', markersize=4, markerfacecolor='cyan', label='Trayectoria')
point_current, = ax.plot([], [], 'o', c='magenta', markersize=12)
title = ax.set_title('Iteración 0')

line_response, = ax_inset.plot([], [], 'b-')
ax_inset.set_xlim(0, n_iterations)
ax_inset.set_ylim(min(response_times) * 0.9, max(response_times) * 1.1)
ax_inset.set_xlabel('Iteración', fontsize=8)
ax_inset.set_ylabel('Tiempo Resp.', fontsize=8)
ax_inset.grid(True)

ax.set_xlabel('Carga Servidor 1 ($x_1$)')
ax.set_ylabel('Carga Servidor 2 ($x_2$)')
ax.set_xlim(x_range[0], x_range[-1])
ax.set_ylim(y_range[0], y_range[-1])
ax.legend()
ax.grid(True, linestyle=':', alpha=0.6)

def animate(i):
    """ Función que actualiza la animación en cada frame 'i'. """
    
    line_trajectory.set_data(trajectory[:i+1, 0], trajectory[:i+1, 1])
    
    # --- ESTA ES LA LÍNEA CORREGIDA ---
    # Se usan [ ] para pasar una lista de un solo elemento
    point_current.set_data([trajectory[i, 0]], [trajectory[i, 1]])
    
    x1, x2 = trajectory[i]
    f_val = response_times[i]
    title.set_text(f'Iteración {i} | Carga: ({x1:.3f}, {x2:.3f}) | Tiempo: {f_val:.4f}')
    
    line_response.set_data(range(i+1), response_times[:i+1])
    
    return line_trajectory, point_current, title, line_response

ani = FuncAnimation(fig, animate, frames=len(trajectory), 
                    interval=100, blit=True, repeat=False)

plt.tight_layout(rect=[0, 0, 0.9, 1])
plt.show()