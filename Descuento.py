
""" Un comerciante que tiene unos productos pone un descuento especial por ser semana santa que
si gastas entre 100€ a 500€ hace un descuento de 5% y para gastos mayores de 500€ te descuenta un 8%.
El algoritmo que hemos hecho da los precio con su descuento respectivo """
# el input del algorittmo tenemos que añadir el precio gastado en la empresa
x=float(input('precio del producto: '))
# el programa del algoritmo va mirando los descuentos y los aplica al precio
def descontado(x):
    if x>=100 and x<500:
        return x-(x*0.05)
    elif x>=500:
        return x-(x*0.08)
    else:
        return x
# Este programa del algoritmo mientras tanto de devuelve el descuento que se va a eliminar al precio
def descuento(x):
    if x>=100 and x<500:
        return (x*0.05)
    elif x>=500:
        return (x*0.08)
    else:
        return 0
z=descuento(x)
#Primer output del Algoritmo: es el precio ya descontado
print('El producto descontado es:',descontado(x),'€')
#Segundo output del Algoritmo: es el descuento y su precio sin descontar respectivament
print('el descuento es de ',z,'€','el precio sin descontar seria de ',x,'€')

