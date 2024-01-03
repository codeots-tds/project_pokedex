How to Boot GraphQL Server with FastAPI:
--Go into your project root directory 
----cd ~
--Enter the command below:
----"uvicorn app.main:app --reload"

How to Boot GraphQL Server with FlaskAPI:
enter in terminal at project root directory
export FLASK_APP=app.main
export FLASK_ENV=development

--Go into your project root directory 
----cd ~
--Enter the command below:
----"flask run"


graphql query:
query {
  filterPokemon(filters: {maxHp: 75, maxAtk: 60, maxDef: 80, maxSpAtk: 90, maxSpDef: 70, maxSpeed: 120}) {
    pokemonName
    pokedexNumber
    statsAbilities {
      hp
      attack
      defense
      spAttack
      spDefense
      speed
    }
  }
}