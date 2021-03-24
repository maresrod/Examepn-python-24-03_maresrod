'''
Autor: Marcelo Espinola Rodriguez
Version de python: 3.9
'''

from libro import Libro
from autor import Autor


def get_list(nombre_fichero):
    f = open(nombre_fichero, mode="r", encoding="utf-8")
    texto = f.read()
    if texto == "":
        raise ValueError("El archivo esta vacio")
    else:
        parsed_text = texto.split()

        final_list = []
        list_of_len = []
        for word in parsed_text:
            if word not in final_list:
                list_of_len.append(len(word))
                final_list.append(word)

        # nos aprovechamos de que las keys de los diccionarios no se puede repetir
        diccionario = {k: [] for k in list_of_len}

        for word in final_list:
            diccionario[len(word)].append(word)

    return diccionario


def mas_antiguos(lista, anyo):
    if len(lista) < 1:
        raise ValueError("La lista de libros esta vacia")
    elif anyo < 1900 or anyo > 2021:
        raise ValueError("El año introducido debe estar entre 1900 y 2021")
    else:
        lista_resultado = []
        for libro in lista:
            if libro.get_anyo() <= anyo:
                lista_resultado.append(libro.get_titulo())

        print(lista_resultado)
        return lista_resultado


print(get_list("texto.txt"))

l1 = Libro(Autor(1,"Ramon", "de Valle-Inclan"), "Luces de bohemia", 1920)
l2 = Libro(Autor(2,"Gabriel","Garcia Marquez"), "Cien años de soledad", 1967)
l3 = Libro(Autor(3,"Apostoles","de Dios"), "La Biblia", 1901)
lista_libros = [l1, l2, l3]

print(mas_antiguos(lista_libros, 1950))
