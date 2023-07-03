# A continuacion se enumeran unos numeros en forma de lista. se usa como para separar los elementos de la lista
print("Ejemplo de lista numerica")
lista = [2, 3, 5, 8, 13, 21, 34]
print("# print (lista)")
print(lista)
print("print (lista, end= " " ", "De esta forma la lista se imprime de forma vertical")
print(lista, end=" ")
print(
    "En este print se coloca : el nombre de la lista  Lista seguido de dos corchetes que indican la posicion del elemento donde 0 es la posicion numero 1 "
)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print()
print()
print(
    "En este ejemplo se crea una lista que contiene 3 elemntos, ademas se ejecuta la modificación de un elemnto mediante el uso del nombre de la lista y corchete ej. y[1] donde se modifica la posicion indicada"
)
print()
y = [
    int(input("ingrese un dato : ")),
    int(input("ingrese otro valor: ")),
    int(input("ingrese otro valor: ")),
]
print(y[0])
print(y[-1])  # se imprime la posicion indicada de la lista "y"
print(y[-2])
print(y)
y[1] = int(
    input("Modifique el elemto 2 de la lista : ")
)  # se indica la lista y y la posición en:  y [1] # a continuación se ejecuta un cambio usando el comando input
print(
    y, f"El numero de elemtos : ", len(y)
)  # atraves de la funcion len se obtiene la cantidad de elemntos de la lista
for (
    f
) in (
    lista
):  # recorrido de la lista, se emplea la estructura repetitiva for donde la variable f va tomando cada uno de los elentos de la lista
    print(f)
print()
print()

# __________________concatenar listas_________________________

print("concatenar listas")
print()
ac = [1, 2, 3]
ab = [4, 5, 6]
print(ac)
print(ab)
print("las listas pueden sumarse ")
print()
print(" Las listas anteriores sumadas")
g = ac + ab  # a la variable "g" se le asigna la suma de la lista "ac" y"ab"
print()
print(
    "A continuacion se muestra un ejemplo de que la lista nueva tambien puede ser multiplicada, como en este ejemplo que se multiplico nueve veces"
)
print()
print(
    g * 9, len(g * 9)
)  # se imprime la varible g y la cantidad de elemntos de la lista "g"

print()
print()
# _______________slicing (rabanado)______________________
ls = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print(ls)
print(ls[0:3])  # se imprime a partir del elemnto cero al elemnto tres
u = ls[
    0:2
]  # a la variable "u" se le asigan los elementos del cero al dos de la lista respectivamente
print(u)

print()
print(ls[3:])  # se imprime solo los primeros 3
print(ls[:4])  # se imprime la lista a partir del 4

# ejemplo 2
print()
print()
# Ejemplo de uso de slicing

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Obtener un rango de elementos (sub-lista)
print(numeros[3:7])  # Imprime [3, 4, 5, 6]

# Obtener un elemento específico
print(numeros[2])  # Imprime 2

# Obtener los últimos tres elementos
print(numeros[-3:])  # Imprime [7, 8, 9]

# Obtener todos los elementos excepto los primeros dos
print(numeros[2:])  # Imprime [2, 3, 4, 5, 6, 7, 8, 9]


# _____________metodos de lista_______________________


# -----------------append-------------------
print()
print("Metodo append")
print()
print(" la lista ls es :", ls)
dato = input("Que dato quiere agregar a la lista : ")
ls.append(dato)  # el metodo "append" agrega un elemto al final de la lista
print(ls, " se agregó el elemnto :", dato, " a la lista")
print()
print()
print()
# ---------------extend(lista)--------------
print()
print("metodo extend(lista)")
print()
ls1 = ["q", "e", "r", "t", "y", "u"]
ls2 = ["a", "s", "d", "f", "g", "h", "j"]
ls1.extend(ls2)
print(ls1)
# El metodo extend combina la lista ls1 a ls2 agregandola al final

print()
# ------------------metodo sort -----------------------
print()
print("Metodo sort")
print()
ls56 = [
    int(input(" digite 5 numeros :")),
    int(input(": ")),
    int(input(": ")),
    int(input(": ")),
    int(input(": ")),
    int(input(": ")),
]
print(ls56)
ls56.sort()
print("La lista anterior ordenada de forma ascendente")
print(ls56)

print()  # este metodo ordena la lista en orden ascendente
print()
# ------------------metodo reverse---------------------
print("La lista anterior invertida")
ls56.reverse()
print(ls56)  # Este metodo invierte la lista
print()
print()
# ------------------metodo count------------------------------
print()
print("metodo count")
print()
ls6 = [
    1,
    2,
    3,
    4,
    4,
    5,
    6,
    4,
    8,
    8,
    7,
    9,
    6,
    4,
    5,
    2,
    1,
    7,
    8,
    6,
    9,
    4,
    2,
    1,
    3,
    6,
    4,
    7,
    8,
    4,
    6,
    5,
    4,
    2,
    1,
    7,
    9,
    8,
    6,
    3,
    5,
    2,
    4,
    2,
    4,
    8,
    5,
    3,
    5,
    5,
    4,
    7,
    9,
    8,
    6,
    3,
    2,
    1,
    4,
    8,
    5,
]
# El metodo count indica la cantidad de ocurrencia del número indicado en la lista
print()
while True:
    ñ = int(input("Indique un número mayor de 1: "))
    if ñ > 1:
        break
print("el número", ñ, "tiene una ocurrencia de...", ls6.count(ñ), " en la lista :", ls6)
print()
print()
# ------------------metodo index-------------
# indica la posicion del numero
ift = [1, 2, 3, 5, 8, 13, 21, 34]
print(ift, "La lista ift")
w = ift.index(21, 5)
print(w)

# ------------------metodo insert-----------
print()
print("Metodo para insertar datos en una lista ")
print(ift)
while True:
    q = int(input("Posición: "))
    r = int(input("elemento: "))
    if q and r >= 0:
        break

ift.insert(q, r)
print(ift)
print()
# ---------------------pop(indice)-------------------
# metodo utilizado para remover un elemnto de la lista
# si no se le proporciona la posicion del elemnto a eliminar, eliminra el ultimo elemento
print(ift)
z = int(input("elija la popsicion del elemento que desea eliminar: "))
eliminado = ift.pop(z)
print("realizado")
print(ift)
print("Elemnto eliminado es: ", eliminado)
print()
print()
# ------------------remove (elemnto)-------------------------
print()  # remueve el elemento de la lista en su primera aparición
print("metodo Remove (elemento)")
print(ift)
bb = int(input("¿Qué elemnto desea eliminar?: "))
ift.remove(bb)
print("realizado elemento eliminado ", ift)
# recibe el elemnto como argumento y borra su primera aparicion

# -----------------------del-------------------------------
# Se utiliza para cortar dos o mas elemntos se agrega el rebanado
print(ift)
print("Elementos a eliminar [1:4]...")
del ift[1:4]
print(ift, "Elementos eliminados")
