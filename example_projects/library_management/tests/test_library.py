import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        library.add_book("Testbuch", "Autor")
        self.assertEqual(len(library.books), 1)

if __name__ == "__main__":
    unittest.main()