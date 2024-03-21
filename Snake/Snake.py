"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#Contador para los movimientos
contador = 0
#Lista de las posiciones disponibles
lista_mov_food = [vector(20,0), vector(-20,0), vector(0,20), vector(0,-20)]

#Funcion para desplegar los nombres del equipo
def info_alumnos():
    color('purple')
    writer.hideturtle()
    writer.up()
    writer.goto(0,190)
    writer.color('blue')
    writer.write('Martha Mendoza Alfaro A01284654', align = 'left', font = ('Century',10,'normal'))
    writer.goto(0,175)
    writer.color('pink')
    writer.write('Mariel Perez Ferrusquía A00832811', align = 'left', font = ('Century',10,'normal'))

def change(x, y):
    """Change snake direction.""" 
    aim.x = x
    aim.y = y
    

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    #Contador global 
    global contador
    #Sumar uno al contador cada vez que se detecte un cambio
    contador += 1
    head = snake[-1].copy()
    head.move(aim)
    
    #Verifica que el contador no se haya pasado de 5
    if contador > 9:
        #Asigna el movimiento a un punto de la lista
        movimiento = choice(lista_mov_food)
        #Crea una copia de la comida
        food_aux = food.copy()
        #Asigna el movimiento a la copia
        food_aux.move(movimiento)

        #Verifica que la copia no se encuentre fuera de los limites ni dentro de la serpiente. 
        if not inside(food_aux) or food_aux in snake:
            #Si no es valida, asigna una nueva posicion
            movimiento = choice(lista_mov_food)
            #Asigna el movimiento a la copia
            food_aux.move(movimiento)

        #Mueve la comida al movimiento de la lista seleccionado
        food.move(movimiento)
        #Reinicia el contador
        contador = 0
        #Actualiza la pagina
        update()

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)


    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    #Dibuja a la serpiente
    for body in snake:
        square(body.x, body.y, 9, 'black')
       
    square(food.x, food.y, 9, 'green')
    #Actualiza la pantalla
    update()
    #Cada tiempo manda a llamar a la funcion
    ontimer(move, 100)
   
   
#Dimensiones de la ventana, ancho, alto, esq. superior izquierda en x, esq. superior izquierda en y
setup(420, 420, 370, 0)
writer = Turtle(visible= False)
info_alumnos()
#Oculta el cursor
hideturtle()
tracer(False)
#Aceptar/escucha/guarda los eventos del teclado en una cola
listen()
#Funcion para llamar el teclado
#Lambda funcion anonima sin argumentos
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
#Llama a la funcion de move()
move()
#Llama a la funcion de done()
done()