# Contando, a la manera del Dojo
# Imprime los números enteros del 1 al 100. Si es divisible por 5, imprime "Codificando" en su lugar. Si es por 10, también imprime "Dojo".
for i in range(1,101):
    if i%10==0:
        print('Dojo')
    elif i%5==0:
        print('Codificado')
    else:
        print(i)

print('FIN')