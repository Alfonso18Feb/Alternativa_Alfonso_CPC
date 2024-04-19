
""" A final de año, la empresa LA CAMPANA paga una prima anual a sus empleados camioneros.
Esta prima depende del recorido y la antigüedad del camion.

El recorrido depende:
casa kilometro añadimos un entimo pero cuando llegas a 400€ no añadimos mas centimos

La antigüedad depende:
A los 4 años la prima es de 200€
Y para cada año mas de 4 años se suma 20€

Luego dependiendo de los acidentes y su responsabilidad:
Si menos de 20% responsable de acidentes entonces el primer acidente es la mitad. El segundo un tercio. El tercer acidente es un cuarto. Y mas de un 4 no te damos prima
Si supera el 20% no te dan prima
Finalmente este algoritmo suma las primas de antigüedad y de recorido. Luego los acidentes pueden cambiar si te dan la prima o no
 """


# el input del algoritmo te pide los kilometros(kilometrs) y la edad del camion 
kilometrs=int(input('cuantos kilometros recoriste en un año: '))
edad=int(input('cuantos años de antigüedad tiene: '))
#El metodo recorido calcula la prima_recorido
def recorido(kilometrs):
    prima_recorido=min(kilometrs*0.01,400)#esto hace que cuando llege a 400€  no añades mas centimos
    return prima_recorido
#Este metodo del algoritmo calcula la prima_antigüedad
def antigüedad(edad):
    if edad>0 and edad<=4:
        return 50+(edad-1)*50
    elif edad>4:
        return 200+(edad-4)*20000
    else:
        ValueError('la edad no puede ser negativa o 0')
#Esta son las variables que damos a las primas
prima_recorido=recorido(kilometrs)
prima_antiguo=antigüedad(edad)
#este metodo del algoritmo suma las primas
def sumar(prima_recorido,prima_antiguo):
    return prima_antiguo+prima_recorido
#la suma de las primas la llamaremos prima
prima=sumar(prima_recorido,prima_antiguo)
#Tenemos otro input para la siguiente funcion que son acidente y resposabilidad
acidentes=int(input('cuanto acidentes tuvieste al año: '))
responsabilidad=int(input('Cual es el porcentaje de responsabilidad por accidente al año: '))
#este metodo del algoritmo te calcula la prima que te dara la empresa LA CAMPANA
def ACIDENTES(acidentes,prima,responsabilidad):
    if responsabilidad<=20:
        if acidentes==1:
            return prima/2
        elif acidentes==2:
            return prima/3
        elif acidentes==3:
            return prima/4
        elif acidentes>3:
            return 0
        else:
            return prima
    else:
        return 0
# el output de este algoritmo te devuelve la prima anual que la empresa concedera al conductor
print('la prima anual que se concederá al conductor es de ',ACIDENTES(acidentes,prima,responsabilidad),'€')
