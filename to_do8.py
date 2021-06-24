# Imprimir y contar
# Imprime todos los múltiplos enteros de 5, de 512 a 4096. Después, también registra cuántos había.

contar=0
for i in range(512,4097,5):
    print(i)
    contar+=1

print('Hay: ',contar)
