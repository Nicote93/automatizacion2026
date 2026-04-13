def sumar(a, b):
    return a + b #para devolver el resultado de la suma en lugar de imprimirlo

def restar(a, b):
    return a - b #para devolver el resultado de la resta en lugar de imprimirlo

def multiplicar(a, b):
    return a * b #para devolver el resultado de la multiplicación en lugar de imprimirlo

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Resultado: Error - No se puede dividir por cero (0)")
    except ValueError:
        print("Resultado: Error - Valor invalido, se esperaba un numero")

# if y else no permitiria que ocurra el error al dividir por cero, pero el manejo de excepciones con try y except permite manejar el error de manera mas elegante y evitar que el programa se detenga abruptamente, ademas de permitir mostrar un mensaje de error personalizado al usuario.

# Controladores de errores
# zero division error = error de division por cero
# value error = error de valor invalido
# key error = error de clave no encontrada en un diccionario
# index error = error de indice fuera de rango en una lista o tupla
# type error = error de tipo de dato invalido, por ejemplo al intentar sumar un numero con una cadena de texto
