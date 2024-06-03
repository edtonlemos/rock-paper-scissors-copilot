import unittest
from game import determine_winner

class TestGame(unittest.TestCase):
    def test_determine_winner(self):
        print("Testando a função determine_winner...")
        self.assertEqual(determine_winner(1, 1), "Empate!")
        print("Teste 1 passou.")
        self.assertEqual(determine_winner(1, 2), "Você perdeu!")
        print("Teste 2 passou.")
        self.assertEqual(determine_winner(1, 3), "Você ganhou!")
        print("Teste 3 passou.")
        self.assertEqual(determine_winner(2, 1), "Você ganhou!")
        print("Teste 4 passou.")
        self.assertEqual(determine_winner(2, 2), "Empate!")
        print("Teste 5 passou.")
        self.assertEqual(determine_winner(2, 3), "Você perdeu!")
        print("Teste 6 passou.")
        self.assertEqual(determine_winner(3, 1), "Você perdeu!")
        print("Teste 7 passou.")
        self.assertEqual(determine_winner(3, 2), "Você ganhou!")
        print("Teste 8 passou.")
        self.assertEqual(determine_winner(3, 3), "Empate!")
        print("Teste 9 passou.")

if __name__ == '__main__':
    unittest.main(verbosity=2)