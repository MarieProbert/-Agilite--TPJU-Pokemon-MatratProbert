class Dresseur:
    def __init__(self, nom):
        self.nom = nom
        self.pokeballs = []

    def get_nom(self):
        return self.nom
    
    def get_pokeballs(self):
        return self.pokeballs

    def ajouter_pokeball(self, pokeball):
        self.pokeballs.append(pokeball)

    def capturer_pokemon(self, pokemon, pokeball):
        if pokeball.capturer_pokemon(pokemon):
            print(f"{self.nom} a capturé {pokemon.nom} dans une Pokéball!")
        else:
            print(f"La Pokéball est déjà pleine ou la capture a échoué.")

    def liberer_pokemon(self, pokeball):
        if pokeball.pokemon is not None:
            print(f"{self.nom} a libéré {pokeball.pokemon.nom} de la Pokéball.")
            pokeball.pokemon.pokeball = None
            pokeball.pokemon = None
        else:
            print("La Pokéball est déjà vide.")