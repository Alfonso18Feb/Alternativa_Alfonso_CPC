
""" UNTEL una empresa muy conocida de microprocesadores tiene unos descuentos especiales por el "black friday" que son los siguientes:

Primer descuento es por el Tipo de cliente que eres:
si COMMAQ 2% de descuento
si BEL 1% de descuento

Segundo descuento es por el numero de microprocesadores comprados:
si son entre 10000 y 20000 es del 10%
sino un 15 % si la cantidad se encuentra entre 20001 y 40000 
sino un 20 % para más de 40000 microprocesadores

Este algoritmo te calcula el descueto del precio y el precio sin descontar. Tambien el precio total descontado,
 """



# Te imprime primero opciones del tipo_cliente para elegir  si no eres ninguna saltas
print('tipo de clientes: \nCOMMAQ\nBEL ')
# el input del Algoritmo tiene variables de Tipo_cliente nºcomponentes y el precio_micro actual sin ningun descuento
Tipo_cliente=str(input('que tipo ed cliente eres: ').upper())
nºcomponentes=int(input('cuantos microprocesadores quieres: '))
precio_micro=float(input('el precio del microprocesador es de: '))

#Este metodo del algoritmo el programa va comprobando los descuentos y los aplica al precio 
def UNTEL(Tipo_cliente,nºcomponentes,precio_micro):
    if Tipo_cliente=='COMMAQ':
        if nºcomponentes>=10000 and nºcomponentes<=20000:
            return (nºcomponentes*precio_micro)-(0.12*precio_micro*nºcomponentes)
        elif nºcomponentes>=20001 and nºcomponentes<=40000:
            return (nºcomponentes*precio_micro)-(0.17*precio_micro*nºcomponentes)
        elif nºcomponentes>40000:
            return (precio_micro*nºcomponentes)-(0.22*precio_micro*nºcomponentes)
        else:
            return (precio_micro*nºcomponentes)-(0.02*precio_micro*nºcomponentes)

    elif Tipo_cliente=='BEL':
        if nºcomponentes>=10000 and nºcomponentes<=20000:
            return (precio_micro*nºcomponentes)-(0.11*precio_micro*nºcomponentes)
        elif nºcomponentes>=20001 and nºcomponentes<=40000:
            return (precio_micro*nºcomponentes)-(0.16*precio_micro*nºcomponentes)
        elif nºcomponentes>40000:
            return (precio_micro*nºcomponentes)-(nºcomponentes*0.21*precio_micro)
        else:
            return (precio_micro*nºcomponentes)-(nºcomponentes*0.01*precio_micro)
    else:
        if nºcomponentes>=10000 and nºcomponentes<=20000:
            return (precio_micro*nºcomponentes)-(0.10*precio_micro*nºcomponentes)
        elif nºcomponentes>=20001 and nºcomponentes<=40000:
            return (nºcomponentes*precio_micro)-(nºcomponentes*0.15*precio_micro)
        elif nºcomponentes>40000:
            return (precio_micro*nºcomponentes)-(0.20*precio_micro*nºcomponentes)
        else:
            return precio_micro*nºcomponentes
        
#Este metodo del algoritmo solo calcula el descuento que se tiene que aplicar luego en el precio
def UNTEL_desc(Tipo_cliente,nºcomponentes,precio_micro):
    if Tipo_cliente=='COMMAQ':
        if nºcomponentes>=10000 and nºcomponentes<=20000:
            return (0.12*precio_micro*nºcomponentes)
        elif nºcomponentes>=20001 and nºcomponentes<=40000:
            return (0.17*precio_micro*nºcomponentes)
        elif nºcomponentes>40000:
            return (0.22*precio_micro*nºcomponentes)
        else:
            return (0.02*precio_micro*nºcomponentes)

    elif Tipo_cliente=='BEL':
        if nºcomponentes>=10000 and nºcomponentes<=20000:
            return (0.11*precio_micro*nºcomponentes)
        elif nºcomponentes>=20001 and nºcomponentes<=40000:
            return (0.16*precio_micro*nºcomponentes)
        elif nºcomponentes>40000:
            return (nºcomponentes*0.21*precio_micro)
        else:
            return (nºcomponentes*0.01*precio_micro)
    else:
        if nºcomponentes>=10000 and nºcomponentes<=20000:
            return (0.10*precio_micro*nºcomponentes)
        elif nºcomponentes>=20001 and nºcomponentes<=40000:
            return (nºcomponentes*0.15*precio_micro)
        elif nºcomponentes>40000:
            return (0.20*precio_micro*nºcomponentes)
        else:
            return 0
# n aqui seria el precio sin descontar
n=precio_micro*nºcomponentes
# Primer output del Algoritmo: te imprime el precio que se debe descontar y el precio sin descontar
print('el descuento del microprocesador es de',UNTEL_desc(Tipo_cliente,nºcomponentes,precio_micro),'€',' el precio sin descunto es',n)
# Segundo output del Algoritmo: Te imprime el precio descontado
print('el precio del microprocesadores descontados es: ',UNTEL(Tipo_cliente,nºcomponentes,precio_micro),'€')
