from behave import given, when, then
from Models.pokemon import Pokemon
from Models.pokeball import Pokeball

@given('un Pokemon de types "Feu" et "Spectre"')
def step_given_pokemon_types(context):
    context.pokemon = Pokemon("Feu", "Spectre")

@given('une Pokéball contenant ce Pokémon')
def step_given_pokeball_with_pokemon(context):
    context.pokeball = Pokeball(600, context.pokemon)
    context.pokemon.pokeball = context.pokeball

@when("J'affiche le type du Pokémon via la Pokéball")
def step_when_afficher_type(context):
    context.result = context.pokeball.afficher_type_pokemon()

@then('afficher le message "De types Feu et Spectre."')
def step_then_afficher_types(context):
    assert context.result == "De types Feu et Spectre."

@given('une Pokéball sans Pokémon')
def step_given_empty_pokeball(context):
    context.pokeball = Pokeball(600)

@then('afficher le message "Cette Pokeball est vide. Aucun type à afficher."')
def step_then_afficher_vide(context):
    assert context.result == "Cette Pokeball est vide. Aucun type à afficher."
