# Gauss Challenge: sum all of the numbers between 1 and 100

lista = list(range(1, 101))

# option 1
suma = 0
for n in lista:
    suma += n

print(f"Option 1:", suma)


# Option 2

print(f"option 2:",sum(lista))

# option 3
N= 100
totalLista = (N/2)*(N+1)

print(f"option3: {totalLista}")
    


