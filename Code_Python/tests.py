import unittest
from pokemon import Pokemon
from pokeball import Pokeball

class TestPokemon(unittest.TestCase):
    """Traduction de PokemonTest.java"""

    def setUp(self):
        # Équivalent des engagements (@BeforeEach)
        self.f_valeur1 = 2.0
        self.f_valeur2 = 3.0

    def test_get_type1(self):
        dracaufeu = Pokemon("Feu", "Vol")
        self.assertEqual("Feu", dracaufeu.get_type1())

    def test_get_type2(self):
        dracaufeu = Pokemon("Feu", "Vol")
        self.assertEqual("Vol", dracaufeu.get_type2())

    def test_set_type1(self):
        dracaufeu = Pokemon("Eau", "Vol")
        dracaufeu.set_type1("Feu")
        self.assertEqual("Feu", dracaufeu.get_type1())

    def test_set_type2(self):
        dracaufeu = Pokemon("Feu", "Spectre")
        dracaufeu.set_type2("Vol")
        self.assertEqual("Vol", dracaufeu.get_type2())


class TestPokeball(unittest.TestCase):
    """Traduction de PokeballTest.java"""

    def setUp(self):
        # Configuration de la relation bidirectionnelle
        self.funecire = Pokemon("Feu", "Spectre")
        self.super_ball = Pokeball(600, self.funecire)
        self.funecire.set_pokeball(self.super_ball)

    def test_afficher_pokeball(self):
        # Vérifie le message renvoyé par la pokéball
        attendu = "De types Feu et Spectre."
        self.assertEqual(attendu, self.super_ball.afficher_type_pokemon())

if __name__ == '__main__':
    unittest.main()