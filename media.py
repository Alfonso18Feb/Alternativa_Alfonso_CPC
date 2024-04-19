""" El profesor de Algebra necesita un programa que le haga media de los cuatro parciales de sus alumnos y si el alumno necesita refuerzo o esta bien.
Este algoritmo seleciona las notas de los cuatro parciales del alumno y te da una evaluacion sobre que bien esta haciendo el alumno en Algebra.
 """



# immporto os y time para hacer este programa mas ascesible para los profesor de Algebra
import os
import time




# primero manda un mensaje por consola para que sepa cual es el rango de las notas que tiene que poner
print('las notas deben de estar entre 0 y 20')
#El input del algoritmo pide las notas de los cutro parciales de este alumno
x=float(input('nota parcial 1 :'))
y=float(input('nota parcial 2 :'))
z=float(input('nota parcial 3 :'))
t=float(input('nota parcial 4 :'))


#Esta es la funcion del algoritmo que calcula la media de los valores ya puestos en el input
def media(x,y,z,t):
    return((x+y+z+t)/4)

os.system ("cls")
time.sleep(0.2)


# a es el valor de la media del alumno en los cuatro parciales
a=media(x,y,z,t)

#Esta funcion comprobar en el algoritmo pone la evaluacion que le damos al alumno dependiendo de su media
#calculada anteriormente
def comprobar(a):
    
    if a>=15:
        return "con talento"
    elif a<15 and a>=12:
        return "con capacidad"
    else:
        return "que debe reorientarse"

""" la salido o output del algoritmo """
#Primer output: la media de este alumno elegido
print("media aritmetica nota de alumnos:",media(x,y,z,t))
time.sleep(5)
#Segundo output: la evaluacion dada ha este alumno
print(" Su evaluacion es un Alumno ",comprobar(a))