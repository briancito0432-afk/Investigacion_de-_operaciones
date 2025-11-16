// Espera a que el contenido del DOM esté cargado
document.addEventListener('DOMContentLoaded', () => {

    // Obtener los elementos del DOM
    const calcularBtn = document.getElementById('calcularBtn');
    const resultadoDiv = document.getElementById('resultado');

    // Función que se ejecuta al hacer clic en el botón
    calcularBtn.addEventListener('click', () => {
        // 1. OBTENER LOS VALORES DE ENTRADA
        const a = parseFloat(document.getElementById('a').value);
        const b = parseFloat(document.getElementById('b').value);
        const c = parseFloat(document.getElementById('c').value);
        const d = parseFloat(document.getElementById('d').value);
        const xMin = parseFloat(document.getElementById('xMin').value);
        const xMax = parseFloat(document.getElementById('xMax').value);

        // 2. VALIDACIÓN DE ENTRADAS
        if ([a, b, c, d, xMin, xMax].some(isNaN)) {
            mostrarError('Todos los campos deben ser números válidos.');
            return;
        }

        if (a === 0) {
            mostrarError('El coeficiente "a" no puede ser cero para una función cúbica.');
            return;
        }

        if (xMin >= xMax) {
            mostrarError('El "X Mínimo" del intervalo debe ser menor que el "X Máximo".');
            return;
        }

        // 3. LÓGICA DE CÁLCULO
        
        // Definimos la función f(x)
        const f = (x) => (a * x**3) + (b * x**2) + (c * x) + d;

        // Puntos a evaluar: Empezamos con los extremos del intervalo
        const candidatosX = [xMin, xMax];

        // Calcular los puntos críticos (donde la derivada es 0)
        // f'(x) = 3ax² + 2bx + c
        // Usamos la fórmula cuadrática: x = [-B ± sqrt(B² - 4AC)] / 2A
        // Donde: A = 3a, B = 2b, C = c

        const A_deriv = 3 * a;
        const B_deriv = 2 * b;
        const C_deriv = c;

        const discriminante = (B_deriv**2) - (4 * A_deriv * C_deriv);

        if (discriminante >= 0) {
            // Si el discriminante es >= 0, hay raíces reales (puntos críticos)
            const x_critico1 = (-B_deriv + Math.sqrt(discriminante)) / (2 * A_deriv);
            const x_critico2 = (-B_deriv - Math.sqrt(discriminante)) / (2 * A_deriv);

            // Añadir los puntos críticos a la lista de candidatos SÓLO SI están dentro del intervalo
            if (x_critico1 >= xMin && x_critico1 <= xMax) {
                candidatosX.push(x_critico1);
            }
            if (x_critico2 >= xMin && x_critico2 <= xMax) {
                // Evitar duplicados si x_critico1 == x_critico2
                if (x_critico1 !== x_critico2) {
                    candidatosX.push(x_critico2);
                }
            }
        }
        // Si el discriminante es < 0, la función no tiene máximos ni mínimos locales,
        // por lo que los absolutos estarán en los extremos del intervalo (que ya están en la lista).

        // 4. ENCONTRAR MÁXIMO Y MÍNIMO ABSOLUTO EN EL INTERVALO
        let puntoMaximo = { x: xMin, y: f(xMin) };
        let puntoMinimo = { x: xMin, y: f(xMin) };

        // Iteramos sobre todos los candidatos (extremos + críticos)
        for (const x of candidatosX) {
            const y = f(x);

            if (y > puntoMaximo.y) {
                puntoMaximo = { x: x, y: y };
            }
            if (y < puntoMinimo.y) {
                puntoMinimo = { x: x, y: y };
            }
        }

        // 5. MOSTRAR RESULTADOS
        mostrarResultado(puntoMaximo, puntoMinimo);
    });

    // Función para mostrar el resultado final
    function mostrarResultado(max, min) {
        resultadoDiv.innerHTML = `
            <h3>Resultados en el intervalo [${xMin.value}, ${xMax.value}]</h3>
            <p><strong>Punto Máximo:</strong></p>
            <p>x = ${max.x.toFixed(4)}</p>
            <p>y = ${max.y.toFixed(4)}</p>
            <hr>
            <p><strong>Punto Mínimo:</strong></p>
            <p>x = ${min.x.toFixed(4)}</p>
            <p>y = ${min.y.toFixed(4)}</p>
        `;
        resultadoDiv.className = ''; // Limpiar clases de error
    }

    // Función para mostrar errores
    function mostrarError(mensaje) {
        resultadoDiv.innerHTML = `<p>${mensaje}</p>`;
        resultadoDiv.className = 'error'; // Añadir clase de error para estilo
    }
});