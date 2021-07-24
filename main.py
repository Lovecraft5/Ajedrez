################################################################################
##
## JUEGO DE AJEDREZ
##
## Autor: Eduardo Molina
##
## Este programa va a imitar un videojuego de ajedrez
## Tablero -> casillas 64 -> cordenadas y sus estados de ocupación
## Piezas->estado->valor->cordenadas->movimiento/comer/morir->tipo de pieza
## Jugador->color->tiempo->puntos
## Main Prgrama del juego
################################################################################

# Definir funcion que imprime menu
def imprimir_menu():
    print("Bienvenido a mi juego de ajedrez")
    modo_de_juego = input(
        """¿Que quieres hacer?
        Pulsa 1 para jugar
        Pulsa 0 para salir""")
    if modo_de_juego == 1:
        print("Vamos a jugar!")
    elif 0:
        print("Adios!")
    return modo_de_juego

# Bucle principal del juego
def main():
    while imprimir_menu():


        # Inicio del programa
main()
