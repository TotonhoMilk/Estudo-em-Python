# Buffer infinito
# 4/1/2025

lista = []
while True:
    numero = int(input("Enter: (-1) to quit: "))
    if numero == -1:
        break
    else:
        lista.append(numero)
cont = 0
total = 0
for num in lista:
    print(f"buffer[{cont}] = {num}")

print(f"Avarage: {sum(lista) / len(lista)}")
