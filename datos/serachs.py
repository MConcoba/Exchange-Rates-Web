# BUSQUEDA LINEAL

""" def busquedaLineal(dato):
  for x in range(len(lista)):
    if lista[x] == dato:
      return x
  return None

def buscar(dato):
  if busquedaLineal(dato) == None:
    return 'El dato %d no se encontro'%(dato)
  else:
    return "El dato %d se encontro en el indice: %d"%(dato, busquedaLineal(dato))

lista = [12,45,78,9,6,5,4,2,1,0,12,45,78,63,25,98]


for i in range(len(lista)):
  print("[%d] => [%d]" %(i, lista[i]))

print(buscar(2)) """


# busqueda binario

def busqueda_binaria(dato):
  izq = 0
  der = len(lista)-1 
  while izq <= der:
    medio = (izq + der) // 2   # Doble diagonal // es para retornar enteros
    if dato == lista[medio]:
      return medio
    elif dato < lista[medio]:
      der = medio - 1
    else:
      izq = medio + 1
  return None

def buscar(dato):
  if busqueda_binaria(dato) == None:
    return 'El dato %d no se encontro'%(dato)
  else:
    return 'El dato %d se encontro en el indice: %d'%(dato, busqueda_binaria(dato))

lista = [5,12,15,30,50,65,70,87,88,96]

for i in range(len(lista)):
  print('[%d] => [%d]'%(i, lista[i]))
print(buscar(100))