# 📈 Calculadora de Máximos y Mínimos

Este es un proyecto web simple para encontrar los puntos máximos y mínimos absolutos de una función cúbica (grado 3) dentro de un intervalo definido por el usuario.

La función tiene la forma:
**f(x) = ax³ + bx² + cx + d**

## 🛠️ Tecnologías Usadas

* **HTML5:** Para la estructura de la página (`index.html`).
* **CSS3:** Para los estilos y el diseño (`style.css`).
* **JavaScript (JS):** Para toda la lógica de cálculo y la interactividad (`script.js`).
* **Python:** Para un servidor web local *opcional* (`run.py`).

## 🚀 ¿Cómo Usarlo?

Tienes dos maneras de ejecutar este proyecto.

### Opción 1: La forma más simple (Recomendada)

Simplemente **haz doble clic en el archivo `index.html`** para abrirlo en tu navegador web (como Chrome, Firefox, o Edge). ¡Eso es todo!

El programa funciona completamente en tu navegador y no necesita nada más.

### Opción 2: Usando el servidor local de Python (Opcional)

Este método es **totalmente opcional** y solo sirve para simular un entorno de servidor real.

1.  Asegúrate de tener [Python](https://www.python.org/downloads/) instalado en tu computadora.
2.  Abre una terminal o línea de comandos en la carpeta donde están los archivos del proyecto.
3.  Ejecuta el siguiente comando:
    ```bash
    python run.py
    ```
    (Si tienes varias versiones de Python, puede que necesites usar `python3 run.py`).
4.  El script iniciará el servidor y (probablemente) abrirá tu navegador automáticamente en **http://localhost:8000**.

> **IMPORTANTE:** Si el comando `run.py` te da un error o no funciona, **no te preocupes**. Simplemente ignora esta opción y **usa la "Opción 1"** (abrir el `index.html` directamente).

## 🧠 ¿Cómo funciona la lógica (el cálculo)?

El programa no prueba todos los números posibles. Utiliza un método de cálculo diferencial para ser eficiente y preciso:

1.  **Función Original:** El usuario introduce los coeficientes $a, b, c, d$ para $f(x) = ax^3 + bx^2 + cx + d$.
2.  **Derivada:** El script calcula la primera derivada de la función: $f'(x) = 3ax^2 + 2bx + c$.
3.  **Puntos Críticos:** La derivada representa la pendiente. Los máximos y mínimos locales ocurren donde la pendiente es cero. El script resuelve $f'(x) = 0$ usando la fórmula cuadrática para encontrar estos "puntos críticos".
4.  **Lista de Candidatos:** El programa crea una lista de puntos "candidatos" donde podría estar el máximo o mínimo absoluto. Esta lista incluye:
    * El inicio del intervalo ($x_{min}$).
    * El final del intervalo ($x_{max}$).
    * Cualquier punto crítico que se encuentre *dentro* del intervalo $[x_{min}, x_{max}]$.
5.  **Evaluación:** Finalmente, el script evalúa la función original $f(x)$ en cada uno de los puntos candidatos.
6.  **Resultado:** Compara todos los resultados y reporta el valor más alto como el **Máximo Absoluto** y el valor más bajo como el **Mínimo Absoluto** en ese intervalo.