'''
Autor: Marcelo Espinola Rodriguez
Version de python: 3.9
'''

from autor import Autor
class Libro():

    def __init__(self,autor,titulo,anyo):
        self.__autor = autor
        self.__titulo = titulo
        self.__anyo = anyo


    def get_anyo(self):
        return self.__anyo

    def get_titulo(self):
        return self.__titulo