## Actividad 4 - Memorama Evidencia de competencias
# SemanaTecTC1001S-101
# Autores
- Martha Mendoza Alfaro A01284654
- Mariel Perez Ferrusquía A00832811

# Funciones agregadas
def info()
- Despliega la información del equipo y el título
- Autor: Martha Mendoza
- Código:

```python
def info():
    writer.hideturtle()
    writer.up()
    writer.goto(-290, 270)
    writer.color('honeydew')
    writer.write('Martha Mendoza Alfaro A01284654', align='left', font=('Cascadia Mono', 14, 'normal'))
    writer.goto(-290, 250)
    writer.color('honeydew')
    writer.write('Mariel Perez Ferrusquía A00832811', align='left', font=('Cascadia Mono', 14, 'normal'))
    writer.goto(-150, 210)
    writer.color('honeydew')
    writer.write('\U0001F337\U0001F43BMemorama de Animales\U0001F43A\U0001F337', align='left', font=('Cascadia Mono', 20, 'normal'))

#Info de los alumnos
writer = Turtle(visible= False)
info()
```

def info_ganador
- Muestra mensaje de ganador cuando se encontraron todas las parejas del memorama
- Autor: Mariel Perez
- Código:

```python
def info_ganador():
    writer3.hideturtle()
    writer3.up()
    writer3.goto(160, -250)
    writer3.color('honeydew')
    writer3.write('¡Felicidades!', align='left', font=('Cascadia Mono', 18, 'normal'))

#Mensaje ganador
writer3 = Turtle(visible= False)
```

def info_taps()
- Muestra la cantidad de clicks que hizo el usuario hasta haber ganado
- Autor: Mariel Perez
- Código:

```python
def info_taps():
    writer2.clear()
    writer2.hideturtle()
    writer2.up()
    writer2.goto(160, 250)
    writer2.color('honeydew')
    writer2.write('Contador: ' + str(contador), align='left', font=('Cascadia Mono', 14, 'normal'))

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    #Contadores globales
    global contador, contador_casillas
    #Incrementa el valor en uno cada vez que se presiona una casilla
    contador+=1
    #Verifica que las casillas esten sin destapar
    if contador_casillas < 32:
        info_taps()
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        #Incrementa el valor en uno del contador que tiene registro de las casillas que han sido descubiertas
        contador_casillas+=1
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    
    #Verifica el punto en el que el juego se gana
    if contador_casillas == 32:
        info_ganador()

#Info de los clicks
writer2 = Turtle(visible= False)
info_taps()
```

Título de pantalla y fondo de pantalla
- Cambia el color de fondo de la pantalla y el título de la pantalla emergente
- Autor: Martha Mendoza
- Código:

```python
bgcolor("LightPink")

screener = Turtle(visible= False)
screener.screen.title("Martha Mendoza y Mariel Pérez")
```
![video](VideoSnake.gif)
