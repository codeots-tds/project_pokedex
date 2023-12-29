import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

#This script is specifically for FASTAPI setup and configuration for routing and server stuff
@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")