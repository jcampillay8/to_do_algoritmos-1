# Guau, es enorme...
# Agrega números enteros impares de -300,000 a 300,000, y console.log la suma final. ¿Existe un atajo?

suma=0
for i in range (-300000,300000):
    if i % 3==0:
        suma+=1
    else:
        pass

print(suma)
