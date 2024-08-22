import random

# Banco de preguntas
preguntas = [
    {"pregunta": "¿Cuál es la capital de Francia?", "respuestas": ["A) París", "B) Londres", "C) Berlín", "D) Madrid"], "correcta": "A"},
    {"pregunta": "¿Cuál es el planeta más grande del sistema solar?", "respuestas": ["A) Mercurio", "B) Venus", "C) Tierra", "D) Júpiter"], "correcta": "D"},
    {"pregunta": "¿Cuál es el autor de la obra 'Don Quijote de la Mancha'?", "respuestas": ["A) Miguel de Cervantes", "B) William Shakespeare", "C) Gabriel García Márquez", "D) Pablo Neruda"], "correcta": "A"},
    {"pregunta": "¿Cuál es el río más largo del mundo?", "respuestas": ["A) Nilo", "B) Amazonas", "C) Yangtze", "D) Mississippi"], "correcta": "A"},
    {"pregunta": "¿Cuál es el país más poblado del mundo?", "respuestas": ["A) China", "B) India", "C) Estados Unidos", "D) Indonesia"], "correcta": "A"},
    {"pregunta": "¿Cuál es el animal más rápido del mundo?", "respuestas": ["A) León", "B) Cheetah", "C) Águila", "D) Guepardo"], "correcta": "B"},
    {"pregunta": "¿Cuál es el elemento químico más ligero?", "respuestas": ["A) Hidrógeno", "B) Helio", "C) Oxígeno", "D) Nitrógeno"], "correcta": "A"},
    {"pregunta": "¿Cuál es el libro más vendido de todos los tiempos?", "respuestas": ["A) La Biblia", "B) El Señor de los Anillos", "C) Harry Potter", "D) El Alquimista"], "correcta": "A"},
    {"pregunta": "¿Cuál es el país con más fronteras internacionales?", "respuestas": ["A) China", "B) Rusia", "C) Canadá", "D) Estados Unidos"], "correcta": "B"},
    {"pregunta": "¿Cuál es el deporte más popular del mundo?", "respuestas": ["A) Fútbol", "B) Baloncesto", "C) Tenis", "D) Cricket"], "correcta": "A"},
    {"pregunta": "¿Cuál es el monumento más famoso de Francia?", "respuestas": ["A) Torre Eiffel", "B) Louvre", "C) Notre Dame", "D) Arc de Triomphe"], "correcta": "A"},
    {"pregunta": "¿Cuál es el país con más islas del mundo?", "respuestas": ["A) Suecia", "B) Grecia", "C) Indonesia", "D) Filipinas"], "correcta": "A"},
    {"pregunta": "¿Cuál es el río más profundo del mundo?", "respuestas": ["A) Amazonas", "B) Congo", "C) Nilo", "D) Yangtze"], "correcta": "B"},
    {"pregunta": "¿Cuál es el país con más montañas del mundo?", "respuestas": ["A) Nepal", "B) China", "C) India", "D) Pakistán"], "correcta": "A"},
    {"pregunta": "¿Cuál es el animal más grande del mundo?", "respuestas": ["A) Ballena azul", "B) Elefante africano", "C) Rinoceronte blanco", "D) Hippopotamo"], "correcta": "A"}
]

# Función para generar una pregunta aleatoria que no se haya usado
def generar_pregunta_usada(preguntas_disponibles):
    pregunta = random.choice(preguntas_disponibles)
    preguntas_disponibles.remove(pregunta)  # Elimina la pregunta seleccionada para evitar repetición
    return pregunta

# Función para mezclar aleatoriamente las respuestas
def mezclar_respuestas(pregunta):
    respuestas = pregunta["respuestas"][:]
    random.shuffle(respuestas)
    pregunta_mezclada = {
        "pregunta": pregunta["pregunta"],
        "respuestas": respuestas,
        "correcta": next(letra[0] for letra in respuestas if letra[0] == pregunta["correcta"])
    }
    return pregunta_mezclada

# Función para mostrar la pregunta y obtener la respuesta del usuario
def mostrar_pregunta(pregunta):
    print(pregunta["pregunta"])
    for respuesta in pregunta["respuestas"]:
        print(respuesta)

# Función para verificar si la respuesta es correcta
def verificar_respuesta(pregunta, respuesta_usuario):
    return respuesta_usuario.upper() == pregunta["correcta"]

# Función para calcular el puntaje usando la serie de Fibonacci
def calcular_puntaje(estacion):
    return fibonacci(estacion)

# Función para calcular la serie de Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

# Función para eliminar dos opciones falsas (50/50)
def ayuda_50_50(pregunta):
    respuestas_falsas = [respuesta for respuesta in pregunta["respuestas"] if respuesta[0] != pregunta["correcta"]]
    respuestas_eliminar = random.sample(respuestas_falsas, 2)
    pregunta["respuestas"] = [respuesta for respuesta in pregunta["respuestas"] if respuesta not in respuestas_eliminar]
    return pregunta

# Función para cambiar de pregunta
def ayuda_cambio_pregunta(preguntas_disponibles):
    return generar_pregunta_usada(preguntas_disponibles)

# Función principal
def juego():
    print("¡Bienvenido al juego '¿Quién quiere ser millonario?'!")
    nombre_usuario = input("Ingrese su nombre: ")
    print(f"¡Hola, {nombre_usuario}! Usted tiene la oportunidad de ganar un gran premio.")
    
    estacion = 1
    puntaje = 0
    ayuda_50_50_disponible = True
    ayuda_cambio_pregunta_disponible = True
    
    # Lista de preguntas disponibles para evitar repetición
    preguntas_disponibles = preguntas[:]
    
    while estacion <= 10:
        pregunta = generar_pregunta_usada(preguntas_disponibles)
        
        # Mezclar respuestas antes de mostrar la pregunta
        pregunta_mezclada = mezclar_respuestas(pregunta)
        
        # Mostrar la pregunta antes de las ayudas
        mostrar_pregunta(pregunta_mezclada)
        
        print("Ayudas disponibles:")
        if ayuda_50_50_disponible:
            print("1. 50/50")
        if ayuda_cambio_pregunta_disponible:
            print("2. Cambio de pregunta")
        
        ayuda_seleccionada = input("Ingrese el número de la ayuda que desea utilizar (0 para no utilizar ayuda): ")
        
        if ayuda_seleccionada == "1" and ayuda_50_50_disponible:
            pregunta_mezclada = ayuda_50_50(pregunta_mezclada)
            ayuda_50_50_disponible = False
            print("Se han eliminado dos opciones falsas.")
            mostrar_pregunta(pregunta_mezclada)  # Volver a mostrar la pregunta después de aplicar la ayuda
        elif ayuda_seleccionada == "2" and ayuda_cambio_pregunta_disponible:
            pregunta_mezclada = ayuda_cambio_pregunta(preguntas_disponibles)
            ayuda_cambio_pregunta_disponible = False
            print("Se ha cambiado la pregunta.")
            mostrar_pregunta(mezclar_respuestas(pregunta_mezclada))  # Mostrar la nueva pregunta
        
        respuesta_usuario = input("Ingrese su respuesta (A, B, C o D): ").upper()
        
        if verificar_respuesta(pregunta_mezclada, respuesta_usuario):
            puntaje += calcular_puntaje(estacion)
            print(f"¡Correcto! Usted ha ganado {puntaje} puntos.")
        else:
            print("Lo siento, respuesta incorrecta. Usted ha perdido.")
            break
        
        # Opción de retirarse en las estaciones 5 y 7
        if estacion == 5 or estacion == 7:
            respuesta = input("¿Desea retirarse del juego? (S/N): ").upper()
            if respuesta == "S":
                print(f"Usted se retira del juego con un puntaje de {puntaje} puntos.")
                break
        
        estacion += 1
    
    # Mostrar el resultado final
    print(f"El juego ha terminado. Su puntaje final es de {puntaje} puntos.")

# Iniciar el juego
juego()
