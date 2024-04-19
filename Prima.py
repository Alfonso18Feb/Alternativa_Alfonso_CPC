kilometrs=int(input('cuantos kilometros recoriste en un año: '))
edad=int(input('cuantos años de antigüedad tiene: '))
def recorido(kilometrs):
    prima_recorido=min(kilometrs*0.01,400)
    return prima_recorido
def antigüedad(edad):
    if edad>0 and edad<=4:
        return 50+(edad-1)*50
    elif edad>4:
        return 200+(edad-4)*20000
    else:
        ValueError('la edad no puede ser negativa o 0')
prima_recorido=recorido(kilometrs)
prima_antiguo=antigüedad(edad)
def sumar(prima_recorido,prima_antiguo):
    return prima_antiguo+prima_recorido
prima=sumar(prima_recorido,prima_antiguo)
acidentes=int(input('cuanto acidentes tuvieste al año: '))
responsabilidad=int(input('Cual es el porcentaje de responsabilidad por accidente al año: '))
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
print('la prima anual que se concederá al conductor es de ',ACIDENTES(acidentes,prima,responsabilidad),'€')
