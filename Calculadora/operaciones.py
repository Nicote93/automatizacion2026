def sumar( a , b ):
    return a + b 

def restar( a , b ):
    return a - b 

def multiplicar( a , b ):
    return a * b 

def dividir( a , b ):
    try:
         return a / b 
    except ZeroDivisionError:
        print("No se puede dividir por cero")

# if y else no permitiria que ocurra el error al dividir por cero, pero el manejo de excepciones con try y except permite manejar el error de manera mas elegante y evitar que el programa se detenga abruptamente, ademas de permitir mostrar un mensaje de error personalizado al usuario.

# Controladores de errores
# zero division error = error de division por cero
# value error = error de valor invalido
# key error = error de clave no encontrada en un diccionario
# index error = error de indice fuera de rango en una lista o tupla
# type error = error de tipo de dato invalido, por ejemplo al intentar sumar un numero con una cadena de texto
