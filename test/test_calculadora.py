import pytest
from calculadora import sumar, restar, multiplicar, dividir

#def test_sumar_positivos():
    #assert suma(2, 3) == 5 # assert es una palabra reservada de python que se utiliza para verificar si una condición es verdadera. Si la condición es falsa, se lanza una excepción AssertionError.

def test_sumar_negativos(numeros_negativos): # pytest inyecta el fixture numeros_negativos en esta función de prueba. El fixture devuelve una tupla con dos números negativos, que se asignan a las variables a y b. Luego, se llama a la función suma con estos dos números y se verifica que el resultado sea -12.
    a,b = numeros_negativos # desempaquetamos la tupla devuelta por el fixture numeros_negativos en las variables a y b
    assert sumar(a, b) == -12

#def test_sumar_mixtos(): # prueba con un número negativo y otro positivo
    #assert suma(-2, 3) == 1

# Para ejecutar las pruebas, se puede usar el comando pytest en la terminal. pytest buscará automáticamente los archivos que comienzan con test_ y ejecutará las funciones que comienzan con test_.
# Si uso pytest -v, se mostrará información detallada sobre cada prueba que se ejecuta, incluyendo el nombre de la prueba y si pasó o falló.