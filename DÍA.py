#input del algoritmo pones el dia de la semana

dia=input('dia de la semana'.lower())
#el metodo del algoritmo que elige el dia siguiente que ha elegido anteriormente

def ser(dia):
    if dia=='lunes':
        return 'martes'
    elif dia=='martes': 
        return 'miercoles'  
    elif dia=='miercoles': 
        return 'jueves'
    elif dia=='jueves': 
        return 'viernes'
    elif dia=='viernes': 
        return 'sabado'
    elif dia=='sabado': 
        return 'domingo'
    elif dia=='domingo': 
        return 'lunes'
    else:
        ValueError('Tienes que poner un dia de la semana')
#el output que te da el dia siguiente del elegido anteriormente

print('el dia siguente es',ser(dia))
