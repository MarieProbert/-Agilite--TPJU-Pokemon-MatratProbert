class Dresseur:
    def __init__(self, nom):
        self.nom = nom
        self.inventaire = []

    def get_nom(self):
        return self.nom

    def get_inventaire(self):
        return self.inventaire

    def ajouter_pokeball(self, pokeball):
        self.inventaire.append(pokeball)

    def capturer_pokemon(self, pokemon, pokeball):
        if pokeball.capturer_pokemon(pokemon):
            print(f"{self.nom} a capturé {pokemon.nom} dans une Pokéball!")
        else:
            print(f"La Pokéball est déjà pleine ou la capture a échoué.")

    def liberer_pokemon(self, pokeball):
        if pokeball.pokemon is not None:
            print(f"{self.nom} a libéré {pokeball.pokemon.nom} de la Pokéball.")
            self.nettoyer_lien_pokemon_pokeball(pokeball)
        else:
            print("La Pokéball est déjà vide.")

    def nettoyer_lien_pokemon_pokeball(self, pokeball):
        pokeball.pokemon.pokeball = None
        pokeball.pokemon = None