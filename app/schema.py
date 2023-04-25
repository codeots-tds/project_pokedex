import strawberry
from app.transform_data import process_pokedex
from app.schemas.poke_schema import Generation
from app.schemas.pie_chart_schema import GenPieChart, Num_Pokemon
from app.transform_data import generation_groupby

def get_pie_chart_data()-> GenPieChart:
    pie_chart_data=[]
    gen_pie=[]
    for idx, row in generation_groupby.iterrows():
        gen_name=row['gen_name']
        points=row['gen_name_points']
        pie_chart_data.append(Num_Pokemon(pokemon_number=points))
        gen_pie.append(
            GenPieChart(
        generation=gen_name,
        chart_data=Num_Pokemon(pokemon_number = points)
        )
        )
    # return (gen_pie)
    return (
    GenPieChart(
        generation=gen_name,
        chart_data=pie_chart_data
        )
)


@strawberry.type
class Query:
    PokeDex: Generation = strawberry.field(resolver=process_pokedex)
    GenBreakDown : GenPieChart = strawberry.field(resolver=get_pie_chart_data) 


# print(get_pie_chart_data())
# print(type(get_pie_chart_data()))


schema = strawberry.Schema(query=Query)