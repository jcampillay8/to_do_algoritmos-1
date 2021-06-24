# Múltiplos de tres, pero no todos
# Usando FOR, imprime múltiplos de 3 de -300 a 0. Omite -3 y -6. 

for i in range(-30,3,3):
    if i == int(-3) or i == int(-6):
        pass
    else:
        print(i)