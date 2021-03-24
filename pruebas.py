from autor import Autor
from libro import Libro

import unittest

class Pruebas(unittest.TestCase):

    def test_prueba_mas_antiguo(self):
        l1 = Libro(Autor(1, "Ramon", "de Valle-Inclan"), "Luces de bohemia", 1920)
        l2 = Libro(Autor(2, "Gabriel", "Garcia Marquez"), "Cien años de soledad", 1967)
        l3 = Libro(Autor(3, "Apostoles", "de Dios"), "La Biblia", 1901)
        lista_libros = [l1, l2, l3]

        self.assertEqual(mas_antiguos(lista_libros, 1920), ["Luces de bohemia", "La Biblia"])
        self.assertEqual(mas_antiguos(lista_libros, 2000), ["Luces de bohemia", "Cien años de soledad", "La Biblia"])
        self.assertEqual(mas_antiguos(lista_libros, 1905), ["La Biblia"])

    def test_anyos(self):
        l1 = Libro(Autor(1, "Ramon", "de Valle-Inclan"), "Luces de bohemia", 1920)
        l2 = Libro(Autor(2, "Gabriel", "Garcia Marquez"), "Cien años de soledad", 1967)
        l3 = Libro(Autor(3, "Apostoles", "de Dios"), "La Biblia", 1901)
        lista_libros = [l1, l2, l3]

        self.assertRaisesRegex(ValueError, "El año introducido debe estar entre 1900 y 2021", mas_antiguos,
                               lista_libros, 2030)
        self.assertRaisesRegex(ValueError, "El año introducido debe estar entre 1900 y 2021", mas_antiguos,
                               lista_libros, 1350)

    def test_lista_vacia(self):
        lista_libros = []
        self.assertRaisesRegex(ValueError, "La lista de libros esta vacia", mas_antiguos, lista_libros, 1950)


if __name__ == "__main__":
    unittest.main()
