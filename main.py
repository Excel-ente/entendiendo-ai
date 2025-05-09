# -*- coding: utf-8 -*-

# 1. DATOS DE ENTRENAMIENTO (Nuestro "corpus" de texto)
# Imagina que estos son los únicos textos que nuestro modelo va a "leer" para aprender.
corpus = [
    "el perro corre en el parque y corre muchisimo",
    "el gato duerme en el sofa y corre poco",
    "el perro juega con la pelota corre muchisimo",
    "un pajaro canta en el arbol y vuela",
    "el gato persigue un raton y anda",
    "el perro come su comida",
    "el gato bebe leche"
]

# 2. PREPROCESAMIENTO Y TOKENIZACIÓN
# Convertimos el texto en unidades más pequeñas (palabras o "tokens").
# También lo pasamos a minúsculas para simplificar.
def tokenizar_corpus(textos):
    tokens_corpus = []
    for frase in textos:
        palabras = frase.lower().split() # Convertir a minúsculas y dividir por espacios
        tokens_corpus.append(palabras)
    return tokens_corpus

tokens_entrenamiento = tokenizar_corpus(corpus)
print("--- Tokens de Entrenamiento ---")
for i, tokens_frase in enumerate(tokens_entrenamiento):
    print(f"Frase {i+1}: {tokens_frase}")
print("-" * 30)

# 3. "ENTRENAMIENTO" DEL MODELO (Construcción de un modelo de transiciones de palabras)
# Crearemos un diccionario donde cada palabra clave tendrá otro diccionario
# con las palabras que le siguen y cuántas veces aparecen.
# Ejemplo: {'el': {'perro': 3, 'gato': 2, 'parque':1, 'sofa':1, 'arbol':1}, 'perro': {'corre':1, 'juega':1, 'come':1}, ...}

def entrenar_modelo_simple(tokens_corpus):
    modelo = {}
    for tokens_frase in tokens_corpus:
        for i in range(len(tokens_frase) - 1):
            palabra_actual = tokens_frase[i]
            palabra_siguiente = tokens_frase[i+1]

            if palabra_actual not in modelo:
                modelo[palabra_actual] = {} # Si la palabra no está en el modelo, la agregamos

            # Incrementamos el contador para la palabra_siguiente después de palabra_actual
            if palabra_siguiente not in modelo[palabra_actual]:
                modelo[palabra_actual][palabra_siguiente] = 0
            modelo[palabra_actual][palabra_siguiente] += 1
    return modelo

modelo_entrenado = entrenar_modelo_simple(tokens_entrenamiento)
print("--- Modelo Entrenado (Frecuencias de Siguiente Palabra) ---")
for palabra, siguientes_palabras in modelo_entrenado.items():
    print(f"Palabra '{palabra}': {siguientes_palabras}")
print("-" * 30)

# 4. "PREDICCIÓN" (Generación de la siguiente palabra)
# Dada una palabra, el modelo buscará la palabra siguiente más frecuente.
def predecir_siguiente_palabra(modelo, palabra_actual):
    palabra_actual = palabra_actual.lower() # Asegurarse que esté en minúsculas
    if palabra_actual in modelo and modelo[palabra_actual]:
        # Encontrar la palabra siguiente con la frecuencia más alta
        siguientes_posibles = modelo[palabra_actual]
        palabra_mas_probable = max(siguientes_posibles, key=siguientes_posibles.get)
        return palabra_mas_probable
    else:
        # Si la palabra no está en el modelo o no tiene siguientes palabras conocidas
        return "<palabra_desconocida_o_final>"

# 5. PROBANDO NUESTRO MODELO
print("--- Probando el Modelo ---")
palabras_de_inicio = ["el", "un", "gato", "perro"]

for palabra in palabras_de_inicio:
    siguiente_palabra = predecir_siguiente_palabra(modelo_entrenado, palabra)
    print(f"Después de '{palabra}', el modelo predice: '{siguiente_palabra}'")

# Ejemplo de generar una pequeña secuencia:
print("\n--- Generando una pequeña secuencia ---")
palabra_inicial = "el"
frase_generada = [palabra_inicial]
palabra_actual = palabra_inicial

for _ in range(4): # Generar 4 palabras más
    siguiente = predecir_siguiente_palabra(modelo_entrenado, palabra_actual)
    if siguiente == "<palabra_desconocida_o_final>":
        break
    frase_generada.append(siguiente)
    palabra_actual = siguiente

print(f"Frase generada: {' '.join(frase_generada)}")
print("-" * 30)

print("\n--- Explicación y Limitaciones ---")
print("""
Este es un ejemplo EXTREMADAMENTE simplificado. Funciona así:
1.  **Tokenización:** El texto se divide en palabras (tokens).
2.  **Entrenamiento (Conteo de Frecuencias):** El "modelo" es solo un diccionario.
    Al "entrenar", contamos cuántas veces una palabra sigue a otra en el corpus.
    Por ejemplo, si "el perro" aparece 3 veces y "el gato" 2 veces, el modelo 'aprende'
    que después de "el", "perro" es más probable que "gato" (en este corpus limitado).
3.  **Predicción:** Cuando se le da una palabra, el modelo busca en su diccionario
    y devuelve la palabra siguiente que apareció con más frecuencia durante el "entrenamiento".

Limitaciones IMPORTANTES:
-   **Contexto muy limitado:** Solo mira la palabra inmediatamente anterior. Los modelos reales consideran secuencias mucho más largas.
-   **No entiende el significado:** No sabe qué es un "perro" o un "gato", solo las estadísticas de cómo aparecen juntas las palabras.
-   **Vocabulario cerrado:** Solo conoce las palabras del corpus de entrenamiento.
-   **Determinista (en esta versión simple):** Dada una palabra, siempre predecirá la misma siguiente palabra más frecuente. Modelos más avanzados introducen aleatoriedad o consideran probabilidades.
-   **No maneja gramática compleja ni creatividad:** No puede formar frases verdaderamente nuevas o coherentes a largo plazo.

Los modelos de IA reales (como los Transformers, GPT, etc.) usan matemáticas mucho más complejas (redes neuronales, atención, embeddings) para capturar relaciones sutiles en grandes cantidades de texto y generar respuestas mucho más sofisticadas y coherentes. Este ejemplo solo rasca la superficie del concepto de "aprender de los datos".
""")