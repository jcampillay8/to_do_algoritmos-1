# Dices que es tu cumpleaños...
# Si 2 números dados representan tu mes y día de nacimiento en cualquier orden, registra "¿Cómo lo supiste?", de lo contrario registra "Un día cualquiera...".

while True:
    adivina=int(input('trata de adivinar que dia del mes nací '))
    if adivina!=24:
        print('trata de nuevo')
    else:
        break

print('si, nací el 24')
