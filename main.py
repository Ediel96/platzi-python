print('hello world')

pesos = input("Cuanto pesos colombianos? : ")
pesos = float(pesos)
# 3000000
valor_dolares = 3654
dolares = pesos / valor_dolares
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")