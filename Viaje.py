""" El profesor de progrmacion planea un viaje universitario por Europa para asi poder ver las necesidades de los Europeos.
Esto nos dara ideas para poder programar programas que ayuden a la sociedad Europea.

Pero el coste del trayecto depende del numero de alumnos que vayan:
si hay menos que 25 entonces cuesta 67.30€ por alumno
si hay mas de 25 alumnos los que van solo cuesta 61€ por alumno

El precio de la comida sera 3.50 por alumno siempre

Mientras, el precio del alojamiento seran de:
si hay menos de 30 alumnos precio 4.75€ por dias por alumnos
si esta entre 31 y 35 alumnos el precio sera de 4€ por dias por alumnos
si hay mas de 35 el precio baja a solo 3.50€ por dias por alumnos

Entonces, creamos un algoritmo que te devuelve el precio que tiene que pagar cada alumno y el precio total del viaje.
Que depende de las variables que ponemos en el input
"""


#EN el input  del algoritmo se debe de poner el numero de alumnos y dias que vamos ha estar viajando
alumnos=int(input('los numeros de alumnos: '))
dias=int(input('cuantos dias van de viaje: '))
#Este metodo calcula el precio del trayecto
def trayecto(alumnos):
    if alumnos<=25:
        return  67.30*alumnos
    elif alumnos>25:
        return 61.00*alumnos
#dejamos constante el precio de la comida
precio_c=3.50
#devuelve el precio de la comida por alumno
def comida(precio_c,alumnos):
    return precio_c*alumnos
#Este metodo del algoritmo devuelve el precio para alojarse en un hotel por dias por alumno
def alojamiento(dias,alumnos):
    if alumnos<30:
        return 4.75*dias*alumnos
    elif alumnos>=31 and alumnos<=35:
        return 4.00*dias*alumnos
    elif alumnos>35:
        return 3.50*dias*alumnos
#estas son las variables del precio
a=trayecto(alumnos)
b=alojamiento(dias,alumnos)
c=comida(precio_c,alumnos)

#print(a)
#print(b)
#print(c)

#Este metodo es el precio que tiene que pagar cada alumno
def suma_p(a,b,c,alumnos):
    return (a+b+c)/alumnos
#Este metodo es el precio total del viaje
def suma(a,b,c):
    return a+b+c
#El primer output:devuelve el precio por alumno
print('el precio de coste por alumno',suma_p(a,b,c,alumnos),'€')
#el segundo output del algoritmo: es el precio total
print('el coste global del viaje',suma(a,b,c),'€')
