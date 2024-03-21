"""
Equipo 10
Martha Mendoza Alfaro A01284654
Mariel Perez Ferrusquía A00832811
"""

from random import randrange, choice
from turtle import *
from freegames import square, vector
from random import randrange, choice

food = vector(50, 10)
snake = [vector(10, 0)]
aim = vector(0, -10)
#Lista random de colores
colores = ["navy", "green", "purple", "pink", "black", "yellow", "blue", "DarkOrange", "cyan", "magenta"]
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
    head.move(aim) #mueve
    
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
        
        #Borra la comida
        foodCircle.clear()
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

    snake.append(head) #añade

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        #elimina la comida
        foodCircle.clear()
        # elige un color random para food y snake
        colorFood = choice(colores)
        colorSnake = choice(colores)
        # guarda nuevo color
        snakeSquare.pencolor(colorSnake)
        foodCircle.pencolor(colorFood)
        
    else:
        snake.pop(0) #elimina 0 de la lista, simula el movimiento el 0 es el primer vector dentro de la lista snake

    clear()

    #aqui dibuja el snake
    for body in snake:
        color2 = snakeSquare.pencolor()
        square(body.x, body.y, 9, color2)

    # aqui dibuja a la comida
    foodCircle.up()
    xCircle = food.x + 4.5
    yCircle = food.y + 4.5
    foodCircle.setpos(xCircle, yCircle)
    #mantener color cada movement
    color = foodCircle.pencolor()
    foodCircle.dot(9, color)

    #actualiza la pantalla lo que tiene el buffer
    update()
    ontimer(move, 100) #aqui se cambia la rapidez

#Turtle para comida
foodCircle = Turtle(visible=False)
#Color inicializado, empieza en morado
foodCircle.pencolor("purple")

#Turtle para snake
snakeSquare = Turtle(visible=False)
#Color inicializado, empieza en negro
snakeSquare.pencolor("black")


   
#Dimensiones de la ventana, ancho, alto, esq. superior izquierda en x, esq. superior izquierda en y
setup(420, 420, 370, 0)
writer = Turtle(visible= False)
info_alumnos()

#Cambiar titulo de pantalla
screener = Turtle(visible= False)
screener.screen.title("Martha Mendoza y Mariel Pérez")

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