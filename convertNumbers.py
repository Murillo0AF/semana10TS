def converte(numeroEmRomano):
    tabela = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    acumulador = 0
    ultimovizinhodireita = 0

    for i in reversed(range(len(numeroEmRomano))):
        atual = 0
        numCorrente = numeroEmRomano[i]
        if numCorrente in tabela:
            atual = tabela[numCorrente]

        multiplicador = 1
        if atual < ultimovizinhodireita:
            multiplicador = -1

        acumulador += atual * multiplicador
        ultimovizinhodireita = atual

    return acumulador

# Testes com unittest
import unittest

class TestConversaoRomanos(unittest.TestCase):
    def test_unidades(self):
        self.assertEqual(converte("I"), 1)
        self.assertEqual(converte("V"), 5)
        self.assertEqual(converte("X"), 10)

    def test_numeros_simples(self):
        self.assertEqual(converte("II"), 2)
        self.assertEqual(converte("XXII"), 22)
        self.assertEqual(converte("IX"), 9)
        self.assertEqual(converte("XXIV"), 24)

if __name__ == "__main__":
    unittest.main()
