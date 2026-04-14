#Comentario python con ¨#¨ inicial
"""

Comentario de varias lineas con comillas triples

"""
#Para comentar todo un bloque de codigo, se puede seleccionar el bloque y presionar Ctrl + K + C para comentar todo el bloque, y Ctrl + K + U para descomentar todo el bloque.

#Entrada/Salida de datos
#Dato = cualquier cosa que escribo
#tipo de dato = numero, texto, booleano, etc

#print("Hola Mundo") #imprime un mensaje en pantalla
#print(45) #imprime un numero en pantalla

#Variables y asignacion de valores
#name = "Luis"
#name2 = "Maria"

# nombre = input("ingrese su nombre: ") #input es una funcion que permite al usuario ingresar datos por teclado
# print("Hola " + nombre) #concatenacion de cadenas de texto

# edad = int(input("ingrese su edad: "))
# print(edad) #imprime un mensaje con la edad ingresada por el usuario
# #print("Tu edad es: " + str(edad)) #str() convierte un numero a texto para poder concatenarlo con el mensaje
# print(type(edad)) #imprime el tipo de dato de la variable edad

# #float = numero con decimales
# pi = 3.14
# print(pi)   

# #range = rango de numeros
# print(*range(16)) #imprime los numeros del 0 al 15
# print(*range(0,21,5)) #imprime los numeros del 0 al 20 con un paso de 5
# el * antes de range es para desempaquetar la lista de numeros que genera range y imprimirlos separados por espacio

# CONDICIONALES
# if = si / else = sino / elif = sino si / and = y / or = o / not = no

#nota = int(input("ingrese su nota: "))
#if nota >= 9:
#    print("Supera")
#elif nota >= 7:
#    print("Regular")
#else:
#    print("Reprobado")

#x=5
#print(x > 3 and x < 10) #true
#y=1
#print(y > 3 and y < 10) #false
#z=5
#print(z < 3 or z < 10) #true

# ingreso de notas con validacion de datos
#nota = int(input("ingrese su nota: "))
#if nota < 0 or nota > 10:
#    print("Nota invalida, ingresar una valida del 0 al 10")
#else:
#    if nota >= 9:
#        print("Supera")
#    elif nota >= 7:
#        print("Regular")
#    else:
#        print("Reprobado")

# Estructuras de control repetitivo
# while = mientras / for = para

# for i in range(11):
#     nota = input("ingrese su nota: ") #no coloco int() para permitir que el usuario ingrese la palabra salir y terminar el ciclo
    
#     if nota == "salir":
#         break   #termina el ciclo si el usuario ingresa la palabra salir
#     nota_final = int(nota) #convierte la nota ingresada a numero entero para poder compararla con los valores de las condiciones
#     if nota_final >= 0 and nota_final <= 10:
#         if nota_final >= 9:
#             print("Supera")
#         elif nota_final >= 7:
#             print("Regular")
#         else:
#             print("Reprobado")
#     else:
#         print("Nota invalida, ingresar una valida del 0 al 10")

# while True: #ciclo infinito que se repetira hasta que el usuario ingrese la palabra salir para terminarlo
#     nota = input("ingrese su nota: ")
    
#     if nota == "salir":
#         break   #termina el ciclo
    
#     nota_final = int(nota)
    
#     if nota_final >= 0 and nota_final <= 10:
#         if nota_final >= 9:
#             print("Supera")
#         elif nota_final >= 7:
#             print("Regular")
#         else:
#             print("Reprobado")
#     else:
#         print("Nota invalida, ingresar una valida del 0 al 10")

# i=0 #inicializacion de la variable i con el valor 0, esta variable se utilizara para controlar el ciclo while y evitar un ciclo infinito
# while i < 5: #condicion del ciclo while, el ciclo se repetira mientras el valor de i sea menor a 5, si i es igual o mayor a 5, el ciclo terminara
#     i = i + 1 #incremento de la variable i para evitar un ciclo infinito, si no se incrementa i, el valor de i siempre sera 0 y la condicion i < 5 siempre sera verdadera, lo que causaria un ciclo infinito
#     print(i)

# f string
#nombre = "Luis"
#edad = 25
#print(f"Hola {nombre}, tu edad es {edad}") #f string permite insertar variables dentro de una cadena de texto utilizando llaves {} para indicar donde se deben insertar las variables, y la letra f antes de las comillas para indicar que se trata de un f string

# Estructura de datos
# listas - mutable, ordenada, permite elementos duplicados
#frutas = ["manzana", "banana", "uva"]
#print(frutas) #imprime la lista de frutas
#print(frutas[0]) #imprime el primer elemento de la lista
#frutas[0] = "pera" #modifica el primer elemento de la lista
#print(frutas) #imprime la lista actualizada
#frutas.append("naranja") #agrega un nuevo elemento al final de la lista
#frutas.remove("banana") #elimina el elemento "banana" de la lista
#frutas.sort(key=len) #ordena la lista de frutas por la longitud de cada elemento

# tuplas - inmutable, ordenada, permite elementos duplicados
#coordenadas = (10, 20)
#print(coordenadas) #imprime la tupla de coordenadas
# coordenadas[0] = 15 #no se puede modificar una tupla, esto causaria un error
#coordenada_1, coordenada_2 = coordenadas #desempaquetado de la tupla, asigna el primer elemento de la tupla a la variable coordenada_1 y el segundo elemento a la variable coordenada_2
#print(coordenada_1) #imprime el valor de la variable coordenada_1

# diccionarios - mutable, no ordenada, no permite elementos duplicados, se accede a los elementos/valores mediante claves
#persona = {
#    "nombre": "Luis",
#    "edad": 25,
#    "ciudad": "Madrid"
#    }
#print(persona) #imprime el diccionario de persona
#print(persona["nombre"]) #imprime el valor de la clave "nombre"
#persona["edad"] = 26 #modifica el valor de la clave "edad"
#print(persona) #imprime el diccionario actualizado
#print(persona.keys()) #imprime las claves del diccionario
#print(persona.values()) #imprime los valores del diccionario
#print(persona.items()) #imprime los pares de claves y valores del diccionario
# No es como un archivo json, es un diccionario de python, aunque tiene una sintaxis similar a un objeto json, no es lo mismo, un diccionario de python es una estructura de datos que se utiliza para almacenar pares de claves y valores, mientras que un objeto json es una representación de datos en formato texto que se utiliza para intercambiar datos entre aplicaciones.

#for i in persona:
#    print(i) #imprime las claves del diccionario
#    print(persona[i]) #imprime los valores del diccionario utilizando las claves para acceder a ellos

# Funciones
#def saludo(nombre):
#    print(f"Hola, {nombre}, bienvenido a mi programa")
    # o se puede usar un return para devolver un valor en lugar de imprimirlo, por ejemplo:
    # def saludo(nombre):
    #     return f"Hola, {nombre}, bienvenido a mi programa"
    # print(saludo("Luis")) #imprime el valor devuelto por la funcion saludo
#saludo("Luis") #llama a la funcion saludo para ejecutar el codigo que contiene

#from Calculadora.operaciones import sumar, restar, multiplicar, dividir #importa las funciones sumar, restar, multiplicar y dividir del modulo operaciones que se encuentra en la carpeta Calculadora