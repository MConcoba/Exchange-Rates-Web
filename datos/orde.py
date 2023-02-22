
# BURBUJA
""" lista = [4,2,6,8,5,6]

for i in range(len(lista)):
  for x in range(len(lista)-1):
    if lista[x] > lista[x+1]:
      aux = lista[x]
      lista[x] = lista[x+1]
      lista[x+1] = aux
      print(lista) """

# Por seleccion

""" lista = [4,2,6,8,5,7,0]


for i in range(len(lista)):
  minimo = i
  for x in range(i, len(lista)):
    if lista[x] < lista[minimo]:
      minimo = x
  aux = lista[i] 
  lista[i] = lista[minimo]
  lista[minimo] = aux """


# Por INSERCION

lista = [5, 10, 3, 12, 10, 6]

for i in range(1, len(lista)):
  aux = lista[i]
  j = i - 1
  print(j)
  while j >= 0 and aux < lista[j]:
    lista[j + 1] = lista[j]
    lista[j] = aux
    j -= 1

print(lista)



