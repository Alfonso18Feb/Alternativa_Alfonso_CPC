dia=input('dia de la semana'.lower())
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