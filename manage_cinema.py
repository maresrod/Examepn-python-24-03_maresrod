from pprint import pprint as pp


class Cinema:

    def __init__(self, rows, seats_per_row):
        """
        Args:
            rows: filas de la sala
            seats_per_row: butacas de cada fila    
        """
        self.__rows = rows
        self.__seats_per_row = seats_per_row
        self.__seating = []

    def create_cinema_seating(self):
        """
        Inicializa el seating de la sala, que es una lista de diccionarios.
          - Cada elemento de la lista representa una fila de butacas, empezando por la fila 0 que esta en la posicion 0.
          - Cada fila tiene un diccionario para representar las butacas de esa fila.
          - Las claves del diccionario son cada una de las butacas de esa fila (1, 2, 3, etc.).
        """

        seating = []
        for i in range(1, self.__rows + 1):
            seating.append({key: None for key in range(1, self.__seats_per_row)})

        self.__seating = seating

    def print_seating(self):
        """
        Imprime el seating de la sala
        """
        pp(self.__seating)

    def book_seat(self, row, seat):
        """
        Marca una butaca como ocupada.
        Args:
            row: la fila de la butaca
            seat: el numero de la butaca
        """

        if self.__seating[row][seat] is None:
            self.__seating[row][seat] = "occupied"

    def count_free_seats(self, rows_seats, total):
        """
        Calcula la cantidad de butacas libres que hay en una lista
        Args:
            rows_seats: lista de butacas a buscar
            total: valor inicial donde se acumulará el total
        """
        for row, seat in rows_seats:
            if self.__seating[row].get(seat) is None:
                total = total + 1
        return total


# ------------------------------------------- MAIN -----------------------------------------------
cinema = Cinema(rows=10, seats_per_row=8)

# ERROR 1: al reservar una butaca (p.e. fila 2 butaca 4) e imprimir el seating, veo que aparece como ocupada la 4 de cada fila, y no solo de la fila 2.
print("------------- Error 1 -----------------")
cinema.create_cinema_seating()
cinema.book_seat(2, 4)
cinema.print_seating()
'''
El problema que he encontrado ha sido la manera de crear el seating del cine, al principio, los objetos que se guardaban
en las rows del seating eran tipo "str". 

La solución ha sido cambiar la manera de iniciar el seating de manera que ahora actua como un diccionario
'''

# ERROR 2: le paso la lista de "seats" donde debería haber 2 libres y me dice que hay 0.
print("\n------------- Error 2 -----------------")
seats = [(2, 4), (3, 1), (5, 2)]
total = 0
total = cinema.count_free_seats(seats, total)
print("total: " + str(total))

''' 
Python crea una copia de la variable que estas pasando por parametros ( cambia de namespace )  de manera que
cuando la modificas en la funcion estas modificando la copia y no la variable con la direccion de memoria original.
Esto se arregla devolviendo el total cuando has acabado con las operaciones.

Otra solucion seria utilizar "global" en la función, que no es muy comun. O las mas elegante de todas (en mi opinion), utilizar las clases.
'''

# ERROR 3: quiero modificar la butaca (2,4) de la lista anterior para que sea la (3,4) y no me deja.
print("\n------------- Error 3 -----------------")
seats[0] = (3, 4)
total = 0
total = cinema.count_free_seats(seats, total)
print("total: " + str(total))

'''
Se trata de una lista de tuplas, las tuplas en python son inmutables, no se pueden actualizar una vez creadas.

Lo que si que puedes hacer llegados a este punto es borrar la antigua y asignarle una nueva. Para eso, en este caso, podemos sobreescribir
la posicion en la lista con la tupla nueva. 

Si se pretendia poder actualizar las butacas se podria haber utilizado una lista,ya que no son inmutables y no tendria que realizarse
como se ha realizado
'''
