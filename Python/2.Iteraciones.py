
lista = []
limite = 25
for i in range(limite):
    if i % 3 == 0:
        continue
    lista.append(i)
print(lista)

contador = int(input("valor: "))
while contador>0:
    contador-=1
    print("Veces repetidas ",contador)
