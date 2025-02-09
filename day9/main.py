from Art import logo
print(logo)

apuestas = {}
while True:
    name = input("ingrese nombre ")
    monto = int(input("ingrese monto "))
    condicion = input("hay algun otro subastador si o no ")
    apuestas[name] = monto
    if condicion == "no":
        break

maximoMonto = 0
print(f"los jugadores que participaron fueron ")
for key in apuestas:
    print(f"{key} con monto de {apuestas[key]}")
    
    if apuestas[key] > maximoMonto:
        maximoMonto = apuestas[key]
        ganador = key

print(f"El ganador de la subasta fue {ganador} con un valor de subasta de {maximoMonto}")
