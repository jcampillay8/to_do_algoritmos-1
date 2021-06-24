# Cuenta regresiva cada cuatro
# Registra números positivos a partir de 2016, contando hacia atrás cada cuatro números (excluye 0), sin un bucle FOR.

valor=2016
while True:
    print(valor)
    valor-=4
    if valor <= 0:
        break

print('FIN')

