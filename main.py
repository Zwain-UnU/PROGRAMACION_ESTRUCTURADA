print("\033c")
print("\n\t╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
print(  "\t║   Sonic Kinetic Hunter - Sistema de escritorio en consola para implementación de un entorno de juego para el refuerzo de competencias en física  ║")
print(  "\t╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
print("\n\tControles:  A = Izquierda  |  D = Derecha")
print("\n\tToca los anillos para responder preguntas de fisica.")
print(  "\tTienes 3 vidas y 12 preguntas. ¡Buena suerte!\n")


print( "\t Created By: ")
print( "\t Leonel Ivan Sifuentes Zaragoza ")
print( "\t Maya Itza Mendiola Valenciano\n ")
print( "\t 2A BIS TI\n ")

print("\tPresiona ENTER para comenzar...")
input()

print("\033c")
"""
Aqui se ejecutara el codigo, implementando
los demas archivos.py, importandolos para asi
tener un archivo main mas limpio y correcto.
"""
import curses
import random
import time

#CONSTANTES
MAX_VIDAS = 3
TOTAL_PREGUNTAS = 12
PUNTOS_POR_ACIERTO = 100

#MANEJO DE EXCEPCIONES: PARA QUE SE ASEGURE DE TENER LA CARPETA Y EN LAS FUNCIONES PARA QUE SI NO HAY
#UN PEQUEÑO PIXEL CARGADO ESTE PIXEL NO SE NOTARA Y NO TIENE PORQEU CANCELAR LA EJECUCION
try:
    import colores
    import diseno
    import preguntas 
    import fisica
    import ring
    import fondo
    import fondo_del_fondo
except:
    print("Asegurate de que los archivos que estas importando esten en la misma carpeta, y con la extension '.py'")

def calcular_tamano(sprite):
    alto = len(sprite)
    ancho = 0
    for fila in sprite:
        if len(fila) > ancho:
            ancho = len(fila)
    return alto, ancho * 2
#FUNCIONES PARA ARRASTRRAR LOS SPRITES DE SUS ARCHIVOS Y ACOMODARLOS EN EL MAIN
def dibujar_figura(pantalla, sprite, pos_y, pos_x, alto_ventana, ancho_ventana):
    for fila_index, fila in enumerate(sprite):
        for col_index, numero_color in enumerate(fila):
            if numero_color != 0:
                y = pos_y + fila_index
                x = pos_x + (col_index * 2)
                if 0 <= y < alto_ventana - 1 and 0 <= x < ancho_ventana - 2:
                    try:
                        pantalla.attron(curses.color_pair(numero_color))
                        pantalla.addstr(y, x, "██")
                        pantalla.attroff(curses.color_pair(numero_color))
                    except:
                        pass

def dibujar_repetido(pantalla, sprite, pos_y, alto_ventana, ancho_ventana):
    if not sprite:
        return
    ancho_sprite = len(sprite[0])
    columnas_pantalla = ancho_ventana // 2 

    for fila_index, fila in enumerate(sprite):
        for col_index in range(columnas_pantalla):
            numero_color = fila[col_index % ancho_sprite] 
            if numero_color != 0:
                y = pos_y + fila_index
                x = col_index * 2
                if 0 <= y < alto_ventana - 1 and 0 <= x < ancho_ventana - 2:
                    try:
                        pantalla.attron(curses.color_pair(numero_color))
                        pantalla.addstr(y, x, "██")
                        pantalla.attroff(curses.color_pair(numero_color))
                    except:
                        pass

#FUNCION PARA IMPORTAR LAS PREGUNTAS DEL MODULO PREGUNTAS Y MOSTRARLAS EN ORDEN DE LOS TEMAS
def mostrar_pantalla_pregunta(pantalla, datos_pregunta):
    pantalla.clear()
    pantalla.border()

    pantalla.addstr(3, 5, "--- Sonic Kinetic Hunter ---", curses.A_BOLD)
    pantalla.addstr(5, 5, datos_pregunta["texto"])

    opciones_letras = ["A", "B", "C"]
    for i, texto_opcion in enumerate(datos_pregunta["opciones"]):
        pantalla.addstr(8 + i, 7, f"{opciones_letras[i]}) {texto_opcion}")

    pantalla.addstr(12, 5, "Elige tu respuesta: (A, B, C): ")
    pantalla.refresh()

    respuesta_pendiente = True
    es_correcta = False

    while respuesta_pendiente:
        tecla_presionada = pantalla.getch()
        if tecla_presionada != -1:
            letra = chr(tecla_presionada).upper()
            if letra in opciones_letras:
                letra_elegida = opciones_letras.index(letra)
                es_correcta = (letra_elegida == datos_pregunta["correcta"])
                respuesta_pendiente = False
        
    return es_correcta

#FUNCION Y ESTRUCTURAS DE CONTROL (IF) PARA PODER IMPORTAR LOS CALCULOS FISICOS
#DEL MODULO FISICA:PY Y PODER MOSTRAR EJEMPLOS PRACTICOS DE FORMA ALEATORIA 
#EN CADA EJECUCION

def mostrar_ejemplo(pantalla, numero_nivel):
    pantalla.clear()
    pantalla.border()
    alto, ancho = pantalla.getmaxyx()

    numeror1 = random.randint(10, 40)
    numeror2 = random.randint(2, 6)

    if numero_nivel < 3:
        resultado_calculo = fisica.calcular_peso(numeror1)
        ejemplo = f"Ejemplo: Si la masa es {numeror1}kg, el Peso es: {resultado_calculo:.2f} Newtons."
    elif numero_nivel < 6:
        resultado_calculo = fisica.calcular_velocidad_mru(numeror1 * 5, numeror2)
        ejemplo = f"Ejemplo: Al recorrer {numeror1*5}m en {numeror2}s, La velocidad es: {resultado_calculo:.2f} m/s."
    elif numero_nivel < 9:
        resultado_calculo = fisica.calcular_fuerza_neta(numeror1, numeror2)
        ejemplo = f"Ejemplo: Para acelerar {numeror1}kg a {numeror2}m/s², la fuerza es: {resultado_calculo:.2f}N."
    else:
        resultado_calculo = fisica.calcular_voltaje_ohm(numeror2, numeror1)
        ejemplo = f"Ejemplo: Con {numeror2}A y {numeror1} ohms, el voltaje es: {resultado_calculo:.2f}V."


    #ESTOS ATRIBUTOS DE LA VARIABLE PANTALLA SON PARA MOSTRAR TEXTO, PONER DELAY 
    # ENTRE CADA UNO LIMPIAR PANTALLA Y CAPTURAS LA TECLA PRESIONADA
    pantalla.addstr(alto//2 - 1, (ancho - 25)//2, "Respuesta correcta :D", curses.A_BOLD)
    pantalla.addstr(alto//2 + 1, (ancho - len(ejemplo))//2, ejemplo)
    pantalla.addstr(alto - 4, 5, "Presiona una tecla para seguir jugando ^_^...")
    curses.flushinp()
    pantalla.nodelay(0)
    pantalla.getch()
    pantalla.nodelay(1)


#LA FUNCION DEL JUEGO PRINCIPAL; ES LA QUE VA MANDAR A LLAMAR LO QUE YA HEMOS DEFINIDO ANTERIORMENTE Y ACOMODARLO EN LA PANTALLA PRINCIPAL
#DE LA EJECUCION DEL PROGRAMA, ASI COMO AQUI MISMO HACER ALGUNOS CALCULOS A TRAVES DE LAS CONSTANTES
#QUE DEFINIMOS MAS ARRIBA EN EL CODIGO
#Y TAMBIEN SE ESTABLECE QUE LA POSICION DEL RING SEA ALEATORIA POR EL MAPA

def juego_principal(pantalla):
    curses.curs_set(0)
    pantalla.nodelay(1)
    colores.setup_colores()

    alto_sonic, ancho_sonic = calcular_tamano(diseno.sprite_1)
    alto_anillo, ancho_anillo = calcular_tamano(ring.sprite_1)

    alto_ventana, ancho_ventana = pantalla.getmaxyx()
    inicio_fondo = alto_ventana - len(fondo.sprite_1)

    # LA POSICION DONDE AL INICIAR APARECEN POR PRIMERA VEZ TANTO EL PERSONAJE COMO LA COLISION A TOCAR
    sonic_x = 10
    sonic_y = inicio_fondo - alto_sonic
    
    vidas_restantes = MAX_VIDAS
    puntaje_jugador = 0
    pregunta_actual = 0
    animacion_anillo = 0
    contador = 0

    objetivo_x = random.randint(20, ancho_ventana - 20)
    objetivo_y = inicio_fondo - alto_anillo

    ##EN ESTE CICLO A RAIZ DE LAS CONSTANTES PARA MANEJAR CUANTO DURA EL PROGRAMA ASI COMO LIMPIARLA Y ESTABLECER UN BORDE Y EVITAR BUGS
    while pregunta_actual < TOTAL_PREGUNTAS and vidas_restantes > 0:
        pantalla.erase() 
        pantalla.border()
        
        #MANTENEMOS LAS VARIABLES DE FORMA ACTUALIZADA AUNQUE LA PANTALLA PUEDA CAMBIAR DE TAMAÑO CON LA FUNCION PANTALLA.GETMAXYX
        alto_ventana, ancho_ventana = pantalla.getmaxyx()
        inicio_fondo = alto_ventana - len(fondo.sprite_1)
        sonic_y = inicio_fondo - alto_sonic
        objetivo_y = inicio_fondo - alto_anillo

        #ESTA SE USA PARA PODER MOSTRAR EL PEQUEÑO HUD EN LA ESQUINA SUPERIOR IZQUIERDA DONDE SE MUESTRA INFORMACION DEL JUEGO
        info = f"Vidas: {vidas_restantes}/{MAX_VIDAS} | Puntos: {puntaje_jugador}  | Pregunta: {pregunta_actual + 1}/{TOTAL_PREGUNTAS}"
        pantalla.addstr(1, 2, info, curses.A_REVERSE)

        inicio_fondo_fondo = alto_ventana - len(fondo_del_fondo.sprite_1)
        
        color_cielo = 0
        for color in fondo_del_fondo.sprite_1[0]:
            if color != 0:
                color_cielo = color
                break
        
        if color_cielo != 0:
            ancho_cielo = ancho_ventana - 4
            if ancho_cielo > 0:
                fila_cielo = "█" * ancho_cielo
                pantalla.attron(curses.color_pair(color_cielo))
                for y_cielo in range(2, inicio_fondo_fondo):
                    try:
                        pantalla.addstr(y_cielo, 2, fila_cielo)
                    except:
                        pass
                pantalla.attroff(curses.color_pair(color_cielo))

        dibujar_repetido(pantalla, fondo_del_fondo.sprite_1, inicio_fondo_fondo, alto_ventana, ancho_ventana)
        
        dibujar_repetido(pantalla, fondo.sprite_1, inicio_fondo, alto_ventana, ancho_ventana)

        if animacion_anillo == 0:
            sprite_actual_anillo = ring.sprite_1
        else:
            sprite_actual_anillo = ring.sprite_2

        dibujar_figura(pantalla, sprite_actual_anillo, objetivo_y, objetivo_x, alto_ventana, ancho_ventana)
        dibujar_figura(pantalla, diseno.sprite_1, sonic_y, sonic_x, alto_ventana, ancho_ventana)

        pantalla.refresh()

        # ESTABLECER LA COLISION Y AL HACERLA LANZAR LA PREGUNTA
        if (sonic_x < objetivo_x + ancho_anillo and
            sonic_x + ancho_sonic > objetivo_x and
            sonic_y < objetivo_y + alto_anillo and
            sonic_y + alto_sonic > objetivo_y):

            datos_pregunta = preguntas.lista_preguntas[pregunta_actual]
            es_correcta = mostrar_pantalla_pregunta(pantalla, datos_pregunta)

            if es_correcta:
                #ESTABLECEMOS UN ACUMULAOR CON EL VALOR DE NUESTRA CONSTANTE
                puntaje_jugador += PUNTOS_POR_ACIERTO
                mostrar_ejemplo(pantalla, pregunta_actual)
                pregunta_actual += 1
                
                #FIJAMOS EL ANILLO EN EL SUELO PERO PUDIENDOSE MOVER LIBRE POR EL EJE X
                objetivo_x = random.randint(10, ancho_ventana - 20)

            else:
                vidas_restantes -= 1
                pantalla.clear()
                pantalla.addstr(alto_ventana//2, (ancho_ventana-30)//2, f"Error, perdiste una vida D: te quedan {vidas_restantes}")
                pantalla.refresh()
                time.sleep(2)

            sonic_x = 10 # Sonic regresa a la izquierda tras la pregunta
            pantalla.nodelay(1)

        contador += 1
        if contador % 15 == 0:
            if animacion_anillo == 0:
                animacion_anillo = 1
            else:
                animacion_anillo = 0

        tecla = pantalla.getch()
        
        #SOLO ESTABLECEMOS MOVIMIENTO LINEAL / HORIZONTAL EN EL JUEGO
        if tecla == ord("a") and sonic_x > 2:
            sonic_x -= 2
        elif tecla == ord("d") and sonic_x < ancho_ventana - ancho_sonic - 2:
            sonic_x += 2

        time.sleep(0.04)

    # Pantalla final
    pantalla.clear()
    pantalla.border()
    
    if vidas_restantes > 0:
        texto_final = "FELICIDADES GANASTE EL JUEGOOOO AAAAA AWJIF"
    else:
        texto_final = "Buuuu Perdiste tonoto jasjdaihfi"
    
    # Lógica de calificación basada en puntaje acumulado
    if puntaje_jugador >= (TOTAL_PREGUNTAS * PUNTOS_POR_ACIERTO * 0.8):
        cal_obtenida = "Aprobado con calificacion destacada"
    elif puntaje_jugador >= (TOTAL_PREGUNTAS * PUNTOS_POR_ACIERTO * 0.6):
        cal_obtenida = "Aprobado"
    else:
        cal_obtenida = "Reprobado"

    pantalla.addstr(10, 5, texto_final, curses.A_BOLD)
    pantalla.addstr(12, 5, f"Puntaje total: {puntaje_jugador}")
    pantalla.addstr(14, 5, cal_obtenida, curses.A_BOLD)
    pantalla.refresh()
    time.sleep(5)

if __name__ == "__main__":
    curses.wrapper(juego_principal)