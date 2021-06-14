
def convertidorDeMoneda(valor, pais):
    pesos = input("Cuanto pesos " + pais +"? : ")
    pesos = float(pesos)
    # 3000000
    valor_dolares = valor
    dolares = pesos / valor_dolares
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """"
Bienvenido al convesor de monedos ✔ 

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

"""
opcion = int(input(menu))

if opcion == 1:
    convertidorDeMoneda(3650, "Colombia")
elif opcion == 2:
    convertidorDeMoneda(65, "Argentina")
elif opcion == 3:
    convertidorDeMoneda(24, "Mexico")
else:
    print('Ingresa una opcion correcta por favor')







