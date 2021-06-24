# Año bisiesto
# Escribe una función que determine si un año determinado es bisiesto. Si un año es divisible por cuatro, es un año bisiesto, a menos que sea divisible por 100. Sin embargo, si es divisible por 400, entonces lo es.

while True:
    ano=int(input('ingresa un año '))
    
    if ano % 400 == 0:
        print('Año bisiesto')
    elif ano % 100 == 0:
        print('Año no bisiesto')
    elif ano % 4 == 0:
        print('Año bisiesto')
    else:
        print('Año no bisiesto')

    continuar = input('Continua s/n ?')
    if continuar == 'n':
        break

print('FIN')