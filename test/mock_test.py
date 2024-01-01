import os
from ..app.schemas.poke_schema import Pokemon


# Assuming you have a Pokemon class and a Stats class structured like this:
class Stats:
    def __init__(self, hp, attack, defense, sp_attack, sp_defense, speed):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed

class Pokemon:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

# Filter function
def filter_pokemon(pokemons, min_hp=None, max_hp=None, min_attack=None, max_attack=None, min_defense=None, max_defense=None, min_sp_attack=None, max_sp_attack=None, min_sp_defense=None, max_sp_defense=None, min_speed=None, max_speed=None):
    filtered_pokemons = []
    for pokemon in pokemons:
        if min_hp is not None and pokemon.stats.hp < min_hp:
            continue
        if max_hp is not None and pokemon.stats.hp > max_hp:
            continue
        if min_attack is not None and pokemon.stats.attack < min_attack:
            continue
        if max_attack is not None and pokemon.stats.attack > max_attack:
            continue
        if min_defense is not None and pokemon.stats.defense < min_defense:
            continue
        if max_defense is not None and pokemon.stats.defense > max_defense:
            continue
        if min_sp_attack is not None and pokemon.stats.sp_attack < min_sp_attack:
            continue
        if max_sp_attack is not None and pokemon.stats.sp_attack > max_sp_attack:
            continue
        if min_sp_defense is not None and pokemon.stats.sp_defense < min_sp_defense:
            continue
        if max_sp_defense is not None and pokemon.stats.sp_defense > max_sp_defense:
            continue
        if min_speed is not None and pokemon.stats.speed < min_speed:
            continue
        if max_speed is not None and pokemon.stats.speed > max_speed:
            continue

        # If none of the conditions were met, add the pokemon to the filtered list
        filtered_pokemons.append(pokemon)

    return filtered_pokemons

# Mock data to test the function
mock_pokemons = [
    Pokemon("Bulbasaur", Stats(45, 49, 49, 65, 65, 45)),
    Pokemon("Charmander", Stats(39, 52, 43, 60, 50, 65)),
    Pokemon("Squirtle", Stats(44, 48, 65, 50, 64, 43))
]

# Test the filter function
filtered = filter_pokemon(mock_pokemons, min_hp=40, max_attack=50)
for pokemon in filtered:
    print(pokemon.name)  # Should print the names of Pokémon matching the criteria
