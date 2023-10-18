'''
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero
 e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''
nombre = input("Como te llamas? ")
n = input(f"{nombre}, por favor introduce un numero entero: ")
print ((nombre + "\n") * int(n))

'''

Escribir un programa que pregunte el nombre completo del usuario en la consola 
y después muestre por pantalla el nombre completo del usuario tres veces,
una con todas las letras minúsculas, otra con todas las letras mayúsculas
y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

'''

name =  input("Como te llamas? ")
print(name.lower())
print(name.upper())
print(name.title())

'''
## Ejercicio

Escribir un programa que pregunte el nombre del usuario en la consola
y después de que el usuario lo introduzca muestre por pantalla
`<NOMBRE> tiene <n> letras`, donde `<NOMBRE>` es el nombre de usuario en mayúsculas
y `<n>` es el número de letras que tienen el nombre.
'''

nombre = input("Como te llamas? ")
print(nombre.upper() +  "tiene" +  str(len(nombre)) +  "letras.")