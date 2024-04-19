""" El problema que tenemos que resolver es que tenemos dos numeros que los
ñades en el input del algoritmo y tenemos que ordenar de menor a mayor los valores
a, a+b, b y a*b. Para conseguir esto primero hice funcion suma y multiplicacion.
Para luego en la funcion clasificar, clasificarlo de menor a mayor."""

#el input del algoritmo es elegir dos numeros enteros multiplicarlos y sumarlos para luego comparar
a=int(input('el valor de a es: '))
b=int(input('el valor de b es: '))
""" Las funcion sumar y multiplicar es un input donde suma y multiplica los valores elegidos
para luego compararos """
def multiplicar(a,b):
    return a*b
def sumar(a,b):
    return a+b
# valores de la suma y mutiplicacion
l=multiplicar(a,b)
n=sumar(a,b)
#El programa principal que clasifica los valores ya eplicados arriba para clasificar de menor a mayor
def clasificar(a,b,l,n):
    if a<b and b<n and n<l:
        return f"{a}<{b}<{n}<{l}"
    elif a<b and b<l and l<n:
        return f"{a}<{b}<{l}<{n}"
    elif a<l and l<b and b<n:
        return f"{a}<{l}<{b}<{n}"
    elif a<l and l<n and n<b:
        return f"{a}<{l}<{n}<{b}"
    elif a<n and n<l and l<b:
        return f"{a}<{n}<{l}<{b}"
    elif a<n and n<b and b<l:
        return f"{a}<{n}<{b}<{l}"
    elif b<a and a<l and l<n:
        return f"{b}<{a}<{l}<{n}"
    elif b<a and a<n and n<l:
        return f"{b}<{a}<{n}<{l}"
    elif b<l and l<a and a<n:
        return f"{b}<{l}<{a}<{n}"
    elif b<l and l<n and n<a:
        return f"{b}<{l}<{n}<{a}"
    elif b<n and n<l and l<a:
        return f"{b}<{n}<{l}<{a}"
    elif b<n and n<a and a<l:
        return f"{b}<{n}<{a}<{l}"
    elif l<a and a<b and b<n:
        return f"{l}<{a}<{b}<{n}"
    elif l<a and a<n and n<b:
        return f"{l}<{a}<{n}<{b}"
    elif l<b and b<a and a<n:
        return f"{l}<{b}<{a}<{n}"
    elif l<b and b<n and n<a:
        return f"{l}<{b}<{n}<{a}"
    elif l<n and n<b and b<a:
        return f"{l}<{n}<{b}<{a}"
    elif l<n and n<a and a<b:
        return f"{l}<{n}<{a}<{b}"
    elif n<a and a<b and b<l:
        return f"{n}<{a}<{b}<{l}"
    elif n<a and a<l and l<b:
        return f"{n}<{a}<{l}<{b}"
    elif n<b and b<a and a<l:
        return f"{n}<{b}<{a}<{l}"
    elif n<b and b<l and l<a:
        return f"{n}<{b}<{l}<{a}"
    elif n<l and l<b and b<a:
        return f"{n}<{l}<{b}<{a}"
    elif n<l and l<a and a<b:
        return f"{n}<{l}<{a}<{b}"
    else:
        ValueError('numeros diferentes de a y b. si son iguales a y b no se pueden diferenciar cual es mayor')


s=clasificar(a,b,l,n)
#En el output te deja ver el resultado de la multiplicacion y suma de los dos numeros elegidos
print('la multiplicacion de a y b: ',l)
print("la suma de a y b :",n)
#Luego te da la clasificacion de menor a mayor de las operaciones y los dos numeros elegidos
print('el orden de menor a mayor:  ',s)
