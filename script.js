// Espera a que todo el contenido del DOM (la estructura HTML) esté completamente cargado y parseado.
document.addEventListener('DOMContentLoaded', function() {

    // --- Funcionalidad para el Tokenizador Simple ---
    const textInput = document.getElementById('textInput');
    const tokenizeButton = document.getElementById('tokenizeButton');
    const tokenOutput = document.getElementById('tokenOutput');

    if (tokenizeButton) { // Verificar que el botón existe antes de añadir el listener
        tokenizeButton.addEventListener('click', function() {
            const inputText = textInput.value.trim(); // Obtener texto y quitar espacios al inicio/final
            tokenOutput.innerHTML = ''; // Limpiar salida anterior

            if (inputText === '') {
                tokenOutput.textContent = 'Por favor, escribe algo para tokenizar.';
                return;
            }

            // Tokenización simple: dividir por espacios.
            // Para una tokenización más real, se usarían expresiones regulares o librerías.
            // Esto es solo para ilustrar el concepto básico.
            const tokens = inputText.split(/\s+/).filter(token => token.length > 0); 
            // \s+ divide por uno o más espacios y filter elimina tokens vacíos si hay múltiples espacios.

            if (tokens.length > 0) {
                tokens.forEach(token => {
                    const tokenSpan = document.createElement('span');
                    tokenSpan.textContent = token;
                    // Podrías añadir clases aquí para estilizar cada token si quisieras
                    tokenOutput.appendChild(tokenSpan);
                });
            } else {
                tokenOutput.textContent = 'No se encontraron tokens (solo ingresaste espacios).';
            }
        });
    }

    // --- Funcionalidad para la Visualización Conceptual de Embeddings ---
    const clickableWords = document.querySelectorAll('.word-embed');
    const embeddingOutput = document.getElementById('embeddingOutput');

    if (clickableWords.length > 0 && embeddingOutput) { // Verificar que los elementos existen
        clickableWords.forEach(wordElement => {
            wordElement.addEventListener('click', function() {
                const word = this.dataset.word; // Obtener la palabra del atributo data-word

                // Generar un "vector" de embedding de ejemplo (¡NO ES REAL!)
                // Solo para fines ilustrativos. Un embedding real tiene cientos de dimensiones
                // y valores específicos aprendidos por el modelo.
                let embeddingVector = [];
                for (let i = 0; i < 5; i++) { // Generamos un vector de 5 dimensiones de ejemplo
                    embeddingVector.push((Math.random() * 2 - 1).toFixed(3)); // Números aleatorios entre -1 y 1 con 3 decimales
                }

                embeddingOutput.innerHTML = `
                    <p><strong>Palabra:</strong> ${word}</p>
                    <p><strong>Vector Conceptual (Ejemplo):</strong></p>
                    <code>[${embeddingVector.join(', ')}]</code>
                    <p class="disclaimer"><em>(Nota: Este es un vector aleatorio solo para ilustración. Los embeddings reales son aprendidos y mucho más complejos.)</em></p>
                `;
            });
        });
    }

    // --- Funcionalidad para el Smooth Scrolling de la Navegación ---
    const navLinks = document.querySelectorAll('nav ul li a');

    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            // Verificar si el enlace es interno (comienza con #)
            if (this.hash !== "") {
                event.preventDefault(); // Prevenir el comportamiento de salto por defecto

                const hash = this.hash; // Obtener el #id_seccion del href

                // Encontrar el elemento de la sección correspondiente
                const targetElement = document.querySelector(hash);

                if (targetElement) {
                    // Calcular la posición del elemento de destino
                    // Se puede restar un offset si tienes un header fijo que tape parte de la sección
                    const headerOffset = document.querySelector('nav').offsetHeight || 70; // Altura de la barra de nav o un valor por defecto
                    const elementPosition = targetElement.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                    window.scrollTo({
                        top: offsetPosition,
                        behavior: "smooth" // Desplazamiento suave
                    });

                    // Opcional: Cerrar menú de navegación en móviles si estuviera abierto
                }
            }
        });
    });


    // --- Actualizar el año actual en el footer ---
    const currentYearSpan = document.getElementById('currentYear');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }

}); // Fin de DOMContentLoaded