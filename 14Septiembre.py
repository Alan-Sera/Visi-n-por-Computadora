b = [3,8,7,11,-1,-9,20,51,7,-1,3,11]
c = [8,2,28,17,2,50,32,21,100,99,20]
print(b)
print(c)
print(b[1])
b[2]=10
print(b)
type(b)
print(len(b))

#----------------------------------------------------------------

b = [3,8,7,11,-1,-9,20,51,7,-1,3,11]
c = [8,2,28,17,2,50,32,21,100,99,20]
a = set(b)  # No es una dupla


#----------------------------------------------------------------

l1 = list(range(2,21,2))
print(l1)
print(l1[5])
print(l1[-1])
print(l1[-2])
dir (l1)
# print dir

#Método insert, append, sort
print("Método insert, append, sort")
l1.insert(5,30)
print(l1, "insert") # inserta un valor en la posicion seleccionada


l1.append(1)
print(l1, "append") # inserta un valor en la ultima posicion

l1.sort()
print(l1, "Sort") # acomodar los valores de menor a mayor
# help (l1.sort) # Muestra para qué sirve el método

l1.clear() #
l1.copy() #
l1.count() #
l1.extend() #
l1.index() #
l1.pop() #
l1.remove() #
l1.reverse() #
l1.sort() # acomodar los valores

print(l1)
milista=l1[1:5]
print(milista)

del milista[0:2]
print(milista)

milista2=l1[:]  #Sin parametros = agarra toda la lista
print(milista2)

milista2.reverse() #
print(milista2)

#----------------------------------------------------------------

# Ciclos for

for x in range(20):
  #Agrupamos a travez de sangrias "tab"
  print(x, end=' ')

for x in range(1,20):
  print(x, end="")
  
for x in range (1,20,2):
  print(x)  

b = [3,8,7,11,-1,-9,20,51,7,-1,3,11]
for x in b:
  print(x)

# Si un número es par imprimir que lo es

for x in range (1,21):
  if x%2 == 0:
    #print(x, " Es par")
    print(f"{x}", "Es par")
  else:
    print(x, " No es par")
  print("Fin del ciclo")
print("Fin del programa")

# ----------------------------------------------------------------

# 21 de Septiembre

# FUNCIONES

# print(factorial())      

# EJERCICIO - Dado una lista de elementos diseñe una funcion que encuentre el elemento menor

def Menor(V):
  menor = V[0]
  for x in V:
    if(menor>x):
      menor=x
  return menor

b = [3,8,7,11,-1,-9,-20,51,7,-1,3,11,-13]
print(b)
print("El valor menor es: ", Menor(b))

# EJERCICIO - Dado una lista de elementos diseñe una funcion que encuentre el elemento mayor

def Mayor(v):
  mayor = v[0]
  for x in v:
    if(mayor > x):
      mayor = mayor
    else:
      mayor = x
  return mayor

b = [1,3,8,7,101,-1,-9,20,51,7,-1,3,11,-13]
print(b)
print("El valor mayor es: ", Mayor(b))

# CLASES

class complejo():
  def __init__(self, a=0, b=0):
    self.R=a
    self.I=b

  def Imprime(self):
    return self.R
    return self.I
