""" Unos niños quieren ir al Parque Warner de Madrid y hoy tienen un descuento especial. Hemos creado un algoritmo donde
tienes que poner el precio actual de las entradas y el numero de niños que van.
El Algoritmo te da el importe descontado y el precio que la familia tiene que pagar """

#Aqui esta el input del algoritmo donde debes añadir el numero de niños y el precio actual de la entrada por niño
niños=int(input('cuantos niños van a ir al Parque Warner Madrid '))
precio=float(input('El precio normal del Parque Warner Madrid es: '))
# Este es el programa donde va mirando los posibles descuentos dependiendo del numero de niños que van al parque
# Te devuelve el precio total que tiene que pagar la familia por los niños que tienen
def Des_PWM(niños,precio):
    if niños==2:
        return (precio*niños)-((precio*niños)*0.1)
    elif niños==3:
        return (precio*niños)-((precio*niños)*0.15)
    elif niños==4:
        return (precio*niños)-((precio*niños)*0.18)
    elif niños>4:
        return (precio*niños)-(precio*niños)*(0.18+((niños-4)*0.01))
    else:
        return precio*niños
# programa que calcula el descuento que se hace a las entradas
def Des_imp(niños,precio):
    if niños==2:
        return ((precio*niños)*0.1)
    elif niños==3:
        return ((precio*niños)*0.15)
    elif niños==4:
        return ((precio*niños)*0.18)
    elif niños>4:
        return (precio*niños)*(0.18+((niños-4)*0.01))
    else:
        return 0
#precio por niño es n
n=precio*niños

#Primer output del Algoritmo: en este print te devuelve el descuento y el valor sin descontar respectivamente.
print('Lo que se ha descontado es de ',Des_imp(niños,precio),"€", ' de',n,'€')
#Segundo output del Algoritmo: en este print te devuelve lo que la familia tiene que pagar en total con el descuento ya realizado.
print('El precio con el descuento de la entrada es de ',Des_PWM(niños,precio),'€')